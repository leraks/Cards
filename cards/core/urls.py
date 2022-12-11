from django.urls import path
from .views import *

urlpatterns = [
    path('', search, name="search"),
    path('cards/<int:pk>/', views_cards, name="views_cards"),
    path('create/', create_card, name="create_card"),

]