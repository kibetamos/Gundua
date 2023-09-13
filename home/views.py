# from django.shortcuts import render
from .models import Crime  # Import your Crime model
# from .forms import CrimeForm  # Import a form for creating crimes if you have one
# Create your views here.
# from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from .forms import CrimeForm
from .models import Crime

def create_crime(request):
    if request.method == 'POST':
        form = CrimeForm(request.POST, request.FILES)
        if form.is_valid():
            new_crime = form.save()
            return render('crime', crime_id=new_crime.id)
    else:
        form = CrimeForm()

    return render(request, 'create_crime.html', {'form': form})



def crime(request, crime_id):
    crime = get_object_or_404(Crime, id=crime_id) 

    data = {
        "crime": crime,
            }
    
    return render(request, "crime.html", data)

def crimes(request):
    data = {
        'crimes':Crime.objects.all().order_by('date'),#1
        }
    return render(request, "crimes.html", data)