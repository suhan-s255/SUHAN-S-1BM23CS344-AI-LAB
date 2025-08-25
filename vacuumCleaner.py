def vacuum_cleaner():
    state_A = int(input("Enter state of A (0 for clean, 1 for dirty): "))
    state_B = int(input("Enter state of B (0 for clean, 1 for dirty): "))
    location = input("Enter location (A or B): ").upper()

    cost = 0
    rooms = {'A': state_A, 'B': state_B}

    if rooms['A'] == 0 and rooms['B'] == 0:
        print("Turning vacuum off")
        print("Cost: ", cost)
        print(rooms)
        return

    if location == 'A':
        if rooms['A'] == 1:
            print("Cleaned A.")
            rooms['A'] = 0
            cost += 1
        else:
            print("A is clean")
        print("Moving vacuum right")
        cost += 1

        if rooms['B'] == 1:
            print("Cleaned B.")
            rooms['B'] = 0
            cost += 1
        else:
            print("B is clean")

    elif location == 'B':
        if rooms['B'] == 1:
            print("Cleaned B.")
            rooms['B'] = 0
            cost += 1
        else:
            print("B is clean")
        print("Moving vacuum left")
        cost += 1

        if rooms['A'] == 1:
            print("Cleaned A.")
            rooms['A'] = 0
            cost += 1
        else:
            print("A is clean")

    print("Cost: ", cost)
    print(rooms)

vacuum_cleaner()
