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



def  create_company(request):
     return render(request, 'CreateComapny.html')

def  update_company(request):
      return render(request, 'UpdateComapny.html')

def  view_companies(request):
    return render(request, 'ViewAllComapnies.html')


def company_dashboard(request):
    return render(request, 'CompanyDashboard.html')

def create_order(request):
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='create_order')
            return redirect('create_order')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address =request.POST['address']
            phone_number = request.POST['phone_number']
            company_name = request.POST['company_name']
            phone_number = request.POST['phone_number']
            order_name = request.POST['order_name']
            order_code_number = request.POST['order_code_number']
            order_price = request.POST['order_price']
            pickup_location = request.POST['pickup_location']
            pickoff_location = request.POST['pickoff_location']
            customer = User.objects.create(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number)
            company = Company.objects.create(company_name=company_name, phone_number=phone_number)
            order = Order.objects.create(order_name=order_name, company=company, order_code_number=order_code_number, pickup_location=pickup_location, pickoff_location=pickoff_location)

            messages.success(request, 'Your order has beed created successfully')
            return redirect('create_order')  
    else:
        return render(request, 'CreateOrder.html')  

def update_order(request):
    return render(request, 'UpdateOrder.html') 

def view_orders(request):
    return render(request, 'ViewAllOrders.html') 

def admin_dashboard(request):
    return render(request, 'admin/index.html')
#############admindashboard

# Admin Dashboard View
def admin_dashboard_view(request):
    users = User.objects.all()
    companies = Company.objects.all()
    orders = Order.objects.all()

    context = {
        'users': users,
        'companies': companies,
        'orders': orders,
    }
    return render(request, 'admin/AdminDashboard.html', context)

# User Management Views
def admin_users_view(request):
    users = User.objects.all()
    return render(request, 'admin/admin_user.html', {'users': users})

def admin_user_edit_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.role = request.POST.get('role')
        user.save()
        return redirect('admin/admin_users')

    return render(request, 'admin_user_edit.html', {'user': user})

def admin_delete_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('admin/admin_users')

# Company Management Views
def admin_companies_view(request):
    companies = Company.objects.all()
    return render(request, 'admin/admin_company.html', {'companies': companies})

def admin_company_edit_view(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        company.company_name = request.POST.get('company_name')
        company.address = request.POST.get('address')
        company.phone_number = request.POST.get('phone_number')
        company.email = request.POST.get('email')
        company.save()
        return redirect('admin_companies')

    return render(request, 'admin/admin_company_edit.html', {'company': company})

def admin_company_delete_view(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    company.delete()
    return redirect('admin_companies')

# Order Management Views
def admin_orders_view(request):
    orders = Order.objects.all()
    return render(request, 'admin/admin_order.html', {'orders': orders})

def admin_order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin_order_detail.html', {'order': order})

def admin_order_delete_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('admin_orders')