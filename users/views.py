from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError


def logout_view(request):
    logout(request)
    return redirect('user:login')


def login_view(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['phone_number'],
                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('pages:home')
            raise ValidationError('Wrong password or phone_number !')
    return render(request, 'login.html', context={
        'form': form,
    })


def user_registration(request):
    form = RegistrationForm

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('user:login')

    return render(request, 'register.html', context={
        'form': form,
    })
