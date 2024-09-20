def columnNumber(columnTitle):
    letters = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
    }

    # the length of the string signifies the power of the result

    result = 0
    for c in columnTitle:
        result = result * 26 + letters[c]
    return result
    # get the length of the string
    # A = 1
    # AA = 27 
    # BA = 53
    # 2
    # B*26 = 53
    # 3
    # BAA = 1379
    # AAA = 703
    # AAAA = 18,279

print(columnNumber("AAA"))

