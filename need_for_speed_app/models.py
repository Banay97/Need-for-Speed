from django.db import models

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
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
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
    def order_validator(self, postDate):
        errors ={}
        if len(postData['order_name']) < 4:
            errors['order_name'] = 'Order name should be at least 4 characters long'
        if len['order_code_number'] < 10:
            errors['order_code_number'] ='Order Code Number should be at least 10 numbers'
        if len(postDate['pickup_location']):
            errors['pickup_location'] ='Pick up location should be valid'
        if len(postData['pickoff_location']):
            errors['pickoff_location'] = 'Pick off location should be valid'
        return errors                


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('company', 'Company'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number =models.IntegerField()
    address= models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(User):
    def __init__(self, first_name, last_name, phone_number, address):
        super().__init__(self, first_name, last_name, phone_number, address)
        self.status = status
    def display_info(self):
        print(f"The customer {self.first_name} {self.last_name} with phone number {self.phone_number} located in {self.address} is {self.status}")


class Delivery(User):
    def __init__(self, first_name, last_name, phone_number, address):
        super().__init__(self, first_name, last_name, phone_number, address)
        self.license =license
        self.status =status
        self.worklocation = worklocation
    def display_info(self):
        print(f"The driver {self.first_name} {self.last_name} with license number {self.license} is {self.status} and at {self.worklocation} this area now.")

def Company(User):
    def __init__(self, first_name, last_name, phone_number, address):
        super().__init__(self, first_name, last_name, phone_number, address)
        self.company_name =company_name
        self.number_of_workers = number_of_workers

    def display_info(self):
        print(f"The {self.company_name} Company has {self.number_of_workers} employee work in it.")


class Order(models.Model):
    order_name = models.CharField(max_length=255)
    order_code_number = models.IntegerField()
    order_status = models.CharField(max_length=255)
    pickup_location =models.CharField(max_length=255)
    pickoff_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.order_name} - {self.order_number}'


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    status = models.BooleanField()
    context = models.TextField()
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.user.company_name   


            


  



