from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contact, Courses
# Create your views here.
def About(request):
    coursedata = Courses.objects.values()
    for item in coursedata:
        # print(item)
        return render(request,'orbils/about.html',{"coursedata": coursedata})

def AllCourses(request):
    coursedata = Courses.objects.values()
    for item in coursedata:
        # print(item)
        return render(request,'orbils/allcourses.html',{"coursedata": coursedata})

def Events(request):
    return render(request,'orbils/events.html')

def ContactUs(request):
    if (request.method == "POST"):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['number']
        querry = request.POST['querry']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        zip = request.POST['zip']
        contact = Contact(firstname = firstname, lastname = lastname, email = email, number = phone, querry = querry, add1 = add1, add2 = add2, country = country, city = city, state = state, zip = zip)
        contact.save()
    return render(request,'orbils/contact-us.html')

def CourseView(request, myid):
    #fetch the product using id
    course = Courses.objects.filter(courseId=myid)
    print(course)
    return render(request,'orbils/courseview.html', {'course':course[0]})

def CartView(request,myid):
    course = Courses.objects.filter(courseId=myid)
    print(course)
    return render(request,'orbils/cart-view.html',{'course':course[0]})