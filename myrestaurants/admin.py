from django.contrib import admin
import myrestaurants.models

# Register your models here.
admin.site.register(myrestaurants.models.Restaurant)
admin.site.register(myrestaurants.models.Dish)
admin.site.register(myrestaurants.models.RestaurantReview)
