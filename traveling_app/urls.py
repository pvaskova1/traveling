from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vsechny-zajezdy/', views.seznam_zajezdu, name='seznam_zajezdu'),
    path('detail/<int:zajezd_id>/', views.detail, name='detail'),
]

