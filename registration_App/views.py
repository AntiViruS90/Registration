from django.shortcuts import render, redirect
from .form import RegistrationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    if request.user.username:
        username = request.user.first_name
    else:
        username = 'Guest'
    context = {'username': username}
    return render(request, 'index.html', context)


def registration(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username_form = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            user_firstname = form.cleaned_data.get('first_name')
            user_lastname = form.cleaned_data.get('last_name')
            user_email = form.cleaned_data.get('email')
            user = authenticate(username=username_form,
                                password=user_password)
            person = User.objects.get(username=username_form)
            person.first_name = user_firstname
            person.last_name = user_lastname
            person.email = user_email
            person.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {'registartion_form': form}
    return render(request, 'registration/registration.html', context)