def agent(max_iters=10):
    state = {
        "done": False,
        "steps": 0
    }

    for i in range(max_iters):

        # OBSERVE
        temperature = int(input("Enter temperature: "))

        # DECIDE
        if temperature < 72:
            decision = "Temperature is low"
            action = "Turn ON heater"

        elif temperature > 72:
            decision = "Temperature is high"
            action = "Turn ON fan"

        else:
            decision = "Temperature is ideal"
            action = "Do nothing"

        # ACT
        print("Observe:", temperature)
        print("Decide:", decision)
        print("Act:", action)

        # Update steps
        state["steps"] += 1

        # SUCCESS STATE
        if temperature == 72:
            state["done"] = True
            return {
                "status": "success",
                "state": state
            }

        print("State:", state)
        print("--------------------")

    # FAILURE STATE
    return {
        "status": "failure",
        "state": state
    }


# Run agent
result = agent(max_iters=10)

print("Final Result:", result)