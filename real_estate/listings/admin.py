from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Agent, Buyer, Property, Listing, Review

admin.site.register(Agent)
admin.site.register(Buyer)
admin.site.register(Property)
admin.site.register(Listing)
admin.site.register(Review)

