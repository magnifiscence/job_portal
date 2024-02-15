import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from ..serializers import UserSerializer, UserSerializerWithToken
from django.contrib.auth.models import User

# initialize the APIClient app
client = APIClient()


class GellAllJobsTest(TestCase):
    """ Test module for GET all jobs API """

    def test_get_all_jobs(self):
        response = client.get('/users/')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class UserLoginTest(TestCase):
    """ Test module for GET single User API """

    def setUp(self):
        User.objects.create_user(username="test", password="test")

    def test_get_valid_single_User(self):
        response = client.post('/token-auth/', data=json.dumps({
            "username": "test",
            "password": "test"
        }), content_type='application/json')

        user = User.objects.get(username="test")
        serializer = UserSerializer(user)
        self.assertEqual(response.data['user'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_username(self):
        response = client.post('/token-auth/', data=json.dumps({
            "username": "none",
            "password": "test"
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_invalid_password(self):
        response = client.post('/token-auth/', data=json.dumps({
            "username": "test",
            "password": "none"
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserSignUpTest(TestCase):
    """ Test module for GET single User API """

    def setUp(self):
        response = client.post('/users/', data=json.dumps({
            "username": "test2",
            "password": "test2",
            "firstName": "test",
            "lastName": "test",
        }), content_type='application/json')
        self.token = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_created_user_with_JWT_auth(self):
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/users/current_user/',
                              content_type='application/json')

        user = User.objects.get(username="test2")
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.credentials()


class UserUpdateTest(TestCase):
    """ Test module to update user profile """

    def setUp(self):
        response = client.post('/users/', data=json.dumps({
            "username": "test2",
            "password": "test2",
            "firstName": "test",
            "lastName": "test",
        }), content_type='application/json')
        self.token = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_signup(self):
        response = client.post('/users/', data=json.dumps({
            "username": "test2",
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_profile_update(self):
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/users/current_user/',
                              content_type='application/json')
        user = response.data
        user['username'] = "test3"
        user['profile']['bio'] = "ABC"
        user['profile']['education'] = "ABC"
        user['profile']['experiance'] = "ABC"
        user['profile']['birthDate'] = "2020-11-11"

        response = client.put('/users/current_user/', data=json.dumps(user),
                              content_type='application/json')

        user = User.objects.get(username="test3")
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.credentials()

    def test_invalid_user_profile_update(self):
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/users/current_user/',
                              content_type='application/json')
        user = response.data
        response = client.put('/users/current_user/', data=json.dumps(user),
                              content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        client.credentials()