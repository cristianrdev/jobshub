from django.db import models
from apps.login_app.models import Developer
from django import forms
import re

# Create your models here.
class Language(models.Model):
   
    skill_name = models.CharField(max_length=45, blank=False, null=False)
    developer = models.ManyToManyField(Developer, related_name="developer_language")
    icon_link_language = models.CharField(max_length=100, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Framework(models.Model):
   
    skill_name = models.CharField(max_length=45, blank=False, null=False)
    developer = models.ManyToManyField(Developer, related_name="developer_framework")
    icon_link_framework = models.CharField(max_length=100, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def ValidarLongitudMinima(cadena):
    if len(cadena) < 10:
        raise forms.ValidationError(
            f'Error:  Se necesitan mas de {10} caracteres'
        )

def ValidarGithub(cadena):
    p = re.compile('(?:https?://)?(?:www[.])?github[.]com/[\w-]+/?')
    if not p.match(cadena):
        raise forms.ValidationError(
            f'Error: Link GitHub inválido'
        )
# https://github.com/cristianrdev
#  a = "https://in.linkedin.com/afadasdf"
#  p = re.compile('(http(s?)://|[a-zA-Z0-9\-]+\.|[linkedin])[linkedin/~\-]+\.[a-zA-Z0-9/~\-_,&=\?\.;]+[^\.,\s<]')
#  p.match(a)



class Biography(models.Model):
    short_bio = models.CharField(max_length=255, null=True, validators=[ValidarLongitudMinima])
    github_link = models.CharField(max_length=255, null=True, blank=True, validators=[ValidarGithub])
    user = models.OneToOneField(Developer, related_name="user_biography", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)