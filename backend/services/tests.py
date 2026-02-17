from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Service

class ServiceApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.service1 = Service.objects.create(
            name="Polimento",
            description="Polimento premium",
            price_start=500.00,
            icon_name="✨"
        )
        self.service2 = Service.objects.create(
            name="Lavagem",
            description="Lavagem detalhada",
            price_start=150.00,
            icon_name="water"
        )

    def test_get_services(self):
        """
        Ensure we can retrieve the list of services.
        """
        url = reverse('service-list')  # Assuming router created 'service-list'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Polimento")
