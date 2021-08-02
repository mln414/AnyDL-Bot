import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1933475915:AAErASODEUWvKRsCjbc5U4TXlU5cc4Y314o")

    APP_ID = int(os.environ.get("APP_ID", 6657305))

    API_HASH = os.environ.get("API_HASH", "10ca9a965d788b977b45226e82dd4174")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "No")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "No")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "forcesub414")
