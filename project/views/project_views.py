from django.shortcuts import render
from project.models import Project

# 项目列表
def list(request):
    pj_list = Project.objects.filter(status=True)
    return render(request, 'project/list.html', {
        'pj_list': pj_list
    })
