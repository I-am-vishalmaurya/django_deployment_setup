from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


# Create your views here.
def greet(request, name=None):
    return render(request, "appOne/index.html", {"name": name or 'World'})