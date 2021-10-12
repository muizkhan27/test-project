from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OnlineClass
from .serializers import OnlineClassSerializer

class OnlineClassListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format='json'):
        queryset = OnlineClass.objects.all()
        serializer = OnlineClassSerializer(queryset, many=True)
        return Response(data=serializer.data)