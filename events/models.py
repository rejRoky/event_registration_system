from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField('Event Title', max_length=255)
    description = models.TextField('Event Description')
    date = models.DateField('Event Date', auto_now_add=False, auto_now=False,
                            help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField('Event Time', auto_now_add=False, auto_now=False,
                            help_text='Please use the following format: <em>HH:MM:SS</em>.')
    location = models.CharField('Event Location', max_length=255)
    available_slots = models.PositiveIntegerField('Available Slots', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['date', 'time']
