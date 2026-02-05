from django.db import models
from django.forms import ModelForm

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)
    hours_consumed = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

class ProjectCreateScreen(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "status", "hours_consumed", "start_date", "end_date"]
# Create your models here.
