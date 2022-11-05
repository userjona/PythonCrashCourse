#3.4
waifus = ['Emilia','Lain','Filo-chan']
 print(f'Hello, {waifus[0]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[1]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[2]}, do you want to have a dinner with me?')

#3.5
 print(f'{waifus[2]} cannot attend.')
del waifus[2]
waifus.append('Rei Ayanami')

 print(f'Hello, {waifus[0]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[1]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[2]}, do you want to have a dinner with me?')

#3.6
waifus.insert(0, 'Chika Fujiwara')
waifus.insert(2, 'Kaguya Shinomiya')
waifus.append('Rem')

 print(f'Hello, {waifus[0]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[1]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[2]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[3]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[4]}, do you want to have a dinner with me?')
 print(f'Hello, {waifus[5]}, do you want to have a dinner with me?')

#3.7
print("I can only invite two people, unfortunately")
print()
print(f"{waifus.pop(0)}, sorry for this.")
print(f"{waifus.pop(0)}, sorry for this.")
print(f"{waifus.pop(0)}, sorry for this.")
print(f"{waifus.pop(-1)}, sorry for this.")
print()
print(f"{waifus[0]}, You are still invited to go out with me.")
print(f"{waifus[1]}, You are still invited to go out with me.")

del waifus[0:]

print(waifus)

