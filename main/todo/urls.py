from django.urls import path
from .views import TodoAction

urlpatterns =[
    path('todo/create', TodoAction.create(),name='task_create'),
    
    path('',TodoAction.read(),name='task_list'),
    path('todos',TodoAction.read(),name='task_list'),
    path('todo',TodoAction.read(),name='task_list'),
    
    path('todo/<int:pk>/update', TodoAction.update(),name='task_update'),
    path('todo/<int:pk>/delete', TodoAction.delete(),name='task_delete'),
]