from django.shortcuts import render
from django.template import Context
from .process_code import import_data


def index_render(request):

	return render(request, "index.html",{"field_names": import_data.getFieldNames()} )

