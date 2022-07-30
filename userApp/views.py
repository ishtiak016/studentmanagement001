from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login
from product.models import Category, Product, Images
from EcomApp.models import Setting
from django.contrib import messages
# Create your views here.
def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.warning(request, 'Your username or password is invalid  ')
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={'setting': setting,'category': category}
    return render(request,'userlogin.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_registration(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={'setting': setting,'category': category}
    return render(request,'userregister.html',context)
