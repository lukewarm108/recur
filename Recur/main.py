from Recur import storage
import questionary



brk = ["back", "break", "b"]
main_menu = [
    "Launch",
    "Tree View",
    "Units",
    "Quit"
]



print("=== RECUR IS RUNNING ===")
def main():
    while True:
        action = questionary.select('What to do?', choices=main_menu).ask()
        if action == "Launch":
            units = storage.load_units()
            units = list(units.keys()) + ["Back"]
            unit = questionary.select('Unit to launch: ', choices=units).ask()
            if unit == "Back":
                continue
            else:
                storage.launch_unit(unit)


        elif action == "Tree View":
            units = storage.load_units()
            storage.tree_view()
            questionary.select('', choices=['Back to Main Menu']).ask()


        elif action == "Units":
            while True:
                units = storage.load_units()
                action = questionary.select('Select your action', choices=['Create', 'Delete', 'Add Instance', 'Remove Instance', 'Back']).ask()

                if action == 'Create':
                    while True:
                        name = input("Name: ")
                        if name in units:
                            print(f"{name} already exists. Try a different name.")
                            continue
                        elif name in brk:
                            break
                        else:
                            storage.create_unit(name)
                            break

                elif action == 'Delete':
                    while True:
                        units = storage.load_units()
                        units = list(units.keys())
                        unit = questionary.select('Unit to Delete', choices=units + ["Back"]).ask()

                        if unit in units:
                            if questionary.confirm('Are you sure?').ask():
                                storage.delete_unit(unit)
                                print(f"Unit {unit} deleted.")
                            else:
                                continue
                        else:
                            break

                elif action == "Add Instance":
                    while True:
                        units = storage.load_units()
                        units = list(units.keys())
                        unit = questionary.select('Select Unit', choices=units + ["Back"]).ask()

                        if unit in units:
                            while True:
                                instance = input("Instance to add: ")
                                if instance in brk:
                                    break
                                else:
                                    storage.add_instance(unit, instance)
                                    print(f"Instance {instance} added to unit {unit}")
                                    continue

                        else:
                            break
                
                elif action == "Remove Instance":
                    while True:
                        units = storage.load_units()
                        units = list(units.keys())
                        unit = questionary.select('Select Unit', choices=units + ["Back"]).ask()

                        if unit in units:
                            while True:
                                instances = storage.load_instances(unit)
                                instance = questionary.select('Instance to delete', choices=instances + ["Back"]).ask()
                                if instance in instances:
                                    storage.remove_instance(unit, instance)
                                else:
                                    break
                        else:
                            break
                
                else:
                    break
        

        elif action == "Quit":
            print("Quitting recur...")
            break



if __name__ == "__main__":
    main()