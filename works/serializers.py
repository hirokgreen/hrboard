import datetime
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
)

from .models import Project, Works

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name',
        )

class WorkBasicSerializer(ModelSerializer):
    class Meta:
        model = Works
        fields = (
            'date',
            'project',
            'working_hour',
            'location',
            'is_cod',
            'details',
            'note'
        )

    def validate_date(self, value):
        today = datetime.datetime.today().date()
        if value < today:
            raise ValidationError('You can\'t select previous date instead of today')
        elif value > today:
            raise ValidationError('You can\'t select future date instead of today')
        return value

class WorkListSerializer(WorkBasicSerializer):
    project = ProjectSerializer()