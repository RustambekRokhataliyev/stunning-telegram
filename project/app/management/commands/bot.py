import nt

from django.core.management.base import BaseCommand
from telebot import TeleBot
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import schedule
from webdriver_manager.chrome import ChromeDriverManager
from app.telegram import amazon_parser
from selenium import webdriver
from app.models import InTransitTrips, UpcomingTrips, TripHistories, SentMessagesHistory, SentMessagesUpcoming, \
    SentMessagesTransit, Notes, SentNotes

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

TOKEN = "5976019254:AAHsvbXzK2rCMuuGRtPb5jWiPn0TNTle-Hw"

bot = TeleBot(TOKEN, parse_mode=None)


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.infinity_polling(skip_pending=True)


def check_upcoming_trips(message):
    amazon_parser.GetIntoTrips().get_upcoming_trip_info(
        driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install())))


def send_message(message):
    chat_id = message.chat.id
    news = UpcomingTrips.objects.filter(status="new").values()

    for upcoming in news:
        load_id = upcoming.get("load_id")
        if not SentMessagesUpcoming.objects.filter(load_id=load_id):
            bot.send_message(chat_id, f'Reminder: New Trip {upcoming.get("load_id")} has been booked')
            time.sleep(180)
            bot.send_message(chat_id,
                             f'Upcoming trip (SDJ Cargo LLC)\n\nTrip : {upcoming.get("load_id")} assigned to\nDriver: --{upcoming.get("drivers")}\nScheduled: --{upcoming.get("city")}, {upcoming.get("date_start")}')
            trip_upcoming = SentMessagesUpcoming()
            trip_upcoming.load_id = load_id
            trip_upcoming.save()

    news = InTransitTrips.objects.filter(status="new").values()
    for transit in news:
        load_id = transit.get("load_id")
        if not SentMessagesTransit.objects.filter(load_id=load_id):
            bot.send_message(chat_id, f'In Transit Trip (SDJ Cargo LLC):\n\n{transit.get("load_id")}\n\nDrivers: {transit.get("drivers")}')
            trip_transit = SentMessagesTransit()
            trip_transit.load_id = load_id
            trip_transit.save()
    news = TripHistories.objects.filter(status="new").values()
    for history in news:
        load_id = history.get("load_id")
        if not SentMessagesHistory.objects.filter(load_id=load_id):
            bot.send_message(chat_id,
                             f'(SDJ Cargo LLC)\n\nTrip: {history.get("load_id")} completed\nDrivers: --{history.get("drivers")}\nLocation: {history.get("city_to")}')
            trip_history = SentMessagesHistory()
            trip_history.load_id = load_id
            trip_history.save()
    news = Notes.objects.filter(status="new").values()
    for note in news:
        load_id = note.get("load_id")
        if not SentNotes.objects.filter(load_id=load_id):
            bot.send_message(chat_id,
                             f'In Transit(SDJ Cargo LLC) trip:\n\n{note.get("trip")}\nLeg: {note.get("load_id")}\nNote:\n{note.get("time")}\n{note.get("comment")}')
            sent_notes = SentNotes()
            sent_notes.load_id = load_id
            sent_notes.save()


@bot.message_handler(commands=["start"])
def welcome(message):
    while True or False:
        send_message(message)


@bot.message_handler(commands=["help"])
def check(message):
    try:
        check_upcoming_trips(message)
    except:
        pass
