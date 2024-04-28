from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from main.tokens import account_activation_token
from masters.models import Masters
from .forms import UserRegistrationForm, UserLoginForm, AppointmentsForm
from .models import Appointments


def index(request):
    current_site = get_current_site(request)
    protocol = 'https' if request.is_secure() else 'http'
    msg = f'{protocol}://{current_site.domain}{static("main/img/favicon.ico")}'
    print(msg)
    return render(request, "main/main.html")


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
    print('LoginUser')
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
                print('Form is not valid:', form.errors)

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
        user_bookings = Appointments.objects.filter(user=request.user)
        return render(request, 'main/user_account.html', {'user_bookings': user_bookings})
    else:
        master = Masters.objects.filter(user=request.user)[0]
        master_bookings = Appointments.objects.filter(master=master)
        return render(request, 'main/master_account.html', {'master_bookings': master_bookings})


def booking(request):
    if request.method == 'POST':
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('account')
        else:
            print(form.errors)
    else:
        form = AppointmentsForm()
    return render(request, 'main/booking.html', {'form': form})


def accept_booking(request, booking_id):
    print('accept')
    if request.method == 'POST':
        bid = Appointments.objects.get(id=booking_id)
        bid.status = '1'
        bid.save()
    return redirect('account')


def decline_booking(request, booking_id):
    print('decline')
    if request.method == 'POST':
        bid = Appointments.objects.get(id=booking_id)
        bid.status = '0'
        bid.save()
    return redirect('account')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
