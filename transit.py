# FINISHED AT 19-11-2019

import requests, json
from datetime import datetime, date, timedelta
api_id = "API_ID"
api_key = "API_KEY"

def standardroute():
    dep_coords = "52.102182, 5.236826"
    arr_coords = "52.359176, 4.909479"
    url = "https://transit.api.here.com/v3/route.json" # this is the public transit API

    time = datetime(2019,11,20,9,0,0) + timedelta(microseconds=1)
    #transport modes here: https://developer.here.com/documentation/transit/dev_guide/topics/key-concepts-transit-codes.html

    parameters = {"app_id":api_id,
                  "app_code":api_key,
                  "dep":dep_coords,
                  "arr":arr_coords,
                  "time": time.isoformat()}


    result = requests.get(url, params=parameters)
    result = json.loads(result.text)["Res"]
    connections = result["Connections"]["Connection"]
    connection = connections[0]
    duration = datetime.strptime(connection["duration"], "PT%HH%MM").time()
    #print(duration)
    now = time
    timeoffset = datetime.combine(now.date(), duration)
    timedelta1 = datetime.combine(date.min, timeoffset.time()) - datetime.min
    correctedtime = datetime.strptime((now - timedelta1).isoformat(), "%Y-%m-%dT%H:%M:%S.%f")

    parameters = {"app_id": api_id,
                  "app_code": api_key,
                  "dep": dep_coords,
                  "arr": arr_coords,
                  "time": correctedtime.isoformat()}

    result = requests.get(url, params=parameters)
    result = json.loads(result.text)["Res"]
    connections = result["Connections"]["Connection"]
    connection = connections[0]
    duration = datetime.strptime(connection["duration"], "PT%HH%MM").time()
    #print(correctedtime)
    transfers = connection["transfers"]

    departure = connection["Dep"]["time"]
    departuretime = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S")
    if departuretime < datetime.now(): # missed it!
        print("missed the bus, reajusting.")

        parameters = {"app_id": api_id,
                      "app_code": api_key,
                      "dep": dep_coords,
                      "arr": arr_coords,
                      "time": datetime.now().isoformat()}

        result = requests.get(url, params=parameters)
        result = json.loads(result.text)["Res"]
        connections = result["Connections"]["Connection"]
        connection = connections[0]
        duration = datetime.strptime(connection["duration"], "PT%HH%MM").time()
        # print(correctedtime)
        transfers = connection["transfers"]

        departure = connection["Dep"]["time"]
        departuretime = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S")

    arrival = connection["Arr"]
    arrivaltime = datetime.strptime(arrival["time"], "%Y-%m-%dT%H:%M:%S")
    if arrivaltime > time:
        print("too late, reajusting")
        parameters = {"app_id": api_id,
                      "app_code": api_key,
                      "dep": dep_coords,
                      "arr": arr_coords,
                      "time": (correctedtime - (arrivaltime - time)).isoformat()}


        result = requests.get(url, params=parameters)
        result = json.loads(result.text)["Res"]
        connections = result["Connections"]["Connection"]
        connection = connections[0]
        duration = datetime.strptime(connection["duration"], "PT%HH%MM").time()
        # print(correctedtime)
        transfers = connection["transfers"]

        departure = connection["Dep"]["time"]
        departuretime = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S")
        arrival = connection["Arr"]
        arrivaltime = datetime.strptime(arrival["time"], "%Y-%m-%dT%H:%M:%S")

    sections = connection["Sections"]["Sec"]
    try:
        origin_name = sections[0]["Dep"]["Stn"]["name"]
        dep_name = True
    except:
        origin = str(sections[0]["Dep"]["Addr"]["y"]) + "," + str(sections[0]["Dep"]["Addr"]["x"])
        origin_name = origin


    try:
        destination_name = sections[-2]["Arr"]["Stn"]["name"]
        arr_name = True
    except:
        destination = str(sections[-2]["Arr"]["Stn"]["y"]) + "," + str(sections[-2]["Arr"]["Stn"]["x"])
        destination_name = destination

    realdeparture = "hey"
    routestring = "Your route to {} will start at {} on {}, take {}, and has {} transfers.\nYou will arrive at: {}".format(destination_name, origin_name, departure, duration, transfers, arrivaltime)
    print(routestring)
    gmapsurl = "https://www.google.com/maps/dir/?api=1" # see: https://developers.google.com/maps/documentation/urls/guide#forming-the-url

    parameters = {"origin":origin_name,
                  "destination": arr_coords,
                  "travelmode": "transit",
                  "dir_action": "navigate"}
    result = requests.get(url=gmapsurl, params=parameters)
    print(result.url)

    finaldict = {"name": dep_name, "origin": origin_name, "deptime":departuretime}
    print(finaldict)
    return departuretime.isoformat()

def nextbus(time):
    url = "https://transit.api.here.com/v3/multiboard/by_geocoord.json"
    now = datetime.now()

    dep_coords = "52.102182, 5.236826"
    parameters = {"app_id": api_id,
                  "app_code": api_key,
                  "center": dep_coords,
                  "radius": "10",
                  "max": "1",
                  "time": time}
    result = requests.get(url, params=parameters)
    #print(result.url)

    result = json.loads(result.text)["Res"]
    stations = result["MultiNextDepartures"]["MultiNextDeparture"]
    for departure in stations:
        stationname = departure["Stn"]["name"]
        stationdistance = departure["Stn"]["distance"]
        stationduration = datetime.strptime(departure["Stn"]["duration"], "PT%HH%MM%SS")
        stationstring = "Station \"{}\" is {}m away, and it will take {} to walk there.".format(stationname, stationdistance, stationduration)
        print(stationstring)
        for departure in departure["NextDepartures"]["Dep"]:
            departuretime = departure["time"]
            direction = departure["Transport"]["dir"]
            line = departure["Transport"]["name"]
            category = departure["Transport"]["At"]["category"]
            ttl = str(datetime.strptime(departuretime, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(datetime.now().isoformat(),"%Y-%m-%dT%H:%M:%S.%f")).split(".")[0]

            departurestring = "At this station you will find {} {}, going in the direction of \"{}\" on {}. It departs in {}.".format(category, line, direction, departuretime, ttl)
            print(departurestring)
            departuredict = {"category": category, "line": line, "direction": direction, "departuretime": departuretime, "timetoleave": ttl}
        print()

        #finaldict =



time = standardroute()

nextbus(time)


