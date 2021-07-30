from django.test import TestCase, Client
from ..models import Challenge
from django.urls import reverse
from ..views import UserEditViewSet
import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
# Create your tests here.
class UserEditTestCase(APITestCase):
    """ Test case for logging activity"""
    def setUp(self):
        # Initialize API client
        self.client = APIClient()
        # Create a user
        self.simpleuser = User.objects.create(username='test', email='test@test.com', first_name='Testy', last_name='Testing')
        self.simpleuser.set_password("MyPassword")

        self.simpleuser.save()
        post_data = {'username':'test', 'password':'MyPassword'}
        response = self.client.post('/api/token/', post_data)
        self.token = response.json()['access']
    def test_user_edit(self):
        """
        Test checks if the user was created in the database.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {'id': str(self.simpleuser.id), 'username': self.simpleuser.username, 'password': 'MyPassword'}
        response = self.client.put('/user/', json.dumps(data), content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)