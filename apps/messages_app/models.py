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




class Message(models.Model):
    message_content = models.CharField(max_length=255, blank=True, null=False, validators=[ValidarLongitudMinima])
    sender_id = models.CharField(max_length=10, blank=False, null=False, validators=[ValidarLongitudMinima])
    reciever_id = models.CharField(max_length=10, blank=False, null=False, validators=[ValidarLongitudMinima])
    user_type = models.CharField(max_length=50, blank=False, null=False, validators=[ValidarLongitudMinima])
    readed = models.BooleanField(max_length=8, default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


