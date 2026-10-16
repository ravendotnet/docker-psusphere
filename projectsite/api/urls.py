from django.urls import path
from . import views

urlpatterns = [
    # College endpoints
    path('colleges/', views.CollegeListCreateAPIView.as_view(), name='college-list-create'),
    path('colleges/<int:pk>/', views.CollegeRetrieveUpdateDestroyAPIView.as_view(), name='college-detail'),
    # Student endpoints
    path('students/', views.StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
    # Program endpoints
    path('programs/', views.ProgramListCreateAPIView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', views.ProgramRetrieveUpdateDestroyAPIView.as_view(), name='program-detail'),
    # Organization endpoints
    path('organizations/', views.OrganizationListCreateAPIView.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', views.OrganizationRetrieveUpdateDestroyAPIView.as_view(), name='organization-detail'),
    # OrgMember endpoints
    path('orgmembers/', views.OrgMemberListCreateAPIView.as_view(), name='orgmember-list-create'),
    path('orgmembers/<int:pk>/', views.OrgMemberRetrieveUpdateDestroyAPIView.as_view(), name='orgmember-detail'),
]