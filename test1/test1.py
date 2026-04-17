'''
1) Vytvoří tři smysluplně pojmenované proměnné: jednu typu String (např. jméno), jednu typu Integer nebo Float (např.
věk nebo výška) a jednu typu Boolean (např. informace, zda má uživatel rád programování).

2) Vytvoří prázdný seznam (list).

3) Pomocí správné metody tyto tři proměnné do seznamu postupně přidá.'''

# name = "Karel"
# age = 5
# is_programmer = True
#
#
# mix = []
# mix.append(name)
# mix.append(age)
# mix.append(is_programmer)
#
# print(mix)
#
# print(mix[1])
#
# future_age = 10 + age
#
# print(f"{name} will be {future_age} old.")
#
# print(f"{name} will be "+str(future_age)+" old.")
#
# if future_age % 2 == 0:
#     print(f"{future_age} is even number.")
# else:
#     print(f"{future_age} is odd number.")
#
# friends_age = [12, 17, 16]
#
# for i in range(len(friends_age)):
#     friends_age[i] = friends_age[i] + 1
# print(friends_age)
#
# karel_age = 10
#
# while karel_age < 18:
#     karel_age += 1
#     print(karel_age)
#     if karel_age >= 13 and karel_age < 18:
#         print(f"Karel is teenager: {karel_age}")

# visitors = [12, 16, 15, 20, 17]
# for visitor in visitors:
#     if visitor < 13:
#         print(f"age {visitor}, skipping kid")
#         continue
#     if visitor >= 18:
#         print(f"age {visitor}, Adult found")
#         break
# else:
#     print("Search finished.")

vip_guests = ["Alice", "Bob", "Charlie"]
my_str = ", ".join(vip_guests)
print(my_str)

from random import shuffle, choice
print(vip_guests)
lucky_guest = choice(vip_guests)
print(lucky_guest)
shuffle(vip_guests)
print(vip_guests)
print(vip_guests[0])