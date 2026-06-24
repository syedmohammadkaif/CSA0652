# Constraint-Based AI Planning using Backtracking

goal = input("Enter goal (house/painted_house): ").strip()

resource_limit = int(input("Enter maximum resource limit: "))

actions = {
    "Gather_Wood": {
        "pre": [],
        "effect": ["wood"],
        "cost": 2
    },
    "Build_House": {
        "pre": ["wood"],
        "effect": ["house"],
        "cost": 5
    },
    "Paint_House": {
        "pre": ["house"],
        "effect": ["painted_house"],
        "cost": 1
    }
}

plan_found = None


def backtrack(state, plan, resource_used):
    global plan_found

    if goal in state:
        plan_found = plan[:]
        return True

    if resource_used > resource_limit:
        return False

    for action, details in actions.items():

        if action in plan:
            continue

        if all(pre in state for pre in details["pre"]):

            new_state = state.copy()

            for effect in details["effect"]:
                new_state.add(effect)

            plan.append(action)

            if backtrack(
                    new_state,
                    plan,
                    resource_used + details["cost"]):
                return True

            plan.pop()

    return False


initial_state = set()

if backtrack(initial_state, [], 0):
    print("\nValid Plan Found:")
    for step_no, step in enumerate(plan_found, start=1):
        print(f"{step_no}. {step}")
else:
    print("\nNo Valid Plan Exists Within Resource Limit")