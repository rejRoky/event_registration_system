from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EventForm


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
