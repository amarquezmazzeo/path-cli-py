# path-cli-py
CLI tool for getting the estimated time of arrival for a given station within the NJ PATH system.

![demo](https://github.com/amarquezmazzeo/path-cli-py/blob/main/demo.gif?raw=true)

# Getting Started

## Pre-requisites

Python 3.12+

## Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/amarquezmazzeo/path-cli-py
   ```

2. **Navigate to the project directory**
   ```bash
   cd path-cli-py
   ```

3. **(Optional) Create and activate a new python venv**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run it! (use help command to get started)**
   ```bash
   python3 main.py <command>

   example: python3 main.py help
   ```

## Usage

Usage:

```help```: Displays help details

```map```: Displays the NJ PATH map

```eta```: Get departures ETA from a given origin
