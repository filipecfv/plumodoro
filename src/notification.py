import os


def notification(message):
    os.system('notify-send ' + message)
