from django.http import response
from django.shortcuts import render
import requests
# Create your views here.

def home_view(request):
    response = requests.get('https://api.covid19india.org/data.json').json()['statewise']
    return render(request, 'index.html', {'response' : response, 'range' : range(len(response))})
