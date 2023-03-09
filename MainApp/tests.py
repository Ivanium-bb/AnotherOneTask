from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse
from rest_framework_simplejwt.tokens import *

from MainApp.models import UserData, Notes
from django.contrib.auth.hashers import make_password

factory = APIRequestFactory()


class AccountTests(APITestCase):

    def test_sign_up(self):
        url = reverse('sign_up')
        data = {
            'email': 'test@test.com',
            'name': 'test',
            'password': 'Skzw11235'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserData.objects.count(), 1)
        self.assertEqual(UserData.objects.get().name, 'test')

    def test_log_in(self):
        password = make_password('Skzw11235')
        UserData.objects.create(email="test@test.com", name='test', password=password)
        url = reverse('log_in')
        data = {
            'email': 'test@test.com',
            'password': 'Skzw11235'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('refresh' and 'access' in response.data)


class NoteTests(APITestCase):
    def test_get(self):
        password = make_password('Skzw11235')
        test_user = UserData.objects.create(email="test@test.com", name='test', password=password)
        Notes.objects.create(author=test_user, title='test_title', description='test_decription')
        url = reverse('note-list')
        header = {'Authorization': 'BadToken'}
        response = self.client.get(url, format='json', **header)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        token = RefreshToken.for_user(test_user)
        header = {'HTTP_AUTHORIZATION': f'Bearer {str(token.access_token)}'}
        response = self.client.get(url, **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['count'] >= 1)

    def test_delete(self):
        password = make_password('Skzw11235')
        test_user1 = UserData.objects.create(email="test1@test.com", name='test1', password=password)
        test_user2 = UserData.objects.create(email="test2@test.com", name='test2', password=password)
        test_user1_notes = Notes.objects.create(author=test_user1, title='test_title1', description='test_decription1')
        test_user2_notes = Notes.objects.create(author=test_user2, title='test_title2', description='test_decription2')


        url = reverse('note-detail', kwargs={'id': test_user1_notes.id})
        token = RefreshToken.for_user(test_user1)
        header = {'HTTP_AUTHORIZATION': f'Bearer {str(token.access_token)}'}
        self.client.delete(url, **header)

        url = reverse('note-detail', kwargs={'id': test_user2_notes.id})
        self.client.delete(url, **header)
        self.assertFalse(Notes.objects.contains(test_user1_notes))
        self.assertTrue(Notes.objects.contains(test_user2_notes))

