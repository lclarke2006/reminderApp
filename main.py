# notif stuff
import time
from winotify import Notification

# app stuff
from flask import Flask, redirect
from threading import Thread

# resource path stuff
import os
import sys

# custom sound stuff
from playsound import playsound
import threading


def play_sound():
    playsound(mp3_path)

# no clue
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

icon_path = resource_path("water.ico")
mp3_path = resource_path("drinking.mp3")


def notif(i):
    threading.Thread(target=play_sound, daemon=True).start()

    toast = Notification(app_id="DRINK WATER",
                         title="YOU NEED TO HYDRATE",
                         msg="Reminder: " + f"{i}",
                         duration="short",
                         icon=icon_path)

    toast.add_actions(label="BUY HERE", launch="http://localhost:5000/clicked")

    i += 1

    toast.show()
    time.sleep(20)
app = Flask(__name__)

@app.route('/clicked')
def clicked():
    global sendNotif
    sendNotif = False

    return redirect('https://www.amazon.co.uk/bottled-water/s?k=bottled+water')

def server():
    app.run(port=5000)

# thread stuff i dont understand
server_thread = Thread(target=server)
server_thread.daemon = True
server_thread.start()

while True:
    i = 1
    sendNotif = True

    while sendNotif:
        notif(i)
        i += 1

    print("User clicked water")

    time.sleep(3600)
