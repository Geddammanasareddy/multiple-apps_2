from django.shortcuts import render

# Create your views here.
def three(request):
    return render(request,'h3.html')
def four(request):
    return render(request,'h4.html')
