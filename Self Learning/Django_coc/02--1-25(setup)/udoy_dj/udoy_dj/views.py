from django.http import HttpResponse

# from http you are taking http response
from django.shortcuts import render


def home(request):
    # return HttpResponse("hello world , you are at chai or Django homepage ")
    return render(request, "index.html")


def about(request):
    # return HttpResponse("hello world , you are at chai or Django About ")
    return render(request, "about.html")


def contact(request):
    # return HttpResponse("hello world , you are at chai or Django contact ")
    return render(request, "contact.html")
