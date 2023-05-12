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
from django.db import transaction

# Create your views here.
def index(request):
    isTeacher = False
    for g in request.user.groups.all():
        if g.name == 'creator':
            isTeacher = True
            break

    quizzes = Quiz.objects.all()
    
    if isTeacher:
        quizzes = quizzes.filter(creator_id = request.user.id)
    context={
        'isTeacher':isTeacher,
        'quizzes':quizzes,
    }
    return render(request, "base.html", context)


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
            record = Creator(creator_id=myuser.id, username=username, email=email)
            record.save()
        elif isteach == "student":
            my_group = Group.objects.get(name='student')
            my_group.user_set.add(myuser)
            record = Student(user_id=myuser.id, username=username)
            record.save()


        check = ""
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            check = "taken"
            context = {
                'check': check
            }
            return render(request, 'base.html', context)


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




def test(request):
    quiz = Quiz.objects.all()
    context = {
        'quiz': quiz,
    }
    return render(request, 'test.html', context)

def QuizCreation(request):
    template = loader.get_template('addQuiz.html')
    context = {}
    return HttpResponse(template.render(context, request))

@permission_required("quizapp.add_quiz")
@transaction.atomic
def addQuiz(request):
    title = request.POST['title']
    questions = request.POST.getlist('question')
    answers = request.POST.getlist('answer')

    if len(questions) != len(answers):
            redirect("/error-page")

    quiz = Quiz(topic=title, creator_id=Creator.objects.get(creator_id=request.user.id))
    quiz.save()

    for i in range (0, len(questions)):
        q = Question(question=questions[i], answer=answers[i], quiz_id=quiz)
        q.save()
        options = request.POST.getlist("q" + str(i + 1) + "options")
        for option in options:
            o = Variant(variant=option, qa_id=q)
            o.save()

    return redirect("/")

