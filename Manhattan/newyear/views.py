from django.shortcuts import render
from datetime import date

# Create your views here.

def index(request):
#    return HttpResponse("Hello Phase1 from index!!!!")
    vandaag = date.today()
    return render(request, "newyear/index.html", {   #remember this is a dictionary
        'newyear': vandaag.month == 1 and vandaag.day == 1

    })
    
