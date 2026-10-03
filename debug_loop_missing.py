def agent(max_iters=10):
    state = {
        "done": False,
        "steps": 0
    }

    log = []

    for i in range(max_iters):

        # OBSERVE
        try:
            temperature = int(input("Enter temperature: "))
        except ValueError:
            return {
                "status": "error",
                "error": "Invalid temperature input",
                "state": state,
                "log": log
            }

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

        # VALIDATE ACTION
        valid_actions = [
            "Turn ON heater",
            "Turn ON fan",
            "Do nothing"
        ]

        if action not in valid_actions:
            return {
                "status": "error",
                "error": "Invalid action",
                "action": action,
                "state": state,
                "log": log
            }

        # ACT
        print("Observe:", temperature)
        print("Decide:", decision)
        print("Act:", action)

        # FIX: Increment steps every iteration
        state["steps"] += 1

        # LOG
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

        print("Step:", state["steps"])
        print("--------------------")

    # FAILURE after max_iters
    return {
        "status": "failure",
        "state": state,
        "log": log
    }


# Run agent
result = agent(max_iters=10)

print("\n========== FINAL RESULT ==========")
print("Status:", result["status"])
print("State:", result["state"])

print("\n========== FULL LOG ==========")
for entry in result["log"]:
    print(entry)