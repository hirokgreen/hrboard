from rest_framework import generics, permissions

from .models import Works
from .serializers import (
    WorkListSerializer,
    WorkBasicSerializer
)


class WorkList(generics.ListCreateAPIView):
    """Get all WorksLog and create new one"""
    permission_classes = (
        permissions.IsAuthenticated,
    )
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkListSerializer
        return WorkBasicSerializer
    
    def get_queryset(self):
        return Works.objects.filter(
            employee=self.request.user,
        )
    
    def perform_create(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, 'employee'):
            self.create_data['employee'] = self.request.user
        serializer.save(**self.create_data)
