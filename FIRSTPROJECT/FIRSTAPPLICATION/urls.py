from . import views
from django.urls import path

urlpatterns = [
    path('HomePage/',views.HomePage),
]