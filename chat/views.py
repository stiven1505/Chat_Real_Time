from django.shortcuts import render, redirect
from .models import Room
from django.contrib.auth.decorators import login_required

# Vista de inicio que también carga la sala si el usuario tiene acceso
@login_required
def home(request, room_id=None):
    rooms = request.user.rooms_joined.all()  # consulta a BD
    
    # Obtener el mensaje de error, si existe
    error_message = request.session.get('error_message', None)
    request.session['error_message'] = None  # Limpiar el mensaje de error
    
    # Si se pasa un `room_id`, intentamos cargar la sala
    selected_room = None
    if room_id:
        try:
            selected_room = request.user.rooms_joined.get(id=room_id)
        except Room.DoesNotExist:
            request.session['error_message'] = 'No Tienes Permiso Para Acceder a Esta Sala'
    
    return render(request, 'chat/home.html', {
        'rooms': rooms, 
        'selected_room': selected_room, 
        'error_message': error_message
    })
