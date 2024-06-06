def split_into_eight_bits(text):
    # Function to split a string into sequences of 8 bits
    return [text[i:i+8] for i in range(0, len(text), 8)]

def decode_text(eight_bit_sequences, encoding):
    # Function to decode sequences of 8 bits using the specified encoding
    return ''.join([bytes([int(bits, 2)]).decode(encoding, errors='replace') for bits in eight_bit_sequences])

def main():
    input_file = input("Enter the name of the file with the text: ")

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            line = file.readline().strip()

        # Split the line into sequences of 8 bits
        eight_bit_sequences = split_into_eight_bits(line)

        # Decode the sequences using Windows-1251, CP866, and KOI8-R encodings
        decoded_windows_1251 = decode_text(eight_bit_sequences, 'windows-1251')
        decoded_cp866 = decode_text(eight_bit_sequences, 'cp866')
        decoded_koi8r = decode_text(eight_bit_sequences, 'koi8-r')

        # Print the decoded results
        print("Decoded with Windows-1251:", decoded_windows_1251)
        print("Decoded with CP866:", decoded_cp866)
        print("Decoded with KOI8-R:", decoded_koi8r)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
