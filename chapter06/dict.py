# 6.1
person = {'first_name' : 'lain', 'last_name' : 'iwakura', 'age' : 14, 'city' :  'tokyo'}

for key,value in person.items():
    print(key +': ', end='')
    print(value)

# 6.2
test = {'debussy': 1, 'satie': 2, 'beethoven': 9, 'mozart': 33, 'fibonacci': 369}
print()
print(f"Debussy : {test['debussy']}")
print(f"Satie : {test['satie']}")
print(f"Beethoven : {test['beethoven']}")
print(f"Mozart : {test['mozart']}")
print(f"Fibonacci : {test['fibonacci']}")
    
