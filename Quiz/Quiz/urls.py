"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from quizapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.my_login_view, name='login'),
    path('logout/', views.my_logout_view, name='logout'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('registration/', views.my_registration_view, name='registration'),
    path('createQuiz/', views.QuizCreation, name='addQuiz'),
    path('addQuiz/', views.addQuiz),
    path('quiz/<int:id>/', views.question, name='quiz'),
    path('teacher_results/<int:id>/', views.teacher_results, name='teacher_results'),
    path('profile/', views.profile, name='profile'),
]
