# 8.1
from ast import arg


def display_message():
    print("Hi, everyone! I learned aan introduction to functions.")

# display_message()

# 8.2
def favorite_book(title):
    print(f"\nThis is my favorit book: {title.title()}")

# favorite_book("Alice in Wonderland")

# 8.3

def make_shirt(size, message):
    print(f"Size: {size} - Messaged printed: {message}")

# make_shirt('large', "supreme")
# make_shirt(message='gucci', size='medium')

# 8.4
def make_shirt(size='large', message='I love Python'):
    print(f"\nSize: {size} - Messaged printed: {message}")

# make_shirt()
# make_shirt(size='medium')
# make_shirt('extra', 'I want to learn Math')


# 8.5
def describe_city(city_name, country='japan'):
    print(f"{city_name} is in {country}")

# describe_city('tokyo')
# describe_city('zurich', 'switzerland')
# describe_city('kyoto')

# 8.6
def city_country(city_name, country):
    return print(f"{city_name}, {country}")

# city_country('Santiago','Chile')

# 8.7
def make_album(artist_name, album_title):
    music_album = {
        'artist' : artist_name,
        'album' : album_title,
    }
    return music_album

# print(make_album('дора', 'MISS'))
# print(make_album('Paramore', '!Riot'))
# print(make_album('RHCP', 'Unlimited Love'))

# 8.8
def make_album(artist_name, album_title):
    music_album = {
        'artist' : artist_name,
        'album' : album_title,
    }
    return music_album

art = "Name of artist: "
alb = "name of album: "

# print("Type 'q' if want to leave!")

# while True:
#     album = input(alb)
#     if album == 'q': 
#         break

#     artist = input(art)
#     if artist == 'q':
#         break

#     album = make_album(artist, album)
#     print(album)


# 8.9

# lista = ['Hello','my','name','is']

# def show_messages(lists):
#     for list in lists:
#         print(list)

# show_messages(lista)

# 8.10
message = ['Hello','my','name','is']
sent_message = []

def show_messages(lists):
    for list in lists:
        print(list)

def send_messages(message, sent_message):
    i = 0
    while message:
        if i == 3:
            i = 0
        i +=1
        current_message = message.pop()
        print("Your message is being sent", end='')
        print('.' * i)
        sent_message.append(current_message)

# send_messages(message, sent_message)

# print("##### MESSAGE SENT #####")
# print(message)
# print(sent_message)

# 8.11
message = ['Hello','my','name','is']
sent_message = []

def show_messages(lists):
    for list in lists:
        print(list)

def send_messages(message, sent_message):
    i = 0
    while message:
        if i == 3:
            i = 0
        i +=1
        current_message = message.pop()
        print("Your message is being sent", end='')
        print('.' * i)
        sent_message.append(current_message)

# send_messages(message[:], sent_message)

# print("##### MESSAGE SENT #####")
# print(message)
# print(sent_message)

# 8.12
def build_sandwich(*args):
    print("\nMaking a sandwich:")
    for sandwitch in args:
        print(f' - {sandwitch}')

# build_sandwich('krabby patty', 'egg', 'x-bacon')
# build_sandwich('grilled cheese', 'chicken', 'ham sandwich')
# build_sandwich('nutella sandwich', 'roast beef', 'seafood')

# 8.13
def build_profile(first, last, **args):
    args['first_name'] = first
    args['last_name'] = last
    return args

me = build_profile('johnathan', 'ferreira',
            location = 'goiania',
            field = 'idk',
            music = 'ecletic',)

# print(me)

# 8.14
def make_car(manufacturer, model_name,  **args):
    car_builder = {
        'manufacturer': manufacturer,
        'model': model_name
    }
    
    for arg, value in args.items():
        car_builder[arg] = value

    return car_builder

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)