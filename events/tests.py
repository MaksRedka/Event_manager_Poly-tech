from django.test import TestCase
from .models import Event
from django.contrib.auth.models import User
from rest_framework import status
import json
import requests
# Create your tests here.
URL = 'http://127.0.0.1:8000/events/'

def get_response_with_token():
    data = {
        'username': 'admin',
        'password': 'admin',
    }
    
    url = URL + 'api-token-auth/'
    response = requests.post(url, data=data)
    return response


class PostMethodTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user('admin', 'admin@gmain.com', 'admin')

    def test_post_method_status_201(self):
        info_json = json.loads('{ "name":"John", "age":30, "city":"New York"}')
        
        response = get_response_with_token()
        token = json.loads(response.text).get('token')

        data = {
            'event_type':'test',
            'info':info_json,
            'timestamp':'1969-7-20',
        }
        headers = {'Authorization': 'Token ' + str(token)}
        url = URL + 'api/'
        
        response = requests.post(url, data=data, headers=headers)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_post_method_status_400(self):
        url = URL + 'api/'
        response = get_response_with_token()
        token = json.loads(response.text).get('token')
        headers = {'Authorization': 'Token ' + str(token)}
        data = {'event_type': 'a'}

        response = requests.post(url, headers=headers, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_token(self):
        response = response = get_response_with_token()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
