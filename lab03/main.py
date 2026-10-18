
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

def hide_message(image, message, output_file):
    image = image.convert("RGB")

    message_bytes = message.encode("utf-8")
    message_length = len(message_bytes)

    data = message_length.to_bytes(4, "big") + message_bytes
    binary_message = "".join(
        format(byte, "08b") for byte in data
    )

    pixels = list(image.get_flattened_data())

    if len(binary_message) > len(pixels) * 3:
        print("Помилка: повідомлення занадто велике")
        return

    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        new_pixel = []

        for color in pixel:
            if bit_index < len(binary_message):
                color = (color & 254) | int(binary_message[bit_index])
                bit_index += 1

            new_pixel.append(color)

        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)
    image.save(output_file, "PNG")

    print("Повідомлення успішно приховано")
    print("Файл збережено:", output_file)

image = open_image("стол.webp")

message = "Тимченко Данило Олексійович\nДата народження: 22.08.2006"

print("\nПриховування повідомлення методом LSB:")
hide_message(image, message, "hidden_message.png")

