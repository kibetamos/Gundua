from django.urls import path
from home import views


urlpatterns = [

    path('crime/<int:crime_id>/', views.crime, name="crime"),
    
    ]