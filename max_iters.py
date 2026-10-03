def agent(max_iters=10):
    for i in range(max_iters):
        print("Iteration:", i + 1)

        # Observe
        temperature = int(input("Enter temperature: "))

        # Decide
        if temperature < 72:
            decision = "Temperature is low"
        elif temperature > 72:
            decision = "Temperature is high"
        else:
            decision = "Temperature is ideal"

        # Act
        if temperature < 72:
            action = "Turn ON heater"
        elif temperature > 72:
            action = "Turn ON fan"
        else:
            action = "Do nothing"

        print("Observe:", temperature)
        print("Decide:", decision)
        print("Act:", action)
        print("-------------------")

        # Goal reached
        if temperature == 72:
            return "success"

    # Maximum iterations exceeded
    return "failure"


result = agent(max_iters=10)
print("Result:", result)