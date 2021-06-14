from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms
from django.db import models
import re
from django.contrib.auth.hashers import make_password, check_password
from datetime import date




MIN_FIELD_LENGHT = 2
def ValidarLongitudMinima(cadena):
    if len(cadena) < MIN_FIELD_LENGHT:
        raise forms.ValidationError(
            f'Error:  Se necesitan mas de {MIN_FIELD_LENGHT} caracteres'
        )

def ValidarLongitudPassword(cadena):
    if len(cadena) < 8:
        raise forms.ValidationError(
            f'Error: la contraseña al menos debe contener 8 caracteres'
        )




def validarEmail(cadena):
    #valida que el email tenga el formato correcto
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not EMAIL_REGEX.match(cadena):          
        raise forms.ValidationError(
            f'Error de formato: {cadena} no es un e-mail valido'
        )
    #valida que el email no se repita
    
    for s in Developer.objects.all():
            # se usa .lower() para ovbiar las mayúsculas en la comparación de palabras
            if cadena.lower() == s.email.lower(): 
                raise forms.ValidationError(
                f'Error: el email {cadena} ya existe en nuestros registros!'
                )


def validarFecha(fecha):
    print(fecha)
    date_today = date.today() #fecha hoy 
    birth_date = str(fecha).split('-')
  
    birth_year = int(birth_date[0]) #año nacimieno
    birth_month = int(birth_date[1]) #mes de nacimiento
    birth_day = int(birth_date[2]) #día de nacimiento

    
    print(birth_date)
    birth_date_user = date(birth_year, birth_month, birth_day )
    days_has_passed = (date_today-birth_date_user).days
    # valida la edad mayor a 18 años
    if days_has_passed < (365.2425*18): #aqui se cambia la edad de acceso---------------------
            raise forms.ValidationError(
            f'Error: la fecha de nacimiento debe ser mayor de 18 años'
            )

numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')



# Create your models here.
class Developer(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False, validators=[ValidarLongitudMinima])
    last_name = models.CharField(max_length=30, blank=False, null=False, validators=[ValidarLongitudMinima] )
    email = models.CharField(max_length=30, blank=False, null=False, validators=[validarEmail])
    address_name = models.CharField(max_length=50, blank=False, null=False,validators=[ValidarLongitudMinima])
    address_number = models.CharField(max_length=8, blank=False, null=False, validators=[ValidarLongitudMinima])
    address_detail = models.CharField(max_length=255, blank=True)
    match = models.CharField(max_length=10, blank=True)
    match_proportion = models.CharField(max_length=10, blank=True)
    skills_number = models.CharField(max_length=50, blank=True)

    # phone_number = models.CharField(max_length=50, blank=False, null=False, validators=[numeric])
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Developer, self).save(*args, **kwargs)

    @staticmethod
    def authenticate(email, password):
        dev = Developer.objects.filter(email = email)
        #buscar si hay un email en la base de datos
        if len(dev) == 1:
            #si existe un email asociado
            #se existe un el usuario (se supone que debe ser uno solo por sus validaciones)
            dev = dev[0]
            bd_password = dev.password
            if check_password(password, bd_password): #convierte los hash y los comparas
                return dev
        print("usuario incorrecto")
        
        return None 



class Organization(models.Model):
   
    org_name = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitudMinima])
    first_name = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitudMinima])
    last_name = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitudMinima] )
    email = models.CharField(max_length=50, validators=[validarEmail])
    address_name = models.CharField(max_length=50, blank=False, null=False, validators=[ValidarLongitudMinima])
    address_number = models.CharField(max_length=8, blank=False, null=False, validators=[ValidarLongitudMinima])
    address_detail = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Organization, self).save(*args, **kwargs)

    @staticmethod
    def authenticate(email, password):
        org = Organization.objects.filter(email = email)
        print ('user', org)
        #buscar si hay un email en la base de datos
        if len(org) == 1:
            #si existe un email asociado
            #se existe un el usuario (se supone que debe ser uno solo por sus validaciones)
            org = org[0]
            bd_password = org.password
            if check_password(password, bd_password): #convierte los hash y los comparas
                return org
        print("usuario incorrecto")
        
        return None 

    

