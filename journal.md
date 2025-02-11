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


