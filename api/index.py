import os
import sys
from mangum import Mangum

# Add project directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myprojects.settings")

from django.core.asgi import get_asgi_application
application = get_asgi_application()
handler =Mangum(application)