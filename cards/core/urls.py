from django.urls import path
from .views import *

urlpatterns = [
    path('', search, name="search"),
    path('create/', create_card, name="create_card"),

]