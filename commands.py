import webbrowser


def command(text):
    cmd = text.replace(" ", "_")
    try:
        return eval(cmd)()
    except Exception as e:
        return e


def open_site():
    try:
        webbrowser.open("http://alvinccruz.pythonanywhere.com/")
        return "Personal site opened."
    except Exception as e:
        return e


def open_google():
    try:
        webbrowser.open("https://google.com")
        return "Google opened."
    except Exception as e:
        return e


def open_github():
    try:
        webbrowser.open("https://github.com")
        return "Github opened."
    except Exception as e:
        return e
