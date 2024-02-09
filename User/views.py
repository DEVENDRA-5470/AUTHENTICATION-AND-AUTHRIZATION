from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    user=User.objects.all()
    data={'user':user}
    return render(request,"home.html",data)


def dashboard(request):
    if request.user.is_authenticated:
        user=User.objects.all()
        data={'name':request.user,'user':user}
        return render(request,"dashboard.html",data)
    else:
        return redirect('login_form')



def sign_up(request):
    if request.method == "POST":
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_form")
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
                return redirect('/dashboard')
    else:
        form = Login_form()
    return render(request, 'login.html', {'form': form})


def logout_here(request):
    logout(request)
    return redirect("login_form")





def change_pass(request):
    if request.user.is_authenticated:
        try:
            if request.method=="POST":
                form=ch_pass_form(user=request.user , data=request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('login_form')
                else:
                    return render(request,"change_pass.html",{'form':form})
        except Exception as e:
            messages.error(request,"Please Login to change password ")
            return render(request,"change_pass.html",{'form':form})
        else:
            form=ch_pass_form(user=request.user , data=request.POST)
        return render(request,"change_pass.html",{'form':form})
    else:
        return redirect("login_form")



def recover_pass(request):
    return render(request,"recover_pass.html")

