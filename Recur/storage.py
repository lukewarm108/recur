import json
import subprocess
import os
from rich.tree import Tree
from rich.console import Console


JSON_PATH = "units.json"


# GENERAL
def save_units(units):
    with open(JSON_PATH, "w") as f:
        json.dump(units, f)

def load_units():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r") as f:
            return json.load(f)
    else:
        save_units({})
        return {}

def load_instances(unit_name):
    units = load_units()
    return units[unit_name]["instances"]


# UNIT COMMAND
def create_unit(unit_name):
    units = load_units()
    units[unit_name] = {"instances": []}
    save_units(units)

def delete_unit(unit_name):
    units = load_units()
    del units[unit_name]
    save_units(units)

def list_units():
    units = load_units()
    for unit in units:
        print(unit)


# INSTANCE COMMAND
def add_instance(unit_name, instance_name):
    units = load_units()
    units[unit_name]["instances"].append(instance_name)
    save_units(units)

def remove_instance(unit_name, instance_name):
    units = load_units()
    units[unit_name]["instances"].remove(instance_name)
    save_units(units)

def list_instances(unit_name):
    units = load_units()
    instances = load_instances(unit_name)
    for instance in instances:
        print(instance)


# LAUNCH
def launch_unit(unit_name):
    units = load_units()
    units = units[unit_name]["instances"]
    for unit in units:
        subprocess.Popen(unit.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# FEATURES
def tree_view():
    units = load_units()
    console = Console()
    tree = Tree("Recur")
    for unit in units:
        branch = tree.add(unit)
        for instance in units[unit]["instances"]:
            branch.add(instance)
    console.print(tree)