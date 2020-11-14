from django.http import HttpResponse
from django.shortcuts import render
from langdetect import detect
from collections import Counter

# GENERAL
def home(request):
    '''
    Renders home page with form to receive user input
    '''
    return render(request, 'home.html')


def about(request):
    '''
    Render "about me" page
    '''
    return render(request, 'about.html')


# FUNCTIONALITY
def result(request):
    '''
    Counts number of words & detects which language input used
    '''
    # grabs entire user input from textarea "fulltext"
    fulltext = request.GET['fulltext']

    frequency = dict(Counter(fulltext.split()))

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # splits the string into array and counts its lenght
    count = len(fulltext.split())
    
    # detects the language in the string
    language = detect(fulltext)

    context = {'fulltext': fulltext, 'count': count, 'language': language, 'sorted_frequency': sorted_frequency}

    return render(request, 'result.html', context)
