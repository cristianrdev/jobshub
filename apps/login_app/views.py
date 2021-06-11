from django.shortcuts import render, redirect
#importar los models
from .models import Organization, Developer
#importar los forms 
from .forms.register import DeveloperForm , OrganizationForm
from .forms.login import LoginOrganizationForm, LoginDeveloperForm

# Create your views here.
def index(request):
    # si se carga el index por medio de un get
    if request.method == 'GET':
        # si no existe la sesión se muestra los forms de login
        if 'id' not in  request.session :
            #presentar LoginForm de empresa y desarrollador
            logindeveloper = LoginDeveloperForm()
            loginorganization = LoginOrganizationForm()
            context = {
                'logindeveloper' : logindeveloper,
                'loginorganization' : loginorganization,
            }
            return render(request, 'login_page.html', context)
        
        else:
            # si existe la sesión se redirecciona al dashboard_app

            if request.session['type'] == "developer":
                return redirect('/jobshubdev') #cambiar acá segun la app----------------------------------
           
            if request.session['type'] == "organization":
                return redirect('/jobshuborg')


def registerdeveloper(request):
    
    if request.method == 'GET':
        developerform = DeveloperForm()
        #si es get
        #obtiene el form de register
        print(developerform)
        context = {
            'developerform' : developerform
        }
        return render(request, 'register_developer.html', context)

    else:
        #si es post
        developerform = DeveloperForm(request.POST) #se obtiene el formulario con los datos recibidos por POST
        if developerform.is_valid():
            print("es valido"*30)
            user = developerform.save()
            request.session['id'] = user.id
            request.session['type'] = "developer"
            print(request.session['id'])
            return redirect('/jobshubdev') #cambiar acá segun la app----------------------------------
        else: 
            print("INvalido"*30)
            context = {
            'developerform' : developerform
            }
            return render(request, 'register_developer.html', context)


def registerorganization(request):
    if request.method == 'GET':
        organizationform = OrganizationForm()
        #si es get
        #obtiene el form de register
        print(organizationform)
        context = {
            'organizationform' : organizationform
        }
        return render(request, 'register_organization.html', context)

    else:
        #si es post
        organizationform = OrganizationForm(request.POST) #se obtiene el formulario con los datos recibidos por POST
        if organizationform.is_valid():
            print("es valido"*30)
            user = organizationform.save()
            request.session['id'] = user.id
            request.session['type'] = "organization"
            print(request.session['id'])
            return redirect('/jobshuborg') #cambiar acá segun la app----------------------------------
        else: 
            print("INvalido"*30)
            context = {
            'organizationform' : organizationform
            }
            return render(request, 'register_organization.html', context)

      



def logindev(request):
    logindeveloper = LoginDeveloperForm(request.POST)
    loginorganization = LoginOrganizationForm()
    # si el form es valido
    if logindeveloper.is_valid():
        #guarda en user la clase 
        user = logindeveloper.login(request.POST)

        if user:
            request.session['id'] = user.id
            request.session['type'] = "developer"
            return redirect("/jobshubdev") #cambiar acá segun la app------------------------------------
    
    message_error = "Usuario y/o contraseña incorrectos"
    context = {
        "logindeveloper" : logindeveloper,
        "message_login_failed_dev" : message_error,
        "loginorganization" : loginorganization,
        
    }
    return render(request, 'login_page.html', context ) 


def loginorg(request):
    loginorganization = LoginOrganizationForm(request.POST)
    logindeveloper = LoginDeveloperForm()
    # si el form es valido
    if loginorganization.is_valid():
        #guarda en user la clase 
        user = loginorganization.login(request.POST)

        if user:
            request.session['id'] = user.id
            request.session['type'] = "organization"
            return redirect("/jobshuborg") #cambiar acá segun la app------------------------------------
    
    message_error = "Usuario y/o contraseña incorrectos"
    context = {
        "loginorganization" : loginorganization,
        "message_login_failed_org" : message_error,
        "logindeveloper" : logindeveloper,
        
    }
    return render(request, 'login_page.html', context ) 




def logout(request):
    request.session.delete()
    return redirect('/')