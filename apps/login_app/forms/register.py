from django.forms import ModelForm
from django import forms
from ..models import  Developer, Organization
from django.forms import widgets



class DeveloperForm(ModelForm):
    # password=forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control", "style":"width: auto;"}), label='Contraseña')
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control", "style":"width: auto;"}), label='Confirme su contraseña')
    class Meta:
        model = Developer
        fields = {'first_name', 'last_name', 'email', 'address_name', 'address_number', 'address_detail', 'password', 'confirm_password' }
        

        widgets = {
                'first_name': forms.TextInput(attrs = {"class":"form-control", "style":"width: auto;"}),
                'last_name': forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
                'email': forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),   
                'address_name': forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
                'address_number' : forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;", "onkeypress":"isInputNumber(event)"}),
                'address_detail' : forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
                'password' : forms.PasswordInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
                    
            }
    
        labels = {
                'first_name': "Nombre",
                'last_name': "Apellido",
                'email': "Correo Electronico",
                'address_name': "Nombre de la calle",
                'address_number' : "Número del domicilio",
                'address_detail' : "Detalle del domicilio Casa/Departamento (opcional)",
                'password': "Contraseña",
                'confirm_password': "Confirme su contraseña"

        }

    def clean(self):
            cleaned_data = super(DeveloperForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "Error: La contraseña de confirmación no coincide"
                )



class OrganizationForm(ModelForm):

    password=forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control", "style":"width: 50%;"}), label='Contraseña')
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control", "style":"width: 50%;"}), label='Confirme su contraseña')
    class Meta:
        model = Organization
        fields = '__all__'

        widgets = {
                'org_name': forms.TextInput(attrs = {"class":"form-control", "style":"width: auto;"}),
                'first_name': forms.TextInput(attrs = {"class":"form-control", "style":"width: auto;"}),
                'last_name': forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
                'email': forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),   
                'address_name': forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
                'address_number' : forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;", "onkeypress":"isInputNumber(event)"}),
                'address_detail' : forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;"}),
                # 'phone_number' : forms.TextInput(attrs = {"class":"form-control ", "style":"width: auto;", 'type':'number'}),       
            }
    
        labels = {
                'org_name': "Nombre de su empresa",
                'first_name': "Nombre representante",
                'last_name': "Apellido representante",
                'email': "Correo Electronico",
                'address_name': "Nombre de la calle",
                'address_number' : "Número del domicilio",
                'address_detail' : "Detalle del domicilio Casa/Departamento (opcional)",
                # 'phone_number' : "Teléfono",
                'password': "Contraseña",
                'confirm_password': "Confirme su contraseña"

        }

    def clean(self):
            cleaned_data = super(OrganizationForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "Error: La contraseña de confirmación no coincide"
                )
        

