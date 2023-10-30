# gobal varible
weight = 41.5
prem_ground = 125.00


# ground Shipping logic
# sing the if statements to create and set the value of "ground_ship"
if weight <= 2:
    ground_ship = (weight * 1.50) + 20.00
    print("Ground Shipping Cost: Price per Pound: $1.50 and Flat Charge: $20.00. Total Price is: $" + str(ground_ship))
elif (weight > 2) and (weight <= 6):
    ground_ship = (weight * 3.00) + 20.00
    print("Ground Shipping Cost: Price per Pound: $3.00 and Flat Charge: $20.00. Total Price is: $" + str(ground_ship))
elif (weight > 6) and (weight <= 10):
    ground_ship = (weight * 4.00) + 20.00
    print("Ground Shipping Cost: Price per Pound: $4.00 and Flat Charge: $20.00. Total Price is: $" + str(ground_ship))
elif (weight > 10):
    ground_ship = (weight * 4.75) + 20.00
    print("Ground Shipping Cost: Price per Pound: $4.75 and Flat Charge: $20.00. Total Price is: $" + str(ground_ship))
else:
    print("Please Enter in weight of Package for Ground Shipping")

print("If you would like Premium Ground Shipping it will cost an additional: $" + str(prem_ground))

# Drone Shipping Logic
# using the if statements to create and set the value of "drone_ship"
if weight <= 2:
    drone_ship = (weight * 4.50)
    print("DroneShipping Cost: Price per Pound: $4.50 Total Price is: $" + str(drone_ship))
elif (weight > 2) and (weight <= 6):
    drone_ship = (weight * 9.00)
    print("Drone Shipping Cost: Price per Pound: $9.00. Total Price is: $" + str(drone_ship))
elif (weight > 6) and (weight <= 10):
    drone_ship = (weight * 12.00)
    print("Drone Shipping Cost: Price per Pound: $12.00. Total Price is: $" + str(drone_ship))
elif (weight > 10):
    drone_ship = (weight * 14.25)
    print("Drone Shipping Cost: Price per Pound: $14.25. Total Price is: $" + str(drone_ship))
else:
    print("Please Enter in weight of Package for Drone Shipping")
