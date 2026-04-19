
from .models import Student,Teacher
from .serializer import StudentSerializer, TeacherSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET","POST"])
def students(request):
    if request.method == "GET":
       students = Student.objects.all()
       serializer = StudentSerializer(students,many=True)
       return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
      serializer = StudentSerializer(data=request.data) 
      if serializer.is_valid():
         serializer.save()    
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors)
      

@api_view(["GET","PUT","DELETE"])
def studentDetail(request,student_id):
   print("student_id",student_id)
   print("request",request.data)
   try:
      stu_queryset=Student.objects.get(pk=student_id)
   except Student.DoesNotExist:
      return Response({
         "message":"Not Found"
      },status=status.HTTP_400_BAD_REQUEST)
   if request.method == "GET":
      student=StudentSerializer(stu_queryset)
      return Response(student.data,status=status.HTTP_200_OK)
   elif request.method == "PUT":
      print("request",request.data)
      student=StudentSerializer(stu_queryset,data=request.data)
      if student.is_valid():
         student.save()
         return Response(student.data,status=status.HTTP_200_OK)
      else:
         return Response({"message":"Not Found"},status=status.HTTP_400_BAD_REQUEST)
   elif request.method == "DELETE":
      student = stu_queryset.delete()
      return Response({"message":"Deleted"},status=status.HTTP_200_OK)


@api_view(["GET","POST"])
def teachers(request):
   if(request.method == "GET"):
      teachers_queryset=Teacher.objects.all()
      teachers = TeacherSerializer(teachers_queryset,many=True)
      
      return Response(teachers.data)
   elif (request.method == "POST"):
      added_teacher=TeacherSerializer(data=request.data)
      if added_teacher.is_valid():
         added_teacher.save()
         return Response(added_teacher.data,status=status.HTTP_201_CREATED)
      return Response({"message":"Bad Request","error":added_teacher.error_messages},status=status.HTTP_400_BAD_REQUEST)


