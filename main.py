# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}
def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse += morse_code_dict[char] + ' '
        else:
            morse += ' '
    return morse.strip()
def morse_to_text(morse):
    text = ''
    morse_chars = morse.split(' ')
    for code in morse_chars:
        for letter, morse_code in morse_code_dict.items():
            if code == morse_code:
                text += letter
                break
        else:
            text += ' '
    return text
def main():
    print("Welcome to Morse Code Translator!")
    while True:
        choice = input("Type 1 for English to Morse Code or 2 for Morse Code to English: ")

        if choice == '1':
            text = input("Enter text to translate to Morse code: ")
            print("Morse Code:", text_to_morse(text))
            break

        # Perform Morse Code to English Translation
        elif choice == '2':
            morse = input("Enter Morse code to translate to English (separate letters with spaces): ")
            print("English:", morse_to_text(morse))
            break

        else:
            print("Invalid choice, please choose 1 or 2.")
            continue
if __name__ == "__main__":
    main()