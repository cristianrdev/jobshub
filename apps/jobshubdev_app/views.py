from apps.jobshubdev_app.models import Framework, Language
from django.shortcuts import render, redirect
from apps.login_app.models import Developer
from .models import Biography
from . import skills_creator
from .forms.update_dev import UpdateDeveloper
from .forms.biography import BiographyForm 

# Create your views here.
def index(request):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        this_user = Developer.objects.get(id = int(request.session['id']))
        all_languages = Language.objects.all()
        all_frameworks = Framework.objects.all()
        all_developer_languages= this_user.developer_language.all()
        all_developer_frameworks= this_user.developer_framework.all()
        user_biography = BiographyForm()
        update_developer = UpdateDeveloper(instance=this_user)

    
        
        try:
        
            user_biography = BiographyForm(instance = this_user.user_biography)
        
        except:
            print("No existe biografia creada")

        context = {
            "active_user" : Developer.objects.get(id = int(request.session['id'])),
            "all_languages" : all_languages,
            "all_frameworks" : all_frameworks,
            "all_developer_languages" : all_developer_languages,
            "all_developer_frameworks": all_developer_frameworks,
            "user_biography" : user_biography,
            "update_developer" : update_developer,
        
        }
        
        return render(request, 'developer_dashboard.html', context)


def addlanguage(request, id_language):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        print(id_language)
        this_user = Developer.objects.get(id = int(request.session['id']))
        this_language = Language.objects.get(id = id_language)
        this_user.developer_language.add(this_language)

        return redirect('/')

def addframework(request, id_framework):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        print(id_framework)
        this_user = Developer.objects.get(id = int(request.session['id']))
        this_framework = Framework.objects.get(id = id_framework)
        this_user.developer_framework.add(this_framework)
        return redirect('/')


def deletelanguage(request, id_language):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        print(id_language)
        this_user = Developer.objects.get(id = int(request.session['id']))
        this_language = Language.objects.get(id = id_language)
        this_user.developer_language.remove(this_language)

        return redirect('/')

def deleteframework(request, id_framework):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        print(id_framework)
        this_user = Developer.objects.get(id = int(request.session['id']))
        this_framework = Framework.objects.get(id = id_framework)
        this_user.developer_framework.remove(this_framework)
        return redirect('/')

def update_developer(request):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        this_user = Developer.objects.get(id = int(request.session['id']))
        update_developer = UpdateDeveloper(request.POST)
        if update_developer.is_valid():
            print("es valido el from de actualización y se graba")
            this_user.address_name = request.POST['address_name']
            this_user.address_number = request.POST['address_number']
            this_user.address_detail = request.POST['address_detail']
            this_user.save(update_fields=['address_name','address_number','address_detail'])

        return redirect('/')
   

def save_bio(request):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        this_user = Developer.objects.get(id = int(request.session['id']))
        bio_form =  BiographyForm(request.POST)
        if bio_form.is_valid:
            try:
                #existe biografía
                this_bio = Biography.objects.get(id= int(this_user.user_biography.id) ) 
                print(f"---------->>>>> {this_bio.short_bio}")

                this_bio.short_bio = request.POST['short_bio']
                print(f"---------->>>>> {this_bio.short_bio}")
                this_bio.save()
            except:
                #no existe biografía
                print("no existe biografia al grabar")
                print("se crea biografía")
                Biography.objects.create(short_bio = request.POST['short_bio'], user = this_user )
        
        return redirect('/')



def makedata(request):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        skills_creator.makelanguage()
        skills_creator.makeframework()
        return redirect('/')