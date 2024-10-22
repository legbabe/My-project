from django.urls import path
from .views import EventsView, register_for_event, EventViewSet

urlpatterns = [
    path('register/<int:event_id>/', register_for_event, name='register_for_event'),
    path('', EventsView.as_view(), name='events-list'),
    path('events/', EventViewSet.as_view({'get': 'list'}), name='events')
]
