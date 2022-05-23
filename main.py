from twilio.rest import Client
import tkinter
import os

TWILIO_AUTH = os.environ.get('TWILIO_AUTH')
gui = tkinter.Tk()

gui.mainloop()

client = Client('a9012830129810941', TWILIO_AUTH)