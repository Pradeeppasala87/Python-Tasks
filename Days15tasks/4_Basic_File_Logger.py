while True:
    try:
        action = input("Enter action (or stop): ")
        if action == "stop":
            break

        file = open("log.txt", "a")
        file.write(action + "\n")
        file.close()

    except:
        print("File error!")
