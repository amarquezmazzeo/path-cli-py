#!/usr/bin/env python3

import sys
from commands.commands import COMMANDS

def main():
    args = sys.argv[1:]
    # print("User arguments:", args)

    if len(args) != 1:
        print("Invalid number of arguments")
        COMMANDS['help']['callback']()
        return 

    if args[0] not in COMMANDS:
        print(f"Invalid command '{args[0]}'")
        COMMANDS['help']['callback']()
        return
    
    COMMANDS[args[0]]['callback']()
    return

if __name__ == "__main__":
    main()