# from gpiozero import Button

# button = Button(2)

# button.wait_for_press()
# print("Button was pressed")

from gpiozero import Button
from signal import pause
from send_message import IFTTT_NOTIFICATION

newNotification = IFTTT_NOTIFICATION(eventName="send email", api_key= "kuonrPeTJC06djmqQ410mXu_ZZ7uMwBpx4Eg2F3chd3")

button = Button(2)

def button_pressed():
    print("Button waas pressed")
    newNotification.make_request()

button.when_pressed = button_pressed

pause()