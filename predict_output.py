def agent():
    state = {
        "done": False,
        "steps": 0
    }

    for i in range(2):
        temperature = [60, 72][i]

        # Observe
        print("Observe:", temperature)

        # Decide
        if temperature < 72:
            action = "Turn ON heater"
        else:
            action = "Do nothing"

        # Act
        print("Act:", action)

        state["steps"] += 1

        # Goal check
        if temperature == 72:
            state["done"] = True
            return {
                "status": "success",
                "state": state
            }

    return {
        "status": "failure",
        "state": state
    }


result = agent()
print("Result:", result)