from django import forms

class UserCreateScreen(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    role = forms.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
    )