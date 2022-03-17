#problem1

dict1 = {
        'drink1' : 'Sprite',
        'drink2' : 'Coca-Cola',
        'drink3' : 'Fanta'}
print(dict1)


#problem2

user = dict

for i in range(3):
    name = input('Name: ')
    password = input('password: ')
    user[name] = password
    print(user)


#prolem3

dict3 = {'Бактияр' : 'Stamatolog',
        'Baha' : 'Fokusnik',
        'Tor' : 'Santehnik'}
for name , profession in dict3.items():
    print('Здраствуйте {}'.format(name), 'Прекраснвя професия {}'.format(profession))

#problem4
menu = {'lagman' : 120, 'plov' : '120' , 'borsh' : 100}
menu.update(besh_barmak = 130)
print(menu)

menu.update(lagman = 135)
print(menu)

del menu['borsh']
print(menu)

#problem5

south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
country = {}
for i, v in enumerate(set(south_american_countries)):
       country[i] = v
       print(country)




