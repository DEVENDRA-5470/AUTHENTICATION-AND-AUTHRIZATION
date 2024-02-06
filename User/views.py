from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib import messages

def sign_up(request):
    if request.method == "POST":
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration successful")
        else:
            
            return render(request, 'signup.html', {'form': form})
    else:
        form = Signup_form()
        return render(request, 'signup.html', {'form': form})





def login_form(request):
    if request.method == 'POST':
        form = Login_form(request=request ,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = Login_form()
    return render(request, 'login.html', {'form': form})


# def login_form(request):
#     if request.method=='POST':
#         form=Login_form(request,data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             user=authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 form=Login_form()
#                 form.add_error('username', 'Invalid username or password')
#                 return render(request, 'login.html', {'form': form})
#     form=Login_form()
#     return render(request,'login.html',{'form':form})