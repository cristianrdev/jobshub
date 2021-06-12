from django.db import models
from django import forms
from django.db.models.fields.related import OneToOneField
from apps.jobshubdev_app.models import Framework, Language
from apps.login_app.models import Developer, Organization



MIN_FIELD_LENGHT = 2
def ValidarLongitudMinima(cadena):
    if len(cadena) < MIN_FIELD_LENGHT:
        raise forms.ValidationError(
            f'Error:  Se necesitan mas de {MIN_FIELD_LENGHT} caracteres'
        )


class MessageOrg(models.Model):
    message_content = models.CharField(max_length=255, blank=True, null=False, validators=[ValidarLongitudMinima])
    message_to_developer = models.ForeignKey(Developer, related_name="developer_message", on_delete = models.CASCADE)
    message_created_by = models.ForeignKey(Organization, related_name="organization_message", on_delete = models.CASCADE)
    readed_for_developer = models.BooleanField(max_length=8, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class MessageDev(models.Model):
#     message_content = models.CharField(max_length=8, blank=True, null=False, validators=[ValidarLongitudMinima])
#     message_to_organization = models.ForeignKey(Organization, related_name="developer_message", on_delete = models.CASCADE)
#     message_created_by = models.ForeignKey(Organization, related_name="organization_message", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
