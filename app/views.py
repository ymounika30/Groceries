from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from django.views import View


def home(request):
    return render(request,'home.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'signup.html', { 'form': UserCreationForm() })

    def post(self, request):
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect(reverse('login'))

        return render(request, 'signup.html', { 'form': fm })


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', { 'form':  AuthenticationForm })

    # really low level
    def post(self, request):
        fm = AuthenticationForm(request, data=request.POST)
        if fm.is_valid():
            user = authenticate(
                request,
                username=fm.cleaned_data.get('username'),
                password=fm.cleaned_data.get('password')
            )

            if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In Successfully!!!')
                    return redirect(reverse('profile'))
            else:
                fm=AuthenticationForm()
            return render(request,'login.html',{'form':fm})
        return redirect(reverse('profile'))


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')

    