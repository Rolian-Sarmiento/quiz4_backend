from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)
    hours_consumed = models.FloatField()
    user = models.ModelChoiceField(queryset=User.objects.all())
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
# Create your models here.

class TaskCreateScreen(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "hours_consumed", "user", "start_date", "end_date"]
