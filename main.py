from Recur import storage

brk = ["back", "break", "b"]

print('''
    === RECUR IS RUNNING ===
    1. Create Unit
    2. Add Instance
    3. Delete Unit
    4. Remove Instance
    5. List Units
    6. List Instances
    7. Launch Unit
    8. Tree View
    q. Quit
''')


def main():
    while True:
        identifier = input("Enter (identifier): ")

        # Create Unit
        if identifier == "1":
            create_unit()
        # Add Instance
        elif identifier == "2":
            add_instance()
        # Delete Unit
        elif identifier == "3":
            delete_unit()
        # Remove Instance
        elif identifier == "4":
            remove_instance()
        # List Units
        elif identifier == "5":
            list_units()
        # List Instances
        elif identifier == "6":
            list_instances()
        # Launch Unit
        elif identifier == "7":
            launch_unit()
        # Tree View
        elif identifier == "8":
            storage.tree_view()
        # Quit
        elif identifier == "q":
            print("Quitting Recur...")
            break
        # ...
        else:
            print("Please enter a correct identifier.")


def create_unit():
    units = storage.load_units()
    while True:
        unit = input("Unit to create: ")
        if unit in units:
            print(f"Unit {unit} already exists.")
        elif unit in brk:
            break
        else:
            storage.create_unit(unit)
            print(f"Unit {unit} is created.")


def add_instance():
    units = storage.load_units()
    while True:
        unit = input("Unit name: ")
        if unit in units: 
            while True:
                instance = input("Instance to add: ")
                if instance in brk:
                    break
                else:
                    storage.add_instance(unit, instance)
                    print(f"Instance {instance} added to unit {unit}")
        elif unit in brk:
            break
        else:
            print(f"Unit {unit} does not exist.")
            continue


def delete_unit():
    units = storage.load_units()
    while True:
        unit = input("Unit to delete: ")
        if unit in units:
            storage.delete_unit(unit)
            print(f"Unit {unit} is deleted.")
        elif unit in brk:
            break
        else: 
            print(f"Unit {unit} does not exist.")
            continue


def remove_instance():
    units = storage.load_units()
    while True:
        unit = input("Unit name: ")
        if unit in units: 
            instances = storage.load_instances(unit)
            while True:
                instance = input("Instance to remove: ")
                if instance in instances:
                    storage.remove_instance(unit, instance)
                    print(f"Instance {instance} removed from unit {unit}")
                elif instance in brk:
                    break
                else:
                    print(f"Instance {instance} does not exist.")
                    continue
        elif unit in brk:
            break
        else:
            print(f"Unit {unit} does not exist.")
            continue


def list_units():
    storage.list_units()


def list_instances():
    units = storage.load_units()
    while True:
        unit = input("Unit name: ")
        if unit in units:
            storage.list_instances(unit)
        elif unit in brk:
            break
        else:
            print(f"Unit {unit} does not exist.")
            continue


def launch_unit():
    units = storage.load_units()
    while True:
        unit = input("Unit to launch: ")
        if unit in units:
            storage.launch_unit(unit)
            print(f"Launching unit: {unit}")
            for instance in units[unit]["instances"]:
                print(f"{instance} launched...")
            break
        elif unit in brk:
            break
        else:
            print(f"Unit {unit} does not exist.")
            continue


if __name__ == "__main__":
    main()