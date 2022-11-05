# 7.8
# sandwich_orders = ['krabby patty',  'egg', 'roast beef']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"Im making your {current_sandwich} sandwich")
#     finished_sandwiches.append(current_sandwich)

# print(f"\nThis is yours sandwiches")
# for item in finished_sandwiches:
#     print("\t" + item.title())

# 7.9
# sandwich_orders = ['krabby patty',  'egg', 'roast beef']
# print("Your sandwich must be without pastrami.")
# i = 0
# while i < 3:
#     sandwich_orders.append('pastrami')
#     i+=1
# print(sandwich_orders)

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# 7.10
user_prompt = "\nWhat is your username? "
dream_prompt = "If you could visit one place in the world, where would you go? "
repeat_prompt = "\nWould you like to let someone else respond?(y/n) "
dreams = {}
flag = True

while flag:
    user = input(user_prompt)
    dream = input(dream_prompt)

    dreams[user] = dream

    repeat = input(repeat_prompt)
    if repeat == 'n':
        break

print("#### POLL ####")

for k,v in dreams.items():
    print(f"User: {k}")
    print(f"Dream: {v}\n")

    



        
        
        

