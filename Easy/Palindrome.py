def is_palindrome(string1: str) -> bool:
    # Convert to lowercase and remove spaces
    cleaned = string1.lower().replace(" ", "")
    
    # Reverse the cleaned string
    reversed_str = cleaned[::-1]
    
    # Compare the cleaned string with its reverse
    result = (cleaned == reversed_str)
    
    print(f"Is Palindrome: {result}")
    
    return result

# thanks to chat gpt for it's example XD"
is_palindrome("a man a plan a canal Panama")
