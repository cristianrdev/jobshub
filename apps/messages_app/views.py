from typing import ContextManager
from apps.jobshuborg_app.models import Position
from django.shortcuts import redirect, render
from apps.login_app.models import Organization, Developer
from apps.jobshubdev_app.models import Language, Framework, Biography
from apps.messages_app.models import MessageOrg


# Create your views here.

def index(request, id_receiver):
    if 'id' not in  request.session:
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
        if request.session['type'] == "organization": ##si la conversación la abre la empresa se va al message_panel_developer

            return redirect('/messages/message_panel_organization/' + str(id_receiver))


        if request.session['type'] == "developer": #si la conversación la hace la abre el developer se va al message_panel_organization

            return redirect('/messages/message_panel_developer/' + str(id_receiver) )


def message_panel_organization(request, id_organization):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        active_user = Organization.objects.get(id = int(request.session['id']))

        this_developer = Developer.objects.get(id = id_organization)


        all_developers = Developer.objects.all()
        all_frameworks =  Framework.objects.all()
        all_languages =  Language.objects.all()
        all_biography = Biography.objects.all()
        all_my_positions = active_user.organization_position.all()
        this_developer_messages = this_developer.developer_message.all()
        
        context = {
            'active_user' : active_user,
            'all_developers' : all_developers,
            'all_frameworks' : all_frameworks,
            'all_biography' : all_biography,
            'all_my_positions' : all_my_positions,
            'all_languages' : all_languages,
            'this_developer' : this_developer,
            'this_developer_messages' : this_developer_messages,

        }
        return render(request, 'message_panel.html', context)





def message_panel_developer(request, id_organization):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:

        active_user = Developer.objects.get(id = int(request.session['id']))
        this_organization = Organization.objects.get(id = id_organization)

        all_developers = Developer.objects.all()
        all_frameworks =  Framework.objects.all()
        all_languages =  Language.objects.all()
        all_biography = Biography.objects.all()
       
    
        
        
        
        context = {
            'active_user' : active_user,
            'all_developers' : all_developers,
            'all_frameworks' : all_frameworks,
            'all_biography' : all_biography,
       
            'all_languages' : all_languages,
            'this_organization' : this_organization,

        }
        return render(request, 'message_panel_developer.html', context)



def make_organization_message(request, id_developer):
    active_user = Organization.objects.get(id = int(request.session['id']))
    this_developer = Developer.objects.get(id = id_developer)
    
    message_content = request.POST['message_content']
    if message_content:
        new_message = MessageOrg.objects.create(
            message_content = message_content,
            message_to_developer = this_developer,
            message_created_by = active_user


        )
    

    return redirect('/messages/' + str(id_developer))



def make_developer_message(request, id_organization):
    active_user = Developer.objects.get(id = int(request.session['id']))
    this_organization = Organization.objects.get(id = id_organization)
    message_content = request.POST['message_content']
    
  
    # if message_content:
    #     new_message = MessageOrg.objects.create(
    #         message_content = message_content,
    #         message_to_developer = this_developer,
    #         message_created_by = active_user


    #     )

    if message_content:
        new_message = MessageOrg.objects.create(
            

        )

    print("ya pasó por acá")
    print(message_content)
    



    return redirect('/messages/' + str(id_organization))
