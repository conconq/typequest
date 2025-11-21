import time

print("Welcome to TypeQuest!")
print("A privacy-first offline typing game.\n")

input("Press ENTER to begin...")

print("You will have 60 seconds to type words.\n")

start_time = time.time()
time_limit = 60

while time.time() - start_time < time_limit:
    time_left = int(time_limit - (time.time() - start_time))
    print(f"Time left: {time_left} seconds", end="\r")

print("\nTime is up!")