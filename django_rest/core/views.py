
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(["GET","POST"])
def students(request):
    print("request",request.data)
    if request.method == "GET":
       students = Student.objects.all()
       serializer = StudentSerializer(students,many=True)
       return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
      students = Student.objects.all()
      StudentSerializer.create(data= request.data)