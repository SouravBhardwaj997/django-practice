from django.urls import path
from . import views
urlpatterns = [
    path("",views.teachers_home),
    path("about/",views.teachers_about),
    path("contact/",views.teachers_contact)
]