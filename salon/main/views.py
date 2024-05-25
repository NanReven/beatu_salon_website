import datetime
import random
import string

from django.utils import timezone
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from main.tokens import account_activation_token
from masters.models import Masters, Users
from products.models import Cart, CartItem, Product
from services.models import MasterCategory, Services
from .forms import UserRegistrationForm, UserLoginForm, AppointmentsForm, ProfileEditForm, ChangePasswordForm
from .models import Appointments


def index(request):
    return render(request, "main/main.html")


@login_required
def schedule(request):
    return render(request, "main/schedule.html")


@login_required
def get_appointments(request):
    appointments_date = datetime.date(int(request.GET.get('year')), int(request.GET.get('month')),
                                      int(request.GET.get('day')))

    if not Masters.objects.filter(user=request.user).exists():
        master = Masters.objects.get(pk=request.GET.get('master'))
    else:
        master = Masters.objects.get(user=request.user)

    appointments = Appointments.objects.filter(master=master, status='1')
    appointment_list = []
    for appointment in appointments:
        if appointment.datetime.date() == appointments_date:
            local_datetime = localtime(appointment.datetime)
            appointment_data = {
                'service': appointment.service.title,
                'time': local_datetime.time(),
                'duration': appointment.service.duration,
                'user': appointment.user.first_name + ' ' + appointment.user.last_name,
                'comment': appointment.comment,
            }
            appointment_list.append(appointment_data)

    return JsonResponse(appointment_list, safe=False)


def get_master_services(request):
    master = request.GET.get('master')
    categories = MasterCategory.objects.filter(master=master)
    services = []
    for category in categories:
        category_services = Services.objects.filter(category=category.pk)
        for service in category_services:
            services.append({'id': service.pk, 'title': service.title})
    return JsonResponse(services, safe=False)


def get_master_weekends(request):
    master = Masters.objects.get(pk=request.GET.get('master'))
    weekends = []
    for day in master.weekend.all():
        weekends.append({'day': day.day})
    return JsonResponse(weekends, safe=False)


@login_required
def cancel_booking(request, booking_id):
    appointment = Appointments.objects.get(pk=booking_id)
    appointment.status = '0'
    appointment.save()
    messages.success(request, 'Ваш успешно')
    return redirect('account')


@login_required
def get_activation_email(request, user):
    current_site = get_current_site(request)
    protocol = 'https' if request.is_secure() else 'http'
    activate_url = reverse('activate', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                               'token': account_activation_token.make_token(user)})
    activation_link = f"{protocol}://{current_site.domain}{activate_url}"

    context = {
        'user': user,
        'protocol': protocol,
        'domain': current_site.domain,
        'activation_link': activation_link,
        'logo_url': f'{protocol}://{current_site.domain}{static("main/img/logo-black.png")}'
    }
    message = render_to_string('main/activation_email.html', context)

    return message


def registrate(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.is_active = False
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            message = get_activation_email(request, new_user)
            send_mail(
                'Подтверждение аккаунта',
                message,
                'nanreven@yandex.ru',
                [new_user.email],
                html_message=message,
            )
            messages.success(request, 'Проверьте вашу почту для подтверждения регистрации.')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'form': user_form})


def activate_account(request, uidb64, token):
    user_model = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user_model.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
        return redirect('login')

    if account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Ваш аккаунт успешно активирован. Теперь вы можете войти.')
    else:
        messages.error(request, 'Ошибка активации аккаунта. Пожалуйста, попробуйте еще раз.')
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('account')
        else:
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and not user.is_active:
                messages.error(request, "Ваш аккаунт неактивен. Проверьте вашу почту для активации.")
            elif user is None:
                messages.error(request, "Неверный адрес почты или пароль.")
            else:
                messages.error(request, form.errors)

    else:
        form = UserLoginForm()

    message_list = messages.get_messages(request)
    messages_to_show = list(message_list)

    return render(request, 'main/auth.html', {'form': form, 'messages': messages_to_show})


