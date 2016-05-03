from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status

from accounts.views import UserSignupView


class TestSignup(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_user_signup(self):
        url = reverse('user_signup')
        view = UserSignupView.as_view()
        request = self.factory.post(
            url, {'email': 'shabeer.ayar@gmail.com', 'first_name': 'shabeer', 'last_name': 'ayar', 'password': 'test1234'})
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_signup_withoutemail(self):
        url = reverse('user_signup')
        view = UserSignupView.as_view()
        request = self.factory.post(
            url, {'first_name': 'shabeer', 'last_name': 'ayar', 'password': 'test1234'})
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_signup_invalidpassword(self):
        url = reverse('user_signup')
        view = UserSignupView.as_view()
        request = self.factory.post(
            url, {'email': 'shabeer.ayar@gmail.com', 'first_name': 'shabeer', 'last_name': 'ayar', 'password': 'test'})
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
