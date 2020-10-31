from django.urls import path
from . import views as user_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('api/auth/', user_views.AuthView.as_view(),name='auth-detail'),
    path('api/user-detail/', user_views.UserDetailView.as_view(),name='details'),
    path('api/current-user/', user_views.current_user,name='current-user'),
    
    #JWT
    path('token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    #Notification
    path('api/get-notification/', user_views.notify,name='get-notification'),
    path('api/activate-reminder/', user_views.activate_reminder,name='activate-reminder'),
    path('api/deactivate-reminder/', user_views.deactivate_reminder,name='deactivate-reminder'),
]