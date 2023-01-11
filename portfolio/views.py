from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import BasePermission

from users.models import User
from users.serializers import UserSerializer


class ResumeAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        queryset = User.objects.prefetch_related(
            'education',
            'experience',
            'portfolio',
            'speciality'
        )
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def patch(self, request, format=None):
        queryset = get_object_or_404(User,
                                     id=request.user.id)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
