from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return HttpResponse('bhavanireddy')

def third(request):
    return HttpResponse('JEJETI BHAVANI REDDY')
def fourth(request):
    return render(request,'bhavani.html')
def fifth(request):
    return render(request,'boni.html')