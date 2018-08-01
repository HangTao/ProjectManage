from django.db import models

# Create your models here.
def func():
    return 1

class Department(models.Model):
    '''
    部门
    '''
    d_name = models.CharField(max_length=100)
    superior_department = models.ForeignKey('self',on_delete=models.CASCADE)


class User(models.Model):
    '''
    系统用户
    '''
    l_name = models.CharField(max_length=50) #登陆名称
    l_pass = models.CharField(max_length=50) #登陆密码
    u_name = models.CharField(max_length=50) #显示名称
    u_sex = models.BooleanField()   #性别
    u_phone = models.CharField(max_length=50) #联系电话
    u_status = models.IntegerField(default=1)  #用户状态，从多方面考虑（在职、离职、删除、休假等）
    u_department = models.ForeignKey(Department,null=True,on_delete=models.SET(func))



class Sys_role(models.Model):
    '''
    系统角色
    '''
    r_name = models.CharField(max_length=50) #角色名称

#
# class Sys_function(models.Model):
#     '''
#     系统功能
#     '''
#     f_name = models.CharField(max_length=50)
#
class File_type(models.Model):
    '''
    文件类型
    '''
    t_name=models.CharField(max_length=100)
    management_department = models.ForeignKey(Department,on_delete=models.SET(func))    #当部门删除后，文件类型归属部门成为总公司


class Company_file(models.Model):
    '''
    公司文件
    '''
    f_name = models.CharField(max_length=1000,default='')                      #文件名称
    f_type = models.ForeignKey(File_type,on_delete=models.SET(func))    #文档类型删除后，文档类型设置为公司私有文档
    f_manager = models.ForeignKey(User,on_delete=models.SET(func))      #文档管理员删除后，文档管理员设置为公司最高管理人
    has_paper = models.BooleanField()                #时候有纸质文件
    pf_path = models.CharField(max_length=1000)     #纸质文件存放位置
    ef_path = models.CharField(max_length=1000)               #电子文件存放位置

class Project_source(models.Model):
    '''
    项目来源
    '''
    ps_name = models.CharField(max_length=50)

class Project_type(models.Model):
    '''
    项目类型
    '''
    pt_name = models.CharField(max_length=50)

class Project(models.Model):
    '''
    项目
    '''
    p_name = models.CharField(max_length=500)   #项目名称
    p_source = models.ForeignKey(Project_source,null=True,on_delete=models.SET_NULL)   #项目来源
    p_type = models.ForeignKey(Project_type,null=True,on_delete=models.SET_NULL)   #项目类型
    p_desc = models.TextField()                 #项目描述
    p_create_user = models.ForeignKey(User,on_delete=models.CASCADE)     #项目创建人
    p_create_datetime = models.DateTimeField()  #项目创建时间
    p_fail_datetime = models.DateTimeField()    #项目失效时间
    p_has_append=models.BooleanField()          #项目描述是否有追加
    p_has_desc_files = models.BooleanField()    #项目是否有相关描述文件
    p_status = models.IntegerField()            #项目状态
#
# class Project_role(models.Model):
#     '''
#     项目角色
#     '''
#     r_name = models.CharField(max_length=100)
#
#
# class Project_file(models.Model):
#     '''
#     项目资料文件
#     '''
#     project = models.ForeignKey(Project)
#     applicant = models.ForeignKey(User)
#     approver = models.ForeignKey(User)
#     application_time = models.DateTimeField()
#     approve_time = models.DateTimeField()
#
#

