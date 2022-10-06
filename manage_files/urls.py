from django.urls import path
from manage_files import views

urlpatterns = [
    path('data/', views.ViewContentFile.as_view()),
]