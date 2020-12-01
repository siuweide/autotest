from django.shortcuts import render

from project.models import Project
from project.forms import AddProjectForm

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

# 修改项目
# def update(request, id):
#
#     # project = Project.objects.filter(pk=id)
#     pass