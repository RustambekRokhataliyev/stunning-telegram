from selenium import webdriver
from time import sleep
import json
from bs4 import BeautifulSoup
from app.models import InTransitTrips, UpcomingTrips, TripHistories, Notes
from selenium.webdriver.common.by import By


class AmazonRelayLogin:
    login = "maxaccteam@gmail.com"
    password = "qwertyuiop123"
    sign_in_url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=86400&openid.return_to=https%3A%2F%2Frelay.amazon.com%2Ftours%2Ftours%3Fstate%3Dhistory&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_relay_desktop_us&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_relay_desktop_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    upcoming_trip_url = "https://relay.amazon.com/tours/tours?state=upcoming"
    in_transit_trip_url = "https://relay.amazon.com/tours/tours?state=in-transit"
    history_url = "https://relay.amazon.com/tours/tours?state=history"
    notification = 'https://relay.amazon.com/notifications?tab=TASK'


class GetIntoTrips(AmazonRelayLogin):

    def get_upcoming_trip_info(self, driver):
        if not self.sign_in_url == driver.current_url:
            driver.get(self.sign_in_url)
            driver.find_element("id", "ap_email").send_keys(self.login)
            driver.find_element("id", "ap_password").send_keys(self.password)
            driver.find_element("id", "signInSubmit").click()
            sleep(5)
            driver.get(self.upcoming_trip_url)
        else:
            driver.get(self.upcoming_trip_url)
        sleep(5)
        string_html = driver.page_source
        soup = BeautifulSoup(string_html)
        sleep(10)
        whole_cart = soup.find("div", class_="tour-listing--tendered")
        sleep(10)
        if whole_cart is not None:
            block_cart = whole_cart.find_all("div", class_="tour-listing__card")
            sleep(10)

            for cart in block_cart:
                load_id_all_upcoming = cart.find_all("span", class_="tour-header__tour-id__tooltip")
                load_id = [item.get_text(strip=True) for item in load_id_all_upcoming]
                _dates = cart.find_all("div", class_="tour-header__secondary")
                dates = [item.get_text(strip=True) for item in _dates]
                _cities = cart.find_all("div", class_="city")
                cities = [item.get_text(strip=True) for item in _cities]
                drivers = cart.find("span", class_="dropdown-text dropdown-text__en").get_text(strip=True)

                if not UpcomingTrips.objects.filter(load_id=load_id[0]).exists():
                    upcoming_trips = UpcomingTrips()
                    upcoming_trips.load_id = load_id[0]
                    upcoming_trips.date_start = dates[0]
                    upcoming_trips.date_end = dates[1]
                    upcoming_trips.drivers = drivers
                    upcoming_trips.city_from = cities[0]
                    upcoming_trips.city_to = cities[1]
                    upcoming_trips.status = str("new")
                    upcoming_trips.save()
                else:
                    UpcomingTrips.objects.filter(load_id=load_id[0]).delete()
                    upcoming_trips = UpcomingTrips()
                    upcoming_trips.load_id = load_id[0]
                    upcoming_trips.date_start = dates[0]
                    upcoming_trips.date_end = dates[1]
                    upcoming_trips.drivers = drivers
                    upcoming_trips.city_from = cities[0]
                    upcoming_trips.city_to = cities[1]
                    upcoming_trips.status = str("old")
                    upcoming_trips.save()
            sleep(10)
        if self.sign_in_url == driver.current_url:
            driver.get(self.sign_in_url)
            driver.find_element("id", "ap_email").send_keys(self.login)
            driver.find_element("id", "ap_password").send_keys(self.password)
            driver.find_element("id", "signInSubmit").click()
            sleep(5)
            driver.get(self.in_transit_trip_url)
        else:
            driver.get(self.in_transit_trip_url)
        sleep(5)
        string_html = driver.page_source
        soup = BeautifulSoup(string_html)
        sleep(5)
        whole_cart = soup.find("div", class_="tour-listing--tendered")
        if whole_cart is not None:
            sleep(5)
            block_cart = whole_cart.find_all("div", class_="tour-listing__card")
            for cart in block_cart:
                load_id_components = cart.find_all("span", class_="tour-header__tour-id__tooltip")
                load_id = [item.get_text(strip=True) for item in load_id_components]
                _dates = cart.find_all("div", class_="tour-header__secondary")
                dates = [item.get_text(strip=True) for item in _dates]
                sleep(5)
                _cities = cart.find_all("div", class_="city")
                cities = [item.get_text(strip=True) for item in _cities]
                sleep(5)
                drivers = cart.find("span", class_="tour-header__drivers-name__truncated-name").get_text(strip=True)
                if not InTransitTrips.objects.filter(load_id=load_id[0]).exists():
                    in_transit_trip = InTransitTrips()
                    in_transit_trip.load_id = load_id[0]
                    in_transit_trip.date_start = dates[0]
                    in_transit_trip.date_end = dates[1]
                    in_transit_trip.drivers = drivers
                    in_transit_trip.city_from = cities[0]
                    in_transit_trip.city_to = cities[1]
                    in_transit_trip.status = str("new")
                    in_transit_trip.save()
                else:
                    InTransitTrips.objects.filter(load_id=load_id[0]).delete()
                    in_transit_trip = InTransitTrips()
                    in_transit_trip.load_id = load_id[0]
                    in_transit_trip.date_start = dates[0]
                    in_transit_trip.date_end = dates[1]
                    in_transit_trip.drivers = drivers
                    in_transit_trip.city_from = cities[0]
                    in_transit_trip.city_to = cities[1]
                    in_transit_trip.status = str("old")
                    in_transit_trip.save()
        if not self.sign_in_url == driver.current_url:
            driver.get(self.sign_in_url)
            driver.find_element("id", "ap_email").send_keys(self.login)
            driver.find_element("id", "ap_password").send_keys(self.password)
            driver.find_element("id", "signInSubmit").click()
            sleep(5)
            driver.get(self.in_transit_trip_url)
        else:
            driver.get(self.in_transit_trip_url)
        sleep(5)
        driver.find_element('class name', 'block-header__tour-id__business_type').click()
        sleep(5)
        driver.find_element('class name', 'tour-summary-header__notes-icon').click()
        sleep(2)
        get_notes_soup = BeautifulSoup(driver.page_source)
        note_cards = get_notes_soup.find("div", class_="load-notes__notes")
        for_trip = get_notes_soup.find('div', class_="tour-summary-modal")
        trip = for_trip.find('h5', class_='modal-title').get_text(strip=True)
        for notes in note_cards:
            time = notes.find('div', class_='time').get_text(strip=True)
            note_load_id = notes.find('div', class_="load-id").get_text(strip=True)
            comment = notes.find('p', class_='comment').get_text(strip=True)
            if not Notes.objects.filter(comment=comment).exists():
                notes = Notes()
                notes.load_id = note_load_id
                notes.time = time
                notes.comment = comment
                notes.status = "new"
                notes.trip = trip
                notes.save()
            else:
                Notes.objects.filter(load_id=note_load_id).delete()
                notes = Notes()
                notes.load_id = note_load_id
                notes.time = time
                notes.comment = comment
                notes.status = "old"
                notes.trip = trip
                notes.save()
        driver.find_element('xpath', '//*[@id="T-11148QGVJ-tour-left-attention-border"]/div[2]/div[3]/div[2]/div/div[2]/div/div/div[1]/button').click()
        sleep(2)
        if driver.current_url == self.sign_in_url:
            driver.find_element("id", "ap_email").send_keys(self.login)
            driver.find_element("id", "ap_password").send_keys(self.password)
            driver.find_element("id", "signInSubmit").click()
            sleep(5)
            driver.get(self.history_url)
        else:
            driver.get(self.history_url)
        sleep(5)
        string_html = driver.page_source
        soup = BeautifulSoup(string_html)
        sleep(10)
        whole_cart = soup.find("div", class_="tour-listing--tendered")
        if whole_cart is not None:
            block_cart = whole_cart.find_all("div", class_="tour-listing__card")
            for cart in block_cart:
                sleep(5)
                load_id_all_history = cart.find_all("span", class_="tour-header__tour-id__tooltip")
                load_id = [item.get_text(strip=True) for item in load_id_all_history]
                run_stop_details = cart.find("div", class_="run-stop-details")
                _dates = run_stop_details.find_all("div", class_="tour-header__secondary")
                dates = [item.get_text(strip=True) for item in _dates]
                drivers = cart.find("span", class_="tour-header__drivers-name__truncated-name").get_text(strip=True)
                _cities = cart.find_all("div", class_="city")
                cities = [item.get_text(strip=True) for item in _cities]
                if cart.find("div", class_="tour-header__completed-stops__overview"):
                    completed_or_not = cart.find("div", class_="tour-header__completed-stops__overview").get_text(
                        strip=True)
                sleep(5)
                if not TripHistories.objects.filter(load_id=load_id[0]).exists():
                    trip_history = TripHistories()
                    trip_history.load_id = load_id[0]
                    # trip_history.date_start = dates[0]
                    # trip_history.date_end = dates[1]
                    trip_history.drivers = drivers
                    trip_history.city_from = cities[0]
                    trip_history.city_to = cities[1]
                    trip_history.status = str("new")
                    # trip_history.completed_or_not = completed_or_not
                    trip_history.save()
                else:
                    TripHistories.objects.filter(load_id=load_id[0]).delete()
                    trip_history = TripHistories()
                    trip_history.load_id = load_id[0]
                    # trip_history.date_start = dates[0]
                    # trip_history.date_end = dates[1]
                    trip_history.drivers = drivers
                    trip_history.city_from = cities[0]
                    trip_history.city_to = cities[1]
                    # trip_history.completed_or_not = completed_or_not
                    trip_history.status = str("old")
                    trip_history.save()

        while True or False:
            if self.sign_in_url == driver.current_url:
                driver.get(self.sign_in_url)
                driver.find_element("id", "ap_email").send_keys(self.login)
                driver.find_element("id", "ap_password").send_keys(self.password)
                driver.find_element("id", "signInSubmit").click()
                sleep(5)
                driver.get(self.upcoming_trip_url)
            else:
                driver.get(self.upcoming_trip_url)
            sleep(5)
            string_html = driver.page_source
            soup = BeautifulSoup(string_html)
            sleep(10)
            whole_cart = soup.find("div", class_="tour-listing--tendered")
            sleep(10)
            if whole_cart is not None:
                block_cart = whole_cart.find_all("div", class_="tour-listing__card")
                sleep(10)

                for cart in block_cart:
                    load_id_all = cart.find_all("span", class_="tour-header__tour-id__tooltip")
                    load_id = [item.get_text(strip=True) for item in load_id_all]
                    _dates = cart.find_all("div", class_="tour-header__secondary")
                    dates = [item.get_text(strip=True) for item in _dates]
                    _cities = cart.find_all("div", class_="city")
                    cities = [item.get_text(strip=True) for item in _cities]
                    drivers = cart.find("span", class_="dropdown-text dropdown-text__en").get_text(strip=True)

                    if not UpcomingTrips.objects.filter(load_id=load_id[0]).exists():
                        upcoming_trips = UpcomingTrips()
                        upcoming_trips.load_id = load_id[0]
                        upcoming_trips.date_start = dates[0]
                        upcoming_trips.date_end = dates[1]
                        upcoming_trips.drivers = drivers
                        upcoming_trips.city = str(cities)
                        upcoming_trips.status = str("new")
                        upcoming_trips.save()
                    else:
                        UpcomingTrips.objects.filter(load_id=load_id[0]).delete()
                        upcoming_trips = UpcomingTrips()
                        upcoming_trips.load_id = load_id[0]
                        upcoming_trips.date_start = dates[0]
                        upcoming_trips.date_end = dates[1]
                        upcoming_trips.drivers = drivers
                        upcoming_trips.city_from = cities[0]
                        upcoming_trips.city_to = cities[1]
                        upcoming_trips.status = str("old")
                        upcoming_trips.save()
                sleep(10)
            if self.sign_in_url == driver.current_url:
                driver.get(self.sign_in_url)
                driver.find_element("id", "ap_email").send_keys(self.login)
                driver.find_element("id", "ap_password").send_keys(self.password)
                driver.find_element("id", "signInSubmit").click()
                sleep(5)
                driver.get(self.in_transit_trip_url)
            else:
                driver.get(self.in_transit_trip_url)
            sleep(5)
            string_html = driver.page_source
            soup = BeautifulSoup(string_html)
            sleep(5)
            whole_cart = soup.find("div", class_="tour-listing--tendered")
            if whole_cart is not None:
                sleep(5)
                block_cart = whole_cart.find_all("div", class_="tour-listing__card")
                sleep(5)
                for cart in block_cart:
                    load_id_all = cart.find_all("span", class_="tour-header__tour-id__tooltip")
                    load_id = [item.get_text(strip=True) for item in load_id_all]
                    driver.find_element("tour-header__tour-id__unsliced" "tour-header__tour-id__unsliced").click()
                    _dates = cart.find_all("div", class_="tour-header__secondary")
                    dates = [item.get_text(strip=True) for item in _dates]
                    sleep(5)
                    _cities = cart.find_all("div", class_="city")
                    cities = [item.get_text(strip=True) for item in _cities]
                    sleep(5)
                    drivers = cart.find("span", class_="tour-header__drivers-name__truncated-name").get_text(strip=True)
                    if not InTransitTrips.objects.filter(load_id=load_id[0]).exists():
                        in_transit_trip = InTransitTrips()
                        in_transit_trip.load_id = load_id[0]
                        in_transit_trip.date_start = dates[0]
                        in_transit_trip.date_end = dates[1]
                        in_transit_trip.drivers = drivers
                        in_transit_trip.city = str(cities)
                        in_transit_trip.status = str("new")
                        in_transit_trip.save()
                    else:
                        InTransitTrips.objects.filter(load_id=load_id[0]).delete()
                        in_transit_trip = InTransitTrips()
                        in_transit_trip.load_id = load_id[0]
                        in_transit_trip.date_start = dates[0]
                        in_transit_trip.date_end = dates[1]
                        in_transit_trip.drivers = drivers
                        in_transit_trip.city = str(cities)
                        in_transit_trip.status = str("old")
                        in_transit_trip.save()
                sleep(10)
            if not self.sign_in_url == driver.current_url:
                driver.get(self.sign_in_url)
                driver.find_element("id", "ap_email").send_keys(self.login)
                driver.find_element("id", "ap_password").send_keys(self.password)
                driver.find_element("id", "signInSubmit").click()
                sleep(5)
                driver.get(self.in_transit_trip_url)
            else:
                driver.get(self.in_transit_trip_url)
            sleep(5)
            driver.find_element('class name', 'block-header__tour-id__business_type').click()
            sleep(5)
            driver.find_element('class name', 'tour-summary-header__notes-icon').click()
            sleep(2)
            get_notes_soup = BeautifulSoup(driver.page_source)
            note_cards = get_notes_soup.find("div", class_="load-notes__notes")
            for_trip = get_notes_soup.find('div', class_="tour-summary-modal")
            trip = for_trip.find('h5', class_='modal-title').get_text(strip=True)
            for notes in note_cards:
                time = notes.find('div', class_='time').get_text(strip=True)
                note_load_id = notes.find('div', class_="load-id").get_text(strip=True)
                comment = notes.find('p', class_='comment').get_text(strip=True)
                if not Notes.objects.filter(comment=comment).exists():
                    notes = Notes()
                    notes.load_id = note_load_id
                    notes.time = time
                    notes.comment = comment
                    notes.status = "new"
                    notes.trip = trip
                    notes.save()
                else:
                    Notes.objects.filter(load_id=note_load_id).delete()
                    notes = Notes()
                    notes.load_id = note_load_id
                    notes.time = time
                    notes.comment = comment
                    notes.status = "old"
                    notes.trip = trip
                    notes.save()
            driver.find_element('xpath',
                                '//*[@id="T-11148QGVJ-tour-left-attention-border"]/div[2]/div[3]/div[2]/div/div[2]/div/div/div[1]/button').click()
            if driver.current_url == self.sign_in_url:
                driver.find_element("id", "ap_email").send_keys(self.login)
                driver.find_element("id", "ap_password").send_keys(self.password)
                driver.find_element("id", "signInSubmit").click()
                sleep(5)
                driver.get(self.history_url)
            else:
                driver.get(self.history_url)
                sleep(5)
            string_html = driver.page_source
            soup = BeautifulSoup(string_html)
            whole_cart = soup.find("div", class_="tour-listing--tendered")
            sleep(10)
            if whole_cart is not None:
                block_cart = whole_cart.find_all("div", class_="tour-listing__card")
                sleep(10)
                for cart in block_cart:
                    load_id_all = cart.find("span", class_="tour-header__tour-id__tooltip")
                    load_id = [item.get_text(strip=True) for item in load_id_all]
                    run_stop_details = cart.find("div", class_="run-stop-details")
                    _dates = run_stop_details.find_all("div", class_="tour-header__secondary")
                    dates = [item.get_text(strip=True) for item in _dates]
                    drivers = cart.find("span", class_="tour-header__drivers-name__truncated-name").get_text(strip=True)
                    _cities = cart.find_all("div", class_="city")
                    cities = [item.get_text(strip=True) for item in _cities]
                    if cart.find("div", class_="tour-header__completed-stops__overview"):
                        completed_or_not = cart.find("div", class_="tour-header__completed-stops__overview").get_text(
                            strip=True)
                    sleep(5)
                    if not TripHistories.objects.filter(load_id=load_id[0]).exists():
                        trip_history = TripHistories()
                        trip_history.load_id = load_id
                        # trip_history.date_start = [0]
                        # trip_history.date_end = dates[1]
                        trip_history.drivers = drivers
                        trip_history.city_from = cities[0]
                        trip_history.city_to = cities[1]
                        trip_history.status = str("new")
                        # if completed_or_not:
                        #     trip_history.completed_or_not = completed_or_not
                        trip_history.save()
                    else:
                        TripHistories.objects.filter(load_id=load_id[0]).delete()
                        trip_history = TripHistories()
                        trip_history.load_id = load_id
                        # trip_history.date_start = [0]
                        # trip_history.date_end = dates[1]
                        trip_history.drivers = drivers
                        trip_history.city_from = cities[0]
                        trip_history.city_to = cities[1]
                        # if completed_or_not:
                        # trip_history.completed_or_not = completed_or_not
                        trip_history.status = str("old")
                        trip_history.save()
