from django.urls import path
from . import views as user_views

urlpatterns = [
    path('api/auth/', user_views.AuthView.as_view(),name='signup'),
    path('api/user-detail/<int:pk>', user_views.UserDetailView.as_view(),name='details'),
]