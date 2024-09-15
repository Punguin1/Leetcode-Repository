 def validParenthis(bracket):
    print(len(bracket))
    if bracket[0] != bracket[(-1)]:
        return  "Not Valid"
    i = 1
    for i in range(len(bracket) - 1):
        print(bracket[i], bracket[-((abs(i) + 1))])
        if bracket[i] ==  bracket[-((abs(i) + 1))]:
            return "Not Valid"
    return "valid"
        
solution = validParenthis("({()()()})")
print(solution)

    #if index[0] == index [-1] -> good
    #if index[1] == index [-2]
    #if index[2] == index [-3]


 firstlist = ["0","1","2","3"]
 reverselist = ["3","2","1","0"]

 paranthesislist = "()[]{}"
reveselist =       "}{][)("

if firstlist[i] == reverselist[i]:

for i in range(1, 10, 2)
