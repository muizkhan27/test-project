from django.urls import path

from .views import (
    OnlineClassListView
)

urlpatterns = [
    path('classes/', OnlineClassListView.as_view(), name='class_list'),
]