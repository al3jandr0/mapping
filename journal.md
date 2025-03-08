# Journal of the project (that has no name yet)

- [x] Instsall latest python
- [x] Install .venv
- [ ] plot parcel center data

- [ ] Figure out how to create points of interest distributions
- [ ] Figure out which format or db is better for area (circle) searching

## Feb 10th 2025

The first challenge I encounter is that the parcels dataset may be too large.
The archive is half a gig but my poor computer get to full utilization of one core, and the memory is less than 1G away from full.
It would be great to edit the dataset to include only manhattans or nyc data as suppose to the entire state.

How can I edit the dataset efficiently?


some people online say that pyogrio is faster, so lets try that. Keep in mind the goal here would be to truncate the data to work only
with NYC dataset. which is another question in on itself.

I think I can filter the dataset (assuming I can load it) in the following way.
1) find the circle that covers all of NYC (manhattan preferable since it is smaller)
2) then filter out any point not in the ciercle

I'm thinking there may be a way to partially load the data as suppose of loading it all into memory for processing

Computer chrashed :/


This is what I came up with thus far. lol mimi-baby steps
```
import geopandas
#import pyogrio
#import fiona

df = geopandas.read_file('./NYS-Tax-Parcel-Centroid-Points.gdb.zip', layer='NYS_Tax_Parcels_Centroid_Points')

print(df.head())
```

The hardest part is to start and at first is slow. I did a bunch of reading of GIS and I spent time looking for datasets and it is time to get hands dirty. One can easily get stuck in the reasearch / learning phase and not build anything.  I think most of my projects die in that nacent phase.


Also, I bought a pull up bar; one of those that go on a doorway. It has to be my best purchase ever.  Im doing pull as I type this (Im typing while resting in between sets).  The biggest challenge to getting started with this project is my shorten attention span.  I reach for my phone, or midnlesly brose the web all the time; news, x.com, youtube, stupid pokemon tcg game. Perhaps this pull up bar will be my escape route. Anytime I feel like reaching to the phone boom - pull up time.


## Feb 16th 2025

It has been a week. Work was busy during the past few days.

Anyways It appears pyogrio offers "pushdown" filters when reading data, so not only can I choose which columns to read but also which rows.
I can fiter with a mash shaped as apoligon. Thos shoould work to give me a subset of the data. 

Lets aim to lad manhattan only, and see whether my computer can handle that.

First, I need to find out the "schema" of the data to know which column to filter by. I could prob figure that out from metadata and loading the first few rows for all columns.

Then, I need to compute which polygon encompases all of manhattan. Google maps and some arithmetic should suffice here.

Then test :)

alright. lets go


btw geopandas also offers a slice function to "paginate" reads. But no filters as far as I can see


This is what the first 10 rows look like
Head
  COUNTY_NAME MUNI_NAME    SWIS             PARCEL_ADDR  ... DUP_GEO CALC_ACRES ORIG_FID                        geometry
0      Albany    Albany  010100           190 Karner Rd  ...    None   9.397254        1   POINT (592664.194 4730435.14)
1      Albany    Albany  010100  Rear 41 Madison Ave Ex  ...    None   4.637584        2   POINT (592044.38 4730316.013)
2      Albany    Albany  010100      41 Madison Ave Ext  ...    None  11.872292        3   POINT (591802.801 4730115.64)
3      Albany    Albany  010100      21 Madison Ave Ext  ...    None  30.199503        4  POINT (592115.987 4729904.671)
4      Albany    Albany  010100      18 Madison Ave Ext  ...    None   2.207024        5   POINT (591988.98 4729724.878)


This is how you can filter by geometry using pyogrio
https://pyogrio.readthedocs.io/en/latest/introduction.html#filter-records-by-a-geometry
```
mask = shapely.Polygon(([-80,8], [-80, 10], [-85,10], [-85,8], [-80,8]))

read_dataframe('ne_10m_admin_0_countries.shp', mask=mask)
```

shapely Vs bbox? w

You can use the bbox parameter to select only those features that intersect with the bbox.
```
read_dataframe('ne_10m_admin_0_countries.shp', bbox=(-140, 20, -100, 40))
```
You can use the mask parameter to select only those features that intersect with a Shapely (>= 2.0) geometry.

I have a point... I suppose intersect means cover? what's the right term? anyways I should try with first. Also, mayebe you can filter by zipcode or county first. 

# Feb 28th 2025

MAIL_ZIP is bananas
pyogrio is the shit
+ dep matplotlib

It appears I would have to find out what is the most common / convenient projection out there

did I say pyogrio is the shit?


Alright, I got to read the parcels data whith pushdown so not to load all the data into memory.
and I can plot it over a manhattan (and nyc) map :)

Reminder of why Im doing all this instead of getting started with google.

I need to validate that im getting correct data from google, rather that I am requesting data correctly (google is prolly right). So by having data sets of cities I can visially and programatically assert some of my assumptions of google's data.

