from django.urls import path
from project.views import project_views

urlpatterns = [
    # 项目列表
    path('list/', project_views.list)
]