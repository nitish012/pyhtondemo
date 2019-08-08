from rest_framework import viewsets,generics
from quickstart.models import Student
from django.shortcuts import get_object_or_404
from quickstart.serializers import StudentSerializer
from rest_framework.response import Response

#Create your views here.

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentviewSet(viewsets.ViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

    # def create(self,request):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        if request.data.get('id'):
            return super(StudentViewSet, self).update(request, *args, **kwargs)
        else:
            return super(StudentViewSet, self).create(request, *args, **kwargs)

class StudentInsert(generics.CreateAPIView):
    ''' Inserting a records of students'''
    queryset = Student.objects.all()
    serializer_class=StudentSerializer


class StudentList(generics.RetrieveUpdateDestroyAPIView):
    ''' fetching list of students'''
    queryset = Student.objects.get_queryset()
    serializer_class=StudentSerializer    