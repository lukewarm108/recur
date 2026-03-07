import subprocess

def main():
    instances = []
    while True:
        x = input("Your instances ('q' for quit): ")
        if x == "q":
            break
        instances.append(x)

    for instance in instances:
        subprocess.run(instance)


if __name__ == "__main__":
    main()