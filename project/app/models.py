from django.db import models


# Create your models here.
class UpcomingTrips(models.Model):
    load_id = models.CharField(verbose_name="load_id", max_length=255)
    city_from = models.TextField(verbose_name='city from', null=True)
    city_to = models.TextField(verbose_name='city to', null=True)
    date_start = models.TextField(verbose_name="load_id", max_length=255, null=True)
    date_end = models.TextField(verbose_name="load_id", max_length=255, null=True)
    drivers = models.TextField(verbose_name="drivers")
    status = models.TextField(verbose_name="status", null=True)

    def __str__(self):
        return self.load_id

    class Meta:
        verbose_name = "Upcoming Trip"
        verbose_name_plural = "Upcoming Trips"


class InTransitTrips(models.Model):
    load_id = models.CharField(verbose_name="load_id", max_length=255)
    city_from = models.TextField(verbose_name='city from', null=True)
    city_to = models.TextField(verbose_name='city to', null=True)
    date_start = models.TextField(verbose_name="date_start", max_length=255, null=True)
    date_end = models.TextField(verbose_name="date_end", max_length=255, null=True)
    drivers = models.TextField(verbose_name="drivers")
    status = models.TextField(verbose_name="status", null=True)

    def __str__(self):
        return self.load_id

    class Meta:
        verbose_name = "In Transit Trip"
        verbose_name_plural = "In Transit Trips"


class TripHistories(models.Model):
    load_id = models.CharField(verbose_name="load_id", max_length=255)
    city_from = models.TextField(verbose_name='city from', null=True)
    city_to = models.TextField(verbose_name='city to', null=True)
    # date_start = models.TextField(verbose_name="load_id", max_length=255, null=True)
    # date_end = models.TextField(verbose_name="load_id", max_length=255, null=True)
    drivers = models.TextField(verbose_name="drivers")
    status = models.TextField(verbose_name="status", null=True)
    completed_or_not = models.TextField(verbose_name="completed", null=True, default="Rejected/Canceled")

    def __str__(self):
        return self.load_id

    class Meta:
        verbose_name = "Trip History"
        verbose_name_plural = "Trip Histories"


class SentMessagesHistory(models.Model):
    load_id = models.CharField(verbose_name="load_id", max_length=255)

    def __str__(self):
        return self.load_id

    class Meta:
        verbose_name = 'Sent Message'
        verbose_name_plural = 'Sent Messages'


class SentMessagesUpcoming(models.Model):
    load_id = models.CharField(verbose_name="load_id", max_length=255)

    def __str__(self):
        return self.load_id

    class Meta:
        verbose_name = 'Sent Message'
        verbose_name_plural = 'Sent Messages'


class SentMessagesTransit(models.Model):
    load_id = models.CharField(verbose_name="load_id", max_length=255)

    def __str__(self):
        return self.load_id

    class Meta:
        verbose_name = 'Sent Message'
        verbose_name_plural = 'Sent Messages'


# class Notifications(models.Model):
#     text_load_id = models.CharField(verbose_name="load_id", max_length=255)
#     Category = models.TextField(verbose_name='city from', null=True)
#     city_to = models.TextField(verbose_name='city to', null=True)
#     date_start = models.TextField(verbose_name="date", max_length=255, null=True)
#     due = models.TextField(verbose_name="why")
#     status = models.TextField(verbose_name="status", null=True)
#
#     def __str__(self):
#         return self.text_load_id
#
#     class Meta:
#         verbose_name = "Trip History"
#         verbose_name_plural = "Trip Histories"

class Notes(models.Model):
    load_id = models.TextField(verbose_name="load_id", null=True)
    time = models.TextField(verbose_name="time_sent", null=True)
    status = models.TextField(verbose_name="status", null=True)
    comment = models.TextField(verbose_name="comment", null=True)
    trip = models.TextField(verbose_name="trip_id", null=True)

    def __str__(self):
        return self.load_id


class SentNotes(models.Model):
    load_id = models.TextField(verbose_name="sent_note_load_id")

    def __str__(self):
        return self.load_id
