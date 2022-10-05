from django.urls import path
from archive import views

urlpatterns = [
    path('archive/', views.FileView.as_view()),
]