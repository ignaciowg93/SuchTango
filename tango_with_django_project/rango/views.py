
from django.shortcuts import render


def index(request):
    #Construyo un diccionario, con las variables que quiero pasarle, y que se reemplazen en el HTML
    context_dict = {'boldmessage': "Holulala mama mia"}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dic = {'user': "Ignacio"}

    return render(request, 'rango/about.html', context=context_dic)
