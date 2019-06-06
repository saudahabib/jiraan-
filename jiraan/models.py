from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    hood_name=models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    hood_count=models.CharField(max_length=50)

    #save function
    def save_hood(self):
        self.save()

    #delete function
    def delete_hood(self):
        del_hoods=Neighborhood.objects.all().delete()
        return del_hoods

    def __str__(self):
        return self.hood_name

    class Meta:
        ordering = ['-id']

class User(models.Model):
    first_name=models.CharField(max_length=50)
    user_id=models.IntegerField()
    email_address=models.CharField(max_length=50)
    neighborhood_id=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name

class Business(models.Model):
    business_name=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood_id=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    business_address=models.CharField(max_length=50)


    def __str__(self):
        return self.business_name
