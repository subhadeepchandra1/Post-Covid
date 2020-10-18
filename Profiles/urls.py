from django.urls import path
from . import views as user_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/auth/', user_views.AuthView.as_view(),name='auth-detail'),
    path('api/user-detail/', user_views.UserDetailView.as_view(),name='details'),
    path('api/current-user/', user_views.current_user,name='current-user'),
    path('token-auth/', obtain_jwt_token)
]