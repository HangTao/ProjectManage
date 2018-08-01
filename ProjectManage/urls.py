from django.urls import path

from ProjectManage import userviews
from ProjectManage.views import UserListView, DepartmentListView, CompanyFileListView
from . import views
from ProjectManage.PMViews.feasibility import EvaluationView
app_name='PM'


urlpatterns = [
    path('login/',views.do_login,name='login'),
    path('home/',views.home,name='home'),
    #todo 用户管理
    path('user/add/'),
    path('user/list/'),
    path('user/detail/<int:pk>'),
    path('user/del/<int:pk>'),
    path('user/edit/<int:pk>'),

    # path('user_project_list/',views.user_project_list,name='user_project_list'),
    # path('get_user_project_list/',views.get_user_project_list,name='get_user_project_list'),
    # path('project_list/',views.project_list,name='project_list'),
    # path('user_list/',UserListView.as_view(),name='user-list'),
    # path('department_list/',DepartmentListView.as_view(),name='department-list'),
    # path('companyfile_list/',CompanyFileListView.as_view(),name='companyfile-list'),
    #
    # path('feasibility_evaluation/',EvaluationView.as_view(),name='feasibility-evaluation'),
    # path('get_projects/',views.get_projects,name='get-projects'),
    #
    # path('user/add/',userviews.user_add,name='user-add'),     #todo 创建新用户
    # path('user/list/',userviews.user_list,name='get-user-list'),
    # path('department/add/'),#todo 创建新部门
    # path('role/add/'),      #todo 创建新角色
    # path('project/add'),    #todo 创建新项目
]