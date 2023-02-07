from django.contrib import admin
from . models import UpcomingTrips, InTransitTrips, TripHistories, SentMessagesHistory, SentMessagesTransit, SentMessagesUpcoming, Notes, SentNotes
# Register your models here.


admin.site.register(UpcomingTrips)
admin.site.register(InTransitTrips)
admin.site.register(TripHistories)
admin.site.register(SentMessagesHistory)
admin.site.register(SentMessagesUpcoming)
admin.site.register(Notes)
admin.site.register(SentMessagesTransit)
admin.site.register(SentNotes)
