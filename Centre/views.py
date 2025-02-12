from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    professor = {"name": "Roger", "surname": "Sobrino", "age": "17"}

    template = loader.get_template('index.html')

    dades = template.render({'nombre': professor["name"],
                             'surname': professor["surname"],
                             'age': professor["age"]})

    return HttpResponse(dades)
