from django.urls import path
from project.views import project_views

urlpatterns = [
    # 项目列表
    path('list/', project_views.list),
    # 添加项目
    path('add/', project_views.add),
    # 修改项目
    path('update/<int:id>/', project_views.update)
]