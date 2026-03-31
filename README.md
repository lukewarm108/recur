# 🔄 RECUR

[![Python 100%](https://img.shields.io/badge/Python-100%25-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-FCC624?logo=linux&logoColor=black)](https://www.kernel.org/)
[![Code style: Modern](https://img.shields.io/badge/Code%20Style-Modern-8A2BE2)]()

> A simple, Linux- and Python-based, multi-instance launcher script for automation and command management.

## 📋 Table of Contents

- [✨ Features](#-features)
- [🎯 What is Recur?](#-what-is-recur)
- [💡 Why Use Recur?](#-why-use-recur)
- [📦 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📁 Project Structure](#-project-structure)
- [⚙️ Configuration](#-configuration)
- [⚠️ Limitations & Recommendations](#-limitations--recommendations)
- [🗑️ Uninstall](#-uninstall)

## ✨ Features

- 🎨 **Intuitive TUI Interface** - Navigate with arrow keys, no scripting required
- 📦 **Command Organization** - Group commands into logical units and instances
- 💾 **Persistent Storage** - Save configurations in JSON format for easy backup and transfer
- 🔧 **Simple Management** - Create, edit, and delete units/instances interactively
- 🐧 **Linux Native** - Built specifically for Linux environments
- 🐍 **Pure Python** - Lightweight and portable

## 🎯 What is Recur?

Recur is an easy-to-use automation tool that simplifies launching multiple commands. You organize commands into **instances**, group them into **units**, and launch them all at once—all through an intuitive terminal interface.

**Perfect for:**
- Launching multiple GUI applications together
- Automating repetitive command sequences
- Managing complex workflows without manual scripting

**Built with:**
- Python 3.x
- `questionary` for the interactive TUI
- JSON for configuration storage

## 💡 Why Use Recur?

Scripting can be intimidating, and managing multiple commands across different windows is tedious. Recur removes these pain points by providing:

- ✅ **No scripting knowledge required** - Use the interactive menu instead
- ✅ **Centralized control** - Launch everything from one interface
- ✅ **Portable configurations** - Transfer your units.json to any machine
- ✅ **Perfect for beginners and power users alike**

## 📦 Installation

### Prerequisites

```
python 3.x
pipx
git
```

### Recommended Installation

#### 1. Clone and install

```bash
# Clone the repository
git clone https://github.com/lukewarm108/recur.git
cd recur

# Install using pipx (recommended - isolated environment)
pipx install .
```

#### 2. Verify installation

```bash
recur --version  # Check installation
recur            # Launch the application
```

### Updating

```bash
# Update from anywhere
pipx upgrade recur

# Or, from the repo directory
git pull origin main
pipx reinstall recur
```

## 🚀 Usage

### Quick Start

```bash
recur
```

You'll be presented with the main menu:

```
» Launch
  Tree View
  Units
  Quit
```

Use **arrow keys** to navigate and **Enter** to select.

### Main Menu Options

| Option | Purpose |
|--------|---------|
| **Launch** | View available units and execute one |
| **Tree View** | ASCII visualization of all units and instances |
| **Units** | Add, edit, or delete units and instances |
| **Quit** | Exit the application |

### Working with Units & Instances

#### Creating a Unit
1. Select **Units** → Create a new unit
2. Enter a descriptive name (e.g., "Development Setup")
3. Add instances to the unit

#### Adding Instances
1. Select a unit and choose to add an instance
2. Enter the command to execute (e.g., `code .`, `firefox`)
3. Enter multiple instances as needed

> **Navigation Tip:** While creating units or adding instances, type `b`, `back`, or `break` to return to the previous menu.

### Example Workflow

**Setup a "Work Session" unit:**
- Instance 1: `code ~/my-project` (open VS Code)
- Instance 2: `spotify` (launch Spotify)
- Instance 3: `thunderbird` (open email client)

Then launch all three with a single command!

## 📁 Project Structure

```
recur/
├── LICENSE                 # MIT License
├── pyproject.toml         # Project configuration
├── README.md              # This file
└── recur/
    ├── __init__.py        # Package initialization
    ├── main.py            # Main application logic
    └── storage.py         # JSON storage management
```

## ⚙️ Configuration

### Data Storage Location

Your units and instances are stored in a JSON file at:

```
~/.local/share/recur/units.json
```

**Example JSON structure:**

```json
{
  "units": {
    "Development": {
      "instances": ["code .", "npm start"]
    },
    "Media": {
      "instances": ["firefox", "vlc"]
    }
  }
}
```

### Manual Configuration

You can edit `units.json` directly, but be careful:
- Maintain valid JSON syntax
- Keep the structure consistent with the format above
- Invalid JSON will prevent the app from running

## ⚠️ Limitations & Recommendations

### Known Limitations

| # | Limitation | Details |
|---|-----------|---------|
| 1 | **JSON Corruption** | Manual editing errors can break the app. Edit carefully! |
| 2 | **No Passwords** | Instances requiring passwords/keys won't work yet |
| 3 | **Instance Limit** | Recommended: 5-10 instances per unit (device dependent) |
| 4 | **Linux Only** | Only Linux is natively supported. Windows requires manual configuration |
| 5 | **No Delays** | All instances launch simultaneously (no configurable delay) |
| 6 | **No Window Management** | Window positioning/sizing is uncontrolled |
| 7 | **No CLI Arguments** | Control via command-line flags not yet available |

### Recommendations

- ✅ Keep your instances simple and reliable
- ✅ Test instances individually before grouping them
- ✅ Backup your `units.json` before major edits
- ✅ Use graphical launchers that don't require interaction

## 🗑️ Uninstall

To completely remove Recur:

```bash
# Remove the application
pipx uninstall recur

# Remove configuration and data
rm -rf ~/.local/share/recur

# Remove the repository (optional)
rm -rf ~/path/to/recur
```

> ⚠️ **Warning:** This permanently deletes all your saved units and configurations.

---

**Made with ❤️ for simplicity and ease of use**

[View on GitHub](https://github.com/lukewarm108/recur) • [Report an Issue](https://github.com/lukewarm108/recur/issues)
