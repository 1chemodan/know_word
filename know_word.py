known_words = set(input().lower() for _ in range(int(input())))

unknown_words = set()
for _ in range(int(input())):
    line = input().lower().split()
    for word in line:
        if word not in known_words:
            unknown_words.add(word)

for word in unknown_words:
    print(word)