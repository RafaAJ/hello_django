from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade): # Ele escreve na pagina o que vier depois da \
    return HttpResponse('<h1>hello {} de {} anos</h1>'.format(nome, idade)) #Por conta do HttpResponse, o navegador vai entender q a string eh um html