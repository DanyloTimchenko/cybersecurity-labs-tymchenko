
from PIL import Image

print("Лабораторна робота №3")
print("Тема: Невидимі дані у власних файлах")
print("Розробник: Тимченко Данило")
print("-" * 45)

def open_image(filename):
    image = Image.open(filename)
    print("Зображення успішно відкрито")
    print("Розмір:", image.size)
    print("Формат:", image.format)
    return image

print("\nПеревірка відкриття зображення:")
image = open_image("стол.webp")
