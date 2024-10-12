from rest_framework import viewsets,  status
from .models import Event, Attendee
from .serializers import EventSerializer,  AttendeeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import api_view
from notifications.models import Notification

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.organizer != self.request.user:
            raise PermissionDenied("You can only edit your own events.")
        serializer.save()

        # Send notification to all attendees
        for attendee in Event.attendees.all():
            Notification.objects.create(
                recipient=attendee.user,
                message=f"The event '{Event.title}' has been updated."
            )

    def perform_destroy(self, instance):
        if instance.organizer != self.request.user:
            raise PermissionDenied("You can only delete your own events.")
        
        # Send notification to all attendees
        for attendee in instance.attendees.all():
            Notification.objects.create(
                recipient=attendee.user,
                message=f"The event '{instance.title}' has been cancelled."
            )
        instance.delete()

@api_view(['POST'])
def register_for_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if event.attendees.count() >= event.capacity:
        return Response({"error": "This event is fully booked."}, status=status.HTTP_400_BAD_REQUEST)

    attendee, created = Attendee.objects.get_or_create(event=event, user=request.user)
    if not created:
        return Response({"error": "You are already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = AttendeeSerializer(attendee)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


