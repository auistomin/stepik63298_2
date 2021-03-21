from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from numpy import random

import data


class MainView(View):
    def get(self, request):
        indexes = [int(i) for i in range(1, len(data.tours) + 1)]
        indexes = random.choice(indexes, 6, replace=False)
        tours = {i: data.tours[i] for i in indexes}
        context = {
            'title': data.title,
            'subtitle': data.subtitle,
            'description': data.description,
            'departures': data.departures,
            'tours': tours
        }
        return render(request, 'index.html', context=context)


class DepartureView(View):
    def get(self, request, departure):
        tours = dict()
        if departure in data.departures:
            for key, tour in data.tours.items():
                if tour["departure"] == departure:
                    tours[key] = tour
        n_tours = len(tours)
        suffix = ('a' if 2 <= n_tours % 10 <= 4 and n_tours % 100 // 10 != 1 else ('' if n_tours % 10 == 1 and n_tours % 100 // 10 != 1 else 'ов'))
        price_min = min(tours.items(), key=lambda item: item[1]['price'])[1]['price']
        price_max = max(tours.items(), key=lambda item: item[1]['price'])[1]['price']
        nights_min = min(tours.items(), key=lambda item: item[1]['nights'])[1]['nights']
        nights_max = max(tours.items(), key=lambda item: item[1]['nights'])[1]['nights']
        context = {
            'title': data.title,
            'subtitle': data.subtitle,
            'description': data.description,
            'departures': data.departures,
            'tours': tours,
            'departure_title': data.departures[departure],
            'n_tours': str(n_tours) + ' тур' + suffix,
            'price_min': price_min,
            'price_max': price_max,
            'nights_min': nights_min,
            'nights_max': nights_max,
        }
        return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, tour_id):
        tour = data.tours.get(tour_id)
        if not tour:
            abort(404)
        stars = '★' * int(tour['stars'])
        context = {
            'title': data.title,
            'subtitle': data.subtitle,
            'description': data.description,
            'departures': data.departures,
            'departure_title': data.departures[tour['departure']],
            'tour': tour,
            'stars': stars,
        }
        return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    #return HttpResponseNotFound('<h1>Ой, страница не найдена</h1><br>Извините, но мы не нашли запрашиваемую страницу...')
    context = {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
    }
    return render(request, "404.html", context=context)


def custom_handler500(request):
    #return HttpResponseServerError('<h1>Ой, ошибка на сервере</h1><br>Мы уже работаем над этим, попробуйте обновить страницу позже...')
    context = {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
    }
    return render(request, "500.html", context=context)
