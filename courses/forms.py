from django import forms
from .models import Course, Instructor, Student, Enrollment

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'email', 'bio']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
