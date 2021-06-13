from typing import ContextManager
from apps.jobshuborg_app.models import Position
from django.shortcuts import redirect, render
from apps.login_app.models import Organization, Developer
from apps.jobshubdev_app.models import Language, Framework, Biography
from apps.messages_app.models import Message


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


def message_panel_organization(request, id_developer):
    if 'id' not in  request.session or request.session['type'] == "developer":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:
        active_user = Organization.objects.get(id = int(request.session['id']))
        this_developer = Developer.objects.get(id = id_developer)
        id_active_user = int(request.session['id'])
        all_developers = Developer.objects.all()
        all_frameworks =  Framework.objects.all()
        all_languages =  Language.objects.all()
        all_biography = Biography.objects.all()
        all_my_positions = active_user.organization_position.all()
        all_messages_organization = Message.objects.filter(sender_id = id_active_user).filter(reciever_id = id_developer)
        all_messages_developer = Message.objects.filter(sender_id = id_developer).filter(reciever_id = id_active_user)
        all_messages = all_messages_organization | all_messages_developer
        



        
        context = {
            'active_user' : active_user,
            'all_developers' : all_developers,
            'all_frameworks' : all_frameworks,
            'all_biography' : all_biography,
            'all_my_positions' : all_my_positions,
            'all_languages' : all_languages,
            'this_developer' : this_developer,
            'all_messages' : all_messages,

        }
        return render(request, 'message_panel.html', context)





def message_panel_developer(request, id_organization):
    if 'id' not in  request.session or request.session['type'] == "organization":
        #si no hay sesión o si es empresa (organization) devuelve al login
        return redirect('/')
    else:

        active_user = Developer.objects.get(id = int(request.session['id']))
        id_active_user = int(request.session['id'])
        this_organization = Organization.objects.get(id = id_organization)
        all_developers = Developer.objects.all()
        all_frameworks =  Framework.objects.all()
        all_languages =  Language.objects.all()
        all_biography = Biography.objects.all()
        # all_messages = Message.objects.filter(sender_id = id_organization)

        all_messages_developer = []
        all_messages_organization = []
        
        # mensajes hechos por el desarrollador
        all_messages_developer = Message.objects.filter(sender_id = id_active_user).filter(reciever_id = id_organization)
        #mensajes hechos por la empresa
        all_messages_organization = Message.objects.filter(sender_id = id_organization).filter(reciever_id = id_active_user)
        #marca los mensajes de la empresa como leidos===> readed = True
        if all_messages_organization:
            for mes in  all_messages_organization:
                print(mes.readed)
                mes.readed = True
                mes.save(update_fields= ['readed'])
                



        print("--------------mensajes desarrollador--------------")
        for i in all_messages_developer:
            print(f"{i.message_content} leido? {i.readed}")

        print("---------------mensajes empresa---------------")
        for i in all_messages_organization:
            print(f"{i.message_content} leido? {i.readed}")

        all_messages = all_messages_developer | all_messages_organization


        context = {
            'active_user' : active_user,
            'all_developers' : all_developers,
            'all_frameworks' : all_frameworks,
            'all_biography' : all_biography,
            'all_languages' : all_languages,
            'this_organization' : this_organization,
            'all_messages' : all_messages,

        }
        return render(request, 'message_panel_developer.html', context)



def make_organization_message(request, id_developer):
    active_user = Organization.objects.get(id = int(request.session['id']))
    this_developer = Developer.objects.get(id = id_developer)
    
    message_content = request.POST['message_content']

    if message_content:
        new_message = Message.objects.create(
            message_content = message_content,
            sender_id = int(request.session['id']),
            reciever_id = id_developer,
            user_type = "organization",
            readed = False
        )
    

    return redirect('/messages/' + str(id_developer))



def make_developer_message(request, id_organization):
    active_user = Developer.objects.get(id = int(request.session['id']))
    this_organization = Organization.objects.get(id = id_organization)
    message_content = request.POST['message_content']
    
    if message_content:
        new_message = Message.objects.create(
            message_content = message_content,
            sender_id = int(request.session['id']),
            reciever_id = id_organization,
            user_type = "developer",
            readed = False

        )
        print("grabó+"*20)

    return redirect('/messages/' + str(id_organization))
