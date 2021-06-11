from django.db.models.base import Model
from apps.login_app.models import Developer
from django import forms
from django.forms import ModelForm


class UpdateDeveloper(ModelForm):
    class Meta:
        model = Developer
        fields = {'address_name','address_number','address_detail'}

        widgets = {
            'address_name': forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
            'address_number' : forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;", "onkeypress":"isInputNumber(event)"}),
            'address_detail' : forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
        }


        labels = {
                'address_name': "Nombre de la calle",
                'address_number' : "Número del domicilio",
                'address_detail' : "Detalle del domicilio Casa/Departamento (opcional)",

        }

