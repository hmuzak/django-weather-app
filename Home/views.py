from django.shortcuts import render, HttpResponse, redirect
import urllib.request
import json
from django.http import Http404
from urllib.error import HTTPError

from django.http import HttpResponseNotFound


# Create your views here.

def home_view(request):
    if request.method == 'POST':
        value = request.POST.get('field')
        link = 'http://api.openweathermap.org/data/2.5/weather?q=' + value + '&appid=3cfd4240ed8f4c009d9a8d21431267e6'
        try:
            webLink = urllib.request.urlopen(link)
            data = webLink.read()
            list_of_data = json.loads(data)
            data = {
                "temp": str(list_of_data['main']['temp']) + 'k',
                "icon":     (list_of_data['weather'][0]['icon']),
                "desc":     (list_of_data['weather'][0]['description'])
            }
        except HTTPError:
            raise Http404("Sayfa bulunamadı!")

        # converting JSON data to a dictionary

        return render(request, 'index.html', data)


    else:
        data = {}
    return render(request, "index.html", {})

def no_page_found(request, exception):
    return render(request, '404.html', {})
