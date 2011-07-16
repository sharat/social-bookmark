# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request) :
	template = get_template('main.html')
	variables = Context({
		'head_title': u'Django Bookmarks',
		'page_title': u'Welcome to Django Bookmarks',
		'page_body': u'Where you can store and share bookmarks!'
	})
	output = template.render(variables)
	return HttpResponse(output)
# Context is a object which can take Python Dictionary elements in the constructor)