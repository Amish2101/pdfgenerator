from django.contrib import admin
from .models import user, reports, pathology, cbcreport
# Register your models here.

class pathologyInline(admin.StackedInline):
    model = pathology
    extra = 3


class pathologyadmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['user','report_name']}),
    ]
    inlines = [pathologyInline]

admin.site.register(user)
admin.site.register(reports, pathologyadmin)
admin.site.register(pathology)
admin.site.register(cbcreport)
