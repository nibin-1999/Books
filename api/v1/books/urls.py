from django.urls import path

from api.v1.books import views

urlpatterns = [
    path('', views.books),
    path('view/<int:pk>', views.book),
]
