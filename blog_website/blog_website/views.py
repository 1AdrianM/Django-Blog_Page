from django.shortcuts import render, redirect

def about(request):
    return render(request,'about.html')



def Home (request):
    return render(request,'home.html')