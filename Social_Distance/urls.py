from django.urls import path
from . import views as social_views
from .ML_Model import views as ml_views

urlpatterns = [

    #Notification
    #path('api/get-notification/', user_views.notify,name='get-notification'),
    path('api/activate-social/', social_views.activate_social,name='activate-social'),
    path('api/deactivate-social/', social_views.deactivate_social,name='deactivate-social'),
    path('api/run-social/', ml_views.run_social,name='run-social'),
]