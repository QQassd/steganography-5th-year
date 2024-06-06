def encode_text_to_bits(text, encoding):
    encoded_bytes = text.encode(encoding)
    encoded_bits = ''.join(format(byte, '08b') for byte in encoded_bytes) # windows - 1251
    return encoded_bits



def count_ones_and_zeros(binary_string):
    ones_count = binary_string.count('1')
    zeros_count = binary_string.count('0')
    return ones_count, zeros_count

def main():
    file_path = input("Введите путь к текстовому файлу: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Читаем строки из файла
            for line in lines:
                encoded_sequence = encode_text_to_bits(line.strip(), 'windows-1251')  # Убираем лишние символы
                ones_count, zeros_count = count_ones_and_zeros(encoded_sequence)
                if ones_count > zeros_count:
                    print(f"да --> 1 (Строка: {line.strip()})")
                else:
                    print(f"нет --> 0 (Строка: {line.strip()})")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print("Произошла ошибка:", e)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
