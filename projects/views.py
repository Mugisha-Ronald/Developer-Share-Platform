from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.


# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website',
#         'topRated' : True
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work',
#         'topRated' : False
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community',
#         'topRated' : True
#     }
# ]

def projects(request):
    projects = Project.objects.all()
    context = {"projects":projects}
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    # projectObject = None
    # for i in projectsList:
    #     if i['id'] == str(pk):
    #         projectObject = i 

    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.review_set.all()
    context = {'project':projectObj,'tags':tags,'reviews':reviews}
    return render(request, 'projects/single-project.html', context)



def createProject(request):

    form = ProjectForm()
    # if request.method == 'POST':
    #     print("FORM DATA:",request.POST)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project-form.html',context)



def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()

            return redirect('projects')

    context = {'form':form}

    return render(request,'projects/project-form.html',context)



def deleteProject(request,pk):

    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request,'projects/delete.html',{'object':project})


