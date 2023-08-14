from state_manager import *
from getkey import getkey
from app import app
import os

if __name__ == "__main__":
    data = {}
    while True:
        os.system('cls')
        app.call(data)
        key = getkey()
        if key.isalnum():
            data["alnum"] = key
            key = "alnum"
        app.transition(key, data)
