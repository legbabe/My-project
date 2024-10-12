from django.urls import path
from .views import EventViewSet, register_for_event
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls + [
    path('register/<int:event_id>/', register_for_event, name='register_for_event'),
]
