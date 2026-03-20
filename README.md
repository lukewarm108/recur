# RECUR
## Contents
1. [Introduction](#1-introduction)
2. [Statement of Objects and Reasons](#2-statement-of-objects-and-reasons)
3. [Installation, Setup, and Update](#3-installation-setup-and-update)
4. [Usage and Troubleshooting](#4-usage-and-troubleshooting)
5. [Files](#5-files)
6. [Clean Uninstall](#6-clean-uninstall)
7. [Limitations and Recommendations](#7-limitations-and-recommendations)
## 1. Introduction
Recur is basically an easy-to-use and simple automation tool. You can organize multiple commands, termed 'instances', into specific 'units', and launch them all at once, everything through the TUI and not manual scripting.

It is written in Python, based on Linux, stores data in a JSON file, and uses the `questionary` module for TUI.
## 2. Statement of Objects and Reasons
Scripting often looks, or perhaps is, intimidating for those not specifically into the technical fields such as software development, etc. Moreover, people often have to open multiple windows for getting on with their work.

For these reasons, inter alia, Recur provides an easy-to-use terminal interface for entering commands, grouping them into 'units', launching them whenever required, as well as storing them in a JSON file which can be transferred manually into a different machine for re-use. The tool is made specifically for opening multiple GUI apps together, but it can also be used for simple scripting.
## 3. Installation, Setup, and Update
Although many paths for installation exist, the following is the recommended one for convenience and ease of use.

Pre-requisites:
```
python 3.x
pipx
git
```

Before proceeding with the installation, it's recommended to update your system.
```bash
sudo pacman -Syu # For Arch, Manjaro
sudo apt update && sudo apt upgrade # For Debian, Ubuntu, Mint
sudo dnf upgrade # For Fedora
```

Clone the repository and move inside:
```bash
git clone https://github.com/lukewarm108/recur.git # Clone repo
cd recur # Move inside
```

`pipx` by itself manages Python CLI tools and their dependencies in isolated environments, keeping them separate from your system Python. Finish the procedure by installing it using `pipx`:
```bash
pipx install .
```

For updating, you can simply:
```bash
pipx reinstall recur
```
Or, from inside the repo directory:
```bash
git pull origin main # Pull the changes
pipx reinstall recur
```
## 4. Usage
The program can be launched with:
```bash
recur
```

The following options will be shown. Arrow keys are used for navigation.
```recur
» Launch  
  Tree View  
  Units  
  Quit
```
### Main Menu
**Launch** - Shows the units and launches the one selected.
**Tree View** - Presents an ASCII view of the units and instances, replicating the `.json` file.
**Units** - Control center for editing the `.json` file interactively. It allows for creating and deleting units, adding and removing instances.
**Quit** - Self-descriptive.

> [!NOTE] Note
> While creating unit(s) or adding instance(s), the program may ask for contents continuously. Entering `b`, `back`, or `break` reverts to the previous menu.

## 5. Files
### File Structure
```file
.
├── LICENSE # MIT
├── pyproject.toml
├── README.md
└── Recur
    ├── __init__.py
    ├── main.py
    └── storage.py
```
### JSON Storage
The units and their respective instances are stored in a `.json` file at:
```path
~/.local/share/recur/units.json
```
## 6. Clean Uninstall
In case of dissatisfaction or any reason whatsoever, if uninstallation of Recur is prompted, the following is the recommended procedure for a clean uninstall.

> [!NOTE] NOTE
> This will permanently delete all data and files and directories associated with Recur in and from your local machine.

> [!NOTE] NOTE
> This section assumes an installation and setup in accordance with the [recommended procedure](#3-installation-setup-and-update) as well as no changes in the files structure have been made.

Start with `pipx`:
```bash
pipx uninstall recur
```

Remove the `.json` file along with its parent directory:
```bash
rm -rf ~/.local/share/recur
```

Remove the repo directory:
```bash
rm -rf recur
```
## 7. Limitations and Recommendations
As a simple program, Recur has several limitation. These limitations may or may not be patched in the future, depending on whether they defeat the purpose of simplicity and ease of use. Some of these limitations, along with certain recommendations, are mentioned below.

1. **`json` corruption:** Manually editing or tinkering with the `.json` file might prevent the program from running as intended.
2. **Passwords:** Instances that require a password or any key will not work (yet).
3. **Instance limit:** In a single unit, it's recommended to add only as many instances as the host device can realistically handle. Generally speaking, 5-10 instances are recommended.
4. **Platforms:** Only Linux is natively supported. Windows and other platforms may be supported via individual editing.
5. **No delay:** All instances in a unit launch simultaneously with no configurable delay in between.
6. **No window management:** Instances that open windows have no control over positioning and size of the windows. They may be opened based on last position or size, individual device configuration, or any other basis.