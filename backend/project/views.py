from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from forms import ProjectCreateScreen

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/v1/projects/', # HomeScreen (/api/v1/projects)
        '/api/v1/projects/<id>', # DetailScreen (/api/v1/projects/<id>)
        '/api/v1/projects/create/', # ProjectCreateScreen (/api/v1/projects/create/)
    ]
    return Response(routes)

@api_view(['GET'])
def getProject(request, pk):
    project = None
    for i in project:
        if i['_id'] == pk:
            project = i
            break
        return Response(project)
# Create your views here.

def ProjectCreateScreen(request):
    if request.method == 'POST':
        form = ProjectCreateScreen(request.POST)
        if form.is_valid():
            return redirect('/api/v1/projects/') 
    else:
        form = ProjectCreateScreen()
    return render(request, '/api/v1/projects/create/', {'form': form})