def count_vowels(str1: str) -> int:
    # Count 1 for each character in the string if it's a vowel (case-insensitive)
    result = sum(1 for char in str1 if char.lower() in "aeiou")
    
    # Print the result for debugging or visual confirmation
    print(result)
    
    return result

count_vowels("mammad is a good guy bro")
