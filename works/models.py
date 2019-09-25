import uuid
from django.db import models
from django.contrib.auth.models import User
from .enums import LocationType

USER_IP_ADDRESS = ''

class Project(models.Model):
    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Projects"

    def __str__(self):
        return u"{}".format(self.name)

class Works(models.Model):
    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    project = models.ForeignKey(
        Project, models.DO_NOTHING,
        related_name='works_of_project'
    )
    employee = models.ForeignKey(
        User, models.DO_NOTHING,
        related_name='works_of_user'
    )
    date =  models.DateField()
    Location = models.IntegerField(
        choices=[(choice.value, choice.name.replace("_", " ")) for choice in LocationType],
        default=LocationType.INSIDE.value
    )
    details = models.TextField(blank=True, null=True)
    working_hour = models.PositiveIntegerField(help_text='eg: 8 Hours')
    is_cod = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Works"

    def __str__(self):
        return u"#{}: {}".format(self.employee, self.project)
