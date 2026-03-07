dictionary = {
    "apple": "A fruit that is typically red, green, or yellow.",
    "banana": "A long curved fruit that grows in clusters and has soft, pulpy flesh and yellow skin when ripe.",
    "cherry": "A small, round stone fruit that is typically red or black.",
    "date": "A sweet fruit that grows on date palm trees, often dried and eaten as a snack."}

print (dictionary.items())
# print (dictionary.keys())
# print (dictionary.values())
# print (dictionary.get("banana"))
# print (dictionary.get("grape", "Not found in the dictionary"))
# print (dictionary.pop("cherry", "Not found in the dictionary"))

dict = { 
    "player" : 100,
    "player1" : 200
    }   
print(dict.items())
print(dict.keys()) # it wll print only key parts 
print("player1" in dict) # it will check the dict and return the bool value
print(dict.values()) #it will print the values of keys 


print(dict['player']) #if it founds in the dict it wll show the value of it
#print(dict['player0']) # it will show error in the program further prongram will not prosceed
print(dict.get("player1")) # if it founds int dict it will give value
print(dict.get("player2"))# if it not found it will show " none"


print(dict.get("player2","nothing found like it in your dictionary"))#it wil show thhe message as player2 is not in the dict if it were it wil show the value AS
print(dict.get("player","nothing found like it in your dictionary"))

my_dict = {"apple": 1, "banana": 2, "orange": 3}

# popitem method example, it is used to remove the last inserted item and return it as a tuple.
# Remove the last inserted item
removed_item = my_dict.popitem()
print(f"Removed item: {removed_item}")
print(f"Updated dictionary: {my_dict}")
# Try again
removed_item_2 = my_dict.popitem()
print(f"Removed item: {removed_item_2}")
print(f"Updated dictionary: {my_dict}")




#pop method exapmle it is used to remove the key and return the value of it. 
my_dict = {"apple": 1, "banana": 2, "orange": 3}

# Remove "banana" and get its value
removed_value = my_dict.pop("banana")
print(f"Removed value: {removed_value}")
print(f"Updated dictionary: {my_dict}")

# Try to remove a non-existent key with a default value
default_value = my_dict.pop("grape", "Not Found")
print(f"Default value returned: {default_value}")
print(f"Dictionary (unchanged): {my_dict}")