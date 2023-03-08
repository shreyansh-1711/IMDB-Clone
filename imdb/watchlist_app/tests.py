from django.contrib.auth.models import User     
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="testcase", password="Testcase@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token '+self.token.key)
        
    
    def test_streamplatform_create(self):
        data = {
            "name": "Netlfix",
            "about": "#1 stream platform",
            "website": "https://netflix.com",
        }
        
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)