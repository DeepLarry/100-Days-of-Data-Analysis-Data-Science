m,n=map(int,input().split())
def basic_operatons():
    addition=m+n
    subtraction=m-n
    multiplication=m*n
    division=m/n
    integrdivision=m//n
    modulus=m%n
    return addition,subtraction,multiplication,division,integrdivision,modulus
print(*basic_operatons(addition,subtraction,multiplication,division,integrdivision,modulus),sep="\n")