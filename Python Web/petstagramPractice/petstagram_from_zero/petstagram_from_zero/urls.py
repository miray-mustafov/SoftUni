from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_from_zero.common.urls')),
    path('accounts/', include('petstagram_from_zero.accounts.urls')),
    path('pets/', include('petstagram_from_zero.pets.urls')),
    path('photos/', include('petstagram_from_zero.photos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
