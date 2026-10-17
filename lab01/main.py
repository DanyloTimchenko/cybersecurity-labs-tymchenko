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

print("\nПеревірка особистих даних:")

name = input("Введіть тестове ім'я: ")
birth_year = input("Введіть тестовий рік народження: ")

has_name = bool(name) and name.lower() in password.lower()
has_year = bool(birth_year) and birth_year in password


if has_name:
    print("Увага! Пароль містить ім'я")
else:
    print("Ім'я в паролі не знайдено")

if has_year:
    print("Увага! Пароль містить рік народження")
else:
    print("Рік народження в паролі не знайдено")

print("\nОцінка надійності пароля:")

score = 1

if length >= 8:
    score += 1

if length >= 12:
    score += 2

if length >= 16:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 2

if has_name:
    score -= 2

if has_year:
    score -= 2

score = max(1, min(score, 10))

print(f"Оцінка пароля: {score}/10")

if score <= 3:
    print("Рівень безпеки: Низький")
elif score <= 6:
    print("Рівень безпеки: Середній")
elif score <= 8:
    print("Рівень безпеки: Високий")
else:
    print("Рівень безпеки: Дуже високий")

print("\nРекомендації щодо покращення пароля:")

recommendations = []

if length < 12:
    recommendations.append("Збільште довжину пароля до 12 символів або більше")

if not has_upper:
    recommendations.append("Додайте великі літери")

if not has_lower:
    recommendations.append("Додайте малі літери")

if not has_digit:
    recommendations.append("Додайте цифри")

if not has_special:
    recommendations.append("Додайте спеціальні символи")

if has_name:
    recommendations.append("Не використовуйте власне ім'я у паролі")

if has_year:
    recommendations.append("Не використовуйте рік народження у паролі")

if recommendations:
    for recommendation in recommendations:
        print("-", recommendation)
else:
    print("Основні вимоги виконано. Використовуйте унікальний пароль для кожного акаунта")
