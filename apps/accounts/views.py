# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trips:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
        