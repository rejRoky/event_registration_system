from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from rest_framework import generics
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def register_for_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        Registration.objects.create(user=request.user, event=event)
        return redirect('event_detail', event_id=event_id)
    return render(request, 'events/register_for_event.html', {'event': event})


def search_events(request):
    query = request.GET.get('q')
    events = Event.objects.filter(title__icontains=query)
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def user_dashboard(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/user_dashboard.html', {'registrations': registrations})


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RegistrationCreateAPIView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class UserRegistrationsAPIView(generics.ListAPIView):
    serializer_class = RegistrationSerializer

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
