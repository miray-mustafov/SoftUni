from django.urls import path, include

from petstagram.pets.views import add_pet, details_pet, edit_pet, delete_pet

# PETS
urlpatterns = (
    path('add/', add_pet, name='add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', details_pet, name='details-pet'),
        path('edit/', edit_pet, name='edit-pet'),
        path('delete/', delete_pet, name='delete-pet'),
    ])),
)
