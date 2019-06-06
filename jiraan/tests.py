from django.test import TestCase
from .models import Neighborhood, Business, User
# Create your tests here.

class NeighborhoodTestClass(TestCase):
    #set up method
    def setUp(self):
        self.hood1 = Neighborhood(hood_name='majengo',hood_location='mombasa',hood_count=258)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood1, Neighborhood))

    def test_save_hood(self):
        self.hood1.save_hood()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods)>0)

    def test_del_hoods(self):
        self.hood1.delete_hood()
        removed=Neighborhood.objects.all()
        self.assertTrue(len(removed)==0)
