from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.models import Group
from account.decorators import unauthenticated_user, allowed_user, teacher_only


# Create your views here.

def home(request):
    return render(request, 'home.html')


@unauthenticated_user
def teacher(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            messages.success(request, "successful registered" + username)
            return redirect('login_page')

    context = {
        'form': form
    }
    return render(request, 'teacher.html', context)


def student(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # so commented this because we created signals for it to disable it and use customer disable signals and apps.py
            # group = Group.objects.get(name='student')
            # user.groups.add(group)
            messages.success(request, "successful registered  " + username)
            return redirect('login_page')


    context = {
        'form': form
    }
    return render(request, 'student.html', context)


@login_required(login_url='login_page')
# @allowed_user(allowed_roles=['teacher'])
@teacher_only
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


def student_dashboard(request):
    return render(request, 'student_dashboard.html')


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('teacher_dashboard')
        else:
            messages.info(request, 'credential not match')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('login_page')
