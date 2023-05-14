from django.urls import path
from .views import TodoAction

urlpatterns = [
    path('', TodoAction.HomePage, name="Home"),
    path('Login', TodoAction.LoginPage, name="Login"),
    path('View-Todo', TodoAction.ViewTodo, name="ViewTodo"),
    path('Write-Todo', TodoAction.WriteTodo, name='WriteTodo'),
    path('Write-Todo/<int:todo_id>/', TodoAction.EditTodo, name='WriteTodo'),
    path('Delete-Todo/<int:todo_id>/', TodoAction.DeleteTodo, name='DeleteTodo'),
]
