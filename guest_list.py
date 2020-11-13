guests = []

print("Let's make a guest-list for your birthday party!")
add_guest = input("Would you like to add a guest on the list?  (Yes/No)")

while add_guest.lower() == 'yes':
    guest_name = input("please enter a player name:  ")
    guests.append(guest_name)
    add_guest = input("Would you like to add another guest on the list?  (Yes/No)")
    
print("\nThere are {} guests on the list!".format(len(guests)))

guest_number = 1
for guest in guests:
    print("guest {}: {}".format(guest_number,guest))
    guest_number += 1
    
helper = input("Please select a helper for preparation by selecting the guest number. (1-{})".format(len(guests)))
helper = int(helper)

print("Great! the helper for your birthday party will be {}!".format(guests[helper-1]))
