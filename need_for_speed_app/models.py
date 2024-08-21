from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData, is_creation=False):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters long'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters long'

        if len(postData['phone_number']) < 5:
            errors['phone_number'] = 'Phone Number should be at least 5 characters long' 
        return errors               

  
class OrderManager(models.Manager):
    def order_validator(self, postData):  
        errors = {}
        if len(postData['order_name']) < 4:
            errors['order_name'] = 'Order name should be at least 4 characters long'
        if len(postData['order_code_number']) < 10:  
            errors['order_code_number'] = 'Order Code Number should be at least 10 characters long'
        if len(postData['pickup_location']) < 5:  
            errors['pickup_location'] = 'Pick up location should be valid'
        if len(postData['pickoff_location']) < 5:
            errors['pickoff_location'] = 'Pick off location should be valid'
        return errors               


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('company', 'Company'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)  
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Customer(User):

    status = models.CharField(max_length=50, default='active') 

    def display_info(self):

        print(f"The customer {self.first_name} {self.last_name} with phone number {self.phone_number} located in {self.address} is {self.status}")

    

    def __str__(self):

        return f'{self.first_name} {self.last_name}'    

 

class Delivery(User):

    license = models.CharField(max_length=50, default='N/A')  

    status = models.CharField(max_length=50, default='active')  

    worklocation = models.CharField(max_length=255, default='Unknown')  

    def display_info(self):

        print(f"The driver {self.first_name} {self.last_name} with license number {self.license} is {self.status} and at {self.work_location} this area now.")

    def __str__(self):

        return f'{self.first_name} {self.last_name}'

class Company(User):

    company_name = models.CharField(max_length=255)  

    number_of_workers = models.IntegerField(blank=True, null= True)

   

    def display_info(self):

        print(f"The {self.company_name}Company has {self.number_of_workers}employees working in it.")

    def __str__(self):

        return self.company_name

class Order(models.Model):
    order_name = models.CharField(max_length=255)
    order_code_number = models.IntegerField()
    order_status = models.CharField(max_length=255)
    pickup_location =models.CharField(max_length=255)
    pickoff_location = models.CharField(max_length=255)
    Total = models.IntegerField(default=0)  # Set default value to 0 for new orders
    customer = models.ForeignKey(User, related_name ='user_order', on_delete=models.CASCADE,  null=True, blank=True)
    delivery = models.ForeignKey(Delivery, related_name='delivering_order', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, related_name='order_from_company', on_delete=models.CASCADE, null=True, blank=True)   
    order_status = models.CharField(max_length=100, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.order_name} - {self.order_code_number}'


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    status = models.BooleanField()
    context = models.TextField()
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.user.company_name   


            