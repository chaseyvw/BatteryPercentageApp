#imports

from email import message
from socket import timeout
from turtle import title
import psutil
from plyer import notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged

if __name__=="__main__":
    if plugged:
        percent = battery.percent
        if percent <= 80:
            notification.notify(
                #give notif a title
                title = "Charging",

                #message content for notif
                message = "To preserve battery life, charge up to 80%",

                #display time
                timeout = 2
            )

        elif percent == 100:
            notification.notify(
                title = "Charging",
                message = "Battery is fully charged, please unplug charger.",
                timeout = 2
                )
        
        else:
            notification.notify(
                title = "Charging",
                message = "To preserve battery life, charge up to 80%",
                timeout = 2
            )
        
    else:
        percent = battery.percent
        if percent <= 20:
            notification.notify(
                title = "Low Battery!",
                message = "Your battery is running low. Please plug in your PC.",
                timeout = 2
            )

        elif percent <= 50:
            notification.notify(
                title = "Battery Percentage",
                message = f'Battery is at {percent}',
                timeout = 2
            )

        elif percent == 100:
            notification.notify(
                title = "Fully Charged!",
                message = "Your battery is fully charged.",
                timeout = 2
            )
        
        else:
            notification.notify(
                title = "Battery Percentage",
                message = f'Battery is at {percent}',
                timeout = 2
            )