from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    # Home / Dashboard
    path('', views.dashboard, name='dashboard'),

    # Login / Logout
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # List Views
    path('courses/', views.course_list, name='course-list'),
    path('students/', views.student_list, name='student-list'),
    path('instructors/', views.instructor_list, name='instructor-list'),
    path('enrollments/', views.enrollment_list, name='enrollment-list'),

    # Create / Update Views
    path('courses/add/', views.course_create, name='course-add'),
    path('courses/<int:pk>/edit/', views.course_update, name='course-edit'),

    path('students/add/', views.student_create, name='student-add'),
    path('students/<int:pk>/edit/', views.student_update, name='student-edit'),

    path('instructors/add/', views.instructor_create, name='instructor-add'),
    path('instructors/<int:pk>/edit/', views.instructor_update, name='instructor-edit'),

    path('enrollments/add/', views.enrollment_create, name='enrollment-add'),
    path('enrollments/<int:pk>/delete/', views.enrollment_delete, name='enrollment-delete'),

]
