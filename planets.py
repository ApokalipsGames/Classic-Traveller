# planetGen.py
# Random subsector/world generator for Classic Traveller

# variables
# name - string
# loc  - string from int, 0101 - 0810 (101-110, 201-210, 301-310 etc)
# upp  - array of objects ['A',0,0,0,0,0,0] 
# bases- string, single character
# notes- string
# zone - ' ', 'A' or 'R'
# gas  - ' ' or 'G'

import random

def intro():
    print("Sector Generator 1.0")
    print("A script for generating random sectors in Classic Traveller")
    print("- For when all that dice rolling is tedious.")
    print("\nCT defined the interstellar space in terms of sectors each")
    print("divided into 16 subsectors, each of which contained 8 columns")
    print("of 10 hexes representing 1 parsec (about 1.3 LY) of distance.\n")
    print(" A | B | C | D ")
    print("---+---+---+---")
    print(" E | F | G | H ")
    print("---+---+---+---")
    print(" I | J | K | L ")
    print("---+---+---+---")
    print(" M | N | O | P ")
    print("\nThis program will let you create sectors or subsectors filled")
    print("with worlds to explore, without all the tedium of dice and math.")
    return

def get_sector_info():
    density = []
    for ss in range(0,16):
        print("Enter the system density of subsector ["+chr(ss+65)+"]: ")
        density.append(int(input()))
    return density

def gen_upp():
    upp = []
    # starport type
    roll = roll_dice()
    if roll == 12: upp.append('X')
    elif roll == 11 or roll == 10: upp.append('E')
    elif roll == 9: upp.append('D')
    elif roll == 8 or roll == 7: upp.append('C')
    elif roll == 6 or roll == 5: upp.append('B')
    elif roll <= 4: upp.append('A')
    # size
    size = roll_dice()
    if size < 0: size = 0
    upp.append(size)
    # atmosphere
    atmo = roll_dice() - 7 + size
    if atmo < 0: atmo = 0
    upp.append(atmo)
    # hydrographics
    hydro = roll_dice() - 7 + atmo
    if hydro < 0: hydro = 0
    upp.append(hydro)
    # population
    ppl = roll_dice() - 2
    if ppl < 0: ppl = 0
    upp.append(ppl)
    # government
    govt = roll_dice() - 7 + ppl
    if govt < 0: govt=0
    upp.append(govt)
    # law level
    law = roll_dice() - 7 + govt
    if law < 0: law=0
    upp.append(law)
    # tech level
    tech = get_tech_level(upp)
    upp.append(tech)
    return upp

def get_tech_level(upp):
    tl = 0
    # from starport
    if upp[0] == 'A':
        tl += 6
    if upp[0] == 'B':
        tl += 4
    if upp[0] == 'C':
        tl += 2
    if upp[0] == 'X':
        tl -= 4
    # from size
    if upp[1] <= 1:
        tl += 2
    elif upp[1] <= 4 and upp[1] >= 2:
        tl += 1
    # from atm
    if upp[2] <= 3:
        tl += 1
    elif upp[2] >= 10:
        tl += 1
    # from hyd
    if upp[3] == 9:
        tl += 1
    if upp[3] == 10:
        tl += 2
    # from population
    if upp[4] >= 1 or upp[3] <= 5:
        tl += 1
    if upp[4] == 9:
        tl += 2
    if upp[4] == 10:
        tl +4
    # from govt
    if upp[5] == 0 or upp[4] == 5:
        tl += 1
    if upp[5] == 13:
        tl -= 2
    if tl < 0: tl = 0
    return convert_to_hexish(tl + random.randint(0,7))
    
def gen_bases(upp):
    bases = ''
    n = False
    s = False
    dm = 0
    # naval
    if upp[0] == 'A' or upp[0] == 'B':
        if roll_dice() >= 8:
            n = True
    # scout
    if upp[0] == 'C': dm -= 1
    elif upp[0] == 'B': dm -= 2
    elif upp[0] == 'A': dm -= 3
    if roll_dice() + dm >= 7: s = True
    if n==True and s==False:
        return 'N'
    elif s==True and n==False:
        return 'S'
    elif s==True and n==True:
        return 'A'
    else:
        return ' '

