def start(data: dict):
    print("Welcome! Press Enter to continue")

def pressed(data: dict):
    if data.get("key") is None:
        print("Press a key")
    else:
        print(f"You pressed \"{data['key']}\"")


def pressed_key(key: str, data: dict):
    if data.get("alnum") is not None:
        data["key"] = data["alnum"]

def restart(key: str, data: dict):
    data["alnum"] = None
    data["key"] = None
