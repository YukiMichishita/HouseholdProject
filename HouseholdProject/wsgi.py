import os
import sys
sys.path.append('/home/bitnami/HouseholdProject')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/HouseholdProject/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HouseholdProject.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
