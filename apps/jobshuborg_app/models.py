from django.db import models
from django.db.models.fields.related import OneToOneField
from apps.jobshubdev_app.models import Framework, Language
from apps.login_app.models import Developer, Organization


class Position(models.Model):
    position_title = models.CharField(max_length=45, blank=False, null=False)
    position_description = models.CharField(max_length=255, blank=False, null=False)
    state_position = models.CharField(max_length=45, blank=False, null=False)
    position_organization = models.ForeignKey(Organization, related_name="organization_position", on_delete = models.CASCADE)
    #una publicacion puede tener muchos lenguajes y un lenguaje puede estar en varias posiciones
    position_language = models.ManyToManyField(Language, blank=True,related_name="language_position")
    position_framework = models.ManyToManyField(Framework, blank=True,related_name="framework_position")

    position_filled_by = models.OneToOneField(Developer, blank=True, null=True ,related_name="developer_position", on_delete=models.Case)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
