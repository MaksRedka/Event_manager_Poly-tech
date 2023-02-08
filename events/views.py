from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Event, EventType
from .serializers import EventSerializer


class EventListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Get all events
    def get(self, request, *args, **kwargs):
        '''
        List all the event items for given requested user
        '''
        events = Event.objects.filter(user = request.user.id)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create new event
    def post(self, request, *args, **kwargs):
        '''
        Create the Event with given todo data
        '''
        event_type_name = request.data.get('event_type')
        try:
            event_type = EventType.objects.get(name=event_type_name)
        except:
            event_type = EventType(name=event_type_name)
            event_type.save()

        data = {
            'user': request.user.id,
            'event_type': event_type.id,
            'info': request.data.get('info'), 
            'timestamp': request.data.get('timestamp')
        }
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)