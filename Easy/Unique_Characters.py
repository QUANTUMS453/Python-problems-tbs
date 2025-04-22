def has_unique_characters(str1: str) -> bool:
    empty_list = []  # Store seen characters
    str_new = list(str1.strip())  # Remove leading/trailing spaces and convert to list
    
    for letter in str_new:
        if letter in empty_list:
            print(f"the word: {str1}, has not unique characters!!!!!!")  
            return False
        empty_list.append(letter)  # Add new character to the seen list
    
    print(f"the word: {str1}, has unique characters")  
    return True

# Examples
has_unique_characters("great")
has_unique_characters("greenland")
has_unique_characters("greeting")
has_unique_characters("glad")