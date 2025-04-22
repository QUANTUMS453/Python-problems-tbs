def most_frequent_char(string1: str) -> str:
    counts = {}
    clean_str = list(string1.strip(""))
    for letter in clean_str:
        if letter != " ":
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    

    maximum = max(counts.values())

    for key, value in counts.items():
        if value == maximum:
            return key



print(most_frequent_char("hello world"))

print(most_frequent_char("aabbbccdd"))
