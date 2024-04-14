from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'', DeckViewSet)

urlpatterns = [
    #path("", DeckAPI.as_view()),
]

urlpatterns += router.urls