
from .models import Student,Teacher
from .serializer import StudentSerializer, TeacherSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView

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


# @api_view(["GET","POST"])
# def teachers(request):
#    if(request.method == "GET"):
#       teachers_queryset=Teacher.objects.all()
#       teachers = TeacherSerializer(teachers_queryset,many=True)
      
#       return Response(teachers.data)
#    elif (request.method == "POST"):
#       added_teacher=TeacherSerializer(data=request.data)
#       if added_teacher.is_valid():
#          added_teacher.save()
#          return Response(added_teacher.data,status=status.HTTP_201_CREATED)
#       return Response({"message":"Bad Request","error":added_teacher.error_messages},status=status.HTTP_400_BAD_REQUEST)



# @api_view(["PUT","DELETE","GET"])
# def teachers_details(request,teacher_id):
#    try:
#       query_set = Teacher.objects.get(pk=teacher_id)
#    except Teacher.DoesNotExist:
#       return Response({"message":"Teacher Does not exist"},status=status.HTTP_400_BAD_REQUEST)
#    if request.method == "GET":
#       teacher = TeacherSerializer(query_set)
#       return Response(teacher.data)
#    elif request.method == "PUT":
#       teacher = TeacherSerializer(query_set,data=request.data)
#       if teacher.is_valid():
#          teacher.save()
#          return Response(teacher.data,status=status.HTTP_200_OK)
#       return Response({"message":"Bad Request","errors":teacher.errors},status=status.HTTP_400_BAD_REQUEST)
#    elif request.method == "DELETE":
#       teacher = query_set.delete()
#       return Response({},status=status.HTTP_204_NO_CONTENT)


class Teachers(APIView):
   def get(self,request):
      teachers = Teacher.objects.all()
      serailizer=TeacherSerializer(teachers,many=True)
      return Response(serailizer.data,status=status.HTTP_200_OK)
   
   def post(self,request):
      serailizer=TeacherSerializer(data=request.data)
      print("serailizer",serailizer)
      if serailizer.is_valid():
         serailizer.save()
         return Response(serailizer.data,status=status.HTTP_201_CREATED)
      return Response({"message":"Bad Request","errors":serailizer.errors})

      

class Teachers_details(APIView):
   pass