
from .models import Student
from rest_framework.response import Response
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(["GET"])
def students(request):
    if request.method == "GET":
       students = Student.objects.all()
       serializer =StudentSerializer(students,many=True)
       return Response(serializer.data,status=status.HTTP_200_OK)