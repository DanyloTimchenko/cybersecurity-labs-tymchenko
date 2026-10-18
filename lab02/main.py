
print("Лабораторна робота №2")
print("Порівняльний аналіз шифрів")
print("Розробник: Тимченко Данило")
print("-" * 45)


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            base = ord("A") if char.isupper() else ord("a")
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(key[key_index % len(key)]) - ord("a")

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
            key_index += 1
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(key[key_index % len(key)]) - ord("a")

            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
            key_index += 1
        else:
            result += char

    return result



message = "Information Security"
shift = 7

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Початковий текст:", message)
print("Ключ (зсув):", shift)
print("Зашифрований текст:", encrypted)
print("Розшифрований текст:", decrypted)
print("\nШифр Віженера")

key = "Tymchenko"
vigenere_result = vigenere_encrypt(message, key)
vigenere_decrypted = vigenere_decrypt(vigenere_result, key)

print("Початковий текст:", message)
print("Ключ:", key)
print("Зашифрований текст:", vigenere_result)
print("Розшифрований текст:", vigenere_decrypted)
