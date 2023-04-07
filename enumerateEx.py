names = ['Peter','Clark', 'Wade', 'Bruce']
heroes = ['spiderman', 'Superman','Deadpool','Batman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')
    #Other way of printing
    #print(name, ' is actually ', hero)
    #print("{} is actually {}".format(name, hero))