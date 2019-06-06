from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    hood_name=models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    hood_count=models.CharField(max_length=50)

class User(models.Model):
    first_name=models.CharField(max_length=50)
    user_id=models.IntegerField(max_length=50)
    email_address=models.CharField(max_length=50)
    neighborhood_id=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

class Business(models.Model):
    business_name=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood_id=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    business_address=models.CharField(max_length=50)
