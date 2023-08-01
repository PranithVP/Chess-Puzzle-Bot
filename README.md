# Chess Puzzle Bot
A python program that uses various libraries and the [Lichess database](https://lichess.org/) to generate images of puzzles, then post them to Instagram. It aims to provide chess enthusiasts with challenging puzzles and engage the chess community on Instagram.

**Instagram account**: https://www.instagram.com/puzzle.paradise/

# How it Works
#### Puzzle Generation: 
The bot fetches chess puzzles from the Lichess database using the puzzles module. Each puzzle is represented in [FEN (Forsyth-Edwards Notation)](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) format, along with its mate-in-N count.
#### Puzzle Storage:
The bot parses chess puzzles from a CSV file (e.g., "puzzles.csv") using the parse_puzzles function. After each puzzle is posted, the script updates the FEN representation of the puzzle to reflect the first move played, resulting in an appropriate position for the puzzle to be posted.
#### Image Creation:
The script converts the FEN puzzle to a chessboard image using the [fentoboardimage](https://pypi.org/project/fentoboardimage/) module. A color scheme is chosen for each puzzle from a list of tuples representing themes. The generated chessboard image is resized and overlaid with a transparent overlay PNG to show the coordinates of each square on the chessboard.
#### Posting to Instagram:
The bot logs into Instagram using the [Instagrapi](https://adw0rd.github.io/instagrapi/) library (credentials provided via environment variables). The puzzle image is uploaded to the Instagram account, accompanied by an appropriate caption that describes the puzzle and includes relevant hashtags.

# Dependencies
The bot relies on the following Python libraries:

**[fentoboardimage](https://pypi.org/project/fentoboardimage/)**: A module for converting FEN strings to chessboard images.<br/>
**[chess](https://python-chess.readthedocs.io/en/latest/)**: A library that allows modifications to a chessboard.<br/>
**[tempfile](https://docs.python.org/3/library/tempfile.html)**, **[os](https://docs.python.org/3/library/os.html)**, **[dotenv](https://pypi.org/project/python-dotenv/)**, **[pathlib](https://docs.python.org/3/library/pathlib.html)**, **[PIL](https://pypi.org/project/Pillow/)**: Standard Python libraries for handling temporary files, environment variables, file paths, and image manipulation.
