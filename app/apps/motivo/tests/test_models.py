from ..models import Profile, Attempt
import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

class UserEditTestCase(APITestCase):
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
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {'id': str(self.simpleuser.id), 'username': self.simpleuser.username, 'password': 'MyPassword'}
        response = self.client.put('/user/', json.dumps(data), content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestInvalidUserEntry(APITestCase):
    #returns django.db.utils.IntegrityError: NOT NULL constraint failed: motivo_profile.user_id
    #maybe some more user friendly error messages?
    def setUp(self):
        Profile.objects.create(title='nedoder',collected_coins=1000)

    def test_access(self):
        Profile.objects.get(title='nedoder')
        self.assertEqual(Profile.objects.count(), 1)

class TestInvalidUser(APITestCase):
    #returns user with just a username, wrong?
    def setUp(self):
        User.objects.create(username='nedoder')

    def test_access(self):
        User.objects.get(username='nedoder')
        self.assertEqual(User.objects.count(), 1)

class TestAttemptWithAnotherUserData(APITestCase):
    #returns ValueError: Cannot assign "'nedoder'": "Attempt.user" must be a "User" instance.
    #cannot access attempts with another user's data
    def setUp(self):
          Attempt.objects.create(user='nedoder', challenge=1)

    def test_access(self):
          Attempt.objects.get(user='nedoder')
          self.assertEqual(Attempt.objects.count(), 1)