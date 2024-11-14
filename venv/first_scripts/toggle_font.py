text = input("Text to be toggle-fonted: ")
togfonted = " ".join(
    "".join(
        char.upper() if i % 2 ==0 else char.lower()
        for i, char in enumerate(word)
    )
    for word in text.split()
)

print(togfonted)