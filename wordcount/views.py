from django.http import HttpResponse
from django.shortcuts import render
from langdetect import detect

def home(request):
    '''
    Renders home page with form to receive user input
    '''
    return render(request, 'home.html')

def result(request):
    '''
    Counts number of words & detects which language input used
    '''
    # grabs entire user input from textarea "fulltext"
    fulltext = request.GET['fulltext']

    # splits the string into array and counts its lenght
    count = len(fulltext.split())
    
    # detects the language in the string
    language = detect(fulltext)

    context = {'fulltext': fulltext, 'count': count, 'language': language}

    return render(request, 'result.html', context)
