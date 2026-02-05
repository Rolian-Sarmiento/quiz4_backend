from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
    )

class UserCreateScreen(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "role"]


# Create your models here.
