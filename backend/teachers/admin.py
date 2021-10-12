from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    model = Teacher

admin.site.register(Teacher, TeacherAdmin)