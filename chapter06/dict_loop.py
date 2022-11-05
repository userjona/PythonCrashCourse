# 6.4
champions = {'Fiora':'Duelist', 'Riven':'Duelist', 'Vayne':'Marksman', 'Draven':'Marksman', 'Ornn':'Tank'}
champions['Ezreal'] = 'Marksman'
champions['Veigar'] = 'Mage' 
champions['Annie'] = 'Mage'
champions['Kassadin'] = 'Mage'
champions['Talon'] = 'Assassin'
champions['Le Blanc'] = 'Mage'
# [print(f"{k}: {v} \n") for k,v in champions.items()]

# 6.5
rivers = {'amazonas' : 'brasil', 'neva' : 'são petesburgo', 'ganges':'india'}

# for i in rivers.keys():
#     if 'amazonas' in i:
#         print(f'O Rio {i.capitalize()} beneficia quem vive no Acre, Amazonas, Roraima, Rondônia, Mato Grosso, Pará e Amapá.\n')
#     elif 'neva' in i:
#         print(f'Durante a Idade Média o largo e navegável rio {i.capitalize()} teve grande importância na ligação entre as regiões do Báltico e do Volga.\n')
#     elif 'ganges' in i:
#         print(f'A poluição do {i.capitalize()} tem afetado as 400 milhões de pessoas que vivem próximas de suas águas.\n')

# for i in rivers.keys():
#     print(i)

# print()

# for i in rivers.values():
#     print(i)

# 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

favorite_languages['michael'] = ''
favorite_languages['lain'] = ''

for k,v in favorite_languages.items():
    if len(v) != 0:
        print(f"{k.title()}, thanks for responding.")
    else:
        print(f"{k.title()}, please tell us what is your favorite language.")
