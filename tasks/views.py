from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskModelForm
from django.views.generic import ListView, DetailView, CreateView
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

def task(request):
    return HttpResponse('Enter a new task.')

def taskFormView(request):
    
    
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TaskModelForm()
        context = {'form' : form}

    return render(request, 'tasks/taskForm.html', context)



def change_state(request, ):
    if request.method == "POST":
        # Get the record ID from the POST data
        record_id = request.POST.get('record_id')
        
        # Fetch the record from the database
        record = get_object_or_404(Task, id=record_id)
        
        # Modify the record's state (or any other field)
        record.complete = True  # Change state to the desired value
        record.save()  # Save the changes to the database
        
        # Redirect or render a template after updating the record
        return redirect('home')  # Redirect to home page or another view
