from enum import Enum

class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())

def distances(string_a, string_b):
    string_a_mod, string_b_mod = " " + string_a, " " + string_b
    len_str_a, len_str_b = len(string_a_mod), len(string_b_mod)
    array = []
    #Generate Array(list) based on string a, b length
    for i in range(len_str_a):
        array.append(len_str_b * [None])

    for j, val_a in enumerate(string_a_mod):
        if j > 0:
            result = array[j-1][0][0]
        else:
            result = 0

        for i, val_b in enumerate(string_b_mod):
            op = None
            #Determine operation cost
            if i > 0 and j > 0:
                result = min(array[j][i-1][0], array[j-1][i-1][0])
            if val_a != val_b:
                result += 1

            #Determine operation type
            if val_a != val_b:
                if len_str_a > len_str_b:
                    op = Operation.DELETED
                    len_str_a -= 1
                elif len_str_a < len_str_b:
                    op = Operation.INSERTED
                    len_str_a += 1
                else:
                    op = Operation.SUBSTITUTED

            array[j][i] = (result,op)

    return (array)