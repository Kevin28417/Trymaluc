from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("creacion", ) 
