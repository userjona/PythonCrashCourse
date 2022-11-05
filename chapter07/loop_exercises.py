# 7.4
 while True:
     message = input("\nEnter the desired topping: ")
     if message == 'quit':
         break
     else:
         print(f"you'll add {message}")
         continue

# 7.5
 while True:
     prompt = int(input("How old are you?\n"))

     if prompt < 3:
         print("The ticket is free for this child")
     elif prompt >= 3 and prompt < 12:
         print("The ticket cost $10")
     else:
         print("The ticket cost $15")

# 7.6
 count = 0
 while True:
     prompt = int(input("\nHow old are you?\n"))
     count += 1

     if prompt < 3:
         print("\nThe ticket is free for this child")
     elif prompt >= 3 and prompt < 12:
         print("\nThe ticket cost $10")
     else:
         print("\nThe ticket cost $15")
    
     if count == 3:
         break

# 7.7
while True:
    print("1")




    


