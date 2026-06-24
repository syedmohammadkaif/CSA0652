def is_safe(board, row, col):
    for r in range(row):
        c = board[r]

        # Same column
        if c == col:
            return False

        # Diagonal check
        if abs(c - col) == abs(r - row):
            return False

    return True


def rotate(solution, n):
    new_sol = [0] * n
    for r in range(n):
        c = solution[r]
        new_sol[c] = n - 1 - r
    return tuple(new_sol)


def reflect(solution, n):
    return tuple(n - 1 - c for c in solution)


def canonical(solution, n):
    forms = []
    current = tuple(solution)

    for _ in range(4):
        forms.append(current)
        forms.append(reflect(current, n))
        current = rotate(current, n)

    return min(forms)


def print_board(solution, n):
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


def solve_nqueens(n):
    board = [-1] * n
    unique_solutions = set()

    def backtrack(row):
        if row == n:
            canon = canonical(board, n)

            if canon not in unique_solutions:
                unique_solutions.add(canon)

            return

        # Symmetry pruning for first row
        if row == 0:
            cols = range((n + 1) // 2)
        else:
            cols = range(n)

        for col in cols:
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)

    print("\nUnique Solutions:\n")
    count = 1

    for sol in unique_solutions:
        print(f"Solution {count}:")
        print_board(sol, n)
        count += 1

    print("Total Unique Solutions =", len(unique_solutions))


# Input
n = int(input("Enter value of N: "))
solve_nqueens(n)