from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Dtag

class ModelTestCase(TestCase):
    """This class defines the test suite for the dtags model"""

    def setUp(self):
        """Define test client"""
        self.dtag_name = "Test dTag"
        self.dtag = Dtag(name=self.dtag_name)

    def test_model_can_create_a_dtag(self):
        old_count = Dtag.objects.count()
        self.dtag.save()
        new_count = Dtag.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.dtag_data = {'name': 'John Doe'}
        self.response = self.client.post(
                reverse('create'),
                self.dtag_data,
                format="json")

    def test_api_can_create_a_dtag(self):
        """Test the api can make dtags"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
