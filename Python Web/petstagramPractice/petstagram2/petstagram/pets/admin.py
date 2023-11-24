from django.contrib import admin
from petstagram.pets.models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('id',"name", "slug")


admin.site.register(Pet, PetAdmin)