''' stores all functions for fitness_classes app '''
from django.shortcuts import render


def members_area(request):
    ''' loads fitness classes page '''

    return render(request, 'fitness_classes/members_area.html')
