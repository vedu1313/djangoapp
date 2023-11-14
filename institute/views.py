# Create your views here.
from django.shortcuts import render,redirect
from .models import Course, Instructor,contact

def home(request):
    courses = Course.objects.all()
    instructors = Instructor.objects.all()
    return render(request, 'home.html', {'courses': courses, 'instructors': instructors})

def  course(request):
    return render(request,'course.html')

def  contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.objects.create(name=name,email=email,message=message)
        return redirect(home)
    return render(request,'contact.html')

def  about(request):
    return render(request,'about_us.html')