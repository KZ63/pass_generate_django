from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generate/", views.generate, name="generate"),
    path("create/", views.create, name="create"),
    path("show_passwords/", views.show_passwords, name="show_passwords"),
    path("export_password", views.export_password, name="export_password"),
]