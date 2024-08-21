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
    path('company-dashboard', views.company_dashboard, name='company_dashboard'),
    # path('create-company', views.create_company, name='create_company'),
    # path('update-company', views.update_company, name='update_company'),
    # path('view-all-companies', views.view_companies, name='view_companies'),

    #Company pages and CRUD operations
    path('create-order', views.create_order, name='create_order'),
    path('update-order', views.update_order, name='update_order'),
    path('view-all-orders', views.view_orders, name='view_orders'),
 
     # Admin Dashboard
    path('admindashboard/', views.admin_dashboard_view, name='admin_dashboard'),

    # User Management
    path('admin/users/', views.admin_users_view, name='admin_users'),
    path('admin/users/edit/<int:user_id>/', views.admin_user_edit_view, name='admin_user_edit'),
    path('admin/users/delete/<int:user_id>/', views.admin_delete_user_view, name='admin_delete_user'),

    # Company Management
    path('admin/companies/', views.admin_companies_view, name='admin_companies'),
    path('admin/companies/edit/<int:company_id>/', views.admin_company_edit_view, name='admin_company_edit'),
    path('admin/companies/delete/<int:company_id>/', views.admin_company_delete_view, name='admin_company_delete'),

    # Order Management
    path('admin/orders/', views.admin_orders_view, name='admin_orders'),
    path('admin/orders/detail/<int:order_id>/', views.admin_order_detail_view, name='admin_order_detail'),
    path('admin/orders/delete/<int:order_id>/', views.admin_order_delete_view, name='admin_order_delete')
]
