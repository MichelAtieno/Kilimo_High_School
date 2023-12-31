from django.shortcuts import render, redirect
from .models import Stream, Student
from .forms import StudentForm
# Create your views here.


# Create your views here.
def home(request):
    return render(request, 'home.html')

def all_streams(request):
    streams = Stream.objects.all()
    context = {
        'streams' : streams
    }

    return render(request, 'all_streams.html', context)

def one_stream(request, id):
    one_stream = Stream.objects.get(id=id)
    students = Student.objects.all()

    context = {
        "one_stream" : one_stream,
        "students" : students
    }

    return render(request, "one_stream.html", context)

def all_students(request):
    students = Student.objects.all()
    
    context = {
        'students' : students
    }

    return render(request, "all_students.html", context)

def one_student(request, id):
    one_student = Student.objects.get(id=id)

    context = {
        'one_student': one_student
    }

    return render(request, "one_student.html", context)

def edit_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('high_school_app:student', id=student.id)

    context = {
        "form" : form,
        "student": student
    }

    return render(request, 'edit_student.html', context)

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    
    return redirect('high_school_app:all_students')

