# from django.shortcuts import render
from django.db.models import Count
from .models import Crime  # Import your Crime model
# from .forms import CrimeForm  # Import a form for creating crimes if you have one
# Create your views here.
# from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from .forms import CrimeForm
from .models import Crime

def create_crime(request):
    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            new_crime = form.save()
            return render(request,'crime_detail', crime_id=new_crime.id)  # Redirect to the crime detail page
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
    # Aggregate the count of crimes for each unique location
    crime_counts = Crime.objects.values('location').annotate(total_crimes=Count('location'))

    # data = {
    #     'crimes':Crime.objects.all().order_by('date'),#1
        
    #     }
    crimes = Crime.objects.all()
    total_crimes = crimes.count()
    return render(request, 'crimes.html', {'crimes': crimes, 'total_crimes': total_crimes, 'crime_counts': crime_counts})
    # return render(request, "crimes.html",  data,{'total_crimes': total_crimes})