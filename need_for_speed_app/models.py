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

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"    

        if len(postData['email']) < 10:
            errors['email'] = 'Email should be at least 10 characters long'    

        if is_creation:
            if len(postData['password']) < 8:
                errors['password'] = 'Password should be at least 8 characters long'

            if postData['password'] != postData['confirm_password']:
                errors['confirm_password'] = 'Passwords do not match'
        
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
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(User):
    status = models.CharField(max_length=50, default='active') 
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    def display_info(self):
        print(f"The customer {self.first_name} {self.last_name} with phone number {self.phone_number} located in {self.address} is {self.status}")


class Delivery(User):
    license = models.CharField(max_length=50, default='N/A')  
    status = models.CharField(max_length=50, default='active')  
    worklocation = models.CharField(max_length=255, default='Unknown')  

    def display_info(self):
        print(f"The driver {self.first_name} {self.last_name} with license number {self.license} is {self.status} and at {self.work_location} this area now.")


class Company(User):
    company_name = models.CharField(max_length=255)  
    number_of_workers = models.IntegerField() 
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    def display_info(self):
        print(f"The {self.company_name} Company has {self.number_of_workers} employees working in it.")


class Order(models.Model):
    order_name = models.CharField(max_length=255)
    order_code_number = models.IntegerField()
    order_status = models.CharField(max_length=255)
    pickup_location =models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, related_name ='customer_order', on_delete=models.CASCADE,  null=True, blank=True)
    delivery = models.ForeignKey(Delivery, related_name='delivering_order', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, related_name='order_from_company', on_delete=models.CASCADE, null=True, blank=True)   
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


            


  



