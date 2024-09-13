from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def IndexView(request):
    '''Esto es la pagina principal'''
    #return HttpResponse("Hola Mundo")
    return render(request,"index.html")
    