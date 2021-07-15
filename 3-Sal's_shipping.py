# Write a program asking customers for package weight and return the cheapest method of shipping.

flat_charge = 20
weight = float(input("Enter a weight in kilogramms: "))

def drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25

def ground_shipping(weight):
    if weight <= 2:
        return weight * 1.50 + flat_charge
    elif weight <= 6:
        return weight * 3.00 + flat_charge
    elif weight <= 10:
        return weight * 4.00 + flat_charge
    else:
        return weight * 4.75 + flat_charge

premium_ground = 125.00

def shipping_and_cost(weight):
    if ground_shipping(weight) < premium_ground and ground_shipping(weight) < drone_shipping(weight):
        return "The cheapest method is ground shipping and it will cost $" + str(ground_shipping(weight)) + "."
    elif premium_ground < ground_shipping(weight) and premium_ground < drone_shipping(weight):
        return "The cheapest method is premium ground shipping and it will cost 125$."
    else:
        return "The cheapest method is drone shipping and it will cost $" + str(drone_shipping(weight)) + "."

print(shipping_and_cost(weight))