And I plan to use this data to validate the efficienncy of my crawling algorithm.

I can test it agains a few cities and if it looks good, then I can assume it works for all if not most cities (Im sure there will be edgecases, but many should be taken care of)


Also for testing I intend to create a dummy Google data service. I could later one use the Google data instead, but first I will be using dummy. The reason for going through this trouble is that Google API is not free 


# March 3rd 2025

I should store only manhattan values as the desired crs. That would make iterations faster, right now loading from the new york state dataset is slow - I think becasue the data is large (I dont use most of it anyways)


# March 4th 2025

I'm having troubles drawing circles using buffers. Geoseries buffers applies the same buffer size to all elements of the series.
Supposedly shapely allows to set a to a single point, but it seems not to take effect, or at least not being picked up by the plotting methof the Geoseries. 

Nvm, the buffer method returns a new object wich I needed to assing

Ok. I figured how to draw circles with different radious. If I wan to draw the center dot, that would have to go on a separate plot

````
point1 = manhatanParcels.geometry[0].buffer(100)
point2 = manhatanParcels.geometry[1000].buffer(1000)
gs = GeoSeries([point1, point2])
gs.plot(ax=ax, facecolor="none", edgecolor="black")
````

- Why do the Points show so big. Hhen I do centroid it looks sizeable when I expected it to be a singel pixel ?


# March 5th 2025

Specifying markersize when plotting changes the thickness of the point. Setting it to 1 makes it nice and small


I can determine whether a point is covered or not using concave_hull although it remains tbd whether it considers buffers or not.

I can determine whether a point is in a hole by using intersetcs

I'm still having trouble how to figure out where to draw a circle
The idea is to choose the the closest point to the centroid as a touching point for teh circle, but there could be many such points. How to choose one?


How about firs fiure out the closes point. 
Determine if a hole  - these are handled specialy
You could also determine whether a point is on a wedge - but Idk what to do with this info yet.

Then you could look for the point farthest away

Why do you have to reverse engineer the thing, cant you remember the circles drawn? It is a geometry problem isn't it?
- I think so though variable circle sizes makes it tricky aka I have not figure out how



```
>>> pointsDf
  name                geometry
0    A  POINT (-87.789 41.976)
1    B  POINT (-87.482 41.677)
2    C  POINT (-87.599 41.908)
3    D  POINT (-87.598 41.708)
4    E  POINT (-87.643 41.675)
>>> pointsDf.buffer(100)
<stdin>:1: UserWarning: Geometry is in a geographic CRS. Results from 'buffer' are likely incorrect. Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.

0    POLYGON ((12.211 41.976, 11.72947 32.17429, 10...
1    POLYGON ((12.518 41.677, 12.03647 31.87529, 10...
2    POLYGON ((12.401 41.908, 11.91947 32.10629, 10...
3    POLYGON ((12.402 41.708, 11.92047 31.90629, 10...
4    POLYGON ((12.357 41.675, 11.87547 31.87329, 10...
dtype: geometry
```

```
>>> dfWitRadious
{'name': ['A', 'B', 'C', 'D', 'E'], 'radius': [10, 50, 100, 20, 500]}

>>> [p.buffer(r) for p, r in zip(points, dfWitRadious['radius'])]
[<POLYGON ((-77.789 41.976, -77.837 40.996, -77.981 40.025, -78.22 39.073, -7...>, <POLYGON ((-37.482 41.677, -37.723 36.776, -38.443 31.922, -39.635 27.163, -...>, <POLYGON ((12.401 41.908, 11.919 32.106, 10.48 22.399, 8.095 12.88, 4.789 3....>, <POLYGON ((-67.598 41.708, -67.694 39.748, -67.982 37.806, -68.459 35.902, -...>, <POLYGON ((412.357 41.675, 409.949 -7.334, 402.75 -55.87, 390.827 -103.467, ...>]

>>> circles = gpd.GeoDataFrame(dfWitRadious, geometry=pointsWithRadius, crs = 'EPSG:4326')
>>> circles
  name  radius                                           geometry
0    A      10  POLYGON ((-77.789 41.976, -77.83715 40.99583, ...
1    B      50  POLYGON ((-37.482 41.677, -37.72276 36.77614, ...
2    C     100  POLYGON ((12.401 41.908, 11.91947 32.10629, 10...
3    D      20  POLYGON ((-67.598 41.708, -67.69431 39.74766, ...
4    E     500  POLYGON ((412.357 41.675, 409.94936 -7.33357, ...
```

I learnt that callin buffer on a df or series it has teh same effect of calling buffer on each point indiviualy
The points become poligons, the dontb belend together unless you union them all 


Next, how to find out point on the boundary that's closes to the centroind.

Would union_all <- combines all points
.boundary <- gets boundary. tets how it looks
.boundary VS concave_hull What's the difference?
What's their resolution?
Plot them and see 

