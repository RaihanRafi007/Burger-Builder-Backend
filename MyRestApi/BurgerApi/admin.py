from django.contrib import admin
from BurgerApi.models import UserProfile
from BurgerApi.models import CustomerDetail, Ingredient, Order

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Ingredient)
admin.site.register(CustomerDetail)
admin.site.register(Order)