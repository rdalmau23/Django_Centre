from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Alumne, Professor

# Vista per a la pàgina principal
def centre_home(request):
    return render(request, 'index.html')

# Vistes per a alumnes
class AlumneListView(ListView):
    model = Alumne
    template_name = 'student_list.html'
    context_object_name = 'alumnes'

class AlumneDetailView(DetailView):
    model = Alumne
    template_name = 'student_detail.html'
    context_object_name = 'alumne'

# Vistes per a professors
class ProfessorListView(ListView):
    model = Professor
    template_name = 'teacher_list.html'
    context_object_name = 'professors'

class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'teacher_detail.html'
    context_object_name = 'professor'
