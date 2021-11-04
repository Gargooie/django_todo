from django.shortcuts import render
from django.http import HttpResponse


def myViews(request):
    return HttpResponse("Hello,world")
