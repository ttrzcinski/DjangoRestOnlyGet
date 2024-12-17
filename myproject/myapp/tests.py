from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import SingleRoll

class SingleRollAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        SingleRoll.objects.create(name="1")
        SingleRoll.objects.create(name="20")

    def test_get_rolls(self):
        response = self.client.get(reverse('rolls-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # There will be 3, because 2 stubbed and 1 random
        self.assertEqual(len(response.data), 3)
