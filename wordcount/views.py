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
    fulltext = request.GET['fulltext']
    
    language = detect(fulltext)

    context = {'fulltext': fulltext, 'language': language}

    return render(request, 'result.html', context)
