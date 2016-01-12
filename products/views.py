# Create your views here.

from django.http import HttpResponse


def product_index(request):
	return HttpResponse("This is a product index")
