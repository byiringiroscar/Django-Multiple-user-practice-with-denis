from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout'),
]
