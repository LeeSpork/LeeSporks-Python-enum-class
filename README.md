# LeeSporks-Python-enum-class
Import this file into any other python project, and you can use it to create enum thingys. Enum values can also be "sub-enums" of each other.

e.g.
from leesporks_enum_class import enum
FOOD_ENUM = enum(["cookie", "doughnut", {"fruit":["apple","banana","orange"]}, "cake"])
print( FOOD_ENUM.DOUGHNUT ) # 1
print( FOOD_ENUM.check_sub(FOOD_ENUM.APPLE, FOOD_ENUM.FRUIT) ) # True
print( FOOD_ENUM.check_sub(FOOD_ENUM.CAKE, FOOD_ENUM.FRUIT) ) # False
