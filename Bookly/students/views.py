from django.shortcuts import render, redirect, reverse, get_object_or_404
from students.models import Student
from students.forms import StudentForm
from django.views.generic import DetailView, CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from students.forms import RegistrationForm

@login_required()
def index(request):
    students = Student.objects.all()
    return render(request, 'students/students_index.html',{'students': students})

def show(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/students_show.html', {'student': student})

@login_required()
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect(reverse('students.index'))

@login_required()
def edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('students.index'))
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

@login_required()
def profile(request):
    url = reverse("students.profile", args=[request.user.id])
    return redirect(url)


class AccountsDetailView(DetailView):
    model = Student
    template_name = 'students/profile.html'
    
class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/signup.html'
    form_class = RegistrationForm
    success_url = "/accounts/login"
