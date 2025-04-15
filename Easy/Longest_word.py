import string

def longest_word(str1: str) -> str:
    cleared = str1.split()
    cleaned_words = [word.strip(string.punctuation) for word in cleared]
    longest = max(cleaned_words, key=len)
    print(f"The longest word is: {longest}")
    return longest

# Example
longest_word("mammad is a good friend foor him and he should keep the friendship up......")
