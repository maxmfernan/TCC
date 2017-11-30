import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_site.settings")

import django
django.setup()

from djvs.models import Alunos

def populate():
	add_aluno()

def add_aluno():
	al = Alunos.objects.get_or_create()
	print(al.__str__())

if __name__ == "__main__":
	populate()