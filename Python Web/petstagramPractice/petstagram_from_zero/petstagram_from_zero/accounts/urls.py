from django.contrib.auth.decorators import login_required
from django.urls import path, include
from petstagram_from_zero.accounts import views

# ACCOUNTS/URLS
urlpatterns = (
    path('register/', views.UserSignUp.as_view(), name='register'),
    path('login/', views.UserSignIn.as_view(), name='login'),
    path('logout/', views.UserSignOut.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', login_required(views.UserDetails.as_view()), name='profile details'),
        path('edit/', views.UserEdit.as_view(), name='profile edit'),
        path('delete/', views.UserDelete.as_view(), name='profile delete'),
    ])),
)
