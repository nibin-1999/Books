from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/v1/books/',include("api.v1.books.urls")),
    path('api/v1/auth/',include("api.v1.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
