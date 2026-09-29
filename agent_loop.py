for i in range(3):
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