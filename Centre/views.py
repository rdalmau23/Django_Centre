from django.views.generic import ListView, DetailView
from .models import Alumne, Professor

# Vistas para alumnes
class AlumneListView(ListView):
    model = Alumne
    template_name = 'student_list.html'
    context_object_name = 'alumnes'

class AlumneDetailView(DetailView):
    model = Alumne
    template_name = 'student_detail.html'
    context_object_name = 'alumne'

# Vistas para professors
class ProfessorListView(ListView):
    model = Professor
    template_name = 'teacher_list.html'
    context_object_name = 'professors'

class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'teacher_detail.html'
    context_object_name = 'professor'
