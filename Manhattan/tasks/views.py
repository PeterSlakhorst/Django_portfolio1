from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# mock data only needed is there are no sessions used
#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value = 1, max_value =10)   # we add extra fields  

# Create your views here.
def index(request):  
    if "tasks" not in request.session:
        request.session['tasks'] = []     # set the session tasks to empty list

    return render(request, "tasks/index.html", {   #remember this is a dictionary
        'tasks': request.session['tasks'],
        
          })

def add(request):
    if request.method == 'POST':   # we need to add the entered data to the tasks list
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:  # not valid
            return render(request, "tasks/add.html", { "form": form})
        
    else:
        return render(request, "tasks/add.html", {
            'form': NewTaskForm()
        
            })