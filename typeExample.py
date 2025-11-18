import time

# START TIME
startTime = time.perf_counter()

# CODE HERE
test = input("type [hello]: ")

# END TIME
endTime = time.perf_counter()

# ELAPSED TIME
elapsedTime = round((endTime - startTime), 2)

if elapsedTime >= 5:
    print("YOU LOSE")
    print(f"{elapsedTime}")

elif test != "hello":
    print("you spelled wrong")
    # If its wrong I need to indicate it in red

else:
    print("You Win")
    print(f"{elapsedTime}")
