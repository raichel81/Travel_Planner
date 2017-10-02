# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
import datetime
from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    destination = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, related_name='trip')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    users = models.ManyToManyField(User, related_name="trips")

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError('End date must be after start date')
        if self.start_date < datetime.date.today():
            raise ValidationError('You can only plan trips in the future, silly!')
    def __str__(self):
        return self.destination

