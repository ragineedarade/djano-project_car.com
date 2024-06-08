from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def images(request):
    return render(request, 'about.html')


def contact(request):
    n = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # case = contact(name=name, email=email, message=message)
        # case.save()
        n = 'Data Send Successfully'
    return render(request, 'contact.html', {'n': n})
