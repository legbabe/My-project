from rest_framework import serializers
from .models import Event, Attendee
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("The event date must be in the future.")
        return value
    
class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'