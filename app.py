import time
import random
import json
import os

WORDS = [
    "focus", "python", "keyboard", "practice", "privacy",
    "local", "speed", "typing", "offline", "secure",
    "quest", "random", "accurate", "computer", "timer"
]

def save_score(wpm, accuracy):
    score_data = {
        "wpm": wpm,
        "accuracy": accuracy,
        "date": time.strftime("%Y-%m-%d")
    }

    if os.path.exists("scores.json"):
        with open("scores.json", "r") as f:
            data = json.load(f)
    else:
        data = {"scores": []}

    data["scores"].append(score_data)

    with open("scores.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Score saved locally (offline).")

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

wpm = correct
accuracy = (correct / total) * 100 if total > 0 else 0

print("\n----- RESULTS -----")
print(f"Words attempted: {total}")
print(f"Correct words: {correct}")
print(f"Words Per Minute (WPM): {wpm}")
print(f"Accuracy: {accuracy:.2f}%")

save = input("Save your score? (y/n): ").lower()

if save.startswith("y"):
    save_score(wpm, accuracy)
else:
    print("Score not saved.")
