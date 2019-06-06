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


class UserTestClass(TestCase):
    def setUp(self):

        '''create a new instance of a hood and save it'''
        self.hood1 = Neighborhood(hood_name='majengo',hood_location='mombasa',hood_count=258)
        self.hood1.save_hood()

        '''create an instance of a user and save it'''
        self.user1 = User(first_name='sukmah', user_id
        ='147', email_address='sukmah@gmail.com', neighborhood_id=self.hood1)

    def tearDown(self):
        Neighborhood.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user1,User))

    def test_save_user(self):
        self.user1.save_users()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

    def test_delete_user(self):
        self.user1.delete_user()
        users=User.objects.all()
        self.assertTrue(len(users)==0)

class BusinessTestClass(TestCase):
    def setUp(self):
        '''create a new instance of a hood and save it'''
        self.hood1 = Neighborhood(hood_name='majengo',hood_location='mombasa',hood_count=258)
        self.hood1.save_hood()

        '''create an instance of a user and save it'''
        self.user1 = User(first_name='sukmah', user_id
        ='147', email_address='sukmah@gmail.com', neighborhood_id=self.hood1)
        self.user1.save_users()
        '''create an instance of a business and delete it'''
        self.bus1=Business(business_name='shahidi', user=self.user1,neighborhood_id=self.hood1,business_address='shahidi@gmail.com')


    def tearDown(self):
        Neighborhood.objects.all().delete()
        User.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.bus1, Business))


    def test_save_bus(self):
        self.bus1.save_bus()
        saved_bus=Business.objects.all()
        self.assertTrue(len(saved_bus)>0)

    def test_delete_bus(self):
        self.bus1.delete_bus()
        deleted_bus=Business.objects.all()
        self.assertTrue(len(deleted_bus)==0)
