from django.shortcuts import render




def indexView(request):
    context = {

    }
    return render(request, 'veriler.html', context)

def index(request):
    context = {

    }
    return render(request, 'index.html', context)


