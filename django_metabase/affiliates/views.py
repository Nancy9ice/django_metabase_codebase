from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to affiliate_dashboard with username as affiliate_name
            affiliate_name = user.username.replace('_', ' ').title()
            return redirect('affiliate_dashboard', affiliate_name=affiliate_name)
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")
