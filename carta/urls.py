from django.urls import path

from . import views

urlpatterns = [
    path("", views.CartaAPI.as_view()),    
]
