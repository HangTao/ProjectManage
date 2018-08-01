from django.contrib import admin

# Register your models here.
from ProjectManage.models import User, Project, Project_type, Department, Company_file, File_type, Project_source

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Project_type)
admin.site.register(Project_source)
admin.site.register(Department)
admin.site.register(File_type)
admin.site.register(Company_file)