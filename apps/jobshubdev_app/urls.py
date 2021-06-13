from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
    path('makedata', views.makedata ),
    path('add_language/<int:id_language>', views.addlanguage ),
    path('add_framework/<int:id_framework>', views.addframework ),
    path('delete_language/<int:id_language>', views.deletelanguage ),
    path('delete_framework/<int:id_framework>', views.deleteframework ),
    path('update_developer', views.update_developer ),
    path('save_bio', views.save_bio ),
    path('delete_developer/<int:id_developer>', views.delete_developer ),


]