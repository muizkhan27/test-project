from django.urls import path

from .views import TeacherMonthInfoView

urlpatterns = [
    path('teachers/info', TeacherMonthInfoView.as_view(), name='teacher_info_list'),
]
