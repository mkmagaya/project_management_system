from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail

# read
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def home_view(request):
    return render(request, 'home.html')

# create
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

# update
login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, 'task': task})

# authentication
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # Perform authentication and login
        # ...
        return redirect('task_list')
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_view')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# email notifications
def send_notification(user, task):
    subject = 'New Task Assigned'
    message = f'You have been assigned a new task: {task.title}'
    send_mail(subject, message, 'makomagaya05@gmail.com', [user.email])

# task assignment
@login_required
def assign_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            assigned_to = form.cleaned_data['assigned_to']
            task.assigned_to = assigned_to
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'assign_task.html', {'form': form, 'task': task})

# report generation
@login_required
def generate_report(request):
    completed_tasks = Task.objects.filter(status='completed').count()
    total_tasks = Task.objects.all().count()
    completion_rate = (completed_tasks / total_tasks) * 100
    return render(request, 'report.html', {'completion_rate': completion_rate})

def logout_view(request):
    logout(request)
    return redirect('home')
