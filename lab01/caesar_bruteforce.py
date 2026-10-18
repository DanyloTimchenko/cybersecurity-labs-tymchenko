print("Лабораторна робота №2")
print("Завдання 3. Злам шифру Цезаря")
print("Розробник: Тимченко Данило")
print("-" * 45)

encrypted_text = "Pumvythapvu Zljbypaf"

for shift in range(1, 26):
    decrypted_text = ""

    for char in encrypted_text:
        if char.isalpha() and char.isascii():
            base = ord("A") if char.isupper() else ord("a")
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char

    print(f"Зсув {shift:2}: {decrypted_text}")