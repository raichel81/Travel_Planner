from django.contrib.auth.models import User

from django import forms
import datetime
from .models import Trip

class NewTripForm(forms.ModelForm):

    class Meta:
        model = Trip
        exclude=['created_by', 'updated_at', 'users']
        widgets={
            'description' : forms.Textarea(attrs={'rows':3, 'placeholder': 'What is the purpose of the trip?'}),
            'start_date' : forms.SelectDateWidget(),
            'end_date' : forms.SelectDateWidget()
            }