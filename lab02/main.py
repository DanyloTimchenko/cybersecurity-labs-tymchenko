import secrets
import string
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


def generate_caesar_key():
    return secrets.randbelow(25) + 1


def generate_vigenere_key(length=10):
    alphabet = string.ascii_lowercase
    return "".join(secrets.choice(alphabet) for _ in range(length))


def personal_caesar_key(name, birth_year):
    data = name.lower() + str(birth_year)
    total = sum(ord(char) for char in data)
    return total % 25 + 1


def personal_vigenere_key(name, birth_year):
    letters = "".join(char for char in name.lower()
                      if char in string.ascii_lowercase)

    year = str(birth_year)
    year_letters = "".join(
        string.ascii_lowercase[int(digit)] for digit in year
    )

    return letters + year_letters


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
print("\nГенерація ключів")
print("Випадковий ключ Цезаря:", generate_caesar_key())
print("Випадковий ключ Віженера:", generate_vigenere_key())

print("\nПорівняння алгоритмів")
print("-" * 45)

caesar_key_count = 25
vigenere_key_count = 26 ** 10

print("Шифр Цезаря:")
print("Кількість можливих ключів:", caesar_key_count)

print("\nШифр Віженера:")
print("Довжина ключа: 10 символів")
print("Кількість можливих ключів:", vigenere_key_count)

print("\nРезультат порівняння:")
if vigenere_key_count > caesar_key_count:
    print("Простір ключів Віженера значно більший")
    print("Шифр Цезаря легко зламати повним перебором")

print("\nГенерація ключів на основі персональних даних")
print("-" * 45)

test_name = "Danylo"
test_year = 2006

personal_caesar = personal_caesar_key(test_name, test_year)
personal_vigenere = personal_vigenere_key(test_name, test_year)

print("Тестове ім'я:", test_name)
print("Тестовий рік народження:", test_year)
print("Ключ Цезаря:", personal_caesar)
print("Ключ Віженера:", personal_vigenere)

print("\nПеревірка персональних ключів")

personal_encrypted = caesar_encrypt(message, personal_caesar)
personal_decrypted = caesar_decrypt(personal_encrypted, personal_caesar)

print("Цезар - зашифровано:", personal_encrypted)
print("Цезар - розшифровано:", personal_decrypted)

personal_vig_encrypted = vigenere_encrypt(message, personal_vigenere)
personal_vig_decrypted = vigenere_decrypt(
    personal_vig_encrypted, personal_vigenere
)

print("Віженер - зашифровано:", personal_vig_encrypted)
print("Віженер - розшифровано:", personal_vig_decrypted)