def gen_notes(upp):
    notes = ''
    if upp[2] >=4 and upp[2] <= 9:
        if upp[3] >= 4 and upp[3] <= 8:
            if upp[4] >= 5 and upp[4] <= 7:
                notes += 'Agricultural. '
    if upp[2] <= 3 and upp[3] <= 3 and upp[4] >= 6:
        notes += 'Non-Agricultural. '
    if (upp[2] >= 2 or upp[2] == 4 or upp[2] == 7 or upp[2] == 9) and upp[4] >= 9:
        notes += 'Industrial. '
    if upp[4] <= 6:
        notes += 'Non-Industrial. '
    if upp[2] == 6 or upp[2] == 8:
        if upp[4] >= 6 and upp[4] <= 8:
            if upp[5] >= 4 and upp[5] <= 9:
                notes += 'Rich. '
    if (upp[2] <= 2 and upp[2] >= 5) and upp[3] <= 3:
        notes += 'Poor. '
    if upp[3] == 10:
        notes += 'Water World. '
    if upp[2] >= 2 and upp[3] == 0:
        notes += 'Desert World. '
    if upp[2] == 0:
        notes += 'Vacuum World. '
    if upp[1] == 0:
        notes += 'Asteroid. '
    if (upp[2] <= 1 and upp[2] > 0) and upp[3] >= 1:
        notes += 'Ice Capped. '
    return notes

def gen_zone():
    return

def gen_gas():
    gas = ' '
    if roll_dice() <= 10: gas = 'G'
    return gas

def roll_dice():
    return random.randint(1,6) + random.randint(1,6)

def convert_upp_to_string(upp):
    upp_string = ''
    upp_string += upp[0]                    # starport
    upp_string += str(convert_to_hexish(upp[1])) # size
    upp_string += str(convert_to_hexish(upp[2])) # atmosphere
    upp_string += str(convert_to_hexish(upp[3])) # hydrographics
    upp_string += str(convert_to_hexish(upp[4])) # population
    upp_string += str(convert_to_hexish(upp[5])) # govt
    upp_string += str(convert_to_hexish(upp[6])) # law
    upp_string += "-"
    upp_string += str(upp[7]) # tech level
    return upp_string


def convert_to_hexish(value):
    if value == 10:
        return 'A'
    elif value == 11:
        return 'B'
    elif value == 12:
        return 'C'
    elif value == 13:
        return 'D'
    elif value == 14:
        return 'E'
    elif value >= 15:
        return 'F'
    else:
        return value
    return value

def format_world_data(name, location, upp, base, notes, gas):
    world_string = ''
    world_string += name + (' ' * (20 - len(name)))
    world_string += (' ' + location)
    world_string += (' ' + upp)
    world_string += (' ' + base)
    world_string += (' ' + notes + (' ' * (50 - len(notes))))
    world_string += (' ' + gas)
    return world_string

def get_density():
    density = 0
    print("Select a system density for the subsector:")
    print("\t1. Rift")
    print("\t2. Sparse")
    print("\t3. Normal")
    print("\t4. Dense")
    print("\t5. Core")
    while density < 1 or density > 5:
        density = int(input("Select 1-5: "))
    return density

def gen_sector(density):
    for ss in range(0,16):
        print("\nSubsector ["+chr(ss+65)+"]")
        for c in range(1,9):
            for r in range(1,11):
                if random.randint(1,6) <= density[ss]:
                    if r < 10:
                        location = '0' + str(c) + '0' + str(r)
                    else:
                        location = '0' + str(c) + str(r)
                    name = 'World-'+location
                    upp = gen_upp()
                    upp_str = convert_upp_to_string(upp)
                    bases = gen_bases(upp)
                    notes = gen_notes(upp)
                    gas = gen_gas()
                    upp_formatted = format_world_data(name, location, upp_str, bases, notes, gas)
                    print(upp_formatted)
    return

def main():
    intro()
    density = get_sector_info()
    gen_sector(density)

main()
