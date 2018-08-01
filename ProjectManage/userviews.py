import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from ProjectManage.models import User


def user_add(request):
    '''
    创建新用户
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request,'ProjectManage/login.html')

    l_name = request.POST.get('l_name','')
    l_password = request.POST.get('l_password','')
    print("用户名:%s ;密码:%s" %(l_name,l_password))
    data = {
        "code":1,
        "message":"添加用户成功"
    }
    return HttpResponse(json.dumps(data))


def user_list(request):
    '''
    获取用户列表
    :param request:
    :return:
    '''
    users = User.objects.all()
    data = [{"u_name":user.u_name,"u_sex":user.u_sex,"u_phone":user.u_phone,"u_status":user.u_status} for user in users]
    return HttpResponse(json.dumps(data))