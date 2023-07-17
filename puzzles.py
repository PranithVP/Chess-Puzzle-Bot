import chess

class Puzzle:
    def __init__(self, puzzle_id, fen, moves, rating, rating_deviation, popularity, num_plays, themes, game_url, opening_tags):
        self.puzzle_id = puzzle_id
        self.fen = fen
        self.moves = moves
        self.rating = rating
        self.rating_deviation = rating_deviation
        self.popularity = popularity
        self.num_plays = num_plays
        self.themes = themes
        self.game_url = game_url
        self.opening_tags = opening_tags

def parse_puzzles(file_path):
    puzzles = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            attributes = line.strip().split(',')
            # Extract puzzle attributes
            puzzle_id = attributes[0]
            fen = attributes[1]
            moves = attributes[2].split()
            rating = int(attributes[3])
            rating_deviation = int(attributes[4])
            popularity = int(attributes[5])
            num_plays = int(attributes[6])
            themes = attributes[7].split()
            game_url = attributes[8]
            opening_tags = attributes[9].split()
            # Create Puzzle object and add it to the list
            puzzle = Puzzle(puzzle_id, fen, moves, rating, rating_deviation, popularity, num_plays, themes, game_url, opening_tags)
            puzzles.append(puzzle)
    return puzzles

def parse_puzzle(line):
    attributes = line.strip().split(',')
    # Extract puzzle attributes
    puzzle_id = attributes[0]
    fen = attributes[1]
    moves = attributes[2].split()
    rating = int(attributes[3])
    rating_deviation = int(attributes[4])
    popularity = int(attributes[5])
    num_plays = int(attributes[6])
    themes = attributes[7].split()
    game_url = attributes[8]
    opening_tags = attributes[9].split()
    # Create Puzzle object and add it to the list
    puzzle = Puzzle(puzzle_id, fen, moves, rating, rating_deviation, popularity, num_plays, themes, game_url, opening_tags)
    return puzzle

def update_puzzles(puzzle_list):
    count = 0
    for puzzle in puzzle_list:
        count += 1
        total = len(puzzle_list)
        print(str(count) + "/" + str(total) + " (" + str(round(count/total, 4) * 100) + "%" + ")")
        fen = puzzle.fen
        latest_move = puzzle.moves[0]
        puzzle.moves.pop(0)
        fen = update_fen(fen, latest_move)
        puzzle.fen = fen

# Accessing puzzle attributes
def print_puzzles(puzzle_list):
    for puzzle in puzzle_list:
        print('Puzzle ID:', puzzle.puzzle_id)
        print('FEN:', puzzle.fen)
        print('Moves:', puzzle.moves)
        print('Rating:', puzzle.rating)
        print('Rating Deviation:', puzzle.rating_deviation)
        print('Popularity:', puzzle.popularity)
        print('Number of Plays:', puzzle.num_plays)
        print('Themes:', puzzle.themes)
        print('Game URL:', puzzle.game_url)
        print('Opening Tags:', puzzle.opening_tags)
        print()

def update_fen(fen: str, move: str):
    board = chess.Board(fen)
    source_square = chess.parse_square(move[:2])
    target_square = chess.parse_square(move[2:4])
    if len(move) > 4:
        promotion = move[4]
        board.push(chess.Move(source_square, target_square, promotion))
    else:
        board.push(chess.Move(source_square, target_square))
    return board.fen()

def filter_puzzles(puzzle_list):
    filtered_puzzles = []
    for puzzle in puzzle_list:
        if ('black' in puzzle.game_url) and (puzzle.rating > 1800) and (puzzle.rating < 2200):
            for tag in puzzle.themes:
                if "mate" in tag:
                    filtered_puzzles.append(puzzle)
                    break
    return filtered_puzzles

def store_puzzles(puzzle_list):
    with open('puzzles.csv', 'w') as file:
        for puzzle in puzzle_list:
            puzzle_id = puzzle.puzzle_id
            fen = puzzle.fen.split()[0]
            moves = ' '.join(puzzle.moves)
            rating = str(puzzle.rating)
            rating_deviation = str(puzzle.rating_deviation)
            popularity = str(puzzle.popularity)
            num_plays = str(puzzle.num_plays)
            themes = ' '.join(puzzle.themes)
            game_url = puzzle.game_url
            opening_tags = ' '.join(puzzle.opening_tags)

            line = f"{puzzle_id},{fen},{moves},{rating},{rating_deviation},{popularity},{num_plays},{themes},{game_url},{opening_tags}\n"
            file.write(line)

def get_puzzle(n: int) -> str:
    filename = 'puzzles.csv'
    count = 1
    with open(filename, "r") as file:
        line = file.readline()
        while(line != ""):
            if count >= n:
                return line
            count += 1
            line = file.readline()
    return ""

# Example usage
# file_path = 'test.csv'
# puzzles = parse_puzzles(file_path)
# update_puzzles(puzzles)
# filtered_puzzles = filter_puzzles(puzzles)
# store_puzzles(filtered_puzzles)
