from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from main.tokens import account_activation_token
from .forms import UserRegistrationForm, UserLoginForm


def index(request):
    return render(request, "main/main.html")


def registrate(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #if user_form.cleaned_data['password'] != user_form.cleaned_data['password2']:
             #   user_form.add_error('password2', 'Passwords do not match.')
            #else:
            new_user = user_form.save(commit=False)
            new_user.is_active = False
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            current_site = get_current_site(request)
            message = render_to_string('main/activation_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            send_mail(
                'Confirm your email for Simpledocs',
                message,
                'nanreven@yandex.ru',
                [new_user.email],
                html_message=message,
            )
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'form': user_form}) # user_form ?


def activate_account(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            #messages.success(request, 'Thank you for your email confirmation. Now you can login your account.') # wtf
            return redirect('login')  # Redirect to login page after activation
        else:
            return render(request, 'account_activation_invalid.html')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return render(request, 'account_activation_invalid.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                #request.session['user'] = user
                return redirect('account')
                #return render(request, 'main/acc.html')
            else:
                form.add_error(None, "Invalid email or password.")
        else:
            print('Form is not valid:', form.errors)
    else:
        form = UserLoginForm()
    return render(request, 'main/auth.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home_page')


@login_required
def account(request):
    return render(request, 'main/acc.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
