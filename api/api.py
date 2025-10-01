import requests
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
    
    resultObj = {
        'ToNJ': [],
        'ToNY': []
    }
    
    for destination in resultPaths['destinations']:
        for message in destination['messages']:
            target = f"{message['headSign']} ({message['target']})"
            etaSec = int(message['secondsToArrival'])
            resultObj[destination['label']].append(
                {'target': target,
                 'eta': etaSec}
            )
        
    
    return resultObj
