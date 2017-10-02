# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User
from ..views import index, add_trip
from ..models import Trip
from ..forms import NewTripForm

class IndexTests(TestCase):
    def setUp(self):
        u=User.objects.create(username='username', email='rai_chel@gmail.com')
        u.set_password('blah')
        u.save()
        Trip.objects.create(destination='Paris', description='PARTY!!!', start_date='2017-12-20', end_date='2017-12-21', created_by_id=u.id)
        self.client.login(username='username', password='blah')
        self.client.session.save()
        url = reverse('trips:index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)


    def test_index_url_resolves_index_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)

    def test_index_view_contains_link_to_add_trip_page(self):
        add_trip_url = reverse('trips:add_trip')
        self.assertContains(self.response, 'href="{0}"'.format(add_trip_url))

class AddTripTests(TestCase):
    def setUp(self):
        u=User.objects.create(username='username', email='rai_chel@gmail.com')
        u.set_password('blah')
        u.save()
        Trip.objects.create(destination='Paris', description='PARTY!!!', start_date='2017-12-20', end_date='2017-12-21', created_by_id=u.id)
        self.client.login(username='username', password='blah')
        self.client.session.save()
        url = reverse('trips:index')
        self.response = self.client.get(url)
        
    def test_add_trip_view_success_status_code(self):
        url = reverse('trips:add_trip')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_add_trip_url_resolves_new_trip_view(self):
        view = resolve('/trips/add/')
        self.assertEquals(view.func, add_trip)

    def test_add_trip_view_contains_link_back_to_trip_view(self):
        add_trip_url = reverse('trips:add_trip')
        index_url = reverse('trips:index')
        response = self.client.get(add_trip_url)
        self.assertContains(response, 'href="{0}"'.format(index_url))

    def test_csrf(self):
        url = reverse('trips:add_trip')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_add_trip_valid_post_data(self):
        url = reverse('trips:add_trip')
        data = {
            'destination': 'Test location',
            'description': 'Test description',
            'start_date': '2017-12-20',
            'end_date': '2017-12-20',
        }
        response = self.client.post(url, data)

    def test_add_trip_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('trips:add_trip')
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_add_trip_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('trips:add_trip')
        data = {
            'destination': '',
            'description': '',
            'start_date': '',
            'end_date': '',
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)

    def test_contains_form(self): 
        url = reverse('trips:add_trip')
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTripForm)

    def test_add_trip_invalid_post_data(self): 
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('trips:add_trip')
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)