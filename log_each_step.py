def agent(max_iters=10):
    state = {
        "done": False,
        "steps": 0
    }

    log = []

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

        # Update state
        state["steps"] += 1

        # Log this step
        log.append({
            "step": state["steps"],
            "observe": temperature,
            "decide": decision,
            "act": action
        })

        # SUCCESS
        if temperature == 72:
            state["done"] = True

            return {
                "status": "success",
                "state": state,
                "log": log
            }

        print("State:", state)
        print("--------------------")

    # FAILURE
    return {
        "status": "failure",
        "state": state,
        "log": log
    }


# Run agent
result = agent(max_iters=10)

print("\n========== FULL LOG ==========")

print("Status:", result["status"])
print("State:", result["state"])

for entry in result["log"]:
    print(entry)