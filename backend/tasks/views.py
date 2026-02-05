from django.shortcuts import render
from django.http import JsonResponse

def getRoutes(request):
    routes = [
        '/api/v1/project/', # HomeScreen (/api/v1/projects)
        '/api/v1/projects/<id>', # DetailScreen (/api/v1/projects/<id>)
        '/api/v1/project/create/', # ProjectCreateScreen (/api/v1/projects/create/)
    ]
# Create your views here.
