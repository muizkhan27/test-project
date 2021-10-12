from django.contrib import admin
from .models import OnlineClass

class OnlineClassAdmin(admin.ModelAdmin):
    model = OnlineClass

admin.site.register(OnlineClass, OnlineClassAdmin)