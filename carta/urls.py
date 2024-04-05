from django.urls import path

from . import views

urlpatterns = [
    #path("list", views.cartas_lista),
    path("list", views.CartaAPI.as_view(), name="list"),
]
