from django.contrib import admin
from django.urls import path
from myprojects import views

# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/',views.projects, name = 'projects')
    
]
