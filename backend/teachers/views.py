from classes.models import OnlineClass
from django.db.models import Sum
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TeacherMonthInfoSerializer


class TeacherMonthInfoView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format="json"):
        """
        Accepts GET request, returns month-wise teachers duration
        """
        queryset = OnlineClass.objects.values('teacher__id', 'teacher__name', 'start__month').annotate(Sum("duration"))
        serializer = TeacherMonthInfoSerializer(queryset, many=True)
        return Response(serializer.data)
