from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def user_register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username} ! You are register")
        return redirect("food:index")

    return render(request, "register/regi.html", {"form": form})
