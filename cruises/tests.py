from django.test import TestCase, Client
from .models import Ship,Cruise, Cabin

# Create your tests here.
class CruiseTests(TestCase):
    fixtures =['cruises']

    def test_index(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cruise')
        self.assertContains(response, 'Davenport-Ponce')
