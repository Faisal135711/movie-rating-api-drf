from rest_framework.test import APITestCase
from rest_framework import status 
from rest_framework.authtoken.models import Token 

from django.urls import reverse
from django.contrib.auth.models import User

from watchlist_app import models
from watchlist_app.api import serializers


class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="12345")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix",
                                                           about="netflix",
                                                           website="https://netflix.com")

    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "netflix",
            "website": "https://netflix.com"
        } 
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
