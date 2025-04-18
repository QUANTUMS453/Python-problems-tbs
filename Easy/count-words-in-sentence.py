def count_words(sentence: str) -> int:

    # Split the sentence into words using default split (handles multiple spaces)
    new_sentence = sentence.split()

    # Count the number of words
    result = len(new_sentence)
    print(result)
    return result



count_words("this is a test sentence")