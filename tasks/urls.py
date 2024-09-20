from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    # path('', views.Home, name="Task-Home"),
    path('', TaskListView.as_view(), name="task-home"),
    path('task/', TaskListView.as_view(), name="task-home"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name="task-create")
    # path('task/new/', views.taskFormView, name="TaskForm")
]
