from instagrapi import Client
import os
from dotenv import load_dotenv

def create_client():
    # Set login settings
    settings = {
    "uuids": {
        "phone_id": "9e51f55d-34fd-41e9-ab14-a69bed90e2c8",
        "uuid": "ece8e2d9-0293-4da9-8c02-cf619c079ed4",
        "client_session_id": "cd03e8fc-2dff-419f-9853-3eaa5b037a42",
        "advertising_id": "50ce87ae-ab02-49bd-83e4-1781160a3969",
        "android_device_id": "android-5642a0cc3eb22318",
        "request_id": "dcef82e0-8178-42cc-bd63-e70db52f4525",
        "tray_session_id": "9f102b5a-9c06-4201-ab44-6f0afff9de08"
    },
    "cookies": {},
    "last_login": 1690616552.5817745,
    "device_settings": {
        "app_version": "269.0.0.18.75",
        "android_version": 26,
        "android_release": "8.0.0",
        "dpi": "480dpi",
        "resolution": "1080x1920",
        "manufacturer": "OnePlus",
        "device": "devitron",
        "model": "6T Dev",
        "cpu": "qcom",
        "version_code": "314665256"
    },
    "user_agent": "Instagram 269.0.0.18.75 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; 6T Dev; devitron; qcom; en_US; 314665256)",
}
    # Create and return client
    cl = Client(settings)
    username = os.getenv("INSTAGRAM_USER")
    password = os.getenv("INSTAGRAM_PASS")
    cl.login(username, password)
    return cl
