from django.urls import path

from . import views

urlpatterns = [
    path("", views.Login, name="Login"),
    path("home", views.index, name="index"),
    path("logout",views.Logout,name="Logout"),
    path("generate/", views.generate, name="generate"),
    path("create/", views.create, name="create"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("show_passwords/", views.show_passwords, name="show_passwords"),
    path("export_password", views.export_password, name="export_password"),
    path('register',views.AccountRegistration.as_view(), name='register'),
]