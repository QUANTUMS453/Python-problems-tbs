def reverse_sentence(sentence: str) -> str:
    new_sentence = sentence.split(" ") # Split the sentence into a list of words
    new_sentence.reverse() # Reverse the list in-place
    result = " ".join(new_sentence) # Join the reversed words into a new sentence
    print(result)
    return result


#Example
reverse_sentence("mammad is the biggest fan of you")