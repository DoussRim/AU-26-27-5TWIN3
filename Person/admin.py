from django.contrib import admin
from Person.models import Person
class PersonAdmin(admin.ModelAdmin):
    search_fields=['username']
# Register your models here.
admin.site.register(Person,PersonAdmin)