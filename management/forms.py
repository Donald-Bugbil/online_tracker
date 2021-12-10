from django.forms import ModelForm 
from .models import clockIn, clockOut
from django import forms


class ClockInForm(ModelForm):
    class Meta:
        model = clockIn
        fields = ['created']

class ClockOutForm(ModelForm):
    class Meta:
        model = clockOut
        fields = ['created']
        widget = {
            'created' : forms.SplitDateTimeWidget()
        }