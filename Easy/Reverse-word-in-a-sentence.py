def reverse_sentence(sentence: str) -> str:
    new_sentence = sentence.split(" ")
    new_sentence.reverse()
    result = " ".join(new_sentence)
    print(result)



reverse_sentence("mammad is the biggest fan of you")