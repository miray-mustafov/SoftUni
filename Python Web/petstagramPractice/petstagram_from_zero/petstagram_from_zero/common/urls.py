from django.contrib.auth.decorators import login_required
from django.urls import path, include
from petstagram_from_zero.common import views

# COMMON/URLS
urlpatterns = (
    path('', views.home_page, name='home page'),
    path('like/<int:photo_pk>/', views.like_functionality, name='photo like'),
    path('share/<int:photo_pk>/', views.share_functionality, name='photo share'),
    path('comment/<int:photo_pk>/', views.comment_functionality, name='photo comment'),
)