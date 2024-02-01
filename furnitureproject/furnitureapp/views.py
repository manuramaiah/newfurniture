from django.shortcuts import render , redirect
from .models import products
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    objects = products.objects.all()
    return render(request, 'index.html', {'objects': objects})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def furniture(request):
    return render(request, 'furniture.html')
def blog(request):
    return render(request, 'blog.html')
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken Please  choose another')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken Please  choose another')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
# for user login
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

# logout function
def logout(request):
    auth.logout(request)
    return redirect('/')


class AboutView(TemplateView):
    template_name = 'about.html'  # Replace with the actual template name
