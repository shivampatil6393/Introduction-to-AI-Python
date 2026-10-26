# Module 01: Control Flow - Conditionals and Loops
print("=== Control Flow in Python ===")

# 1. Conditional Statements (if-elif-else)
score = 88
print(f"\nTest Score: {score}")

if score >= 90:
    print("Grade: A (Excellent)")
elif score >= 75:
    print("Grade: B (Good job)")
elif score >= 60:
    print("Grade: C (Needs improvement)")
else:
    print("Grade: F (Keep practicing)")

# 2. For Loop (Iterating over a range)
print("\nFor Loop Example (Counting 1 to 5):")
for i in range(1, 6):
    print(f"Iteration number: {i}")

# 3. While Loop (Countdown)
print("\nWhile Loop Example (Countdown):")
countdown = 3
while countdown > 0:
    print(f"Countdown... {countdown}")
    countdown -= 1
print("Liftoff! 🚀")