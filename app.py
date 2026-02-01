import os
from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gmwebsite.settings')

# Create the WSGI application
app = get_wsgi_application()
   