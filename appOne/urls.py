from django.urls import path
from .views import greet

urlpatterns = [
    path('<str:name>', greet, name="greet")
]