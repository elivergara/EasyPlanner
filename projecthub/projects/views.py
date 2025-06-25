from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm
from django.shortcuts import redirect

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Project
from django.contrib import messages

@login_required
def project_list(request):
    sort = request.GET.get('sort', 'due')  # default to due date
    if sort == 'priority':
        projects = Project.objects.filter(user=request.user).order_by('-is_pinned', 'priority', 'due_date')
    elif sort == 'title':
        projects = Project.objects.filter(user=request.user).order_by('-is_pinned', 'title')
    else:  # 'due' or unknown
        projects = Project.objects.filter(user=request.user).order_by('-is_pinned', 'due_date')

    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def toggle_pin(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    project.is_pinned = not project.is_pinned
    project.save()
    return redirect('dashboard')  # or use 'project_list' if that's your URL name



@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # optional: log them in immediately
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


#  Add project creation functionality
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('dashboard')  # or 'project_list'
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


# Create Projects
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('dashboard')  # or 'project_list' or wherever
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

# Edit Projects
@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # or 'project_list'
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'editing': True})

# Enable the Delete Page functions
@login_required
def delete_projects(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_projects')
        if selected_ids:
            projects_to_delete = Project.objects.filter(id__in=selected_ids, user=request.user)
            deleted_count = projects_to_delete.count()
            projects_to_delete.delete()
            messages.success(request, f"{deleted_count} project(s) deleted.")
        else:
            messages.warning(request, "No projects were selected for deletion.")
        return redirect('dashboard')

    projects = Project.objects.filter(user=request.user).order_by('title')
    return render(request, 'projects/delete_projects.html', {'projects': projects})
