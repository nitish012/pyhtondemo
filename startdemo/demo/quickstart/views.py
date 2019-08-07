from rest_framework import generics,viewsets
from quickstart.serializers import StudentSerializer
from quickstart.models import Student, Teacher
from rest_framework import mixins


# Create your views here.

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


class StudentviewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def list(self, request):
    #     queryset = Student.objects.all()
    #     serializer = StudentSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     queryset = Student.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentSerializer(user)
    #     return Response(serializer.data)
