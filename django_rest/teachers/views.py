from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def teachers_home(request):
    return HttpResponse("<h1>Teachers Home Page</h1>")


def teachers_about(request):
    return HttpResponse("<h1>Teachers About</h1>")

def teachers_contact(request):
    return HttpResponse("<h1>Teachers Contact</h1>")