# Importing necessary Modules
from logo import art
from quotes_module import birthday_quotes, famous_quotes
import random  # Import the random module

# Logo display
print(art)

# Welcome Message
print("HELLO WELCOME TO TIFE QUOTES")

# Setting a bridge
print('+-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+')

# Title
print("Select your 'quote choice below: ")
quotes ={
    "1" : "Birthday quote",
    "2" : "Famous quote"
}

# Displaying quote choices
for key, value in quotes.items():
    print(f"{key}. {value}")

# User input for quote choice
user_choice = input("Enter the number corresponding to your choice: ")

# Function to display a random quote
def display_random_quote(quote_list):
    if quote_list:
        print("Here is a random quote:")
        random_quote = random.choice(quote_list)
        print(random_quote)
    else:
        print("No quotes available.")

# Function to display the selected quote
def display_quote(quote_type):
    if quote_type == "1":
        # Birthday quote logic
        display_random_quote(birthday_quotes)
    elif quote_type == "2":
        # Famous quote logic
        display_random_quote(famous_quotes)
    else:
        print("Invalid choice. Please enter a valid number.")

# Call the function to display the selected quote
display_quote(user_choice)
