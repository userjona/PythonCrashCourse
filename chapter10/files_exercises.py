# 10.3 Guest
filename = 'guest.txt'
bookname = 'guest_book.txt'

# with open(filename, 'w') as username:
#     file = username.write(user)

# 10.4 Guest Book
bool = True
userbook = []
user_prompt = "Your name: "
repeat_prompt = "One more name? (y/n)"
# while bool:
#     user = input(user_prompt)
#     print(f"Hello, {user.capitalize()}!")
#     repeat = input(repeat_prompt)

#     userbook.append(user)

#     if repeat.lower() == 'n':
#         break
        
# with open(bookname, 'a') as username:
#     for item in userbook:
#         username.write(f"{item.capitalize()}\n")

# 10-6 Addition
# try:
#     x = int(input())
#     y = int(input())
#     print(x, y)
# except ValueError:
#     print("Please, enter a number.")

# 10-7 Addition Calculator
# active = True
# while active:
#     try:
#         x = int(input())
#         y = int(input())
#         print(x, y)
#     except ValueError:
#         print("Please, enter a number.")

# 10-8 Cats and Dogs
# filename = 'dogs.txt'

# try:
#     with open(filename, 'r') as f:
#         contents = f.read()
#         print(contents)
# except FileNotFoundError:
#     print(f"This file:{filename} doensn't exist.")

# 10-9 Silent Cats and Dogs
# filename = 'dogs.txt'

# try:
#     with open(filename, 'r') as f:
#         contents = f.read()
#         print(contents)
# except FileNotFoundError:
#     pass
    
# 10-10 Common Words
filename = 'gutenberg.txt'

# try:
#     with open(filename, encoding='UTF-8') as f:
#         line = f.read()
        
#         print(line.lower().count('the '))
# except FileNotFoundError:
#     pass

# 10-11 Favorite Number
import json

def get_favorite_number():
    number = input("Enter your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)

def read_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        None
    else:
        print(number)

# 10-12 Favorite Number Remembered
filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Enter your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(number)

# 10-13 Verify User
# def greet_user():
#     """Greet the user by name"""
#     username = get_stored_username()
#     if username:
#         verify = input(f"Are you? {username} (y/n)")
#         if verify == 'y':
#             print(f"Welcome back, {username}")
#         else:
#             username = get_new_username()
