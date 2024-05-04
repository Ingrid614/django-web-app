from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django !</h1>');

def about(request):
    return HttpResponse('<h1> A propos </h1> <p> Nous adorons Merch !</p>');

def listings(request):
    return HttpResponse('<h1> Tous les articles </h1> <p>Listings</p>');

def contact(request):
    return HttpResponse('<h1> Contactez-nous </h1><p> Contacts</p>');