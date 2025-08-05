from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        'variable1':"Uday",
        'variable2':"Rupali"
    }
    messages.success(request, "This is a test message")
    return render(request,'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()

        messages.success(request, "Your message was sent successfully!")

        return redirect('/contacts/')
    return render(request, 'contacts.html')