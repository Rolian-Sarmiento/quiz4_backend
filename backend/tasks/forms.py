from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class TaskCreateScreen(forms.Forms):
    name = forms.CharField(max_length=255)
    description = forms.TextField()
    status = forms.BooleanField(default=True)
    hours_consumed = forms.FloatField()
    user = forms.ModelChoiceField(queryset=User.objects.all())
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()