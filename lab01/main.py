print("Аналізатор безпеки паролів")
print("Лабораторна робота №1")
print("Розробник: Тимченко Данило")
print("-" * 40)

password = input("Введіть тестовий пароль: ")

length = len(password)

print(f"Довжина пароля: {length} символів")

if length < 8:
    print("Пароль занадто короткий")
elif length < 12:
    print("Рекомендується збільшити довжину пароля")
else:
    print("Пароль має достатню довжину")

print("\nПеревірка символів:")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

print("Великі літери:", "Так" if has_upper else "Ні")
print("Малі літери:", "Так" if has_lower else "Ні")
print("Цифри:", "Так" if has_digit else "Ні")
print("Спеціальні символи:", "Так" if has_special else "Ні")
