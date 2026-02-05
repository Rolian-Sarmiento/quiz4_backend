from django.shortcuts import render

def getRoutes(request):
    routes = [
        '/api/v1/users', # UserListScreen (/api/v1/users)
        '/api/v1/users/create/', # UserCreateScreen (/api/v1/users/create/)
    ]
# Create your views here.
