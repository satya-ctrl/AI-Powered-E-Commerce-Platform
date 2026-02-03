from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product
from .recommender import recommend_products
from django.http import JsonResponse

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    recommendations = recommend_products(id)
    return render(request, "product_detail.html", {
        "product": product,
        "recommendations": recommendations
    })

def add_to_cart(request, id):
    cart = request.session.get("cart", {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session["cart"] = cart
    return redirect("cart")

def cart(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, "cart.html", {"products": products, "cart": cart})

def checkout(request):
    request.session["cart"] = {}
    return render(request, "checkout.html")

def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        return redirect("login")
    return render(request, "register.html")

def chatbot(request):
    user_msg = request.GET.get("msg")
    reply = "I can help you with orders, products, and payments."
    return JsonResponse({"reply": reply})
