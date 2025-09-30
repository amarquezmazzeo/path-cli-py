

def help_command():
    from .commands import COMMANDS
    print("\nNJ PATH CLI Tool (NON-OFFICIAL)")
    print()
    print("Usage:")
    for name in COMMANDS:
        print(f"  {name}: {COMMANDS[name]['description']}")
    print()
