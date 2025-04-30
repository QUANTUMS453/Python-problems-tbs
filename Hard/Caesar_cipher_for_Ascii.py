import string

ascii_chars = string.printable

print(ascii_chars)

def caesar_shift(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char in ascii_chars:
            idx = ascii_chars.index(char)
            if encrypt:
                shifted_idx = (idx + shift) % len(ascii_chars)
            else:
                shifted_idx = (idx - shift) % len(ascii_chars)
            result += ascii_chars[shifted_idx]
        else:
            result += char  # Leave unknown characters as-is
    return result

def main():
    while True:
        print("\n=== Caesar Cipher for ASCII ===")
        choice = input("Choose (e)ncrypt, (d)ecrypt, or (q)uit: ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice not in ('e', 'd'):
            print("Invalid choice. Try again.")
            continue

        text = input("Enter text: ")
        try:
            shift = int(input("Enter shift amount (e.g., 5): "))
        except ValueError:
            print("Shift must be a number.")
            continue

        result = caesar_shift(text, shift, encrypt=(choice == 'e'))
        print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
