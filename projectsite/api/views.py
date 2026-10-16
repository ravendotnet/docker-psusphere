from rest_framework import generics
from studentorg.models import College, Student, Program, Organization, OrgMember
from .serializers import CollegeSerializer, StudentSerializer, ProgramSerializer, OrganizationSerializer, OrgMemberSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# List all or create new colleges (protected)
class CollegeListCreateAPIView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]  # Require login or token

# Retrieve, update, or delete a single college (protected)
class CollegeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]  # Require login or token

# List all students or create one (protected)
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, update, delete a student (protected)
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

# List all programs or create one (protected)
class ProgramListCreateAPIView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]  # Require token/login

# Retrieve, update, delete a program (protected)
class ProgramRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class OrganizationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class OrgMemberListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrgMember.objects.all()
    serializer_class = OrgMemberSerializer
    permission_classes = [IsAuthenticated]

class OrgMemberRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrgMember.objects.all()
    serializer_class = OrgMemberSerializer
    permission_classes = [IsAuthenticated]