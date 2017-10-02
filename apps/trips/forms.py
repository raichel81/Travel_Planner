from django.contrib.auth.models import User

from django import forms
import datetime
from .models import Trip

class NewTripForm(forms.ModelForm):
    # destination = forms.CharField(label='Destination:', max_length=30)
    # description = forms.CharField(
    #     widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
    #     ),
    #     max_length=4000,
    #     help_text='The max length of the text is 4000.'
    # )
    # start_date = forms.DateField(
    #     input_formats='%m/%d/%Y')
    # end_date = forms.DateField(
    #     input_formats='%m/%d/%Y')

    class Meta:
        model = Trip
        exclude=['created_by', 'updated_at', 'users']
        widgets={
            'description' : forms.Textarea(attrs={'rows':3, 'placeholder': 'What is the purpose of the trip?'}),
            'start_date' : forms.SelectDateWidget(),
            'end_date' : forms.SelectDateWidget()
            }