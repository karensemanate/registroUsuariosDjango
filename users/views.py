from django.shortcuts import render


# Create your views here.
def registerUser(request):
    if request.method == 'POST': 
        form = personaForm (request.POST)  
