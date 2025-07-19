def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def get_text():
    return "Nirav"

print(get_text())  # Output: <b><i>Nirav</i></b>