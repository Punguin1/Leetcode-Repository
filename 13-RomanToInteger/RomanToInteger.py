class Solution:
    def romanToInt(s: str) -> int:
    # Go through string, add number of corresponding symbol. if there is valid symbol before it, remove corresponding amount
        p = ""
        result = 0
        for c in s:
            if c == "I":
                result += 1
            if c == "V":
                result += 5
                if p == "I":
                    result -= 2
            if c == "X":
                result += 10
                if p == "I":
                    result -= 2
            if c == "L":
                result += 50
                if p == "X":
                    result -= 20
            if c == "C":
                result += 100
                if p == "X":
                    result -= 20
            if c == "D":
                result += 500
                if p == "C":
                    result -= 200
            if c == "M":
                result += 1000
                if p == "C":
                    result -= 200
            p = c
        return result

print(Solution.romanToInt("IX"))
