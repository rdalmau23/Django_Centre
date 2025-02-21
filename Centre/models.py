from django.db import models

class Module(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Alumne(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField()
    curs = models.CharField(max_length=50)
    moduls = models.ManyToManyField(Module, blank=True, related_name='alumnes')

    def __str__(self):
        return f"{self.nom} {self.cognom1}"

class Professor(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField()
    curs = models.CharField(max_length=50)
    tutor = models.BooleanField(default=False)
    moduls = models.ManyToManyField(Module, blank=True, related_name='professors')

    def __str__(self):
        return f"{self.nom} {self.cognom1}"
