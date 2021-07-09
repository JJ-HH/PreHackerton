# /var/www/user_pythonanywhere_com_wsgi.py
import os
import sys


path = "/home/JJHHPA/EDA/WebEDA"
if path not in sys.path:
    sys.path.append(path)



from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebEDA.settings")
application = get_wsgi_application()

