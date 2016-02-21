# barbarian.py
# module for Marines characters

import random
import math

# attributes
service = "Barbarian"
ranks = ["", "Warrior", "Warrior", "Warrior", "Warrior", "Chief", "Chief"]
muster_out_benefits = ["Low Psg", "Blade", "Blade",
                       "Blade", "'", "High Psg", "High Psg"]
muster_out_cash = [0, 0, 1000, 2000, 3000, 4000, 5000]

skills = [["Str", "Str", "Str", "Carousing", "Dex", "End"],  # pdt
          ["Brawling", "Blade Cbt", "Blade Cbt", "Bow Cbt", "Bow Cbt", "Gun Cbt"],  # sst
          ["Blade Cbt", "Mechanical", "Survival", "Recon", "Streetwise", "Bow Cbt"],  # aed
          ["Medical", "Interrogation", "Tactics", "Leader", "Instruction", "Jack-o-T"]]  # ed8+


# functions
def enlistment(upp):
    print("Attempting to join a {} tribe.".format(service))
    dm = 0
    if upp[2] >= 9:
        dm += 1
    if upp[0] >= 10:
        dm += 2
    if roll_two_dice() + dm >= 5:
        print("Your attempt to join the {} horde was accepted!".format(service))
        return True
    else:
        print("Your attempt to join the {} horde was denied.".format(service))
        return False


def survival(upp):
    dm = 0
    if upp[0] >= 8:
        dm += 2
    if roll_two_dice() + dm >= 6:
        print("You survived four years fighting for the horde!")
        return True
    else:
        print("You were injured during a raid and forced to retire.")
        return False


def commission(upp):
    dm = 0
    if upp[4] >= 9:
        dm += 1
    if roll_two_dice() + dm >= 9:
        print("You were elevated above the rest. Congratulations!")
        print("Your rank is now {}.".format(ranks[1]))
        return True
    else:
        print("You were not granted a commission this term. Congratulations!")
        return False


def promotion(upp, rank):
    dm = 0
    if upp[3] >= 6:
        dm += 1
    if roll_two_dice() + dm >= 9:
        rank += 1
        print("You were promoted to {}. Congratulations!".format(ranks[rank]))
    else:
        print("You were not promoted this term.")
    if rank > 6:
        rank = 6
    return rank


def reenlist():
    if roll_two_dice() >= 6:
        return True
    else:
        return False


def career(name, terms, age, reup, comm, rank, upp):
    skills_learned = ["Sword"]
    print("Service skill learned: Sword")
    while reup == 'Y':
        terms += 1
        print("UPP:", upp)
        print("Term:", terms)
        print("Age at start of this term:", age)
        age += 4
        skills_available = 1
        if not survival(upp):
            muster_out(name, terms, age, rank, upp,
                       dict((i, skills_learned.count(i)) for i in skills_learned))
            break
        if terms == 1:
            skills_available += 1
        if comm == 'N':
            if commission(upp):
                comm = 'Y'
                rank = 1
                skills_available += 1
        if comm == 'Y' and (0 < rank < 6):
            rank = promotion(upp, rank)
            if rank == 2:
                skills_learned.append("Blade Cbt")
            if rank == 5:
                skills_learned.append("Leader")
            skills_available += 1
        # skills step
        print("Skills learned this term:")
        for a in range(0, skills_available):
            if upp[3] >= 8:
                skill = skills[random.randint(0, 3)][random.randint(0, 5)]
            else:
                skill = skills[random.randint(0, 2)][random.randint(0, 5)]
            print(skill)
            if skill == 'Str' or skill == 'Dex' or skill == 'End':
                upp = update_upp(upp, skill)
            else:
                skills_learned.append(skill)
        print("UPP: ", upp)
        sorted_skills = dict((i, skills_learned.count(i)) for i in skills_learned)
        print_current_skills(sorted_skills)
        reup = input("Re-enlist for another term? (Y/N) ")[0].upper()
        if reup == 'Y':
            if reenlist():
                print("Your re-enlistment request was approved!\n")
                reup = 'Y'
            else:
                print("Your re-enlistment request was denied!")
                print("Mustering you out!")
                muster_out(name, terms, age, rank, upp, sorted_skills)
                reup = 'N'
        else:
            print("Mustering you out!")
            muster_out(name, terms, age, rank, upp, sorted_skills)
            reup = 'N'


def print_current_skills(sorted_skills):
    skill_list = 'Current skills: '
    for key, value in sorted_skills.items():
        skill_list += "{}-{}  ".format(key, value)
    print(skill_list)


def print_muster_benefits(sorted_muster):
    muster_list = "Muster-out benefits earned: "
    for key, value in sorted_muster.items():
        muster_list += "{}({})  ".format(key, value)
    print(muster_list)


def muster_out(name, terms, age, rank, upp, sorted_skills):
    benefits = terms + math.ceil(rank / 2)
    muster_benefits = []
    cash = 0
    pension = 0
    print("\nYou exited the {} horde at rank {} after {} terms of service.".format(service, rank, terms))
    print("You are given {} mustering-out benefits.".format(benefits))
    print("Three of these may be cash.")
    rolls = 0
    cash_rolls = 0
    while rolls + cash_rolls < benefits:
        ben = input("(B)enefit or (C)ash? ")[0].upper()
        if ben == 'B':
            roll = roll_one_dice()
            if rank > 4:
                roll += 1
            muster_benefits.append(muster_out_benefits[roll - 1])
            print("You earned a {}".format(muster_out_benefits[roll - 1]))
            rolls += 1
        elif ben == 'C':
            roll = roll_one_dice()
            if 'Gambling' in sorted_skills:
                roll += 1
            cash += muster_out_cash[roll - 1]
            cash_rolls += 1
            print("You earned Cr{}".format(muster_out_cash[roll - 1]))
    if terms >= 5:
        pension = 4000 + ((terms - 5) * 2000)
    sorted_muster = dict((i, muster_benefits.count(i)) for i in muster_benefits)
    print_muster_benefits(sorted_muster)
    print("Cash earned: Cr{}".format(cash))
    print("Annual pension: Cr{}".format(pension))
    print_character(name, terms, age, rank, upp, sorted_skills, sorted_muster, cash)


def print_character(name, terms, age, rank, upp, sorted_skills, sorted_muster, cash):
    character_sheet = "\n+-------------------------------------------------+\n"
    character_sheet += "{}, {} {}\n".format(name, service, ranks[rank])
    character_sheet += "{}\tAge {}\t{} term(s)\t".format(convert_upp(upp), age, terms)
    character_sheet += "Cr{}\n".format(cash)
    character_sheet += "Skills: "
    for key, value in sorted_skills.items():
        character_sheet += "{}-{}  ".format(key, value)
    character_sheet += "\nBenefits: "
    for key, value in sorted_muster.items():
        character_sheet += "{}({})  ".format(key, value)
    character_sheet += "\n+-------------------------------------------------+\n"
    print(character_sheet)


def update_upp(upp, skill):
    if skill == 'Str':
        upp[0] += 1
    if skill == 'Dex':
        upp[1] += 1
    if skill == 'End':
        upp[2] += 1
    if skill == 'Int':
        upp[3] += 1
    if skill == 'Edu':
        upp[4] += 1
    if skill == 'Soc':
        upp[5] += 1
    return upp


def convert_upp(upp):
    true_upp = ''
    for stat in upp:
        true_upp += str(convert_to_hex(stat))
    return true_upp


def convert_to_hex(value):
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


def roll_one_dice():
    return random.randint(1, 6)


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)
