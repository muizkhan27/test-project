from rest_framework import serializers

from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherMonthInfoSerializer(serializers.Serializer):
    """
    Serializer for month-wise teachers info
    """
    teacher__name = serializers.CharField(max_length=255)
    start__month = serializers.IntegerField()
    duration__sum = serializers.CharField(max_length=255)
