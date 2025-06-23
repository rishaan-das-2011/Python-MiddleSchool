"""
LESSON: 4.1 - Lists
TECHNIQUE 3: User-Built Lists
DEMO
"""

# --- Setup --- #
guests = []

# --- Enter guests --- #
guest = ""
while guest != "done":
    guest = input("Enter a guest's name (enter done to exist): ")
    if guest == "done":
        break
    guests.append(guest)






# --- Print results --- #
print("Here are your guests:")
index = 0
while index < len(guests):
    print("   -" + guests[index])
    index += 1
print("You'll need to cut any pizza into " + str(len(guests)) + " slices.")