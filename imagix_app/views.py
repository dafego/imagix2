import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render



# Create your views here.
def hola(request):
    return HttpResponse("Hola Mundo")


def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual':ahora})


def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body><h1>En %s hora(s), seran:</h1><h3>" \
           "%s</h3></body></html>" %(offset, dt)
    return HttpResponse(html)


def index(request):
    return render(request, 'landio/index.html')

def static(request):
    return render(request, '../static')