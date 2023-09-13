from django.contrib import admin
from home.models import Person, Crime
# Register your models here.


# @admin.register(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Crime)
class CrimeAdmin(admin.ModelAdmin):
    pass