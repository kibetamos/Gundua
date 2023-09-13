from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 


def crimes(request): 
    content = "Nicky\nYour Name" 
        
    return HttpResponse(content, content_type="text/plain")