def has_unique_characters(str1: str) -> bool:
    empty_list = []
    str_new = list(str1.strip())  
    for letter in str_new:
        if letter in empty_list:
            print(f"the word: {str1}, is NOT!!!unique")  
            return False
        empty_list.append(letter)  
    
    print(f"the word: {str1}, is unique")  
    return True

#Example
has_unique_characters("great")
has_unique_characters("greenland")
has_unique_characters("greeting")
has_unique_characters("glad")