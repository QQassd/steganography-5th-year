def encode_text(text, cyrillic_alphabet):
    # Function to encode text using the specified Cyrillic alphabet
    encoded_sequence = ""
    for char in text:
        found = False
        for bits, cyrillic_char in cyrillic_alphabet.items():
            if char == cyrillic_char:
                encoded_sequence += bits
                found = True
                break
        if not found:
            encoded_sequence += ""  # Placeholder for unknown characters
    return encoded_sequence

def main():
    cyrillic_alphabet = {
        '00011': 'А', '11001': 'Б', '01001': 'Г', '11001': 'Д',
        '00001': 'Е', '11110': 'Ж', '10001': 'З', '00110': 'И', '01011': 'Й',
        '01111': 'К', '10010': 'Л', '11100': 'М', '01100': 'Н', '11000': 'О',
        '10110': 'П', '01010': 'Р', '00101': 'С', '10000': 'Т', '00111': 'У',
        '01101': 'Ф', '10100': 'Х', '01110': 'Ц', '00100': 'Ч', '11010': 'Ш',
        '10100': 'Щ', '10011': 'В', '10101': 'Ы', '11101': 'Ь', '01101': 'Э',
        '01011': 'Ю', '10111': 'Я', '11111': ' ', '?': '?'
    }

    input_text = input("Enter the text to encode: ")

    try:
        # Encode the text using the specified Cyrillic alphabet
        encoded_sequence = encode_text(input_text, cyrillic_alphabet)

        # Print the encoded sequence
        print("Encoded sequence:", encoded_sequence)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()




def split_into_five_bits(text):
    # Function to split a string into sequences of 5 bits
    return [text[i:i+5] for i in range(0, len(text), 5)]

def decode_text(five_bit_sequences, cyrillic_alphabet):
    # Function to decode sequences of 5 bits using the specified encoding
    decoded_text = ""
    for bits in five_bit_sequences:
        if bits in cyrillic_alphabet:
            decoded_text += cyrillic_alphabet[bits]
        else:
            decoded_text += "?"  # Placeholder for unknown sequences
    return decoded_text

def main():
    cyrillic_alphabet = {
        '00011': 'А', '11001': 'Б', '01001': 'Г', '11001': 'Д',
        '00001': 'Е', '11110': 'Ж', '10001': 'З', '00110': 'И', '01011': 'Й',
        '01111': 'К', '10010': 'Л', '11100': 'М', '01100': 'Н', '11000': 'О',
        '10110': 'П', '01010': 'Р', '00101': 'С', '10000': 'Т', '00111': 'У',
        '01101': 'Ф', '10100': 'Х', '01110': 'Ц', '00100': 'Ч', '11010': 'Ш',
        '10100': 'Щ', '10011': 'В', '10101': 'Ы', '11101': 'Ь', '01101': 'Э',
        '01011': 'Ю', '10111': 'Я', '11111': ' ', '?': '?'
    }

    input_sequence = input("Enter the encoded sequence: ")

    try:
        # Split the sequence into sequences of 5 bits
        five_bit_sequences = split_into_five_bits(input_sequence)

        # Decode the sequences using the specified Cyrillic alphabet
        decoded_text = decode_text(five_bit_sequences, cyrillic_alphabet)

        # Print the decoded result
        print("Decoded text:", decoded_text)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
