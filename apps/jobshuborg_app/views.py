from typing import ContextManager
from apps.jobshuborg_app.models import Position
from django.shortcuts import redirect, render
from apps.login_app.models import Organization, Developer
from apps.jobshubdev_app.models import Language, Framework, Biography
from .forms.position import PositionForm

# Create your views here.
def index(request):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        active_user = Organization.objects.get(id = int(request.session['id']))
        all_developers = Developer.objects.all()
        all_framewors =  Framework.objects.all()
        all_biography = Biography.objects.all()
        all_my_positions = active_user.organization_position.all()
        
        context = {
            'active_user' : active_user,
            'all_developers' : all_developers,
            'all_framewors' : all_framewors,
            'all_biography' : all_biography,
            'all_my_positions' : all_my_positions,

        }
        return render(request, 'organization_dashboard.html' , context)


def new_position(request):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        active_user = Organization.objects.get(id = int(request.session['id']))
        all_languages = Language.objects.all()
        all_frameworks = Framework.objects.all()
        
        # request.session['hidden_step_two'] = "hidden"

        position_form = PositionForm()
        context = {
            'active_user' : active_user,
            'position_form' : position_form,
            'all_languages' : all_languages,
            'all_frameworks' : all_frameworks,
            
        }
    return render(request, 'new_position.html' , context)
  




def add_language(request, id_language):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        this_language = Language.objects.get(id = id_language)
        if "selected_languages" in request.session:
            # ya existe la lista  
            language_list = request.session['selected_languages']
            #se verifica que el id no esté ya en la lista del session
            exist = False
            for i in language_list:
                if i == id_language:
                    exist = True

            if exist == False:
                language_list.append(this_language.id)
                request.session['selected_languages'] = language_list
        else:
            #si no hay lenguajes seleccionado se crea una lista en sessions
            request.session['selected_languages'] = []
            request.session['selected_languages'].append(this_language.id)

        
        print(f"la lista de lenguajes actual -----> {request.session['selected_languages']}")

        # return redirect('/jobshuborg/new_position')
        return redirect('/jobshuborg/step_two')


def add_framework(request, id_framework):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        this_framework = Framework.objects.get(id = id_framework)
        if "selected_framework" in request.session:
            # ya existe la lista  
            framework_list = request.session['selected_framework']
            #se verifica que el id no esté ya en la lista del session
            exist = False
            for i in framework_list:
                if i == id_framework:
                    exist = True

            if exist == False:
                framework_list.append(this_framework.id)
                request.session['selected_framework'] = framework_list
        else:
            #si no hay lenguajes seleccionado se crea una lista en sessions
            request.session['selected_framework'] = []
            request.session['selected_framework'].append(this_framework.id)

        
        print(f"la lista de lenguajes actual -----> {request.session['selected_framework']}")
        # return redirect('/jobshuborg/new_position')
        return redirect('/jobshuborg/step_two')




def delete_language(request, id_language):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        list = request.session['selected_languages']
        list.remove(id_language)
        request.session['selected_languages']  = list
        # return redirect('/jobshuborg/new_position')
        return redirect('/jobshuborg/step_two')


def delete_framework(request, id_framework):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        list = request.session['selected_framework']
        list.remove(id_framework)
        request.session['selected_framework']  = list
        # return redirect('/jobshuborg/new_position')
        return redirect('/jobshuborg/step_two')

def cancel_new_position(request):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        print("pasó a borrar acá")

        request.session['selected_languages'] = []
        request.session['selected_framework'] = []
        request.session['position_title'] = []
        request.session['position_description'] = []
        return redirect('/')


def step_two(request):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        
        active_user = Organization.objects.get(id = int(request.session['id']))
        all_languages = Language.objects.all()
        all_frameworks = Framework.objects.all()
        position_form = PositionForm(request.POST)

        try:
            request.session['position_title']  = request.POST['position_title']
            request.session['position_description'] = request.POST['position_description']
        except:
            print("ya existe")
        context = {
            'active_user' : active_user,
            'all_languages' : all_languages,
            'all_frameworks' : all_frameworks,
            'position_form' : position_form,
            # 'position_title' : position_title,
            # 'position_description' : position_description,
        }
        
        return render(request, 'new_position_step2.html', context)
        
    






def save_position(request):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es developer devuelve al login
        return redirect('/')
    else:
        print(f"El título de la posición --->{request.session['position_title']}")
        print(f"La descripción de la posición --->{request.session['position_description']}")
        
        
        active_user = Organization.objects.get(id = int(request.session['id']))
        print(f"{active_user.first_name}")

        #obtener la lista de objetos según id
        langs_objects_list = []
        frameworks_objects_list = []

        
        if 'selected_languages' in request.session:
            print(f"Los id´s de los lenguajes --->{request.session['selected_languages']}")
            for langs in request.session['selected_languages']:
                print(langs)
                langs_objects_list.append(Language.objects.get(id=langs))

        if 'selected_framework' in request.session:
            print(f"Los id´s de los frameworks --->{request.session['selected_framework']}")
            for frame in request.session['selected_framework']:
                print(frame)
                frameworks_objects_list.append(Framework.objects.get(id=frame))

        print(langs_objects_list)
        print(frameworks_objects_list)

        # for l in langs_objects_list:
        #     print(l.skill_name)

        # for f in frameworks_objects_list:
        #     print(f.skill_name)

        # aqui quedé me falta guardar la position

        new_posit = Position.objects.create(
            position_title = request.session['position_title'],
            position_description = request.session['position_description'],
            state_position = "Publicada: En contratación",
            position_organization = active_user,

            # position_filled_by = [] #aun no se contrata a nadie

        )

        #HASTA AQUI LLEGUE------------------------------------------------------
        for l in langs_objects_list:
            new_posit.position_language = l
            new_posit.save()

        for f in frameworks_objects_list:
            new_posit.position_framework = f
            new_posit.save()



        #se borran todas las variables de sesión utilizadas para crear un nuevo puesto de trabajo
        request.session['selected_languages'] = []
        request.session['selected_framework'] = []
        request.session['position_title'] = []
        request.session['position_description'] = []




        return  redirect('/')


