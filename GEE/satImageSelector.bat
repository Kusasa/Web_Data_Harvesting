C:\Python38-32\python -c "import ee; ee.Initialize()"

C:\Python38-32\python -c "import ee; import pprint; import os; ee.Initialize()", "cape_town = ee.Geometry.Point([18.459778, -34.270836]); satelliteImages = ee.ImageCollection('COPERNICUS/S2_SR'); spatialFiltered = satelliteImages.filterBounds(cape_town); temporalFiltered = spatialFiltered.filterDate('2020-03-09', '2020-04-09'); sorted = temporalFiltered.sort('CLOUD_COVERAGE_ASSESSMENT'); scene = sorted.first(); pp = pprint.PrettyPrinter(depth=4); printout = pp.pprint(scene.getInfo()); file = open('./image_metadata.txt','w+'); file.write(printout); file.close()"

PAUSE