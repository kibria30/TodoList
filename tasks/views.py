from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# def Home(request):
    
#     tasks = Task.objects.all()
    
#     return render(request, 'tasks/home.html', {'tasks': tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'
    ordering = ['-pk']
    
class TaskDetailView(DetailView):
    model = Task
    
class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-home')
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task-home')

# def task(request):
#     return HttpResponse('Enter a new task.')

# def taskFormView(request):
    
    
#     if request.method == "POST":
#         form = TaskModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#     else:
#         form = TaskModelForm()
#         context = {'form' : form}

#     return render(request, 'tasks/taskForm.html', context)
