def categorize_usage(power):
    if power < 1.0:
        return "Low Usage"
    elif power < 2.0:
        return "Medium Usage"
    else:
        return "High Usage"

def suggestion(category):
    if category == "Low Usage":
        return "Great job! Consider scheduling heavy appliances during this time for efficiency."
    elif category == "Medium Usage":
        return "Usage is moderate. Check if any unnecessary devices are running."
    elif category == "High Usage":
        return "High consumption detected! Try to turn off non-essential devices."

predicted_power = 2.5 
category = categorize_usage(predicted_power)
print(f"Predicted Power Consumption: {predicted_power:.2f} kW")
print(f"Assigned Category: {category}")
print(f"Suggestion: {suggestion(category)}")
