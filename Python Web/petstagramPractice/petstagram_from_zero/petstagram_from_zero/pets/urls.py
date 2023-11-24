from django.contrib.auth.decorators import login_required
from django.urls import path, include

from petstagram_from_zero.pets import views

# PETS / URLS
urlpatterns = (
    path('add/', views.pet_add, name='pet add'),
    path('<str:username>/pet/<slug:pet_slug>/', login_required(views.pet_details), name='pet details'),
    path('<str:username>/pet/<slug:pet_slug>/edit', views.pet_edit, name='pet edit'),
    path('<str:username>/pet/<slug:pet_slug>/delete', views.pet_delete, name='pet delete'),
)
