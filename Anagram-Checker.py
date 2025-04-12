def is_anagram(str1: str, str2: str) -> bool:
    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()
    result = sorted(str1_clean) == sorted(str2_clean)
    print(f"is_anagram('{str1}', '{str2}') → {result}")
    return result


inp1 = input("enter the first string")
inp2 = input("enter the second string")

is_anagram(inp1, inp2)