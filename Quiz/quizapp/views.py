from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect, redirect)
from django.template import loader
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
def index(request):
    return render(request, "base.html")


def my_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/my_profile')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


def my_registration_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        isteach = request.POST['radio']




        if User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            check = "taken"
            context = {
                'check': check
            }
            return render(request, 'registration.html', context)

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_staff = True
        myuser.save()

        if isteach == "creator":
            my_group = Group.objects.get(name='creator')
            my_group.user_set.add(myuser)
            record = Creator(username=username, email=email)
            record.save()
        elif isteach == "student":
            my_group = Group.objects.get(name='student')
            my_group.user_set.add(myuser)
            record = Student(username=username)
            record.save()






        # check = ""
        # if pass1 != pass2:
        #     messages.error(request, "Passwords didn't matched!!")
        #     check = "taken"
        #     context = {
        #         'check': check
        #     }
        #     return render(request, 'base.html', context)


        messages.success(request, "Your account has been signed up successfully!")
        return redirect('login')

    return render(request, "registration.html")


def my_logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def my_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'my_profile.html', context)
