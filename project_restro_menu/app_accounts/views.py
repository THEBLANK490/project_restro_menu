from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.views import View
from django.contrib import auth, messages
from django.db.models import Count
# from django.contrib.auth.decorators import login_required
from app_menus.models import Menu

# Create your views here.

class DashboardView(LoginRequiredMixin,View):
    login_url = '/login/' 
    def get(self,request):
        menu_total = Menu.objects.aggregate(Count('id'))
        context ={"menu_total":menu_total.get('id__count')}
        return render(request,'dashboard.html',context)

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request, "You're logged out...")
        return redirect('login')

class LoginView(View):
    def get(self,request):
        return render(request ,'accounts/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'You are logged in...')
                return redirect('menu-list')
            messages.error(request,"Login Failed.")
            return redirect('login')

        except User.DoesNotExist as error:
            print(error)

class RegisterView(View):
    def get(self,request):
        return render(request,'accounts/register.html')

    def post(self,request):
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username = username, email=email, password= password)
        if user is not None:
            user.first_name = fname
            user.last_name = lname
            user.is_active = True
            user.save()
            return redirect('login')
        return redirect('register')