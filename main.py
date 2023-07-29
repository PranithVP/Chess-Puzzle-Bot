import auth
import puzzles
from fentoboardimage import fenToImage, loadPiecesFolder
import tempfile
import os
from dotenv import load_dotenv
from pathlib import Path
from PIL import Image

def get_puzzle_number():
    # Retrieve environment variable
    load_dotenv()
    counter = int(os.getenv("COUNTER"))
    return counter

def post_fen(fenString: str, mateInN: int):
    # Initialize colours and colour number
    colours = [("#C5D3F0","#727DB3"), ("#FCE4B4", "#CE8C1A"), ("#E6F7E7","#57A9AE"), ("#E5CEA3","#BD864B"),
                ("#DFDFDF","#828282"), ("#E8DCF2", "#9A7FB6"), ("#FFFEDD", "#85A665"),
                ("#F4DCBC", "#BA5544")]
    colour_number = get_puzzle_number() % 8

    # Create chess board image
    image = fenToImage(
	fen=fenString,
	squarelength=200,
	pieceSet=loadPiecesFolder("./pieces"),
	lightColor=colours[colour_number][0],
	darkColor=colours[colour_number][1])

    # Open the image directly from the response content using PIL
    image = image.convert("RGBA")
    overlay = Image.open("./images/overlay.png")
    overlay = overlay.convert("RGBA")

    # Update image dimensions, add overlay
    new_image = image.resize((1600, 1600))
    new_image.paste(overlay, (0, 0), overlay)
    new_image = new_image.convert("RGB")

    # Create temporary file and assign filepath
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        new_image.save(temp_file)
        temp_file.seek(0)
        filepath = Path(temp_file.name)

    # Post using to Instagram using Instagrapi 
    cl = auth.create_client()
    if (mateInN == 0):
        caption = "White to play and win.\nCan you find the solution? Comment below! \nFollow @puzzle.paradise for daily chess puzzles! \n.\n.\n.\n#chess #chessmaster #chesstactics #chesstactic #chessplayer #chesscombinations #chesscombination #chesscom #chessdotcom #chessclub #chesstricks #dailychess #chesspuzzle #chesspuzzles #chessproblem #chessproblems #playchess #шахматы #shataranj #schach #schack #ajedrez #shah #schach #sjakk #szachy #scacco #shakh #echecs"
    else:
        caption = "White to play. Mate in " + str(mateInN) + " moves.\nCan you find the solution? Comment below! \nFollow @puzzle.paradise for daily chess puzzles! \n.\n.\n.\n#chess #chessmaster #chesstactics #chesstactic #chessplayer #chesscombinations #chesscombination #chesscom #chessdotcom #chessclub #chesstricks #dailychess #chesspuzzle #chesspuzzles #chessproblem #chessproblems #playchess #шахматы #shataranj #schach #schack #ajedrez #shah #schach #sjakk #szachy #scacco #shakh #echecs"

    cl.photo_upload(filepath, caption)
    cl.logout()

# Run script to post puzzle
puzzle_text = puzzles.get_puzzle(get_puzzle_number())
puzzle = puzzles.parse_puzzle(puzzle_text)
fen = puzzle.fen
count = 0
for theme in puzzle.themes:
    if 'mateIn' in theme:
        count = int(theme[-1])
        break
    
post_fen(fen, count)