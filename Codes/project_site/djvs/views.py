from django.shortcuts import render
from django.template import Context
from .process_code import import_data


def index_render(request):
	fields_to_read = []

	if "op" in request.POST:
		# DEBUG
		#print("DEBUG >> " + " ".join( request.POST.getlist("op") ) )
		fields_to_read = request.POST.getlist("op")

	return render(request, "index.html",{"field_names": import_data.getFieldNames()} )

