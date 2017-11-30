from django.db import models
from djvs.process_code import import_data
import os

model_dir = os.path.dirname(__file__)
path = os.path.join(model_dir, "input_test_file.dat")

class Alunos(models.Model):
	print("Teste 1")
	fields = import_data.getFieldNames()
	fields_dict = {}
	print("Teste 2 " + str( fields ) )
	for field in fields:
		fields_dict[field] = models.CharField(max_length=200)


