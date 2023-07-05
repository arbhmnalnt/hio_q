from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class AyadaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Ayada, AyadaAdmin)

class VisitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'ayada', 'count', 'created_by', 'created_at')

admin.site.register(Visit, VisitAdmin)
