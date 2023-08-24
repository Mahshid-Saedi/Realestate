from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterationForm, UserLoginForm
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

class UserRegisterView(View):
    form_class = UserRegisterationForm
    form_template ='account/register.html'


    def get(self, request):
        form = self.form_class
        return render(request, self.form_template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            request.session['user_registration_info'] = {
                'phone_number':form.cleaned_data['phone_number'],
                'email':form.cleaned_data['email'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password'],

            }
            messages.success(request, 'با موفقیت ثبت نام شدید','success')
            return redirect('home:home')
        return render(request, self.form_template, {'form':form})



class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email = cd['email'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'با موفقیت وارد شدید', 'success')
                return redirect('home:home')
            messages.error(request,'ایمیل یا پسورد اشتباه است', 'error')
        return render(request, self.template_name, {'form':form})

class UserLogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت از حساب کاربری خارج شدید', 'success')
        return redirect('home:home')


