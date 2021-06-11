from django.db import models
from django.db.models.fields.related import OneToOneField
from apps.jobshubdev_app.models import Framework, Language
from apps.login_app.models import Developer, Organization


class Position(models.Model):
    position_title = models.CharField(max_length=45, blank=False, null=False)
    position_description = models.CharField(max_length=255, blank=False, null=False)
    state_position = models.CharField(max_length=45, blank=False, null=False)
    position_organization = models.ForeignKey(Organization, related_name="organization_position", on_delete = models.CASCADE)
    position_language = models.ForeignKey(Language, related_name="language_position", on_delete = models.CASCADE)
    position_framework = models.ForeignKey(Framework, related_name="framework_position", on_delete = models.CASCADE)
    position_filled_by = models.OneToOneField(Developer, related_name="developer_position", on_delete=models.Case)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class StatePosition(models.Model):
#     state_name = models.CharField(max_length=45, blank=False, null=False)
#     state_position = models.ForeignKey(Framework, related_name="position_state", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
