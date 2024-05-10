from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def registerView(request):
    if request.method == "POST":
         form = UserCreationForm(request.POST)
         if form.is_valid():
              login(request,form.save())
              return redirect("/home")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })

def LoginView(request):
    if request.method == "POST":
         form = AuthenticationForm(data=request.POST)
         if form.is_valid():
              login(request, form.get_user())
              return redirect("/home")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

def Logout(request):
    if request.method == 'POST':
     logout(request)
     return redirect("/home")