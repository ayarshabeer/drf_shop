from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status

from model_mommy import mommy, generators

from accounts.models import User
from products.models import Manufacturer
from products.views import ManufacturerViewSet


class TestManufacturer(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = mommy.make(User, email='testuser@drf_shop.com')
        self.staff = mommy.make(User, email='staff@drf_shop.com', is_staff=True)

    def test_create_manufacture(self):
        url = reverse('manufacturer-list')
        view = ManufacturerViewSet.as_view({'post': 'create'})
        request = self.factory.post(
            url, {'name': 'apple', 'slug': 'apple'})
        force_authenticate(request, user=self.staff)
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        manufactures = Manufacturer.objects.all()
        self.assertEqual(len(manufactures), 1)
        self.assertEqual(manufactures[0].name, 'apple')

    def test_create_manufacture_unauthorised(self):
        url = reverse('manufacturer-list')
        view = ManufacturerViewSet.as_view({'post': 'create'})
        request = self.factory.post(
            url, {'name': 'apple', 'slug': 'apple'})
        force_authenticate(request, user=self.user)
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_manufacture_withoutlogin(self):
        url = reverse('manufacturer-list')
        view = ManufacturerViewSet.as_view({'post': 'create'})
        request = self.factory.post(
            url, {'name': 'apple', 'slug': 'apple'})
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
