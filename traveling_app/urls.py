from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   path('vsechny-zajezdy/', views.seznam_zajezdu, name='seznam_zajezdu'),    # Vyhledávání/Filtr
    path('detail/<int:zajezd_id>/', views.detail, name='detail'),




    path(
        '',
        views.index,
        name='index'
    ),

    path(
        'zajezdy/',
        views.seznam_zajezdu,
        name='seznam_zajezdu'
    ),

    path(
        'zajezd/<int:trip_id>/',
        views.detail_zajezdu,
        name='detail_zajezdu'
    ),
]