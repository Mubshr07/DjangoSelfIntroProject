from django.http import HttpResponse
from django.shortcuts import render
 

def homePage(request):
    data = dict()
    data['title'] = "Mubashir Iqbal +92-318-5099232"
    return render(request, 'home.html', data)




def clientsList(request):
    data = dict()
    data['title'] = "Mubashir Iqbal +92-318-5099232"
    return render(request, 'clients.html', data)


def blog(request):
    return render(request, 'base.html')