def logoutUser(request):
    logout(request)
    return redirect('home_page')


@login_required
def account(request):
    if request.user.is_customer:
        user_bookings = Appointments.objects.filter(user=request.user, datetime__gte=timezone.now()) \
            .filter(Q(status='1') | Q(status='2')).order_by('-datetime')
        for book in user_bookings:
            if book.datetime.date() == datetime.datetime.now().date():
                if book.datetime.time() <= datetime.datetime.now().time():
                    user_bookings.exclude(pk=book.pk)
                    obj = Appointments.objects.get(pk=book.pk)
                    obj.status = '0'
                    obj.save()
        return render(request, 'main/user_account.html', {'user_bookings': user_bookings})
    else:
        master = Masters.objects.filter(user=request.user)[0]
        master_bookings = Appointments.objects.filter(master=master, status='2')
        for book in master_bookings:
            if book.datetime.date() == datetime.datetime.now().date():
                if book.time <= datetime.datetime.now():
                    master_bookings.exclude(pk=book.pk)
                    obj = Appointments.objects.get(pk=book.pk)
                    obj.status = '0'
                    obj.save()
        return render(request, 'main/master_account.html', {'master_bookings': master_bookings})


@login_required
def booking(request):
    if request.method == 'POST':
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            for master_appointment in Appointments.objects.filter(datetime=appointment.datetime, master=appointment.master,
                                                                  status='1'):
                appointment_end = datetime.timedelta(hours=master_appointment.datetime.time().hour,
                                                     minutes=master_appointment.datetime.time().minute) + \
                                  datetime.timedelta(hours=master_appointment.service.duration.hour,
                                                     minutes=master_appointment.service.duration.minute)
                appointment_start = datetime.timedelta(hours=master_appointment.datetime.time().hour,
                                                       minutes=master_appointment.datetime.time().minute)
                if appointment_start <= appointment.datetime.time() <= appointment_end:
                    messages.error(request, "Выбранное время уже занято.")
                    return render(request, 'main/booking.html', {'form': form})

            appointment.save()
            return redirect('account')
    else:
        form = AppointmentsForm()
    message_list = messages.get_messages(request)
    messages_to_show = list(message_list)
    return render(request, 'main/booking.html', {'form': form, 'messages': messages_to_show})


@login_required
def accept_booking(request, booking_id):
    if request.method == 'POST':
        bid = Appointments.objects.get(id=booking_id)
        bid.status = '1'
        bid.save()
    return redirect('account')


@login_required
def decline_booking(request, booking_id):
    if request.method == 'POST':
        bid = Appointments.objects.get(id=booking_id)
        bid.status = '0'
        bid.save()
    return redirect('account')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = ProfileEditForm(request.POST)
        if edit_form.is_valid():
            user = Users.objects.get(pk=request.user.pk)
            user.first_name = edit_form.cleaned_data['first_name']
            user.last_name = edit_form.cleaned_data['last_name']
            user.email = edit_form.cleaned_data['email']
            user.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('account')
    else:
        edit_form = ProfileEditForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name,
                                             'email': request.user.email})
    return render(request, 'main/edit_profile.html', {'form': edit_form})


@login_required
def change_password(request):
    if request.method == 'POST':
        edit_form = ChangePasswordForm(request.POST)
        if edit_form.is_valid():
            if not check_password(edit_form.cleaned_data['old_password'], request.user.password):
                messages.error(request, 'Your old password did not match')
                return redirect('change_password')
            new_password = edit_form.cleaned_data['new_password']
            repeat_new_password = edit_form.cleaned_data['repeat_new_password']
            if new_password and repeat_new_password and new_password != repeat_new_password:
                messages.error(request, 'Your new passwords did not match')
                return redirect('change_password')
            user = Users.objects.get(pk=request.user.pk)
            user.password = make_password(new_password)
            user.save()
            messages.success(request, 'Your password has been successfully updated.')
            logout(request)
            return redirect('login')
    else:
        edit_form = ChangePasswordForm()

    return render(request, 'main/change_password.html', {'form': edit_form})


