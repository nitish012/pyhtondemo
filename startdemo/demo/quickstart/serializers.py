from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields =  ('first_name','last_name','age','roll_no','teacher')
        #exclude = ['teacher']
        depth = 1

class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    class Meta:
        model = Teacher
        fields = ('first_name','last_name','subject','role', 'students')
        depth = 1

    def create(self, validated_data):
        students_data = (validated_data.pop('students'))[0]
        print(students_data.get('last_name', None))
        # already created by create() teacher=Teacher.objects.create(**validated_data)
        student_qs = Student.objects.filter(
            last_name = students_data.get('last_name', None),
            first_name = students_data.get('first_name', None),
            age = students_data.get('age',None),
            roll_no = students_data.get('roll_no',None)
            )
  
        if not student_qs:
            student = Student.objects.create(last_name = students_data.get('last_name', None),
                                                first_name = students_data.get('first_name', None),
                                                age = students_data.get('age',None),
                                                roll_no = students_data.get('roll_no',None)
                                                )
        else:
            student = student_qs.first()
        
        validated_data["student"] = student

        return super(TeacherSerializer,self).create(validated_data)    
        
    def update(self, instance, validated_data):
        students_data = (validated_data.pop('students'))[0]
        student_qs = Student.objects.filter(
            last_name = students_data.get('last_name', None),
            first_name = students_data.get('first_name', None),
            age = students_data.get('age',None),
            roll_no = students_data.get('roll_no',None))
        if not student_qs:
            student = Student.objects.create(last_name = students_data.get('last_name', None),
                                                first_name = students_data.get('first_name', None),
                                                age = students_data.get('age',None),
                                                roll_no = students_data.get('roll_no',None))
        else:
            student = student_qs.first()

        instance.student = student
        instance.save() 
        return instance