from enum import Enum
from enum import IntEnum
class Country(Enum):
    USA = 10
    India = 0
    Argentina = 30
    Japan = 8
    China = 5
#print("Country name: {}".format(Country.Japan.name))
#print("Country value: {}".format(Country.Japan.value))

#Write a Python program that iterates over an enum class and displays each member and their value.
def iterate_enum(enum_name):
    for i in enum_name:
        print(i.name, i.value)
#iterate_enum(Country)

#Write a Python program to display all the member names of an enum class ordered by their values.
class IntCountries(IntEnum):
    USA = 10
    India = 0
    Argentina = 30
    Japan = 8
    China = 5

def ordered_enum():
    print("Country name ordered by their values: ")
    print([(c.name, c.value) for c in sorted(IntCountries)]) #to use sorted, the enum must be an IntEnum
#ordered_enum()
#--------------------------------------------------------------------------------------------------------------------------------



