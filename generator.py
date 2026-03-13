# generator.py
import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not chars:
        return "Error, no char selected."
    return "".join(random.choice(chars) for _ in range(length))

def main():
    print("=== Password Generator ===")
    length = int(input("Lenght: "))

    print("Add:")
    use_letters = input("letters? (y/n): ").lower() == 'y'
    use_digits = input("numbers? (y/n): ").lower() == 'y'
    use_symbols = input("symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print("\n LNew Password:\n" + password)

    save = input("\n Save the password? (y/n): ").lower() == 'y'
    if save:
        with open("passwords.txt", "a") as f:
            f.write(password + "\n")
        print("Saved in passwords.txt")

if __name__ == "__main__":
    main()
