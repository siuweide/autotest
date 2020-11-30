from django.shortcuts import render
from project.models import Project
from django.http import JsonResponse

# 项目列表
def list(request):
    pj_list = Project.objects.filter(status=True)
    return render(request, 'project/list.html', {
        'pj_list': pj_list
    })

# 创建项目
def add(request):
    name = request.POST.get('name', '')
    describe = request.POST.get('describe', '')
    status = request.POST.get('status', '')
    if status == 'true':
        real_status = True

    Project.objects.create(name=name, describe=describe, status=real_status)

    return JsonResponse({"code": 200, "msg": "success"})


