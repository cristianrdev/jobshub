from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
    path('registerdeveloper', views.registerdeveloper),
    path('registerorganization', views.registerorganization),
    # path('register_organization', views.register_organization),
    # path('register', views.register),
    path('logindev', views.logindev,),
    path('loginorg', views.loginorg,),
    path('logout', views.logout ),

]