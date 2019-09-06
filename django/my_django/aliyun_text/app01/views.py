from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("django1-----hello，夏雨豪!")
