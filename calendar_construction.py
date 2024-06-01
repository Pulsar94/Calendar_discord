import requests
import icalendar
import datetime
import time
import pytz
import json
from setup import setup_planning, setup_discord

CONFIG = {}

try:
    with open("config.json", "r") as f:
        CONFIG = json.load(f)
except FileNotFoundError:
    print("La configuration des URL va commencer.")
    CONFIG = setup_planning(CONFIG)
    CONFIG = setup_discord(CONFIG)
    print("Configuration terminée !")

    with open("config.json", "w") as f:
        json.dump(CONFIG, f)


# DISCORD_APPID = "1016321832992903168"


def get_agenda():
    r = requests.get(CONFIG["agenda_url"])
    cal = icalendar.Calendar.from_ical(r.content)
    return cal




def get_current_event(calendar):
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


# def show_presence(event):
#     RPC.update(details=event[CONFIG["first_key"]], state=event[CONFIG["second_key"]], large_image=CONFIG["large_icon"],
#                large_text=CONFIG["large_icon_text"], start=int(time.mktime(event["start"].timetuple())) + 3600,
#                end=int(time.mktime(event["end"].timetuple())) + 3600, buttons=[{"label": "Website", "url": "https://github.com/DocSystem/EfreiRPC"}])
#
#

# RPC = Presence(DISCORD_APPID)
# RPC.connect()


# def run_rpc():
#     try:
#         while True:
#             curr_event = get_current_event(cal)
#             if curr_event is not None:
#                 show_presence(curr_event)
#             else:
#                 hide_presence()
#             time.sleep(15)
#     except KeyboardInterrupt:
#         print("Arrêt de EfreiRPC...")
#         RPC.close()
#         exit(0)
#     except:
#         print("Une erreur est survenue, redémarrage dans 15 secondes.")
#         time.sleep(15)
#         run_rpc()
#
#
# run_rpc()
