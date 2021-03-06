from apps.jobshuborg_app.models import Position
from apps.jobshubdev_app.models import Framework, Language
from django.shortcuts import render, redirect
from apps.login_app.models import Developer, Organization
from .models import Biography
from . import skills_creator
from .forms.update_dev import UpdateDeveloper
from .forms.biography import BiographyForm 
from apps.messages_app.models import Message
import re
# Create your views here.
def index(request):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        request.session.delete() # se borra cualquier sesión abierta por seguridad
        return redirect('/')
    else:
        this_user = Developer.objects.get(id = int(request.session['id']))
        this_user_id = int(request.session['id'])
        all_messages = Message.objects.all()
        all_positions = Position.objects.all()

        user_biography = BiographyForm() # si no hay bio
        this_bio = ""
        try:
            user_biography = BiographyForm(instance = this_user.user_biography) #si hay bio
            this_bio = this_user.user_biography #obtiene el objeto bio del usuario
        except:
            print("No existe biografia creada"*50)

        all_languages = Language.objects.all()
        all_frameworks = Framework.objects.all()
        all_developer_languages= this_user.developer_language.all()
        all_developer_frameworks= this_user.developer_framework.all()
        

        update_developer = UpdateDeveloper(instance=this_user)
        #mensajes hechos por la empresa para este desarrollador
        all_messages_for_dev = Message.objects.filter(reciever_id = this_user_id)
        #mensajes NO leidos
        messages_pending = all_messages_for_dev.filter(readed = False)

        #mensajes  leidos
        messages_readed = all_messages_for_dev.filter(readed = True)

        messages_pending_list = []
        messages_readed_list = []



        
        if messages_pending:
            for mess_pend in messages_pending:
                
                org = Organization.objects.get(id = int(mess_pend.sender_id))
                pend = {mess_pend.sender_id : org.org_name}
                if not pend in messages_pending_list:
                    messages_pending_list.append(pend)

        if messages_readed:
            for mess_readed in messages_readed:
                org = Organization.objects.get(id = int(mess_readed.sender_id))
                pend = {mess_readed.sender_id : org.org_name}
                if not pend in messages_readed_list and not pend in messages_pending_list:
                    messages_readed_list.append(pend)

   
        print(f" Lista de conversaciones pendientes de leer {messages_pending_list}")
        print(f"Lista de conversaciones ya leidas {messages_readed_list}")
    
      


        context = {
            "active_user" : Developer.objects.get(id = int(request.session['id'])),
            "all_languages" : all_languages,
            "all_frameworks" : all_frameworks,
            "all_developer_languages" : all_developer_languages,
            "all_developer_frameworks": all_developer_frameworks,
            "user_biography" : user_biography,
            "update_developer" : update_developer,
            "messages_pending" : messages_pending_list,
            "messages_readed" : messages_readed_list,    
            "all_messages" : all_messages,    
            "this_bio" : this_bio,    
            "all_positions" : all_positions,    

        }
        
        return render(request, 'developer_dashboard.html', context)


def addlanguage(request, id_language):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        request.session.delete() # se borra cualquier sesión abierta por seguridad
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
        request.session.delete() # se borra cualquier sesión abierta por seguridad
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
        request.session.delete() # se borra cualquier sesión abierta por seguridad
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
        request.session.delete() # se borra cualquier sesión abierta por seguridad
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
        request.session.delete() # se borra cualquier sesión abierta por seguridad
        return redirect('/')
    else:
        request.session['error_messages'] = []
        request.session['error_messages_bio'] = []
        this_user = Developer.objects.get(id = int(request.session['id']))
        update_developer = UpdateDeveloper(request.POST)
        if update_developer.is_valid():
            print("es valido el from de actualización y se graba")
            this_user.address_name = request.POST['address_name']
            this_user.address_number = request.POST['address_number']
            this_user.address_detail = request.POST['address_detail']
            this_user.save(update_fields=['address_name','address_number','address_detail'])
        else:
            if len(request.POST['address_name']) < 2:
                request.session['error_messages'] = ["Nombe de la calle menor 2 caracteres"] #se crea una variable de sesión que es un lista de errores
            if len(request.POST['address_number']) < 2:
                request.session['error_messages'].append("El número del domicilio debe contener al menos 2 caracteres") #se crea una variable de sesión que es un lista de errores
            

        return redirect('/')

   

def save_bio(request):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        request.session.delete() # se borra cualquier sesión abierta por seguridad
        return redirect('/')
    else:
        request.session['error_messages_bio'] = []
        request.session['error_messages'] = []
        this_user = Developer.objects.get(id = int(request.session['id']))
        bio_form =  BiographyForm(request.POST)
        print(bio_form.is_valid())
        
        if bio_form.is_valid():
            try:
                #si existe biografía
                this_bio = Biography.objects.get(id= int(this_user.user_biography.id) )
                this_bio.short_bio = request.POST['short_bio']
                this_bio.github_link = request.POST['github_link']
                this_bio.save(update_fields=['short_bio','github_link'])
               
            except:  #si NO existe biografia
                Biography.objects.create(
                    short_bio = request.POST['short_bio'],
                    github_link = request.POST['github_link'],
                    user = this_user,
                )
        #si no es valido avisar porque no es valido
        p = re.compile('(?:https?://)?(?:www[.])?github[.]com/[\w-]+/?')
        if not p.match(request.POST['github_link']):
            request.session['error_messages_bio'].append("El link no es válido")

        if len(request.POST['short_bio']) < 10:
            request.session['error_messages_bio'].append("Su perfil debe contener entre 10 a 255 caracteres")        
            

        return redirect('/')
        # try:
        #     aa = this_user.user_biography.id
        #     this_user_have_biography = True
            
        # except:
        #     this_user_have_biography = False

        # if this_user_have_biography == True:
        #     #existe biografía
        #     this_bio = Biography.objects.get(id= int(this_user.user_biography.id) )
        #     if bio_form.is_valid():
        #         print(f"---------->>>>> {this_bio.short_bio}")
        #         this_bio.short_bio = request.POST['short_bio']
        #         this_bio.github_link = request.POST['github_link']
        #         print(f"---------->>>>> {this_bio.short_bio}")
        #         this_bio.save(update_fields=['short_bio','github_link'])
        #     else:
        #         p = re.compile('(?:https?://)?(?:www[.])?github[.]com/[\w-]+/?')
        #         if not p.match(request.POST['github_link']):
        #             request.session['error_messages_bio'].append("El link no es válido")
        #         if len(request.POST['short_bio']) < 10:
        #             request.session['error_messages_bio'].append("Su perfil debe contener entre 10 a 255 caracteres")        
        #             return redirect('/')


        # try:
        #     this_bio = Biography.objects.get(id= int(this_user.user_biography.id) ) 
        # except:
        #     #no existe biografía
        #     print("no existe biografia al grabar")
        #     print("se crea biografía")
        #     Biography.objects.create(short_bio = request.POST['short_bio'], user = this_user )



def makedata(request):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        request.session.delete() # se borra cualquier sesión abierta por seguridad
        return redirect('/')
    else:
        skills_creator.makelanguage()
        skills_creator.makeframework()
        return redirect('/')


def  delete_developer(request, id_developer):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        request.session.delete() # se borra cualquier sesión abierta por seguridad
        return redirect('/')
    else:
        print(f'usuario a borrar {id_developer}')
        this_user = Developer.objects.get(id = id_developer)
        this_user.delete()
        request.session.delete()
        return redirect('/')
