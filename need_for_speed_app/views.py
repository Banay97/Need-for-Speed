from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse , JsonResponse
import bcrypt
from .models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'AboutUs.html')

def contact_us(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        service_type = request.POST.get('service_type')
        comment = request.POST.get('comment')
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'service_type': service_type,
            'comment': comment
        }

    return render(request, 'ContactUs.html', {}) 

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
    
        if user and bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['email'] = email
            if user.role == 'admin':
                messages.success(request, 'Welcome!')
                return render(request, 'AdminDashboard.html', {'user': user})
            else:
                messages.success(request, 'Welcome!')
                return render(request, 'CompanyDashboard.html', {'user': user})
        else:
            messages.error(request, 'Invalid email or password', extra_tags='sign_in')
            return redirect('sign_in')
        
    return render(request, 'SignIn.html')     


def sign_up(request):
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='sign_up')
            return redirect('sign_up')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
            role =request.POST.get('role')
            email = request.POST['email']
            password = request.POST['password']
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number= phone_number,
                role = role,
                email=email,
                password=hashed_password
                )
            user.save()
            if user.role == 'admin':
                messages.success(request, 'Registration successful! Please log in.')
                return render(request, 'AdminDashboard.html', {'user': user})
            else:
                messages.success(request, 'Registration successful! Please log in.')
                return render(request, 'CompanyDashboard.html', {'user': user})
    else:
        return render(request, 'SignUp.html') 

def sign_out(request):
    if request.method == 'POST':
        request.session.flush()# make sure all session data is securely removed
        messages.success(request, 'Logout successful!', extra_tags='sign_out')
        return redirect('home')
    return redirect('home')     
    

def services(request):
    return render(request, 'Services.html')   

def admin_dashboard(request):
    return render(request, 'AdminDashboard.html')

def  create_company(request):
    return render(request, 'CreateComapny.html')

def  update_company(request):
    return render(request, 'UpdateComapny.html')

def  view_companies(request):
    return render(request, 'ViewAllComapnies.html')


def company_dashboard(request):
    return render(request, 'CompanyDashboard.html')

def create_order(request):
    return render(request, 'CreateOrder.html')     

def update_order(request):
    return render(request, 'UpdateOrder.html') 

def view_orders(request):
    return render(request, 'ViewAllOrders.html') 