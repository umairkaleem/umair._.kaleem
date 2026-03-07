# name = "Umair Kaleem"
# print (len(name))  # This will print the length of the string

# print (name.endswith("eem"))  # This will check if the string ends with "eem"
# print (name.casefold())  # This will convert the string to lowercase
# print (name.center(20, '*'))  # This will center the string within 20 characters, padding with '*'

# print (name.replace("Umair","Uzair"))  # This will replace "Uamir" with "Uzair"
# print (name.split(" "))  # This will split the string into a list at each space

# print("This will trigger a system bell sound:\a")

name = input("Enter your name: ")
product = input("Enter the product name: ")
message = f"Dear {name}, thank you for purchasing {product}."
print (message)

message = '''Dear <|name|>
Thank you for your purchase of <|product|>. We hope you enjoy it!
Best regards,'''
print (message.replace("<|name|>",name).replace("<|product|>", product))