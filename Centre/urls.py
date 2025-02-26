from django.urls import path
from . import views

urlpatterns = [
    # pàgina principal de Centre
    path('', views.centre_home, name='centre-home'),

    # Per a alumnes
    path('alumnes/', views.AlumneListView.as_view(), name='alumne-list'),
    path('alumnes/<int:pk>/', views.AlumneDetailView.as_view(), name='alumne-detail'),

    # Per a professors
    path('professors/', views.ProfessorListView.as_view(), name='professor-list'),
    path('professors/<int:pk>/', views.ProfessorDetailView.as_view(), name='professor-detail'),
]
