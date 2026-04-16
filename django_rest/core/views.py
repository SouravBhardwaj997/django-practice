from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def students(request):
    return JsonResponse({"id":1,"name":"Soruav","age":2})