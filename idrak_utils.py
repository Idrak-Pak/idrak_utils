from num2words import num2words
import re

def convert_numbers_to_words(string):
    words = []
    for word in re.findall(r'\b\w+\b', string):
        if word.isdigit():
            words.append(num2words(int(word)))
        else:
            words.append(word)
    return ' '.join(words)

# Example usage
string = "House 89, Ward 6 Talagang"
converted_string = convert_numbers_to_words(string)
print(converted_string)
