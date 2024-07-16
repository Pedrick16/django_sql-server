from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, "playground/index.html")


def submitTest(request):
    if request.method == "POST":
        calendar = CalendarEvents()
        calendar.title = request.POST.get('title')
        calendar.save()
        return redirect('playground:home_landing')


