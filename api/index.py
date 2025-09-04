from myprojects.wsgi import application  # replace 'myproject' with your project folder name
from mangum import Mangum

handler = Mangum(application)
