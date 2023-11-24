from django.contrib import admin
from django.urls import path, include

urlpatterns = [     # DONT FORGET THE COMMA ,  , , , ,
    path('admin/', admin.site.urls),
    path('', include('mid_exam.web.urls')),
]