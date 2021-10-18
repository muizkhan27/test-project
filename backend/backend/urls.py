from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('classes.urls')),
    path('api/', include('teachers.urls')),
]
