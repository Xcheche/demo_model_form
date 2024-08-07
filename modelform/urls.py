from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listprojects/", views.listprojects, name="listprojects"),
    path("addproject/", views.addproject, name="addproject"),
]
