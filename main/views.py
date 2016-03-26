from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.models import Cereal, Manufacturer
from django.views.decorators.csrf import csrf_exempt

from django.template import RequestContext

# Create your views here.


def cereal_list(request):
	context = {}
	cerealeverything = Cereal.objects.all()
	context['cerealeverything'] = cerealeverything
	return render(request, 'cereal_list.html', context)











@csrf_exempt
def get_search(request):

	get_var = request.GET.get('q', None)

	print dir(request)

	print request.GET
	print request.POST

	text_string = ''
	text_string += 'Search Term: %s <br>' % get_var
	text_string += """

	<form action="/get_search/" method="GET">
	Search Cereal:
	<input type='text' name='q'>
	<br>

	<input type='submit' value="Submit">
	
	</form>
	
	"""

	if get_var != None:
		cereal_list = Cereal.objects.filter(name__icontains=get_var)
		for cereal in cereal_list:
			text_string += '%s <br>' % cereal.name

	return HttpResponse(text_string)

@csrf_exempt	
def get_post(request):

	get_var = request.GET.get('q', None)
	post_var = request.POST.get('q', None)

	print request.GET
	print request.POST

	text_string = ''
	text_string += 'Get Var: %s <br>' % get_var
	text_string += 'Post Var: %s <br>' % post_var
	text_string += """

	<form action="/get_post/" method="POST">
	Enter Var:
	<input type='text' name='q'>
	<br>

	<input type='submit' value="Submit">
	
	</form>
	
	"""

	return HttpResponse(text_string)

def cereal_detail(request, name):

	manufacturername = Manufacturer.objects.get(name=name)

	cerealall = manufacturername.cereal_set.all()

	text_string = '<h4> %s <h4>'  % manufacturername.name

	for cereal in cerealall:
		try:
			text_string += '%s </br>' % cereal.name
		except Exception, e:
			print e

	return HttpResponse(text_string)

# def cereal_list(request):
# 	cerealeverything = Cereal.objects.all()
# 	cereal_list = []
# 	for cerealall in cerealeverything:
# 		cereal_list.append("<a href='/cereal_detail/%s'> %s </a></br>" % (cerealall.name, cerealall.name))
# 	return HttpResponse(cereal_list)	
