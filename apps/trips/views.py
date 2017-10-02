# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTripForm

from .models import Trip

def index(request):
    mytrips = None
    if request.user.is_authenticated:
        mytrips = request.user.trips.all()
    context={
        'trips' : Trip.objects.all(),
        'mytrips' : mytrips
    }    
    return render(request, 'index.html', context)

def destination(request, pk):
    trip = Trip.objects.get(id = pk)
    context={
        'trip' : trip
    }
    return render(request, 'destination.html', context)

def add_trip(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewTripForm(request.POST)
            if form.is_valid():
                trip = form.save(commit=False)
                trip.created_by_id = request.user.id
                trip.save()
                trip.users.add(request.user)
                return redirect('trips:index')  
        else:
            form = NewTripForm()
        return render(request, 'add_trip.html', {'form': form})
    else:
        return redirect('trips:index')

def join(request, pk):
    if request.user.is_authenticated:
        trip= Trip.objects.get(id = pk)
        user = request.user
        trip.users.add(user)
    return redirect('trips:index')