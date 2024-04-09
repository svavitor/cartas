from django.urls import path

from .views import *

urlpatterns = [
    path("", CardAPI.as_view()),
    path("<int:card_id>", CardAPI.as_view()),
    path("to-review", CardViewSet.as_view({'get':'cards_to_review'})),
]

