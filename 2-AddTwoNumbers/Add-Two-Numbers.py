# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1, l2):
    # Reverse, combine into integer, add, reverse result
    strL1 = [str(s) for s in l1]
    strL2 = [str(s) for s in l2]
    intL1 = "".join(strL1[::-1])
    intL2 = "".join(strL2[::-1])
    result_int = int(intL1) + int(intL2)
    result = list(str(result_int))
    result_list_int = [int(s) for s in result]

    
    return result_list_int[::-1]

print(addTwoNumbers([2,4,3], [5,6,4]))

        
