import json

def save_unit(x):
    with open("units.json", "w") as f:
        json.dump(x, f)

def load_unit():
    with open("units.json", "r") as f:
        return json.load(f)

def create_unit(name):
    x = load_unit()
    x[name] = {"instances": []}
    save_unit(x)

def delete_unit(name):
    x = load_unit()
    del x[name]
    save_unit(x)

def list_units():
    x = load_unit()
    print(**x)