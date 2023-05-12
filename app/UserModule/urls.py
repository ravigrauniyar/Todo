from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="Home"),
    path('Login', views.LoginPage, name="Login"),
    path('View-Todo', views.ViewTodo, name="ViewTodo"),
    path('Write-Todo', views.WriteTodo, name='WriteTodo'),
    path('Write-Todo/<int:todo_id>/', views.EditTodo, name='WriteTodo'),
    path('Delete-Todo/<int:todo_id>/', views.DeleteTodo, name='DeleteTodo'),
]
