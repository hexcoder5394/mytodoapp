from django.contrib import admin
from .models import atasks, ftasks

class atasksAdmin(admin.ModelAdmin):
  list_display = ("id", "task", "pri", "date",)
  
admin.site.register(atasks, atasksAdmin)

class ftasksAdmin(admin.ModelAdmin):
  list_display = ("id", "task", "pri", "date",)
  
admin.site.register(ftasks, ftasksAdmin)

