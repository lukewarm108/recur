from Recur import storage
import sys


print('''
    === RECUR IS RUNNING ===
    1. Create Units 
    2. Delete Units
    3. List Units
    q. Quit
''')
while True:
    units = storage.load_unit()
    x = input("Enter (identifier): ")
    if x == "1":
        while True:
            y = input("Enter unit name: ")
            if y in units:
                print("A unit by that name already exists.")
                continue
            else:
                storage.create_unit(y)
                sys.exit(f"A unit by the name {y} is created.")
    elif x == "2":
        while True:
            y = input("Enter the name of the unit you wish to delete: ")
            if not y in units:
                print(f"No unit by the name {y} exists.")
                continue
            else: 
                storage.delete_unit(y)
                sys.exit(f"The unit named {y} is deleted.")
    elif x == "3":
        print(list(units.keys()))
        break
    elif x == "q":
        sys.exit("Quitting Recur...")
    else:
        print("Please enter a correct identifier.")