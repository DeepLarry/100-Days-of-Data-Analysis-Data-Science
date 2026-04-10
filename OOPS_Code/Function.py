def is_even(x):
    """This function return if a given number even or odd
    input- any valid integer
    output - odd/even
    created on 10/04/26
    created by deeptiwari"""
    if x%2==0:
        return "Even"
    else:
        return "odd"
# if type(x)== int:
for i in range(1,11):
    x=is_even(i)
    print(x)
is_even(7)
# else:
    # return "pagal hai kya yah code function galat hai"

