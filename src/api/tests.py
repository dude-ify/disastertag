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
    def test_api_can_get_a_dtag(self):
        """Thest the api can get a given dtag"""
        dtag = Dtag.objects.get()
        response = self.client.get(
                reverse('details', kwargs={'pk': dtag.id}), 
                format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, dtag)

    def test_api_can_update_dtag(self):
        """Test the api can update a given dtag"""
        dtag = Dtag.objects.get()
        change_dtag = {'name': 'Reborn dtag'}
        res = self.client.put(
                reverse('details', kwargs={'pk':dtag.id}),
                change_dtag, 
                format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_dtag(self):
        """Test the api can delete a dtag"""
        dtag = Dtag.objects.get()
        response = self.client.delete(
                reverse('details', kwargs={'pk': dtag.id}),
                format="json",
                follow=True)
