from django.urls import path
from . import views


urlpatterns = [
    path('<int:id_receiver>', views.index ),
    path('message_panel_organization/<int:id_developer>', views.message_panel_organization ),

    
    path('message_panel_developer/<int:id_organization>', views.message_panel_developer ),

    path('message_panel_organization/make_organization_message/<int:id_developer>', views.make_organization_message ),
    path('message_panel_developer/make_developer_message/<int:id_organization>', views.make_developer_message ),
    
]