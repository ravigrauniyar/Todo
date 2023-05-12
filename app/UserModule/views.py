from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .forms import loginForm, todoForm
from .models import todo

# todo.objects.all().delete()


def HomePage(request):
    details = {
        'title': 'Home',
        'loginForm': loginForm
    }
    return render(request, 'Home.html', details)


def LoginPage(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return redirect('/View-Todo')
            else:
                details = {
                    'title': 'Login',
                    'loginForm': loginForm,
                    'invalidMsg': 'Invalid username or password'
                }
                return render(request, 'Home.html', details)


def ViewTodo(request):

    todoList = todo.objects.all()
    details = {
        'todoList': todoList,
        'title': 'View Todo',
    }
    return render(request, 'View-Todo.html', details)


def DeleteTodo(request, todo_id):
    todoEntry = get_object_or_404(todo, id=todo_id)
    todoEntry.delete()
    return redirect('/View-Todo')

def WriteTodo(request):
    if request.method == 'POST':
        editTodoForm = todoForm(request.POST)
        if editTodoForm.is_valid():
            title = editTodoForm.cleaned_data['todo_title']
            details = editTodoForm.cleaned_data['todo_details']

            todoEntry = todo(todo_title = title, todo_details = details)
            todoEntry.save()
            return redirect('/View-Todo')

    details = {
        'title': 'Write Todo',
        'todoForm': todoForm
    }
    return render(request, 'Write-Todo.html', details)

def EditTodo(request, todo_id):

    if request.method == 'POST':
        editTodoForm = todoForm(request.POST)
        if editTodoForm.is_valid():
            title = editTodoForm.cleaned_data['todo_title']
            details = editTodoForm.cleaned_data['todo_details']

            todoEntry = todo.objects.get(id=todo_id)

            todoEntry.todo_title = title
            todoEntry.todo_details = details
            todoEntry.save()
            return redirect('/View-Todo')

    else:
        todoEntry = get_object_or_404(todo, id=todo_id)
        title = todoEntry.todo_title
        details = todoEntry.todo_details

        editTodoForm = todoForm(
            initial={'todo_title': title, 'todo_details': details})

        data = {
            'title': 'Edit Activity',
            'todoForm': editTodoForm,
            'todo_id': '/'+str(todo_id)+'/'
        }
        return render(request, 'Write-Todo.html', data)
