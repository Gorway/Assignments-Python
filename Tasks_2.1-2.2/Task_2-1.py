def kg_to_pounds(kg):
    pounds = kg * 2.2
    return pounds

weight_kg = float(input("Enter weight in kilograms: "))

weight_pounds = kg_to_pounds(weight_kg)

print("Weight in pounds: ", weight_pounds)
