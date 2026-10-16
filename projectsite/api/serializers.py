from rest_framework import serializers
from studentorg.models import College, Student, Program, Organization, OrgMember

class CollegeSerializer(serializers.ModelSerializer):
  class Meta:
      model = College
      fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.prog_name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'last_name', 'first_name', 'middle_name', 'program', 'program_name']
        read_only_fields = ['program_name']

class ProgramSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True, source='student_set')

    class Meta:
        model = Program
        fields = ['id', 'prog_name', 'college', 'students']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class OrgMemberSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.__str__', read_only=True)
    organization_name = serializers.CharField(source='organizations.name', read_only=True)

    class Meta:
        model = OrgMember
        fields = ['id', 'student', 'student_name', 'organizations', 'organization_name', 'date_joined']
        read_only_fields = ['student_name', 'organization_name']
        