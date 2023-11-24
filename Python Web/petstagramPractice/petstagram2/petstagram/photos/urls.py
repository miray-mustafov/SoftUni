from django.urls import path

from petstagram.photos.views import add_photo, details_photo, edit_photo, delete_photo

# PHOTOS
urlpatterns = (
    path('<int:pk>/', details_photo, name='details-photo'),
    path('add/', add_photo, name='add-photo'),
    path('edit/<int:pk>/', edit_photo, name='edit-photo'),
    path('delete/<int:pk>/', delete_photo, name='delete-photo'),
)