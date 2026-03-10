from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Course, Student, Instructor, Enrollment
from .forms import InstructorForm, StudentForm, CourseForm, EnrollmentForm


# ------------------- HOME (redirect to dashboard) -------------------
def home(request):
    return redirect('dashboard')


# ------------------- DASHBOARD (open to all) -------------------
def dashboard(request):
    stats = {
        "course_count": Course.objects.count(),
        "student_count": Student.objects.count(),
        "instructor_count": Instructor.objects.count(),
        "enrollment_count": Enrollment.objects.count(),
    }
    return render(request, "courses/dashboard.html", {"stats": stats})


# ------------------- LIST VIEWS (open to all) -------------------
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'courses/student_list.html', {'students': students})

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'courses/instructor_list.html', {'instructors': instructors})

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'courses/enrollment_list.html', {'enrollments': enrollments})


# ------------------- CREATE / UPDATE VIEWS (login required) -------------------

# Instructors
@login_required(login_url='/login/')
def instructor_create(request):
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('instructor-list')
    return render(request, 'courses/instructor_form.html', {'form': form})

@login_required(login_url='/login/')
def instructor_update(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    form = InstructorForm(request.POST or None, instance=instructor)
    if form.is_valid():
        form.save()
        return redirect('instructor-list')
    return render(request, 'courses/instructor_form.html', {'form': form})


# Students
@login_required(login_url='/login/')
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student-list')
    return render(request, 'courses/student_form.html', {'form': form})

@login_required(login_url='/login/')
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student-list')
    return render(request, 'courses/student_form.html', {'form': form})


# Courses
@login_required(login_url='/login/')
def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course-list')
    return render(request, 'courses/course_form.html', {'form': form})

@login_required(login_url='/login/')
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course-list')
    return render(request, 'courses/course_form.html', {'form': form})


# Enrollments
@login_required(login_url='/login/')
def enrollment_create(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('enrollment-list')
    return render(request, 'courses/enrollment_form.html', {'form': form})

@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment-list')
    return redirect('enrollment-list')


# ------------------- LOGIN VIEW -------------------
class CustomLoginView(LoginView):
    template_name = "courses/login.html"
