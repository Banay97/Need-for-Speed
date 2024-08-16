from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about_us, name='about_us'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),
]
