''' stores all functions for home app '''
from django.shortcuts import render 



def index(request):
    ''' loads home page '''

    return render(request, 'home/index.html')

