from django.shortcuts import render
from django.template import Context
from .process_code import import_data


def index_render(request):
	fields_to_read = []
	graphs_to_render = []

	if "op" in request.POST:
		# DEBUG
		#print("DEBUG >> " + " ".join( request.POST.getlist("op") ) )
		fields_to_read = request.POST.getlist("op")
		if not fields_to_read:
			return render(request, "index.html",{"field_names": import_data.getFieldNames()} )
		else:
			# DEBUG
			print("Else branch.")
			graphs_to_render = import_data.getGraphsWebComponents(fields_to_read)
			return_obj = render(request, "index.html",{
					"field_names": import_data.getFieldNames(),
					"graph_1": graphs_to_render.pop(0),
					"graphs": graphs_to_render
				} ) 

			# DEBUG

			print("\n\n\nDEBUG >> " + "\n\n\n".join(graphs_to_render))
			
			return return_obj 
	else:
		return render(request, "index.html",{"field_names": import_data.getFieldNames()} )

def sql_render(request):

	return render(request, "sql.html")
