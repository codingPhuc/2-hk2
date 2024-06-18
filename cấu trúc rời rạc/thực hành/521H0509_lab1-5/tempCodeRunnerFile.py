import itertools

# assume we have a matrix called `grid` with dimensions m x n

# generate all possible symbols for each cell (true -> green, false -> red)
symbols = [[f"{i},{j}" for j in range(n)] for i in range(m)]

# create an empty list to hold all CNF clauses
clauses = []

# iterate over each cell in the matrix
for i in range(m):
    for j in range(n):
        # get the symbol for the current cell
        symbol = symbols[i][j]
        
        # get the number in the current cell
        number = grid[i][j]
        
        # skip blank cells
        if number is None:
            continue
        
        # generate clauses for the adjacent cells
        adjacent_symbols = []
        for x, y in itertools.product(range(i-1, i+2), range(j-1, j+2)):
            if (0 <= x < m) and (0 <= y < n) and (x != i or y != j):
                adjacent_symbols.append(symbols[x][y])
        
        # generate all possible combinations of green and red cells for the adjacent cells
        combinations = list(itertools.product([True, False], repeat=len(adjacent_symbols)))
        
        # iterate over each combination and add a clause if it satisfies the constraint
        for combo in combinations:
            num_green = sum(combo)
            if num_green == number:
                clause = [f"{'-' if not combo[k] else ''}{adjacent_symbols[k]}" for k in range(len(combo))]
                clause.append(f"{'-' if not combo[-1] else ''}{symbol}")
                clauses.append(clause)

# print out the resulting CNF clauses
for clause in clauses:
    print(clause)