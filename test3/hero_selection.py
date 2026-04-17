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