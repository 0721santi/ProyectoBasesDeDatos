from django.http import HttpResponse
from django.shortcuts import render, redirect
# import requests
import json

# Create your views here.
def init(request):
    return render(request, 'index.html')
def create(request):
    return render(request, './db/create.html')
def delete(request):
    return render(request, './db/delete.html')
def retrieve(request):
    return render(request, './db/retrieve.html')
def update(request):
    return render(request, './db/update.html')