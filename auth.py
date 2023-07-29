from instagrapi import Client
import os
from dotenv import load_dotenv

def create_client():
    # Set login settings
    settings = {
        "uuids": {
            "phone_id": "d0ccfa47-8a4a-4825-9087-7582c187b99f",
            "uuid": "0faba0fd-8d93-41b6-bb56-d6d333a0fa5e",
            "client_session_id": "a72f86a9-e807-4670-9872-f6353754fe46",
            "advertising_id": "362b0f8f-ce2e-4e74-92e9-e2294c072312",
            "android_device_id": "android-a2a177fb4596eee6",
            "request_id": "0135d501-e006-4537-8cb9-a43311c0a25a",
            "tray_session_id": "8110b5cc-19bb-4bdd-8e46-042298b1d562"
        },
        "cookies": {},
        "last_login": 1689462393.3357425,
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
