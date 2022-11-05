person = {
    'liwakura' : {
        'first_name' : 'lain',
        'last_name' : 'iwakura',
        'age' : 14,
        'city' :  'tokyo',
        },

    'rayanami' : {
        'first_name' : 'rei',
        'last_name' : 'ayanami',
        'age' : 14,
        'city' :  'tokyo-3'
        },
    }

# for username, user_info in person.items():
#     print(f"\nUsername: {username}")
#     print(f"Full name: {user_info['first_name']} {user_info['last_name']}")
#     print(f"Age: {user_info['age']}")
#     print(f"Location: {user_info['city']}")


# 6.8

test = {
    'pitchula': {
        'owner': 'chad',
        'type': 'dog',   
    },
    'kyubi': {
        'owner': 'isaac',
        'type': 'cat',  
        
    },
    'frozen': {
        'owner': 'chika',
        'type': 'python',  
        
    },
    'glyph': {
        'owner': 'kaguya',
        'type': 'duck',   
    },
}

pets = []

pets.append(test)

# for pet in pets:
#     print(f"Ohayo, {pet}")

# 6.9
favorite_places = {
    'lain': {
        'places': 'room'
    },
    'rem': {
        'places': 'mansion'
    },
    'ram': {
        'places': 'mansion'
    }
}

# for name, place in favorite_places.items():
#     print(f"\nOhayo, {name}, what is your favorite place?")
#     print(f"{place['places']}")

# 6.10
test = {
    'debussy': [2,3,4],
    'satie': [2,6,8],
    'beethoven': [9,7,4],
    'mozart': [33,66,99],
    'fibonacci': [3,6,9],
    }

# for name, numbers in test.items():
#     print(f"\n{name} likes these numbers: ")
#     for number in numbers:
#         print(f"\t {number}")


# 6.11
cities = {
    'blumenau': {
        'population': '361,855',
        'country': 'santa catarina',
    },
    'goiania': {
        'population': '1.555.626',
        'country': 'goiás',
    },
    'sao paulo': {
        'population': '12.33M',
        'country': 'sao paulo',
    },
}

# for city, city_info in cities.items():
#     print(f"\nCity name: {city}")
#     print(f"Population: {city_info['population']}")
#     print(f"Country: {city_info['country']}")

    