from django import forms

class loginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'id': 'form1Example1',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'form-control',
            'id': 'form1Example1',
        })
    )
class todoForm(forms.Form):
    todo_title = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'id': 'form1Example1',
        })
    )
    todo_details = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'form1Example1',
            'rows': '4',
        })
    )
