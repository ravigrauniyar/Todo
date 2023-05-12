from django.utils import timezone
from django.db import models


class users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class todo(models.Model):
    todo_date = models.DateTimeField(default= timezone.now)
    todo_title = models.CharField(max_length=30)
    todo_details = models.TextField()

# user1 = users(username='ravi', password='pwd')
# user1.save()

