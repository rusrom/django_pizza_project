from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return redirect(pizzashop)

@login_required(login_url='/login/')
def pizzashop(request):
    return render(request, 'pizza_app/home.html')

def signup(request):
    return render(request, 'pizza_app/signup.html')
