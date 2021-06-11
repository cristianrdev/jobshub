from django.db import models
from apps.login_app.models import Developer

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




class Biography(models.Model):
    short_bio = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(Developer, related_name="user_biography", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)