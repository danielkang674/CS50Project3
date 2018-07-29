from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Pizza, Size, PizzaTopping, PizzaStyle, PizzaType

# Create your views here.
def index(request):
  if not request.user.is_authenticated:
    return render(request, "users/login.html", {"message": None})
  return render(request, "orders/menu.html", {"user": request.user})

def login_view(request):
  username = request.POST["username"]
  password = request.POST["password"]
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse("index"))
  else:
    return render(request, "users/login.html", {"message": "Login failed"})

def signup_view(request):
  if request.method == "GET":
    return render(request, "users/signup.html")
  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    verifypass = request.POST["verifypass"]
    if len(username) <= 0 or len(password) <= 0 or len(first_name) <=0 or len(last_name) <= 0 or len(email) <= 0:
      return render(request, "users/signup.html", {"message": "Fields can't be blank"})
    if password != verifypass:
      return render(request, "users/signup.html", {"message": "Passwords do not match"})
    try:
      user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    except:
      return render(request, "errors/error.html", {"header": "Registration Error","error": "Username already taken"})
    user.save()
    return HttpResponseRedirect(reverse("index"))

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse("index"))

def pizza_view(request):
  if request.method == "GET":
    context = {
      "sizes": Size.objects.all(),
      "styles": PizzaStyle.objects.all(),
      "types": PizzaType.objects.all(),
      "toppings": PizzaTopping.objects.all()
    }
    return render(request, "orders/pizza.html", context=context)