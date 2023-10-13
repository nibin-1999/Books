from django.urls import path
from api.v1.books import views

urlpatterns = [
    path("",views.books ),
    path('<int:pk>/',views.bookssingle),
    path('create/',views.create),
    path('<int:pk>/update/',views.update ),
    path('<int:pk>/delete/',views.delete ),
    path('<int:pk>/add-to-favorites/',views.add_to_favorites),
    path('view-favorites/',views.view_favorites),
    path("comments/create/<int:pk>",views.create_comment),
    path("comments/list/<int:pk>",views.comments)
    
]
