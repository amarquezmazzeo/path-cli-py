from .mapp import map_command
from .help import help_command

COMMANDS = {
    'help': {
        'name': 'help',
        'description': "Displays help details",
        'callback': help_command,
    },
    'map': {
        'name': 'map',
        'description': "Displays the NJ PATH map",
        'callback': map_command,  
    }
}