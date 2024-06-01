import requests
import json
import icalendar
import datetime
import time
import pytz


class Calendar:
    def __init__(self):
        self.CONFIG = {}
        try:
            with open("config.json", "r") as f:
                self.CONFIG = json.load(f)
        except FileNotFoundError:
            print("La configuration des URL va commencer.")
            self.setup_planning()
            print("Configuration terminée !")

            with open("config.json", "w") as f:
                json.dump(self.CONFIG, f)

    def number_user(self):
        """
        Ask the user how many people he wants to add
        :return:
        """
        number_new_user = 0
        while number_new_user >= 10 or number_new_user < 0:
            try:
                number_new_user = int(input("Combien de personnes voulez-vous ajouter (pas plus de 10 à la fois) ? ").strip())
                if number_new_user >= 10 or number_new_user < 0:
                    print("Veuillez ajouter pas plus de 10 personnes à la fois.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")

        return number_new_user

    def add_new_user(self):
        """
        Add new user to the config file
        :return: none
        """
        # TODO : convertir tout en dictionnaire de dictionnaire pour plus de clarté (nom de la personne, lien ICAL)
        new_user = {"agenda_url": []}
        number_new_user = self.number_user()

        for i in range(number_new_user):
            new_user["agenda_url"].append(input("Coller le lien ICAL : ").strip().replace("webcal://", "https://"))

        for key in new_user.keys():
            if key in self.CONFIG:  # self.CONFIG = old file
                for element in new_user[key]:
                    if element not in self.CONFIG[key]:
                        self.CONFIG[key].append(element)

        with open("config.json", "w") as new_file:
            json.dump(self.CONFIG, new_file)

    def setup_planning(self):
        print("======== PLANNING MYEFREI ========\n")
        self.CONFIG["agenda_url"] = [input("Coller le lien ICAL : ").strip().replace("webcal://", "https://")]
        # TODO : [0] pour faire marcher mais à changer
        r = requests.get(self.CONFIG["agenda_url"][0])
        if r.status_code != 200:
            print("Erreur : Le lien que vous avez entré n'est pas valide.\n")
            self.setup_planning()

    def get_agenda(self):
        # TODO : [0] pour faire marcher mais à changer
        r = requests.get(self.CONFIG["agenda_url"][0])
        cal = icalendar.Calendar.from_ical(r.content)
        return cal

    def get_current_event(self, calendar):
        current_utc = pytz.UTC.localize(datetime.datetime.utcnow())
        events = []
        for event in calendar.walk():
            if event.name == "VEVENT":
                start = event.get("dtstart").dt
                end = event.get("dtend").dt
                summary = event.get("summary")
                location = event.get("location")
                description = event.get("description")
                events.append(
                    {"start": start, "end": end, "nom_cours": summary, "salle": location, "nom_prof": description})
        for event in events:
            if event["start"] < current_utc < event["end"]:
                return event
        return None