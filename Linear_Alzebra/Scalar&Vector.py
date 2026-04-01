import numpy as np

# --- 1. SCALARS ---
# Scalar sirf ek single number hota hai
age = 25
temperature = 30.5
print(f"Scalar Example: Age is {age} and Temp is {temperature}")

# --- 2. VECTORS ---
# Vector numbers ki ek list (array) hoti hai
# Maano ye ek 'Fruit' ka data hai: [Weight in grams, Redness scale 1-10]
apple = np.array([150, 9])
orange = np.array([130, 2])

print(f"\nApple Vector: {apple}")
print(f"Orange Vector: {orange}")

# Vector Addition (Dono fruits ka total data)
total_vector = apple + orange
print(f"Combined Vector (Addition): {total_vector}")

# Scalar Multiplication (Agar hum apple ka size double kar dein)
big_apple = apple * 2
print(f"Big Apple (Scalar Mult): {big_apple}")

# --- 3. DOT PRODUCT (The Similarity Score) ---
# Dot product humein batata hai ki do vectors kitne 'aligned' hain
# Calculation: (150*130) + (9*2)
dot_result = np.dot(apple, orange)

print(f"\nDot Product of Apple and Orange: {dot_result}")

# ML Logic: Agar Dot Product bada hai, toh vectors similar direction mein ho sakte hain.

#Output
#Scalar Example: Age is 25 and Temp is 30.5
# Apple Vector: [150   9]
# Orange Vector: [130   2]
# Combined Vector (Addition): [280  11]
# Big Apple (Scalar Mult): [300  18]
# Dot Product of Apple and Orange: 19518