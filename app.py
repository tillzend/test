
num_tickets = int(input("enter value: "))
bus_capacity = 48 

bus_quantity = num_tickets // bus_capacity
num_tickets_left = num_tickets % bus_capacity

empty_seats = 0
no_full_bus = False

if num_tickets_left >= bus_capacity / 2 :
    bus_quantity += 1
    no_full_bus = True
    empty_seats = num_tickets_left - bus_capacity


print("count of full bus + 1: ", bus_quantity)
print("left tickets: ", num_tickets_left)
print("Incomplete bus: ", no_full_bus)
print("Count of empty seats: ", empty_seats)