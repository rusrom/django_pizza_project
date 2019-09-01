from django.shortcuts import render


def home(request):
    return render(request, 'pizza_app/home.html')
