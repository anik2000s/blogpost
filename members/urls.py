from django.urls import path
from .views import UserRegisterView, ViewProfile


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ViewProfile, name='profile')
   
]
