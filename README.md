# LeeSporks-Python-enum-class
Import this file into any other python project, and you can use it to create "enum" objects.

Give it a list of strings, and it will create a constant (variable) named after each string in the list. This is usefull if you want to use ID codes for something, but still have it readable (using readable names instead of numbers), and also has the benifit of allowing you to auto-complete the items.

Enum values can also be "sub-enums" of each other. This is done by defining the item as a dictionary key instead of a string, and it's sub-items inside a list that is in the value of the dict.

You can also get the original name from an enum value. This is done like reading an index from a list or string or something. e.g. if you had an enum object called "FOOD_ENUM" you could ask it what the name for the item with value 4 is by typing "FOOD_ENUM[4]", and it will return a string such as 'Apple', for example.

e.g.

from leesporks_enum_class import enum

FOOD_ENUM = enum(["cookie", "doughnut", {"fruit":["apple","banana","orange"]}, "cake"])

print( FOOD_ENUM.DOUGHNUT ) # 1

print( FOOD_ENUM.check_sub(FOOD_ENUM.APPLE, FOOD_ENUM.FRUIT) ) # True

print( FOOD_ENUM.check_sub(FOOD_ENUM.CAKE, FOOD_ENUM.FRUIT) ) # False

food_on_table = [ FOOD_ENUM.APPLE, FOOD_ENUM.CAKE ]

for i in food_on_table: print("There is a {} on the table. It is {} that it is a fruit.".format(FOOD_ENUM[ i ], FOOD_ENUM.check_sub(i, FOOD_ENUM.FRUIT)))
