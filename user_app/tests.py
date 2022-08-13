from rest_framework.test import APITestCase
from rest_framework import status 
from rest_framework.authtoken.models import Token 

from django.urls import reverse
from django.contrib.auth.models import User

class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testcase",
            "email": "test@test.com",
            "password": "123321",
            "password2": "123321"
        }

        response = self.client.post(reverse("register"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
