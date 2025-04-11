from constraint import *
import time

def load_words(filename):
    """Load words from a dictionary file."""
    words = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().lower()
                length = len(word)
                if length not in words:
                    words[length] = []
                words[length].append(word)
    except FileNotFoundError:
        print(f"Warning: File {filename} not found.")
    return words

def solve_crossword():
    # Load dictionary
    dictionary = load_words("words.txt")
    
    # Create CSP problem
    problem = Problem()
    
    # Define variables with their domains
    variables = {
        #variable name : (row, col, length, direction)
        "1A": (0, 0, 5, "across"),
        "1D": (0, 0, 6, "down"),
        "2D": (0, 2, 11, "down"),
        "3D": (0, 2, 4, "down"),
        "4D": (0, 6, 6, "down"),
        "5D": (0, 8, 11, "down"),
        "5A": (0, 8, 3, "across"),
        "6D": (0, 10, 4, "down"),
        "7A": (1, 4, 5, "across"),
        "8A": (2, 0, 5, "across"),
        "9A": (3, 4, 7, "across"),
        "10A": (5, 0, 11, "across"),
        "11D": (5, 4, 6, "down"),
        "12D": (5, 10, 6, "down"),
        "13A": (7, 0, 7, "across"),
        "13D": (7, 0, 4, "down"),
        "14D": (7, 6, 4, "down"),
        "15A": (8, 6, 5, "across"),
        "16A": (9, 2, 5, "across"),
        "17A": (10, 0, 3, "across"),
        "18A": (10, 6, 5, "across")
    }
    
    # Add variables to the problem with their domains
    for var_name, (_, _, length, _) in variables.items():
        if length in dictionary:
            problem.addVariable(var_name, dictionary[length])
        else:
            print(f"No words of length {length} found for {var_name}")
            problem.addVariable(var_name, ["X" * length])  # Placeholder
    
    # Define constraints
    constraints = [
        ("1A", 0, "1D", 0),  # 1A[0] == 1D[0] (at 0,0)
        ("1A", 2, "2D", 0),  # 1A[2] == 2D[0] (at 0,2)
        ("1A", 4, "3D", 0),  # ..
        ("5A", 0, "5D", 0),
        ("5A", 2, "6D", 0),
        ("7A", 0, "3D", 1),
        ("7A", 2, "4D", 1),
        ("7A", 4, "5D", 1),
        ("8A", 0, "1D", 2),
        ("8A", 2, "2D", 2),
        ("8A", 4, "3D", 2),
        ("9A", 0, "3D", 3),
        ("9A", 2, "4D", 3),
        ("9A", 4, "5D", 3),
        ("9A", 6, "6D", 3),
        ("10A", 0, "1D", 5),
        ("10A", 2, "2D", 5),
        ("10A", 4, "11D", 0),
        ("10A", 6, "4D", 5),
        ("10A", 8, "5D", 5),
        ("10A", 10, "12D", 0),
        ("13A", 0, "13D", 0),
        ("13A", 2, "2D", 7),
        ("13A", 4, "11D", 2),
        ("13A", 6, "14D", 0),
        ("15A", 0, "14D", 1),
        ("15A", 2, "5D", 8),
        ("15A", 4, "12D", 3),
        ("16A", 0, "2D", 9),
        ("16A", 2, "11D", 4),
        ("16A", 4, "14D", 2),
        ("17A", 0, "13D", 3),
        ("17A", 2, "2D", 10),
        ("18A", 0, "14D", 3),
        ("18A", 2, "5D", 10),
        ("18A", 4, "12D", 5)
    ]
    
    # Add constraints to the problem
    for var1, idx1, var2, idx2 in constraints:
        problem.addConstraint(lambda w1, w2, i1=idx1, i2=idx2: w1[i1] == w2[i2], (var1, var2))
    
    # Solve the problem
    print("Solving crossword puzzle...")
    start_time = time.time()
    
    # Using backtracking with most constrained variable and most constraining value heuristics
    solutions = problem.getSolution()
    
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    return solutions, variables

def display_grid(solution, variables):
    if not solution:
        print("No solution found.")
        return
    
    # Find grid dimensions
    max_row = max(row for row, _, _, _ in variables.values())
    max_col = max(col for _, col, _, _ in variables.values())
    
    # Account for word lengths
    for _, col, length, direction in variables.values():
        if direction == "across":
            max_col = max(max_col, col + length - 1)
    
    for row, _, length, direction in variables.values():
        if direction == "down":
            max_row = max(max_row, row + length - 1)
    
    # Create empty grid
    grid = [[' ' for _ in range(max_col + 1)] for _ in range(max_row + 1)]
    
    # Fill in the grid with solution
    for var_name, word in solution.items():
        row, col, length, direction = variables[var_name]
        
        if direction == "across":
            for i, char in enumerate(word):
                grid[row][col + i] = char
        else:  # down
            for i, char in enumerate(word):
                grid[row + i][col] = char
    
    # Print the grid
    print("+", end="")
    for _ in range(max_col + 1):
        print("---+", end="")
    print()
    
    for row in grid:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
        print("+", end="")
        for _ in range(max_col + 1):
            print("---+", end="")
        print()
    
    # Also print the solution in word format
    print("\nCrossword Solution:")
    for var_name, word in solution.items():
        print(f"{var_name}: {word}")



solution, variables = solve_crossword()
display_grid(solution, variables)

