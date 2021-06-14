from django.db.models.base import Model
from apps.jobshubdev_app import models
from apps.login_app.models import Developer
from django import forms
from django.forms import ModelForm
from apps.jobshubdev_app.models import Biography

class BiographyForm(ModelForm):
    class Meta:
        model = Biography
        fields = ['short_bio','github_link']
        widgets = {
            'short_bio': forms.Textarea(attrs = {"class":"form-control ", "rows":4, "cols": "50%" , "style":"resize: none;"}),

        }

        labels = {
                'short_bio': "Breve descripción profesional:",
        }

    def clean(self):
        cleaned_data = super(BiographyForm, self).clean()
        short_bio = cleaned_data.get("short_bio")
        if len(short_bio) < 10:
            raise forms.ValidationError(
                "Error: Su descripción debe ser mayor a 10 caracteres"
            )

        if len(short_bio) > 255:
            raise forms.ValidationError(
                "Error: Su descripción debe ser menor a 255 caracteres"
            )