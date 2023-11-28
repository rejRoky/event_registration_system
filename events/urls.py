from django.urls import path
from .views import event_list, event_detail, register_for_event, search_events, user_dashboard
from .views import EventListAPIView, EventDetailAPIView, RegistrationCreateAPIView, UserRegistrationsAPIView

urlpatterns = [
    path('events/', event_list, name='event_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('events/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('search/', search_events, name='search_events'),
    path('dashboard/', user_dashboard, name='user_dashboard'),

    # API Endpoints
    path('api/events/', EventListAPIView.as_view(), name='api_event_list'),
    path('api/events/<int:pk>/', EventDetailAPIView.as_view(), name='api_event_detail'),
    path('api/register/', RegistrationCreateAPIView.as_view(), name='api_register'),
    path('api/user-registrations/', UserRegistrationsAPIView.as_view(), name='api_user_registrations'),
]
