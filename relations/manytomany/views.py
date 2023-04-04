from django.shortcuts import render, HttpResponse
from .models import Article, Publication

# Create your views here.



def create(request):
    art1 = Article(headline = "Articulo Primero")
    art1.save()
    art2 = Article(headline = "Articulo Segundo")
    art2.save()
    art3 = Article(headline = "Articulo Tercero")
    art3.save()
    
    pub1 = Publication(title="Publication Primera")
    pub1.save()
    pub2 = Publication(title="Publication Segunda")
    pub2.save()
    pub3 = Publication(title="Publication Tercera")
    pub3.save()
    pub4 = Publication(title="Publication Cuarta")
    pub4.save()
    pub5 = Publication(title="Publication Quinta")
    pub5.save()
    pub6 = Publication(title="Publication Sexta")
    pub6.save()
    pub7 = Publication(title="Publication Septima")
    pub7.save()
    
    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)
	
    art1.publications.remove(pub1)
    pub1 = Publication.objects.get(id=1)
    
    result = art1.publications.all()
    result = pub1.article_set.all()
    
    return HttpResponse(result)
