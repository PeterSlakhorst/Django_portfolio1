from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
#    return HttpResponse("Hello Phase1 from index!!!!")
    return render(request, "Phase1/hello.html")


def greet(request, name):
    return render(request, "Phase1/greet.html", {"name": name.capitalize()})