from django.urls import path
from . import views

urlpatterns = [
    #main website pages
    path('', views.home, name='home'),
    path('about-us', views.about_us, name='about_us'),
    path('services', views.services, name='services'),
    path('contact-us', views.contact_us, name='contact_us'),

    #Sign in, up, and out paths
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('sign-out', views.sign_out, name='sign_out'),
    
    #admin pages and CRUD operations
    path('admin-dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('create-company', views.create_company, name='create_company'),
    path('update-company', views.update_company, name='update_company'),
    path('view-all-companies', views.view_companies, name='view_companies'),

    #Company pages and CRUD operations
    path('company-dashboard', views.company_dashboard, name='company_dashboard'),
    path('create-order', views.create_order, name='create_order'),
    path('update-order', views.update_order, name='update_order'),
    path('view-all-orders', views.view_orders, name='view_orders'),


    
]
