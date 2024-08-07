from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Project
from modelform.forms import ProjectForm

# Create your views here.


def index(request):
    return render(request, "modelform/index.html")


def listprojects(request):
    projects = Project.objects.all()

    return render(request, "modelform/listprojects.html", {"projects": projects})


def addproject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project added successfully!")
            return redirect("index")

    else:
        form = ProjectForm()

    return render(request, "modelform/addproject.html", {"form": form})
