from django.urls import path
from . import views

urlpatterns = [
    # Para alumnes
    path('students/', views.AlumneListView.as_view(), name='alumne-list'),
    path('students/<int:pk>/', views.AlumneDetailView.as_view(), name='alumne-detail'),

    # Para professors
    path('teachers/', views.ProfessorListView.as_view(), name='professor-list'),
    path('teachers/<int:pk>/', views.ProfessorDetailView.as_view(), name='professor-detail'),
]
