from django.contrib import admin

from webapp.models import IssueTracker, Status, Type, Project

admin.site.register(IssueTracker)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
