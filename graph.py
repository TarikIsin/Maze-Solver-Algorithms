import sys
from maze import Maze


class Node:
    def __init__(self, square_number):
        self.square_number = square_number
        self.cost = 0
        self.parent = None
        self.east = None
        self.west = None
        self.north = None
        self.south = None
        self.heuristic = 0

    def check_equality(self, square_number):
        return square_number == self.square_number

    def __str__(self):
        return str(self.square_number)

    def direction(self, square_number):
        maze_instance = Maze()
        pos_move = maze_instance.get_possible_moves(square_number)
        print(pos_move)
        if square_number + 1 in pos_move:
            self.east = 1
        if square_number - 1 in pos_move:
            self.west = 1
        if square_number - 8 in pos_move:
            self.north = 1
        if square_number + 8 in pos_move:
            self.south = 1


class Graph:
    nodes = []  # Keeping all nodes in a list to prevent duplicate nodes.
    maze = None

    def __init__(self):
        # Creating the graph.
        self.maze = Maze()
        self.root = self.create_node(self.maze.start_square)
        # Finding maximum depth.
        self.maximum_depth = self.find_maximum_depth() - 1

        # Creating heuristic...
        self.create_heuristic()

        # We will make the cost of root node 0, because that's where we start.
        self.root.cost = 0

    def create_node(self, square_number):
        node = Node(square_number)
        node.cost = 1
        if square_number in self.maze.trap_squares:
            node.cost = 7

        node.direction(node.square_number)
        self.nodes.append(node)
        # Setting all child nodes.
        directions = ["east", "west", "north", "south"]
        for direction in directions:
            if self.maze.can_pass(node.square_number, direction):
                neighbor_square = self.get_neighbor_square(square_number, direction)
                child_node = self.node_exists(neighbor_square)

                if child_node is None:
                    child_node = self.create_node(neighbor_square)[0]
                    setattr(node, direction, child_node)
                    child_node.parent = node

        return node

    def get_neighbor_square(self, square_number, direction):
        if direction == "east":
            return square_number + 1
        elif direction == "west":
            return square_number - 1
        elif direction == "north":
            return square_number - 8
        elif direction == "south":
            return square_number + 8

    def node_exists(self, square_number):
        for node in self.nodes:
            if node.check_equality(square_number):
                return node
        return None

    def find_maximum_depth(self):
        maximum_depth = 0

        for node in self.nodes:
            current_node = node
            local_depth = 0
            while current_node is not None:
                current_node = current_node.parent
                local_depth += 1

            # If local_depth is greater, we will set it as maximum_depth.
            maximum_depth = max(maximum_depth, local_depth)

        return maximum_depth

    def get_node_cost(self, square_number):
        for node in self.nodes:
            if node.check_equality(square_number):
                return node.cost
        return 0

    def clear_parents(self):
        for node in self.nodes:
            node.parent = None

    def create_heuristic(self):
        # Create a heuristic for each node...
        for node in self.nodes:
            # Select minimum distance to a closest goal...
            total_cost = sys.maxsize
            for goal_square in self.maze.goal_squares:
                cost = self.calculate_distance_cost(node.square_number, goal_square)

                # Select the minimum heuristic...
                total_cost = min(total_cost, cost)

            # After calculating the total cost, we assign it into node's heuristic...
            node.heuristic = total_cost

    def calculate_distance_cost(self, start_square, goal_square):

        start_x, start_y = start_square // 8 + 1, start_square % 8 + 1
        goal_x, goal_y = goal_square // 8 + 1, goal_square % 8 + 1

        vertical_distance = abs(goal_y - start_y)
        horizontal_distance = abs(goal_x - start_x)

        return vertical_distance + horizontal_distance
