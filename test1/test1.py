# from turtle import Turtle, done
# t=Turtle()
#
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# done()

# from turtle import Turtle # obecny ctverec definovany manualne
#
# julie = Turtle()
#
# def square(side):
#     for i in range(4):
#         julie.forward(side)  # jde dopredu o side
#         julie.left(90)       # zahne o 90stupnu
#
# square(200)

# from turtle import Turtle #obecny pentagon
# julie = Turtle()
#
# def pentagon(side):
#     for i in range(5):
#         julie.forward(side)
#         julie.left(72)
#
# pentagon(100)

# from turtle import Turtle #obecny mnohouhelnik
#
# julie = Turtle()
#
# def polygon(pocet_stran, delka_strany):
#
#     uhel = 360 / pocet_stran
#
#     for i in range(pocet_stran):
#         julie.forward(delka_strany)
#         julie.left(uhel)  # Želva zatočí o námi spočítaný úhel
#
# polygon(pocet_stran=7, delka_strany=50)
# polygon(pocet_stran=5, delka_strany=100)

#opilec na ceste

from random import randint

def drunkman_simulator(size, steps):

    pozice = size // 2 # 1. Opilec začíná přesně v polovině cesty

    # Smyčka pro každý krok
    for i in range(steps):
        # 2. Vykreslení aktuální situace na ulici (tohle jsem ti připravil, to bývá pro začátečníky těžké)
        leva_ulice = ". " * (pozice - 1)
        prava_ulice = " ." * (size - pozice - 1)
        print(f"home {leva_ulice}*{prava_ulice} pub")

        krok = randint(0, 1) # 3. Hození mincí (Náhodný krok)

        if krok == 0:
            pozice = pozice - 1
        else:
            pozice = pozice + 1

        if pozice == 0:
            print("Doma!")
            break
        elif pozice == size:
            print("Zase v hospode!")
            break
    if pozice != 0 and pozice != size:
        print("Opilec usnul na ulici!")

# Zkušební spuštění (velikost 10, max 100 kroků)
drunkman_simulator(10, 100)