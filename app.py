# TypeQuest - super simple starter
# How it works:
# - Shows 5 words
# - You type them
# - It tells you how many you got right

WORDS = ["focus", "python", "keyboard", "practice", "privacy"]

print("TypeQuest (Starter)")
print("Type each word exactly, then press ENTER.\n")

correct = 0
for w in WORDS:
    print("Word:", w)
    typed = input("> ").strip()
    if typed == w:
        correct += 1

total = len(WORDS)
accuracy = (correct / total) * 100
print(f"\nDone! Correct: {correct}/{total}  |  Accuracy: {accuracy:.0f}%")
