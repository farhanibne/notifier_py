import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title =  "**please Drink Water Now",
            message = "from the specialists, it is required to drink minimum 3 liter of water a day!!",
            
            timeout=12
        )
        time.sleep(60*60)