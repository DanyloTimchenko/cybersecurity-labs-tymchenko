
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

message = "Information Security"
shift = 7

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Початковий текст:", message)
print("Ключ (зсув):", shift)
print("Зашифрований текст:", encrypted)
print("Розшифрований текст:", decrypted)