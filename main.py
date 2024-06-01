import time
# from calendar_construction import get_agenda, get_current_event, show_presence, hide_presence
from Calendar import Calendar

# print("Démarrage de la Rich Presence Discord...")
# RPC = Presence(DISCORD_APPID)
# RPC.connect()
# print("Rich Presence connectée !")

'''print("Téléchargement du Planning...")
cal = get_agenda()
print("Planning téléchargé !")

print("Démarrage de l'actualisation de la Rich Presence...")'''


'''def run_rpc():
    try:
        while True:
            curr_event = get_current_event(cal)
            if curr_event is not None:
                show_presence(curr_event)
            else:
                hide_presence()
            time.sleep(15)
    except KeyboardInterrupt:
        print("Arrêt de EfreiRPC...")
        # RPC.close()
        exit(0)
    except:
        print("Une erreur est survenue, redémarrage dans 15 secondes.")
        time.sleep(15)
        run_rpc()


run_rpc()'''

if __name__ == "__main__":
    calendrier = Calendar()
    cal = calendrier.get_agenda()