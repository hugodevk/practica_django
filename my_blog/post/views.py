from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse



def update(request):
    author = Author.objects.get(id=1)
    author.name = "juango"
    author.email = "juango@demo.com"
    author.save()
    return HttpResponse("Modificado")

def queries(request):
    # obtener todos los elementos
    authors = Author.objects.all()

    #OBTENER DATOS FILTRADOS
    # filtered = Author.objects.filter(email="brett03@example.net")

    #obtener un inico objeto (filtrado)
    author = Author.objects.get(id=1)

    #obtener los 10 primeros elementos (filtrado)
    limits = Author.objects.all()[:10]

    #obtener los 5 elemntos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    #obtener todos los elemntos ordenados
    orders = Author.objects.all().order_by('email')

    #obtener todos los elementos cuyo id sea imenor o igual a 15
    # filtered = Author.objects.filter(id__lte=15)

    # #obtener todos los autores que contiene en su nombre la palabra yes
    # filtered = Author.objects.filter(name__contains="yes")

    # # obtener todos los elementos
    # authors = Author.objects.all.order_by('email')

    # # Obtener todos los elementos cuyo sea menor o iguala 15
    # filtered = Author.objects.filter(id__lte=15)
    
    # obtener todos los autores que contienen en su nombre  las palabras  yes
    filtered = Author.objects.filter(name__contains="yes")

    return render(request, "post/queries.html", {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, })



