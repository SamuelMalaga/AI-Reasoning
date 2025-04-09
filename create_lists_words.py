import random

with open("words.txt", "r", encoding="utf-8") as f:
    all_words = f.readlines()

all_words = [word.strip() for word in all_words if word.strip()]

random.shuffle(all_words)

sizes = {
    "very_small": 1000,
    "small": 10000,
    "intermediate1": 80000,
    "intermediate2": 150000
}

for name, size in sizes.items():
    subset = all_words[:size]
    with open(f"dictionary_{name}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(subset))
