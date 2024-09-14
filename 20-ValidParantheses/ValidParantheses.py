def isValid(s: str) -> bool:
    slist = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for c in s:
        if c in {"(", "[", "{"}:
            slist.append(c)
        elif len(slist) == 0 or c != pairs[slist.pop()]:
            return False
    return slist == []

                    

        
print(isValid("([)]"))
