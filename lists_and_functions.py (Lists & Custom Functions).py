# Module 01: Lists and Functions
print("=== Lists and Functions ===")

# 1. Working with Lists
ai_domains = ["Machine Learning", "Computer Vision", "Natural Language Processing"]
print(f"Original AI Domains List: {ai_domains}")

# Adding an item
ai_domains.append("Deep Learning")
print(f"After adding an item: {ai_domains}")

# Accessing items by index
print(f"First domain in list: {ai_domains[0]}")

# Iterating through a list
print("\nIterating through all domains:")
for domain in ai_domains:
    print(f"- {domain}")


# 2. Defining and Using Functions
def calculate_accuracy(correct_predictions, total_predictions):
    """Calculates and returns the percentage accuracy of a model."""
    if total_predictions == 0:
        return 0.0
    accuracy = (correct_predictions / total_predictions) * 100
    return round(accuracy, 2)


# Testing the function
corrects = 45
totals = 50
model_accuracy = calculate_accuracy(corrects, totals)

print(f"\nFunction Output:")
print(
    f"Model Accuracy: {model_accuracy}% (Based on {corrects}/{totals} correct"
    " predictions)"
)