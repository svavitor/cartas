from django.urls import path

from .views import *

urlpatterns = [
    path("", CartaAPI.as_view()),
    path("<int:card_id>", CartaAPI.as_view()),
]
