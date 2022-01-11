from django.urls import path
from django.urls.conf import include
from . import views
from proj.views import specific_book
urlpatterns = [
    
    
    path('',views.books),
    path('<id>/update',views.update_book),
    path('<id>/delete',views.delete_book),
    path('<id>/',views.show_book)
]
