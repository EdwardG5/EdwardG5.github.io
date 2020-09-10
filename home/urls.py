from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deep", views.deep, name="Deep"),
    path("fun", views.fun, name="Fun"),
]