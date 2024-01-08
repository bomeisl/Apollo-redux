import requests
import simplejson
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView


class SnakeView(View):

    def get(request):
        url = 'https://nas.er.usgs.gov/api/v2/occurrence/search?group=Reptiles-Snakes'
        raw = requests.get(url=url)
        json = simplejson.loads(raw.text)
        paginator = Paginator(json['results'], per_page=25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'snakes.html', {"data": page_obj})