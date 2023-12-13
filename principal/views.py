from django.shortcuts import render

def holamundo(request):
    contex={}
    return render(request, "index.html", )
