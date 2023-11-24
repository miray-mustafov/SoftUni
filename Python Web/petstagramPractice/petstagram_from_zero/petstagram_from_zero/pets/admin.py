from django.contrib import admin
from petstagram_from_zero.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug']

