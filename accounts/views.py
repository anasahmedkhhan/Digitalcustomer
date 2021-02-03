from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from accounts.models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.


def homepage(request):
    return render(request,'Home\index.html')


def signUpRedirect(request):
    return render(request,'Home\SignUp.html')


def signInRedirect(request):
    return render(request,'Home\SignIn.html')


def registerUser(request):
    if request.method=='POST':
        fName = request.POST["first_name"]
        lName = request.POST["last_name"]
        email = request.POST["email"]
        cnic = request.POST["cnic"]
        password = request.POST["password"]
        phoneNo = request.POST["phoneNumber"]
        print(fName)
        print(lName)
        print(email)
        print(cnic)
        print(password)
        print(phoneNo)
        if checkEmail(email):
            return JsonResponse({"status": False, "msg": "An account with entered email already exists."})
        user = User.objects.create_user(username=email, password=password, email=email,first_name=fName, last_name=lName)
        UserDetails.objects.create(cnic=cnic,phoneNo=phoneNo,userId_id=user.id)

        return redirect("user/")


def login(request):
    print('In Login request recieved ')
    if request.method == "POST":
        #   Finding if doctor or patient wants to log in
        username_post = request.POST['email']
        password_post = request.POST['password']
        print("email :", username_post)
        print("Password  :", password_post)
        user = auth.authenticate(username=username_post, password=password_post)
        print(user.id)
        # Finding if it is teacher or student that logged in
        if user is not None:
            try:
                print("Redirecting to user login")
                User.objects.get(id=user.id)
                auth.login(request, user)
                request.session["LoginType"] = "User"
                request.session.set_expiry(7200)  # 2 hours session expiry
                return redirect("user/")
            except:
                pass
    # If request is not validated or user is not valid, it is redirected to homepage
    request.session["LoginMessage"] = "Try Again"
    return redirect("/#section-login")




def checkEmail(email):
    try:
        if User.objects.filter(email=email).exists():
            return True
        return False
    except Exception as e:
        print("Exception in check_duplicate_email(accounts:helpers):", str(e))
        return False


