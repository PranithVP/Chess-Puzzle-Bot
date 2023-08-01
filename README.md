# Chess Puzzle Bot
A python program that uses various libraries and the [Lichess database](https://lichess.org/) to generate images of puzzles, then post them to Instagram. It aims to provide chess enthusiasts with challenging puzzles and engage the chess community on Instagram.

# How it Works
#### Puzzle Generation: 
The bot fetches chess puzzles from the Lichess database using the puzzles module. Each puzzle is represented in FEN (Forsyth-Edwards Notation) format, along with its mate-in-N count.
#### Image Creation:
The script converts the FEN puzzle to a chessboard image using the fentoboardimage module. A color scheme is chosen based on the puzzle's theme.
#### Image Enhancement: 
The generated chessboard image is resized and overlaid with an aesthetic transparent overlay PNG to enhance its appearance.
#### Posting to Instagram:
The bot logs into Instagram using the [Instagrapi](https://adw0rd.github.io/instagrapi/) library (credentials provided via environment variables). The puzzle image is uploaded to the Instagram account, accompanied by an appropriate caption that describes the puzzle and includes relevant hashtags.
#### Puzzle Storage and Updates:
The bot parses chess puzzles from a CSV file (e.g., "puzzles.csv") using the parse_puzzles function. After each puzzle is posted, the script updates the FEN representation of the puzzle to reflect the moves played.

# Dependencies

The bot relies on the following Python libraries:

fentoboardimage: A module for converting FEN strings to chessboard images.
chess: A library that allows modifications to a chess board.
tempfile, os, dotenv, pathlib, PIL: Standard Python libraries for handling temporary files, environment variables, file paths, and image manipulation.




