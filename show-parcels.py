import shapely
import geopandas
from geopandas import GeoSeries
from geopandas import read_file
from geodatasets import get_path
import pyogrio
from pyogrio import read_dataframe, list_drivers, read_info, write_dataframe
from matplotlib import pyplot

#df = geopandas.read_file('./NYS-Tax-Parcel-Centroid-Points.gdb.zip', layer='NYS_Tax_Parcels_Centroid_Points')


# 1. use pyogrio
# 2. read single layer
# 3. Filter by zipcode
#
#
#print(read_info('./NYS-Tax-Parcel-Centroid-Points.gdb.zip', layer='NYS_Tax_Parcels_Centroid_Points'))

#gdf = read_dataframe('./NYS-Tax-Parcel-Centroid-Points.gdb.zip', 
#               layer='NYS_Tax_Parcels_Centroid_Points',
#               #columns=['COUNTY_NAME', 'LOC_ZIP', 'MAIL_ZIP'],
#               columns=['COUNTY_NAME', 'MUNI_NAME', 'SWIS', 'CITYTOWN_SWIS', 'PARCEL_ADDR', 'LOC_ZIP'],
#               #where="LOC_ZIP IN ('10022')",
#               where="COUNTY_NAME IN ('NewYork') AND MUNI_NAME IN ('Manhattan')"
#               #max_features=10
#            )

# 'crs': 'EPSG:2263', 'encoding': 'ISO-8859-1'
nycBackgroundMap = read_dataframe(get_path("nybb"), where="BoroName IN ('Manhattan')").to_crs('EPSG:26918')

#write_dataframe(gdf, "manhatan_parcels.gpkg")

#print(read_info("manhatan_parcels.gpkg"))
manhatanParcels = read_dataframe("manhatan_parcels.gpkg")

point1 = manhatanParcels.geometry[0].buffer(100)
point2 = manhatanParcels.geometry[1000].buffer(1000)

point1 = manhatanParcels.geometry[0]
point2 = manhatanParcels.geometry[1000]
#point1.buffer(100)
#point2.buffer(1000)

# can yhou plot a single point? shapely.plot_points()
# you can plot a geoseries

fig, ax = pyplot.subplots()
nycBackgroundMap.boundary.plot(ax=ax)
#manhatanParcels.plot(ax=ax, color='red')
gs = GeoSeries([point1, point2])
#gs.plot(ax=ax, facecolor="none", edgecolor="black")
gs.plot(ax=ax, color='red', markersize=1)
#shapely.plotting.plot_points(point1, ax=ax)
#shapely.plotting.plot_points(point2, ax=ax)

# grab 10 parcels 
# make into a geroseries
# try having it with different buffers
#
# Im concern geoseries may not allow points with differnt buffers suzes
# You mnay need to assiung a buffer to a point at a time 
#

pyplot.show()
#df = geopandas.read_file('./NYS-Tax-Parcel-Centroid-Points.gdb.zip', rows=10)
