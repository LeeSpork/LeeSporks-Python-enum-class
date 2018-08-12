"""
    Version: 1.1
    Creted by LeeSpork

    Update log 1.1:
    + enum.__getitem__ actually works now
    + enum.check_sub will now consider any value to be a "sub" of itself.
    + enum.check_sub will now return False if it gets a KeyError.
"""

class enum:

    def __init__(self, values, force_uppercase_enums=True):
        """Gives this object an attribute for every string in the list given to it.

            If a value of the list is a dictionary with value(s) of list,
            then both the keys and the lists will be given enums.
            Also, check_sub will consider the enums of the items inside
            the dict values to the sub-enums of the dict key's enum.

            e.g.:
            enum(["cookie", "doughnut", {"fruit":["apple","banana","orange"]}, "cake"])
        """
        self._LIST = {} #key is the enum ID, value is the original name of the enum value.
        self._SUBS = {} #Keeps track of what is super to what.

        _loop_thru_list_and_assign_enum_values(values, self, uppercase=force_uppercase_enums)


    def __getitem__(self, index):
        """enum.__getitem__(n) is the same as enum[n]"""
        return self._LIST[index]


    def check_sub(self, sub_index, super_index):
        """Tests if sub_index is a sub of super_index.

            e.g.:
            >>> FOOD_ENUM = enum(["cookie", {"fruit":["apple","banana"]}])
            >>> FOOD_ENUM.is_sub(FOOD_ENUM.APPLE, FOOD_ENUM.FRUIT)
            True
        """
        try: return sub_index == super_index or sub_index in self._SUBS[super_index]
        except KeyError: return False


#==============| Functions used in enum object creation |=======================


def _assign_enum_value(pValue, pEnumObj, pNumber, pSupers=[], uppercase=True):
    new_string = ""
    obj = pEnumObj
    
    for i in pValue:
        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz":
            new_string += '_'
        else:
            if uppercase: new_string += i.upper()
            else: new_string += i

    #Add attribute to enum
    exec( "obj."+ new_string +"=pNumber" )

    #Add to list of names
    obj._LIST[pNumber] = pValue

    #Add to list of supers
    for i in pSupers:
        #print(pSupers) ########DEBUG####
        try:
            obj._SUBS[i].append(pNumber) #Append to the value of the key
        except KeyError:
            obj._SUBS[i] = [pNumber] #Inilize the key, since it wasn't there, apparently.



def _loop_thru_list_and_assign_enum_values(pList, pEnumObj, pNumber=0, pSupers=[], uppercase=True):
    n = pNumber
    obj = pEnumObj
    
    for i in range(len(pList)):

            
        if isinstance(pList[i], str):
            _assign_enum_value(pList[i], pEnumObj, n, pSupers, uppercase)
            n+=1


        #Allow using dicts to sub-enum
        elif isinstance(pList[i], dict):
            for key in pList[i]:
                _assign_enum_value( key, pEnumObj, n, pSupers, uppercase)

                #Recursivly loop through the list that is the value of this dict key, and get the update n value from it.
                n = _loop_thru_list_and_assign_enum_values(
                    pList[i][key],
                    obj,
                    n+1,
                    pSupers + [n],  # The ID for this key will be a super to all in this dict key's value.
                                    # Adding instead of appending because we need to not edit the original pSuper.
                    uppercase
                    )


        else: raise TypeError("enum values must be a list of strings or dictionarys with a single key and the value of a list...")

        
    return n

#==============| test |=========================================================

if __name__ == "__main__":
    
    test = enum([
        "brick",
        "paper",
        {"weapon": [
            "crowbar",
            "butterknife",
            {"sword": [
                "iron sword",
                "excalibur"
                ]},
            "sharp rock"
            ]}
        ])

    bobs_inventory = [test.BRICK, test.IRON_SWORD]

    for i in bobs_inventory:
        print("Bob has a {}. It is item number {}. Is it a weapon? {}.".format(
            test[ i ], #Ask test what the name of that enum is
            i,
            test.check_sub(i, test.WEAPON) #Ask test if bob's item ID is a sub-item of weapon
            )
              )
