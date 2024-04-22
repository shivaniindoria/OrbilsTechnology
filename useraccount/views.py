from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from notifypy import Notify

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('/')
        else:
            messages.error(request,'invalid username or password!')
            return redirect('login')
    return render(request,"useraccount/login.html")

def SignUpView(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        useremail = request.POST['useremail']
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['confirmpassword']

        if pass1 != pass2:
            messages.error(request,'Password didn\'t match')

        # checks for username
        if len(username) > 15 :
            messages.error(request,'Username must be less under 10 characters')
            return redirect('signup')
        #checks for password
        if len(pass1) < 8 :
            messages.error(request,'Password should have minimum length of 8 characters.')
            return redirect('signup')
        #     pass
        # if not any(char.isupper() for char in pass1) or not any(char.islower() for char in pass1) or not any(char.isdigit() for char in pass1) :
        #     pass
        # if not any(not char.isalnum() for char in pass1):
        #     messages.error(request,'Instructions: 1. Password should have minimum length of 8 characters.',
        #                 '2. Password must contains at least one uppercase and one lowercase letter and one digit (0-9).',
        #                 '3. Password must contains at least one special character such as !, @, #, $, %, etc.')
        #     return redirect('signup')

        new_user = User.objects.create_user(username=username, password=pass1)
        new_user.first_name=firstname
        new_user.last_name=lastname
        new_user.email=useremail
        new_user.save()
        print('account has been created successfully')
        messages.success(request, 'Account has been created successfully')
        return render(request, 'useraccount/signup.html')
    return render(request,"useraccount/signup.html")

# def ForgotPasswordView(request):
#     return render(request,'forgot-password.html')
# def PasswordResetView(request):
#     return render(request,'password-reset.html')
# def WelcomeView(request):
#     return render(request,'welcome.html')
def LogoutView(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
    return redirect("signup")

