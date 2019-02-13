

entitieslocation = [{'lat': 28.677419 , 'lon': 77.499774}, 
                {"lat": 28.635340, "lon": 77.445700}, 
                {"lat": 28.553905, "lon": 77.099349},
                {"lat":28.622259, "lon":77.239361 }]
latlist = []
longlist = []

for coordinates in entitieslocation:
    latlist.append(coordinates['lat'])
    longlist.append(coordinates['lon'])

nearestlat = lambda userlocation: min(latlist, key=lambda x: abs(x - userlocation))
nearestlong = lambda userlocation: min(longlist, key=lambda x: abs(x - userlocation))

print(nearestlat(28.540600), nearestlong(77.212967))