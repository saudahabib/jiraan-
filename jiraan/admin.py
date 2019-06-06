from django.contrib import admin
from .models import User, Business, Neighborhood
# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(User)
