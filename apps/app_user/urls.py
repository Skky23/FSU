from django.urls import path
from apps.app_user import views

urlpatterns = [
    path('', views.index),
]