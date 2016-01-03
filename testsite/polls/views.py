from django.http import HttpResponse

def index(response):
	return HttpResponse("Hello world!  Oh my!  Whoa!")