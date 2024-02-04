from django.http import HttpResponse
from django.shortcuts import render
from .forms import Signup_form

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
