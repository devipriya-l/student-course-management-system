from django.contrib import admin
from .models import Course, Instructor, Student, Enrollment

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Enrollment)
