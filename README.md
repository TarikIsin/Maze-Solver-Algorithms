# Maze-Solver-Algorithms

## 1. Introduction
This project involves a maze solver application developed as part of an Artificial Intelligence course. By applying different search algorithms on the labyrinth, the aim is to find the shortest path.

## 2. Project Structure
The project consists of five main Python files:

- search.py: Contains different search algorithms and enables the implementation of these algorithms.
- maze.py: Contains the definition of the maze and it processes the maze data.
- main.py: It is the main application file. The graph is created, and different search algorithms are run.
- graph.py: Contains the Graph class that creates the maze graph.
- maze.txt: It is the text file containing the definition of the maze.

## 3. search.py File
#### 3.1. Search Algorithms Functions
- depth_first_search(): Implements the depth-first search algorithm.
- breadth_first_search(): Implements the breadth-first search algorithm.
- iterative_deepening_search(): Implements the iterative depth-first search algorithm.
- uniform_cost_search(): Implements the uniform cost search algorithm.
- greedy_best_first_search(): Implements the heuristic best first search algorithm.
- a_star_search(): Implements the A* search algorithm.

#### 3.2. Auxiliary Functions
- heuristic_search(algorithm, sort_by): Contains the main function of heuristic search algorithms.
- dfs_bfs_ids_ucs(algorithm): Contains the main function of DFS, BFS, IDS, UCS algorithms.
- add_to_frontier(current_node, algorithm ): Manages adding nodes in to Frontier.
- set_parent(parent_node, child_node, algorithm): Sets the parents of nodes.
- is_in_visited(node): Checks whether a node has been visited.
- is_goal(node ): Checks whether a node is the target state.
- print_results(algorithm, solution_cost, solution, expanded_nodes): Prints the algorithm results to the screen.
- return_cost(node), return_heuristic(node), return_cost_and_heuristic(node): Returns sorting functions.
- sort_frontier(sort_by): Sorts the frontier based on a specific criteria.

## 4. maze.py File
#### 4.1. Maze Class
- size: Holds the size of the maze.
- wall_vertical, walls_horizontal, traps: Holds maze features such as walls and traps.
- start: Holds the starting point.
- goals: Holds the target points.

#### 4.2. Helper Methods
- read_maze(): Reads and processes the maze information from the "maze.txt" file.
- set_size(x, y): Determines the size of the maze.
- set_walls(walls), set_traps(traps), set_start(start), set_goals(goals): Determines the properties of the maze.
- can_pass(row, column, direction): Checks whether there is a cell that can be passed in a certain direction.

## 5. main.py File
Creates the maze graph using the Graph class.
Runs it on the maze by calling different search algorithms in search.py.

## 6. graph.py File
#### 6.1. Node Class
Contains node properties (coordinates, cost, parent, neighbors, heuristic value).
- check_equality(x, y): Checks whether the node has certain coordinates.

#### 6.2. Graph Class
Contains the Graph class that creates and manages the labyrinth graph.
- calculateDepth(node): Calculates the depth of a node.
- create_node(x, y): Creates a new node and adds it to the graph.
- node_exists(x, y): Checks whether a node with a certain coordinates exists.
- find_maximum_depth(): Finds the maximum depth of the graph.
- get_node_cost(x, y): Gets the cost of a specific node.
- clear_parents(): Clears all node parents.
- create_heuristic(): Creates the heuristic value for each node.
- create_and_set_neighbors(node): Creates and sets the node's neighbors.
- create_and_set_neighbor(node), direction, dx, dy): Creates and sets a node neighbor in a specific direction.

## 7. maze.txt File
It is a text file containing the definition of the maze.
It contains information such as maze size, walls, traps, starting point and targets.
