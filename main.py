from getkey import getkey
from app import app
import os

def update_screen():
    os.system("cls" if os.name == "nt" else "clear")
    app.call()

if __name__ == "__main__":
    update_screen()
    while True:
        key = getkey()
        if app.transition(key):
            update_screen()
