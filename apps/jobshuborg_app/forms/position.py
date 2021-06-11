from django.forms import ModelForm
from django import forms
from django.forms import widgets
from apps.jobshuborg_app.models import Position


class PositionForm(ModelForm):

    class Meta:
        model = Position
        fields = ['position_title', 'position_description']

        widgets = {
            'position_description': forms.Textarea(attrs = {"class":"form-control ", "rows":4, "cols": "25%" , "style":"resize: none;"}),

        }

        labels = {

                "position_title" : "Titulo de la oferta de trabajo",
                "position_description" : "Descripción de la oferta de trabajo",

        }


        def clean(self):
            cleaned_data = super(PositionForm, self).clean()
            position_title = cleaned_data.get("position_title")
            position_description = cleaned_data.get("position_description")
   

            if position_title < 3:
                raise forms.ValidationError(
                    "Error: EL título debe tener al menos 3 caracteres"
                )
            
            if position_description <10:
                raise forms.ValidationError(
                    "Error: La descripción debe tener al menos 8 caracteres"
                )