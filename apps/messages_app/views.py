from typing import ContextManager
from apps.jobshuborg_app.models import Position
from django.shortcuts import redirect, render
from apps.login_app.models import Organization, Developer
from apps.jobshubdev_app.models import Language, Framework, Biography


# Create your views here.

def index(request):
    if 'id' not in  request.session:
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
        active_user = Organization.objects.get(id = int(request.session['id']))
        all_developers = Developer.objects.all()
        all_frameworks =  Framework.objects.all()
        all_languages =  Language.objects.all()
        all_biography = Biography.objects.all()
        all_my_positions = active_user.organization_position.all()
        
        context = {
            'active_user' : active_user,
            'all_developers' : all_developers,
            'all_frameworks' : all_frameworks,
            'all_biography' : all_biography,
            'all_my_positions' : all_my_positions,
            'all_languages' : all_languages,

        }
        return render(request, 'message_panel.html', context)
