
import geopandas
#import pyogrio
#import fiona

df = geopandas.read_file('./NYS-Tax-Parcel-Centroid-Points.gdb.zip', layer='NYS_Tax_Parcels_Centroid_Points')

print(df.head())
