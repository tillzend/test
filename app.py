
num_tickets = 237
bus_capacity = 48 

full_bus_quantity = num_tickets // bus_capacity
num_tickets_left = num_tickets % bus_capacity

print(full_bus_quantity, num_tickets_left)