# Idrak Text Utils

## Requirments

```
pip install -r requirments.txt
```

## Ussage

```
from idrak_utils import convert_numbers_to_words

string = "House 89, Ward 6 Rawalpindi"
converted_string = convert_numbers_to_words(string)
print(converted_string)



----------------------------------------------------------
docs: 
item(str): query item
array(list): possible menu or vocab to search
threshold(int): how much things should be similar 
return (most_similar_item, scores)

from idrak_utils import find_most_similar

search_item = "chkn wings"
menu = ["zinger burger","chicken wings","pepsi ","2 litter pepsi","chicken fajita pizza","chicken supreme pizza"]

result = find_most_similar(search_item,menu,60)
print(result)



result==> ('chicken wings', 87)

```