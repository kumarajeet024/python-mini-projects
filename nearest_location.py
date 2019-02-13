tempDataList = [{'lat': 39.7612992 , 'lon': -86.1519681}, 
                {"lat": 39.762241, "lon": -86.158436}, 
                {"lat": 39.7622292, "lon": -86.1578917}]

tempLatList = []
tempLonList = []

for item in tempDataList:
    tempLatList.append(item['lat'])
    tempLonList.append(item['lon'])

closestLatValue = lambda myvalue: min(tempLatList, key=lambda x: abs(x - myvalue))
closestLonValue = lambda myvalue: min(tempLonList, key=lambda x: abs(x - myvalue))

print(closestLatValue(39.7622290), closestLonValue(-86.1519750))