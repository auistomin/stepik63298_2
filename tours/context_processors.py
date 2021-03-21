import data


def site_title(request):
    return {'site_title': data.title}


def all_departures(request):
    return {'all_departures': data.departures}
