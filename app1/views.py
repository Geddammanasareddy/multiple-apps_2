from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("THE FIRST VIEW IN APP 1")
def second(request):
    return HttpResponse("<h1>THE SECOND VIEW IN APP 2</h1>")