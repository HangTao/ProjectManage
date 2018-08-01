import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from ProjectManage.models import User, Project, Department, Company_file


def do_login(request):
    if request.method == 'GET':
        return render(request,'ProjectManage/login.html')

    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return redirect(reverse('PM:home'))
    else:
        return render(request,'ProjectManage/login.html',{
            'username':username,
            'password':password,
            'errorMessage':'请您输入正确的用户名或密码！'
        })

@login_required(login_url='PM:login')
def home(request):
    return render(request,'ProjectManage/home.html')


def user_project_list(request):
    return render(request, 'ProjectManage/user_project_list.html')

def get_projects(request):
    data = serializers.serialize('json',Project.objects.all())
    return HttpResponse(data)

def get_user_project_list(request):
    # projects = Project.objects.all()
    # page =  get_page(request)
    # print(page)
    # data = serializers.serialize('json',projects)
    data = {
        "rows": [{"id": "123", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "124", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "125", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "126", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "127", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "128", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "129", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1210", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1211", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1212", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1213", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1214", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1215", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1216", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"},
                 {"id": "1217", "name": "张三", "sex": "0", "birthday": 326044800000, "grade": "一年级四班",
                  "address": "湖北省武汉市 430017江岸区沿江大道159号"}],
        "results": 40
    }
    return HttpResponse(json.dumps(data))

def project_list(request):
    return render(request,'ProjectManage/project_list.html')

def get_page(request):
    start = request.GET.get('start')
    limit = request.GET.get('limit')
    pageIndex = request.GET.get('pageIndex')
    return (start,limit,pageIndex,)


class UserListView(ListView):
    model = User
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class DepartmentListView(ListView):
    model = Department
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CompanyFileListView(ListView):
    model = Company_file
    paginate_by = 100
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context