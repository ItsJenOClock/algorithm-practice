# Add your clarifying questions here
# Will shift_by be less than the length of the list? 
#   The value could be less than/equal/greater than length of list
# What if shift_by is a value not in the list? 
#   Still rotate the list by shift_by if valid
# Are negative number allowed for rotation value? 
#   Only valid shift_by values will be greater than 1
# Will the list always contain integers? 
#   Not necessarily, but we should still be able to shift it
# What if the list is empty? 
#   Return the empty list
# What if shift_by is invalid input? 
#   Raise an error or return None

def rotate_list(list, shift_by):
    if shift_by > len(list):
        shift_by %= len(list)

    for i in range(shift_by):
        last_number = list.pop()
        list.insert(0, last_number)

    return list

assert rotate_list(["a", "b", "c"], 1) == ["c", "a", "b"]
assert rotate_list([1, "c", 11], 3) == [1, "c", 11]
assert rotate_list([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]



