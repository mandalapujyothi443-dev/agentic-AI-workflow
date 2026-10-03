def agent(max_iters=10):
    state = {
        "done": False,
        "steps": 0
    }

    for i in range(max_iters):

        # Observe
        temperature = int(input("Enter temperature: "))

        # Decide
        if temperature < 72:
            decision = "Temperature is low"
            action = "Turn ON heater"
        elif temperature > 72:
            decision = "Temperature is high"
            action = "Turn ON fan"
        else:
            decision = "Temperature is ideal"
            action = "Do nothing"

        # Act
        print("Observe:", temperature)
        print("Decide:", decision)
        print("Act:", action)

        # Update state
        state["steps"] += 1

        # Check goal
        if temperature == 72:
            state["done"] = True
            return state

        print("State:", state)
        print("-------------------")

    # Maximum iterations exceeded
    return {
        "done": state["done"],
        "steps": state["steps"],
        "result": "failure"
    }


result = agent(max_iters=10)
print("Final Result:", result)