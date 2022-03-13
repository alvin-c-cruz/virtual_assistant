def command(text):
    cmd_dict = {
        "open google": open_google,
        "open excel": open_excel,
        "play music": play_music,
    }
    cmd = cmd_dict.get(text)
    return cmd() if cmd else None


def open_google():
    print("Opening google.")
    return "Opening google."


def open_excel():
    print("Opening Excel")
    return "Opening Excel"


def play_music():
    print("Playing music.")
    return "Playing music."
