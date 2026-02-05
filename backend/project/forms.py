from django import forms

class Project(forms.Forms):
    name = forms.CharField(max_length=255)
    description = forms.TextField()
    status = forms.BooleanField(default=True)
    hours_consumed = forms.FloatField()
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()