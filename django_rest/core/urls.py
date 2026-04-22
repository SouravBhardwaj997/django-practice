from django.urls import path
from . import views
urlpatterns=[
    path('students',views.students),
    path('students/<int:student_id>',views.studentDetail),
    path('teachers',views.Teachers.as_view()    ),
    path('teachers/<int:pk>',views.TeacherDetail.as_view())
]