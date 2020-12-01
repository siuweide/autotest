from django.shortcuts import render, redirect

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
        print('进入get请求')
        form = AddProjectForm()
        return render(request, 'project/add.html', {
            'form':  form
        })
    elif request.method == 'POST':
        print('进入post请求')
        form = AddProjectForm(request.POST)
        if form.is_valid():
            print('表单验证成功')
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']

            Project.objects.create(name=name, describe=describe, status=status)
            return redirect('/project/list/')

# 修改项目
# def update(request, id):
#
#     # project = Project.objects.filter(pk=id)
#     pass