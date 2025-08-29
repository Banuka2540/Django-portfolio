from django.http import HttpResponse

def homepage(request):
    return HttpResponse("hi")

def about(request):
    return HttpResponse("about")