Bakery Problem
For today, Chef is out of town, and his evil son has taken over his bakery.

Normally, Chef sells his cakes for 
100
100 rupees each. However, his son can be bribed with 
K
K rupees, to sell each cake for 
60
60 rupees instead. Note that you have to pay this bribe only one time, not for each cake.

You want to buy 
N
N cakes from the bakery. You can choose whether to bribe Chef's son or not. What is the minimum cost of buying the 
N
N cakes.

Input Format
The first and only line contains 
2
2 integers - 
N
N and 
K
K, the number of cakes you need to buy, and the bribe amount.
Output Format
Output the minimum total cost of buying the 
N
N cakes.
#######################################################################
my approch:

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    t = 0
    for s in range(n, m, -1):
        t = t + s
    print(t)
