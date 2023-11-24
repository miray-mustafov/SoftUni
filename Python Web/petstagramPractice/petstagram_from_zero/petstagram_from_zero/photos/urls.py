from django.urls import path, include

from petstagram_from_zero.photos import views

# PHOTOS / URLS

urlpatterns = (
    path('add/', views.photo_add, name='photo add'),
    path('<int:pk>/', views.photo_details, name='photo details'),
    path('<int:pk>/edit/', views.photo_edit, name='photo edit'),
    path('<int:pk>/delete/', views.photo_delete, name='photo delete'),
)