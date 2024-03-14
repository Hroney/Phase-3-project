# RPG Campaign Management CLI

This Command Line Interface (CLI) allows users to manage RPG campaigns and Dungeon Masters. With this tool, you can perform various actions such as creating, updating, and deleting campaigns, as well as registering new Dungeon Masters.

## Usage

Upon running the CLI, you will be presented with the main menu. Choose options to manage campaigns, Dungeon Masters, or register new Dungeon Masters. Follow the prompts to perform specific actions such as updating campaign details or registering a new Dungeon Master.

## Requirements

- Python 3.x
- Pipenv (for managing virtual environments)

## Setup

1. Install Pipenv if you haven't already:
```bash
pip install pipenv
```
2. Navigate to the project directory containing Pipfile and run the following command to set up the virtual environment and install dependencies:
```bash
pipenv install
```
3. Activate the pipenv shell:
```bash
pipenv shell
```

## debugging

To use the ipdb debugger included in this project, follow these steps:

Install ipdb:
```bash
pipenv install ipdb
```

Run the debuber file:
```bash
python lib/debug.py
```

Alternatively:

Import ipdb in the code where you want to set breakpoints:
```bash
import ipdb; 
# ... code
ipdb.set_trace()
```

## Structure

- `lib/cli.py`: Main CLI script containing functions for menu navigation and actions.
- `helpers.py`: Helper functions for managing campaigns and Dungeon Masters.

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── campaign
    │   │   ├── _Campaign.py
    │   │   └── Campaign.py
    │   └── dungeon_master
    │       ├── _Dungeon_Master.py
    │       └── Dungeon_Master.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```
#### Please note, `player` and `player_campaign` folders are left overs from a previous build.


## Features

- **Main Menu:** Navigate through different options including managing campaigns, Dungeon Masters, and registering new Dungeon Masters.
- **Campaign Management:** Change campaign names, ownership, and end campaigns.
- **Dungeon Master Management:** Start or cancel campaigns, change between online and in-person modalities, and delete Dungeon Masters.
- **Registration:** Register new Dungeon Masters along with their preferred modality.