@login_required
def visits_history(request):
    appointments = Appointments.objects.filter(user=request.user, status='1')
    current_date = timezone.now()
    for appointment in appointments:
        if appointment.datetime >= current_date:
            appointments = appointments.exclude(pk=appointment.pk)
    return render(request, 'main/visits_history.html', {'appointments': appointments})


def cart(request):
    if not request.user.is_authenticated:
        return render(request, 'main/cart.html')

    if not Cart.objects.filter(user=request.user, status='pending').exists():
        return render(request, 'main/cart.html')
    else:
        user_cart = Cart.objects.get(user=request.user, status='pending')
    cart_items = CartItem.objects.filter(cart=user_cart)
    prices = []
    for item in cart_items:
        product = Product.objects.get(pk=item.product.pk)
        prices.append(product.price)

    return render(request, 'main/cart.html', {'cart_items': zip(cart_items, prices)})


@csrf_exempt
def add_product(request):
    if not request.user.is_authenticated:
        messages.error(request, 'please enter your account')
        return JsonResponse('login', safe=False)

    user_cart = Cart.objects.filter(user=request.user, status='pending').first()
    if not user_cart:
        user_cart = Cart.objects.create(user=request.user)
    product_id = request.POST.get('product')

    if CartItem.objects.filter(cart=user_cart, product_id=product_id).exists():
        return JsonResponse("item is already here", safe=False)

    cart_product = CartItem.objects.create(cart=user_cart, product_id=product_id)
    cart_product.save()
    return JsonResponse("Its ok", safe=False)


def get_cart_items(request):
    try:
        user_cart = Cart.objects.get(user=request.user, status='pending')
    except Cart.DoesNotExist:
        return JsonResponse([], safe=False)
    data = []
    for item in CartItem.objects.filter(cart=user_cart):
        data.append({'item_id': item.product.pk})
    return JsonResponse(data, safe=False)


@csrf_exempt
def remove_cart_item(request):
    product_id = request.POST.get('item')
    user_cart = Cart.objects.get(user=request.user, status='pending')
    CartItem.objects.get(cart=user_cart, product_id=product_id).delete()
    return JsonResponse("Its ok", safe=False)


def generate_unique_code():
    code = ''
    characters = string.ascii_letters + string.digits
    for i in range(4):
        code += random.choice(characters)

    return code


@csrf_exempt
def reserve(request):
    data = request.POST.get('quantity')
    items = data[1:-1].split(",")
    try:
        user_cart = Cart.objects.get(user=request.user, status='pending')
    except Cart.DoesNotExist:
        return JsonResponse([], safe=False)

    for item in items:
        temp = item.split(":")
        item_id = int(temp[0][1:-1])
        item_quantity = int(temp[1])
        cart_item = CartItem.objects.get(cart=user_cart, product=item_id)
        cart_item.quantity = item_quantity
        cart_item.save()

        product = cart_item.product
        product.quantity -= item_quantity
        product.save()

    user_cart.issue_code = generate_unique_code()
    user_cart.status = 'ready'
    user_cart.order_date = timezone.now()
    user_cart.total_sum = float(request.POST.get('sum'))
    user_cart.save()
    messages.success(request, 'Everything is ok')
    return JsonResponse("true", safe=False)


@login_required
def order_history(request):
    user_orders = Cart.objects.filter(user=request.user)
    orders_info = []

    for order in user_orders:
        order_info = {
            'order': order,
            'items': CartItem.objects.filter(cart=order)
        }
        orders_info.append(order_info)

    return render(request, 'main/order_history.html', {'orders_info': orders_info})


@csrf_exempt
def cancel_order(request):
    order_id = request.POST.get('order')
    try:
        user_cart = Cart.objects.get(pk=order_id)
    except Cart.DoesNotExist:
        return JsonResponse('error', safe=False)

    user_cart.status = 'canceled'
    user_cart.save()
    return JsonResponse("cancel order", safe=False)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
