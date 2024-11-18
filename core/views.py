from django.shortcuts import render



# Create your views here.

def index (request):

    return render(request,'core/index.html')



def store (request):

    return render(request,'core/DLCs.html')

def about (request):

    return render(request,'core/Novedades.html')