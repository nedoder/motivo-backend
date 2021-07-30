from django.test import TestCase, Client
from ..models import Challenge
from django.urls import reverse
from ..views import UserEditViewSet
client = Client()

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# class testEdit(APITestCase):
#
#     def test_User(self):
#         self.user = User.objects.create(
#             username='test', email='test@test.com', first_name='testing', last_name = 'testtest', password='password')
#
#         self.valid_payload = {
#             'username': 'test',
#             'email': 'test@test.com',
#             'first_name': 'Tanja',
#             'last_name': 'Nedoder',
#             'password' : 'password'
#         }
#
#     def test_editUser(self):
#         url = ('user')
#         data = {'username': 'test'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().username, 'test')

class testChallege(TestCase):

    def test_Challenge(self):
        Challenge.objects.create(
            title='test', coins_to_win=4, description='testtest'
        )

    def test_Test(self):
        try:
            challenge = Challenge.objects.get(title='test')
            self.assertEqual(challenge, 'test')
        except Challenge.DoesNotExist:
            print('You have no challenge to display')