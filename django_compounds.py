# elements = ['1', 'hydrogen', '1+', '2', 'helium', '0', '3', 'lithium', '1+', '4']
#
# print(new_list)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'QuickChemistry.settings')

import django
django.setup()

import random
import csv

from quickapp.models import ChemProblems




my_elements = {}
used_elemnts = {}
anions = {}
cations = {}
filename = "element_list.csv"

# amount = int(input("How many problems will you like to solve today?: "))
# question = input("What kind of bonding will you like today?: ")

with open(filename, newline='') as csvfile:
    element_reader = csv.reader(csvfile, delimiter=',')
    for row in element_reader:
        a, b, c = row
        if "Nonmetal" in row:
            cations[b] = c
        else:
            anions[b] = c
# new_list = [my_elements[i:i+3] for i in range(0, len(my_elements), 3)]


anion_list = list(anions.items())
cations_list = list(cations.items())



def pickCation():
    cation = random.choice(cations_list)
    return cation[0]


def pickAnion():
    anion = random.choice(anion_list)
    return anion[0]

def gen(N,type):
    for i in range(N):
        if type == "Ionic":
            my_cation = pickCation()
            my_anion = pickAnion()

            return f"Combine {my_cation} with {my_anion}"

        elif type == "Covalent":
            cation1 = pickCation()
            cation2 = pickCation()

            return f"Combine {cation1} with {cation2}"

        else:
            return f'{type} is not available as of yet!'

        # else:
        #     return ' I did not understand!'


# for i in range(1,amount+1):
#     comp = gen()
#     print(comp)

# def store_data():
#
#
# store_data()
