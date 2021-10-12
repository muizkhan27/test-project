from rest_framework import serializers
from teachers.serializers import TeacherSerializer
from .models import OnlineClass

class OnlineClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    class Meta:
        model = OnlineClass
        fields = '__all__'