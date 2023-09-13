# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404

from .models import Crime

# def crime(request, crime_id): 
#     crime = get_object_or_404(Crime, id=crime_id) 
#     data = {
#         "crime": crime, 
#         }
#     return render(request, "crime.html", data)

def crime(request, crime_id):
    crime = get_object_or_404(Crime, id=crime_id) 

    data = {
        "crime": crime,
            }
    
    return render(request, "crime.html", data)
