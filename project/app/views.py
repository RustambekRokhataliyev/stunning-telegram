from django.shortcuts import render
from django.http import HttpResponse
from .models import InTransitTrips, UpcomingTrips, TripHistories


def index(request):
    load_id = '114YPPF9H114YPPF9H'
    dates = ['2023-01-29', '2023-01-28']
    drivers = 'D. Smith, B. Washington'
    cities = ['BFI5 KENT, WASHINGTON 98032', 'EWR8 TETERBORO, NJ 07608']

    if not TripHistories.objects.filter(load_id=load_id).exists():
        trip_history = TripHistories()
        trip_history.load_id = load_id
        trip_history.date_start = dates[0]
        trip_history.date_end = dates[1]
        trip_history.driver = drivers
        trip_history.save()

        return HttpResponse('ok')
        # tripHistories = TripHistories.objects.filter(load_id=load_id)
    # return HttpResponse('ok')
