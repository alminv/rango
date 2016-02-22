from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<a href = '/rango/about'>About</a> <br/> Rango says hello world")

def about(request):
	return HttpResponse("<a href = '/rango/'>Home</a><br/> This is about page")

# Create your views here.
