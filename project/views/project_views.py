from django.shortcuts import render, redirect

from project.models import Project
from project.forms import AddProjectForm, EditProjectForm

# 项目列表
def list(request):
    pj_list = Project.objects.filter(status=True)
    return render(request, 'project/list.html', {
        'pj_list': pj_list
    })

# 创建项目
def add(request):
    if request.method == 'GET':
        form = AddProjectForm()
        return render(request, 'project/add.html', {
            'form':  form
        })
    elif request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']

            Project.objects.create(name=name, describe=describe, status=status)
            return redirect('/project/list/')

# 修改项目
def edit(request, id):
    if request.method == 'GET':
        if id:
            project = Project.objects.get(pk=id)
            form = EditProjectForm(instance=project)
            return render(request, 'project/edit.html', {
                'form': form,
                'pid': id
            })
    elif request.method == 'POST':
        project = Project.objects.get(pk=id)
        form = EditProjectForm(request.POST)
        if form.is_valid():
            project.name = form.cleaned_data['name']
            project.describe = form.cleaned_data['describe']
            project.status = form.cleaned_data['status']
            project.save()
            return redirect('/project/list/')
