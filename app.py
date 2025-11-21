import time
import random

WORDS = [
    "focus", "python", "keyboard", "practice", "privacy",
    "local", "speed", "typing", "offline", "secure",
    "quest", "random", "accurate", "computer", "timer"
]

print("Welcome to TypeQuest!")
print("A privacy-first offline typing game.\n")
input("Press ENTER to begin...")

print("You will have 60 seconds to type words.\n")

start_time = time.time()
time_limit = 60

correct = 0
total = 0

while time.time() - start_time < time_limit:
    word = random.choice(WORDS)
    print(f"\nType this word: {word}")
    typed = input("> ").strip()

    if typed == word:
        correct += 1
    total += 1

# ----- RESULTS -----
wpm = correct
accuracy = (correct / total) * 100 if total > 0 else 0

print("\n----- RESULTS -----")
print(f"Words attempted: {total}")
print(f"Correct words: {correct}")
print(f"Words Per Minute (WPM): {wpm}")
print(f"Accuracy: {accuracy:.2f}%")
