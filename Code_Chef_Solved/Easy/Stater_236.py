# Chef planned a party and expected X people to attend. However, more people showed up, and the total number of guests became Y.

# Chef had already ordered X plates of food, each costing 100 rupees.

# For every extra guest (i.e., Y - X), Chef needs to order an additional plate, each costing 150 rupees.

# ❓ Task

# Calculate the total amount of money Chef needs to spend to provide food for all guests.

# 📥 Input Format

# A single line containing two space-separated integers:
# X Y

# X → Expected number of guests
# Y → Actual number of guests
# 📤 Output Format

# Print a single integer — the total cost of food.

# 📌 Constraints
# 1 ≤ X < Y ≤ 200


# My Approach:

# cook your dish here
X,Y=map(int,input().split())
Z=X*100
A=Y-X
K=A*150
print(Z+K)