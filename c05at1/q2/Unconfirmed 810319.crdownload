# Boolean Circuit Satisfiability using Backtracking

variables = ["A", "B", "C"]

solution = None


def evaluate(assign):
    A = assign["A"]
    B = assign["B"]
    C = assign["C"]

    return (A and B) or (not C)


def backtrack(index, assignment):
    global solution

    if index == len(variables):

        if evaluate(assignment):
            solution = assignment.copy()
            return True

        return False

    var = variables[index]

    for value in [False, True]:

        assignment[var] = value

        if backtrack(index + 1, assignment):
            return True

    assignment.pop(var)

    return False


print("Boolean Circuit:")
print("F = (A AND B) OR (NOT C)")

backtrack(0, {})

if solution:
    print("\nSatisfying Assignment Found:")
    for k, v in solution.items():
        print(k, "=", v)

    print("\nCircuit Output =", evaluate(solution))
else:
    print("\nNo Satisfying Assignment Exists")