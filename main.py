import auth
import puzzles
import requests
import tempfile
import os
from dotenv import load_dotenv
from io import BytesIO
from pathlib import Path
from PIL import Image

def get_puzzle_number():
    load_dotenv()
    counter = int(os.getenv("COUNTER"))
    return counter

def post_fen(fen: str):
    url = "http://www.fen-to-image.com/image/125/single/" + fen
    response = requests.get(url)
    image_data = BytesIO(response.content)

    # Open the image directly from the response content using PIL
    image = Image.open(image_data)
    image = image.convert("RGBA")
    overlay = Image.open("overlay.png")
    overlay = overlay.convert("RGBA")

    new_image = image.resize((1250, 1250))
    new_image.paste(overlay, (0, 0), overlay)
    new_image = new_image.convert("RGB")

    # Create a temporary file in memory using BytesIO
    bytes_file = BytesIO()
    new_image.save(bytes_file, format="JPEG")

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        new_image.save(temp_file)
        temp_file.seek(0)
        filepath = Path(temp_file.name)

    # Use Instagrapi client to post image
    cl = auth.create_client()
    cl.photo_upload(filepath, "White to play and win")
    cl.logout()

puzzle_text = puzzles.get_puzzle(get_puzzle_number())
fen = puzzles.parse_puzzle(puzzle_text).fen
post_fen(fen)