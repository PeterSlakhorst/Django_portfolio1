from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello Phase1!!!!")

def peter(request):
    return HttpResponse("Hello Peter!!!!")