from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def About(request):
    return render(request,'orbils/about.html')