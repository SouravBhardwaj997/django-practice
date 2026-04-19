from django.urls import path
from . import views
urlpatterns=[
    path('students',views.students),
    path('students/<int:student_id>',views.studentDetail),
    path('teachers',views.teachers)
]