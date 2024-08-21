from django.contrib import admin
from need_for_speed_app.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'role')
    list_filter = ('role',)
    ordering = ('-created_at',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'number_of_workers', 'phone', 'email')
    search_fields = ('company_name', 'email')
    ordering = ('company_name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone','email', 'status')
    search_fields = ('name', 'phone')
    ordering = ('name',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'license', 'status', 'worklocation')
    search_fields = ('first_name', 'last_name', 'license', 'worklocation')
    list_filter = ('status',)
    ordering = ('first_name',)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'customer', 'company', 'pickup_location', 'dropoff_location', 'order_status', 'created_at')
    search_fields = ('order_name', 'customer__name', 'company__name')
    list_filter = ('order_status',)
    ordering = ('-created_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'context', 'link', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'context')
    list_filter = ('status',)
    ordering = ('-created_at',)

# Customizing the admin site's appearance
admin.site.site_header = "Need for Speed Admin"
admin.site.site_title = "Need for Speed Admin Portal"
admin.site.index_title = "Welcome to Need for Speed Administration"
