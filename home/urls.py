from django.urls import path
from home import views


urlpatterns = [

    path('crime/<int:crime_id>/', views.crime, name="crime"),
    path('crimes/', views.crimes, name="crimes"),
    path('create_crime/', views.create_crime, name='create_crime')

    ]