from api.api import get_departure_eta
import pprint

stations = {
    0: {"shortName": "NWK", "longName": "Newark"},
    1: {"shortName": "HAR", "longName": "Harrison"},
    2: {"shortName": "JSQ", "longName": "Journal Sq"},
    3: {"shortName": "GRV", "longName": "Grove St"},
    4: {"shortName": "NEW", "longName": "Newport"},
    5: {"shortName": "EXP", "longName": "Exchange Pl"},
    6: {"shortName": "HOB", "longName": "Hoboken"},
    7: {"shortName": "WTC", "longName": "World Trade Center"},
    8: {"shortName": "CHR", "longName": "Christopher St"},
    9: {"shortName": "09S", "longName": " 9 St"},
    10: {"shortName": "14S", "longName": "14 St"},
    11: {"shortName": "23S", "longName": "23 St"},
    12: {"shortName": "33S", "longName": "33 St"},
}

def eta_command():
    
    # Get input station
    station = -1
    while station not in stations:
        try:
            station = int(
                input(
                    "Select origin station\n"
                    + "\n".join(
                        [
                            f"  {x}.\t{stations[x]['longName']} ({stations[x]['shortName']})"
                            for x in stations
                        ]
                    )
                    + "\n  "
                )
            )
        except ValueError:
            print("\nPlease enter a number...\n")
            continue
        if station not in stations:
            print("\nInvalid station...\n")
    
    # Print to console
    
    long_name = stations[station]['longName']
    print("\n╔══════"+"═"*len(long_name)+"═══════════════╗")
    print(f"╠═════ {long_name} selected ═════╣")
    print("╚══════"+"═"*len(long_name)+"═══════════════╝\n")
    
    departures = get_departure_eta(station)
    for destination in departures:
        print(f"{destination[:2]} {destination[2:]}:")
        for train in departures[destination]:
            etaMin = train['eta'] // 60
            etaSec = train['eta'] % 60
            print(f" - {train['target']} - {etaMin}m {etaSec}s")
    print()
    
    # pprint.pp(get_departure_eta(station))
