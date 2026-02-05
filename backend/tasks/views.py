from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def getRoutes(request):
    routes = [
        '/api/v1/projects/<id>/task/create/', # TaskCreateScreen (/api/v1/projects/<id>/task/create/)
    ]

@api_view(['GET'])
def getProject(request, pk):
    project = None
    for i in project:
        if i['_id'] == pk:
            project = i
            break
        return Response(project)
# Create your views here.
