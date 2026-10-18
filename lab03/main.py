
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


def extract_message(filename):
    image = Image.open(filename).convert("RGB")
    pixels = list(image.get_flattened_data())

    binary_data = ""

    for pixel in pixels:
        for color in pixel:
            binary_data += str(color & 1)

    if len(binary_data) < 32:
        print("Помилка: зображення занадто мале")
        return None

    message_length = int(binary_data[:32], 2)

    if message_length > (len(binary_data) - 32) // 8:
        print("Помилка: некоректна довжина повідомлення")
        return None

    message_bits = binary_data[32:32 + message_length * 8]

    message_bytes = bytes(
        int(message_bits[i:i + 8], 2)
        for i in range(0, len(message_bits), 8)
    )

    try:
        message = message_bytes.decode("utf-8")
        return message
    except UnicodeDecodeError:
        print("Помилка: не вдалося декодувати повідомлення")
        return None


print("\nПеревірка відкриття зображення:")
image = open_image("стол.webp")

message = "Тимченко Данило Олексійович\nДата народження: 22.08.2006"

print("\nПриховування повідомлення методом LSB:")
hide_message(image, message, "hidden_message.png")

print("\nВитягування прихованого повідомлення:")
extracted_message = extract_message("hidden_message.png")

if extracted_message is not None:
    print("Відновлений текст:")
    print(extracted_message)

    if extracted_message == message:
        print("\nПеревірка успішна: повідомлення збігаються")
    else:
        print("\nПомилка: повідомлення не збігаються")
