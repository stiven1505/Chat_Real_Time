from django.shortcuts import render, redirect
from .models import Room
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone  # Importar timezone para obtener la fecha y hora actual
import re
import bleach

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


def send_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message', '')

        # Validar el mensaje con una expresión regular
        regex = re.compile(r'^[a-zA-Z0-9\s.,!?]+$')
        if not regex.match(message_content):
            return JsonResponse({'error': 'El mensaje contiene caracteres no permitidos 2.'}, status=400)

        # Sanitizar el mensaje para permitir solo texto seguro
        sanitized_message = bleach.clean(message_content)

        # Obtener la fecha y hora actual
        current_time = timezone.now()  # Esto ahora debería funcionar correctamente

        # Aquí puedes procesar y guardar el mensaje si es válido
        return JsonResponse({
            'message': sanitized_message,
            'username': request.user.username,
            'timestamp': current_time.strftime("%Y-%m-%d %H:%M:%S")  # Formatear la fecha y hora
        })
      