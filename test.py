from Recur import storage
import questionary

brk = ["back", "break", "b"]
main_menu = [
    "Create Unit",
    "Delete Unit",
    "Add Instance",
    "Remove Instance",
    "List Units",
    "List Instances",
    "Launch Unit",
    "Tree View",
    "Quit"
]


print("=== RECUR IS RUNNING ===")
def main():
    while True:
        action = questionary.select('What to do?', choices=main_menu).ask()
        if action == "Create Unit":
            create_unit()
        elif action == "Add Instance":
            add_instance()
        elif action == "Delete Unit":
            delete_unit()
        elif action == "Remove Instance":
            remove_instance()
        elif action == "List Units":
            list_units()
        elif action == "List Instances":
            list_instances()
        elif action == "Launch Unit":
            launch_unit()
        elif action == "Tree View":
            storage.tree_view()
        elif action == "Quit":
            print("Quitting Recur...")
            break
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