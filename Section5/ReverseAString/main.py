# Reverse a string

def reverse_string(input_text: str):
    reversed_string = ""
    for index in range(len(input_text) - 1, -1, -1):
        reversed_string = reversed_string + input_text[index]
    return reversed_string


text = input("Please enter a string: ")
print(reverse_string(text))
