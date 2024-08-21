from django.contrib import admin
from .models import User, Order, Notification, Customer, Delivery, Company
# Register your models here.

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Delivery)
admin.site.register(Company)


