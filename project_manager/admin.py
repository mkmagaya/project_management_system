from django.contrib import admin
from .models import Project, Task, Comment
from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy


# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)

admin.site.site_header = 'Project Management System'
admin.site.index_title = 'PMS Login Portal'
admin.site.site_title = 'Project Management System'
