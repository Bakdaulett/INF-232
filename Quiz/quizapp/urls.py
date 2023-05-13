from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login_view, name='login'),
    path('registration/', views.my_registration_view, name='registration'),
    path('logout/', views.my_logout_view, name='logout'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('teacher_results/', views.teacher_results, name='teacher_results'), # add this line
]
