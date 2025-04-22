def most_frequent_char(string1: str) -> list:
    counts = {}
    keys = []
    string1 = string1.lower()

    for letter in string1:
        if letter.isalpha():  # Only count alphabetic characters
            counts[letter] = counts.get(letter, 0) + 1

    if not counts:
        return []

    maximum = max(counts.values())

    for key, value in counts.items():
        if value == maximum:
            keys.append(key)

    return keys



# Examples
print(most_frequent_char("hello world"))
print(most_frequent_char("this world is beatiful"))     
print(most_frequent_char("jack is going to save the world???!!!!?!?!?"))
print(most_frequent_char("finish"))