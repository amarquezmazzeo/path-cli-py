import requests
import math
import time

def get_path_data():
    timestamp  = int(round(time.time()*1000,-2))
    url = f"https://www.panynj.gov/bin/portauthority/ridepath.json?timeStamp={timestamp}"
    r = requests.get(url)
    return r.json()['results'] # TODO: Add error handling

def get_departure_eta(station):
    
    data = get_path_data()
    if len(data) <= station:
        return
    
    resultPaths = data[station]
    # Return the raw result paths for the requested station.
    # Tests can mock get_path_data() and assert this return value.
    return resultPaths