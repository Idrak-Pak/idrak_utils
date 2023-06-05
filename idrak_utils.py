from num2words import num2words
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Example menu items
# menu = ["zinger burger","chicken wings","pepsi ","2 litter pepsi","chicken fajita pizza","chicken supreme pizza"]

def find_most_similar(item='',array=[],threshold=60):
    '''
    To match item from menu or search over menu use this function
    If exact match not found it will return the most similar one

    ;params:
    item(str): query item
    array(list): possible menu or vocab to search
    threshold(int): how much things should be similar 

    return (most_similar_item, scores)
    '''
    # Calculate the similarity ratio between the search item and each menu item
    ratios = process.extract(item, array, scorer=fuzz.token_sort_ratio)

    # Sort the ratios in descending order
    ratios = sorted(ratios, key=lambda x: x[1], reverse=True)

    # Get the most similar menu item and its ratio
    most_similar = ratios[0]

    # Check if the similarity ratio is above a certain threshold
    if most_similar[1] >= 60:
        return most_similar[0],most_similar[1]
    else:
        return "Item not found",most_similar[1]


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
