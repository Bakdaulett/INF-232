from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


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