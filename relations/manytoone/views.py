from django.shortcuts import render, HttpResponse
from .models import Reporter, Article 
from datetime import date

# Create your views here.

def create(request):
	rep = Reporter(first_name = 'Juanjo', last_name = 'Ruiz', email = 'juanjo@demo.com')
	rep.save()

	art1 = Article(headline='Lorem ipsum dolot', pub_date=date(2022,5,5), reporter = rep)
	art1.save()

	art2 = Article(headline='Lorem set aimet', pub_date=date(2022,3,7), reporter = rep)
	art2.save()

	art3 = Article(headline='dolot aimet lorent', pub_date=date(2022,4,9), reporter = rep)
	art3.save()


	result = rep.article_set.count()
	# result = art1.reporter.first_name

	# article_set el set te permite traer todos los registros many to one

	#	result = rep.article_set.all().filter(headline='Lorem ipsum dolot')
	#	result = rep.article_set.all()
	
	return  HttpResponse(result)


