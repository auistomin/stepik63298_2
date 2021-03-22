from django.shortcuts import render
from django.views import View
from django.http import Http404

from random import sample

import data


class MainView(View):
    def get(self, request):
        context = {
            'title': data.title,
            'subtitle': data.subtitle,
            'description': data.description,
            'tours': dict(sample(data.tours.items(), 6)),
        }
        return render(request, 'index.html', context=context)


class DepartureView(View):
    def get(self, request, departure):
        if departure not in data.departures:
            raise Http404
        tours = dict()
        if departure in data.departures:
            for key, tour in data.tours.items():
                if tour["departure"] == departure:
                    tours[key] = tour
        prices = [int(tour['price']) for tour in tours.values()]
        nights = [int(tour['nights']) for tour in tours.values()]
        context = {
            'tours': tours,
            'departure_title': data.departures[departure],
            'tours_count': len(tours),
            'price_min': min(prices),
            'price_max': max(prices),
            'nights_min': min(nights),
            'nights_max': max(nights),
        }
        return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, tour_id):
        tour = data.tours.get(tour_id)
        if tour is None:
            raise Http404
        context = {
            'departure_title': data.departures[tour['departure']],
            'tour': tour,
        }
        return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    response = render(request, '404.html')
    response.status_code = 404
    return response


def custom_handler500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response
