from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "todos/home.html")
    # return HttpResponse("<h1>Hello, Django!</h1>")