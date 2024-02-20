class Maze:
    def __init__(self):
        # Variables
        self.trap_squares = []
        self.start_square = 0
        self.total_node_number = 64
        self.G = dict()
        self.goal_squares = []
        self.possibleMoves = dict()

        # read maze
        with open('maze.txt', 'r') as file:
            text = file.read()

        # read important squares
        with open('square_indexes_and_types.txt', 'r') as file:
            squares = file.read()

        # read important squares
        self.readSquares(squares)

        # split text file into an array
        array = text.split(";\n")

        # Check if the length of the array is sufficient
        if len(array) < self.total_node_number:
            print("Insufficient file")
            return

        for i in range(self.total_node_number):
            array[i] = array[i].replace("'", "")
            cell_name = array[i].split(", ")
            cell_index = []
            for possibleMove in cell_name:
                if "east" in possibleMove:
                    cell_index.append(i + 1)
                elif "west" in possibleMove:
                    cell_index.append(i - 1)
                elif "north" in possibleMove:
                    cell_index.append(i - 8)
                elif "south" in possibleMove:
                    cell_index.append(i + 8)

            self.possibleMoves[i] = cell_index

    # string[start: end: step]
    def readSquares(self, all_squares):
        for line in all_squares.splitlines():
            parts = line.split(",")
            index = int(parts[1])
            if "S" in parts[0]:
                self.start_square = index
            elif "T" in parts[0]:
                self.trap_squares.append(index)
            elif "G" in parts[0]:
                self.goal_squares.append(index)
                self.G[parts[0]] = index

    def coordinate_from_index(self, index):
        return "(" + str((index // 8) + 1) + ", " + str((index % 8) + 1) + ")"

    def can_pass(self, square_number, direction):
        if square_number in self.possibleMoves:
            values = self.possibleMoves[square_number]
            if direction in values:
                return True
            else:
                return False

    def possibleMoves(self):
        return self.possibleMoves

    def get_possible_moves(self, square_number):
        return self.possibleMoves.get(square_number, [])
