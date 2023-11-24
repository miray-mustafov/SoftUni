from django.urls import path, include
from mymusicapp.web import views

urlpatterns = [  # WEB URLS
    path('', views.home_page_view, name='home-page'),
    path('profile/details/', views.profile_details_view, name='details-profile'),
    path('profile/delete/', views.profile_delete_view, name='delete-profile'),

    path('album/', include([
        path('add/', views.album_add_view, name='add-album'),
        path('details/<int:pk>/', views.album_details_view, name='details-album'),
        path('edit/<int:pk>/', views.album_edit_view, name='edit-album'),
        path('delete/<int:pk>/', views.album_delete_view, name='delete-album'),
    ])),
]
