from colorama import Fore, Style

PATH_MAP = """
                    NJ              HUDSON RIVER       NY

                                       ≈≈≈≈≈
                                       ≈≈≈≈≈         ◖◗ 33 St
                                       ≈≈≈≈≈         ║│
                                       ≈≈≈≈≈         ◖◗ 23 St
                                       ≈≈≈≈≈         ║│
                                       ≈≈≈≈≈         ◖◗ 14 St
                                       ≈≈≈≈≈         ║│
                                       ≈≈≈≈≈         ◖◗  9 St
                                       ≈≈≈≈≈         ║│
                      Hoboken          ≈≈≈≈≈         ║│
                            ●══════════=====════════█╝│ 
                            │  ╭───────-----────────█─╯ 
                            │  │       ≈≈≈≈≈       Christopher St
                   ╭────────█──╯       ≈≈≈≈≈        
                   │        │ Newport  ≈≈≈≈≈        
                   │        │          ≈≈≈≈≈
                   │        │          ≈≈≈≈≈
                   │        │          ≈≈≈≈≈
             █────█╯        ╰█─────────-----────█ World Trade
  Journal Sq █════█══════════█═════════=====════█ Center
             ║   Grove St   Exchange   ≈≈≈≈≈      
    Harrison ●              Pl         ≈≈≈≈≈
             ║                         ≈≈≈≈≈
             ║                         ≈≈≈≈≈
   Newark ●══╝                         ≈≈≈≈≈


  LEGEND:
  ──--│  Hoboken-WTC / JSQ-33rd St 
  ══==║  Hoboken-33rd St / Newark-WTC
  ≈≈≈≈≈  Hudson River
  """

def colorize_map(text):
    # Hudson River - cyan
    text = text.replace('≈≈≈≈≈', f'{Fore.CYAN}≈≈≈≈≈{Style.RESET_ALL}')
    text = text.replace('HUDSON RIVER', f'{Fore.CYAN}HUDSON RIVER{Style.RESET_ALL}')
    
    # Stations - yellow
    text = text.replace('◖◗', f'{Fore.YELLOW}◖◗{Style.RESET_ALL}')
    text = text.replace('█', f'{Fore.YELLOW}█{Style.RESET_ALL}')
    text = text.replace('●', f'{Fore.YELLOW}●{Style.RESET_ALL}')

    # Legend 1 - red
    text = text.replace('═', f'{Fore.RED}═{Style.RESET_ALL}')
    text = text.replace('╝', f'{Fore.RED}╝{Style.RESET_ALL}')
    text = text.replace('=', f'{Fore.RED}={Style.RESET_ALL}')
    text = text.replace('║', f'{Fore.RED}║{Style.RESET_ALL}')

    # Legend 2 - green
    text = text.replace('│', f'{Fore.GREEN}│{Style.RESET_ALL}')
    text = text.replace('╭', f'{Fore.GREEN}╭{Style.RESET_ALL}')
    text = text.replace('-', f'{Fore.GREEN}-{Style.RESET_ALL}')
    text = text.replace('─', f'{Fore.GREEN}─{Style.RESET_ALL}')
    text = text.replace('╯', f'{Fore.GREEN}╯{Style.RESET_ALL}')
    text = text.replace('╰', f'{Fore.GREEN}╰{Style.RESET_ALL}')
    
    # Junctions - white/bright
    # text = text.replace('█', f'{Style.BRIGHT}█{Style.RESET_ALL}')
    
    return text

def map_command():
    print(colorize_map(PATH_MAP))