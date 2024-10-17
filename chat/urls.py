from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:room_id>/', views.home, name='home_with_room'),  # Ruta para cargar una sala
]
