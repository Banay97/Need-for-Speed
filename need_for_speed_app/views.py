from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'AboutUs.html')

def contact_us(request):
    return render(request, 'ContactUs.html') 

def sign_in(request):
    return render(request, 'SignIn.html')       


def sign_up(request):
    return render(request, 'SignUp.html') 