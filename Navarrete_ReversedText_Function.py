def reverse_text():
    user_input = input("Enter a word or phrase: ")

    if user_input.isalpha() or user_input.isspace():
        reversed_text = ' '.join(word[::-1] for word in user_input.split())
        print(f"Reversed text: {reversed_text}")
    else:
        print("Error! Please input a valid text.")
        reverse_text()

# Call the function to start the program
reverse_text()
