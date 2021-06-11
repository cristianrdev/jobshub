from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
    path('new_position', views.new_position ),
    path('add_language/<int:id_language>', views.add_language ),
    path('add_framework/<int:id_framework>', views.add_framework ),
    path('delete_language/<int:id_language>', views.delete_language ),
    path('delete_framework/<int:id_framework>', views.delete_framework ),
    path('cancel_new_position', views.cancel_new_position ),
    path('save_position', views.save_position ),
    path('step_two', views.step_two ),

]