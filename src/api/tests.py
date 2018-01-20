from django.test import TestCase
from .models import Dtag

class ModelTestCase(TestCase):
    """This class defines the test suite for the dtags model"""

    def setUp(self):
        """Define test client"""
        self.dtag_name = "Write world class code"
        self.dtag = Dtag(name=self.dtag_name)

    def test_model_can_create_a_dtag(self):
        old_count = Dtag.objects.count()
        self.dtag.save()
        new_count = Dtag.objects.count()
        self.assertNotEqual(old_count, new_count)
