from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import UserForm, PizzaShopForm


def home(request):
    return redirect(pizzashop)

@login_required(login_url='/login/')
def pizzashop(request):
    return render(request, 'pizza_app/home.html')

def signup(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()


    if request.method == 'POST':
        user_form = UserForm(request.POST)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizzashop_form.save(commit=False)
            new_pizzashop.owner = new_user
            new_pizzashop.save()

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
            ))

            return redirect(pizzashop)


    context = {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form,
    }
    return render(request, 'pizza_app/signup.html', context)
