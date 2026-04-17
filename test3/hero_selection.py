import random
'''hero faze 1'''

power_levels = [8, 15, 12, 22, 9]
heroes = []

for level in power_levels:
    if level < 10:
        print(f'{level} is too weak, skip')
        continue
    elif level >= 20:
        print(f'{level} is strong, superhero found!')
        break
    else:
        heroes.append(level)
else:
    print('Recruitment of candidates has ended.')

'''hero faze 2'''

hero_power = heroes[0]
print(hero_power)

while hero_power < 20:
    hero_power += 1
    if hero_power % 2 == 0:
        print(f"Training: level {hero_power} reached - Strength bonus gained!")
    else:
        print(f"Training: level {hero_power} reached")

'''hero faze 3'''
names = ["Karel", "Alice", "Bob"]
our_company = ", ".join(names)
print(our_company)
boss = random.choice(names)
print(f"The boss is {boss}.")