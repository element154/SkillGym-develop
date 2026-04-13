## Source: https://geopandas.org/en/stable/docs/user_guide.html

# User guide#

The user guide covers different parts of basic usage of GeoPandas. Each page focuses on a single topic and outlines how it is implemented in GeoPandas, with reproducible examples.

If you don’t know anything about GeoPandas, start with the Introduction to GeoPandas.

Advanced topics can be found in the Advanced Guide and further specification in the API Reference.

## Source: https://geopandas.org/en/stable/docs/user_guide/data_structures.html

# Data structures#

GeoPandas implements two main data structures, a `GeoSeries`

and a
`GeoDataFrame`

. These are subclasses of `pandas.Series`

and
`pandas.DataFrame`

, respectively.

## GeoSeries#

A `GeoSeries`

is essentially a vector where each entry in the vector
is a set of shapes corresponding to one observation. An entry may consist
of only one shape (like a single polygon) or multiple shapes that are
meant to be thought of as one observation (like the many polygons that
make up the State of Hawaii or a country like Indonesia).

GeoPandas has three basic classes of geometric objects (which are actually Shapely objects):

Points / Multi-Points

Lines / Multi-Lines

Polygons / Multi-Polygons

Note that all entries in a `GeoSeries`

do not need to be of the same geometric type, although certain export operations will fail if this is not the case.

### Overview of attributes and methods#

The `GeoSeries`

class implements nearly all of the attributes and
methods of Shapely objects. When applied to a `GeoSeries`

, they
will apply elementwise to all geometries in the series. Binary
operations can be applied between two `GeoSeries`

, in which case the
operation is carried out elementwise. The two series will be aligned
by matching indices. Binary operations can also be applied to a
single geometry, in which case the operation is carried out for each
element of the series with that geometry. In either case, a
`Series`

or a `GeoSeries`

will be returned, as appropriate.

A short summary of a few attributes and methods for GeoSeries is presented here, and a full list can be found in the GeoSeries API reference. There is also a family of methods for creating new shapes by expanding existing shapes or applying set-theoretic operations like “union” described in Geometric manipulations.

#### Attributes#

`area`

: shape area (units of projection – see projections)`bounds`

: tuple of max and min coordinates on each axis for each shape`total_bounds`

: tuple of max and min coordinates on each axis for entire GeoSeries`geom_type`

: type of geometry.`is_valid`

: tests if coordinates make a shape that is reasonable geometric shape according to the Simple Feature Access standard.

#### Basic methods#

`distance()`

: returns`Series`

with minimum distance from each entry to`other`

`representative_point()`

: returns`GeoSeries`

of points that are guaranteed to be within each geometry. It does**NOT**return centroids.`to_crs()`

: change coordinate reference system. See projections

#### Relationship tests#

`geom_equals_exact()`

: is shape the same as`other`

(up to a specified decimal place tolerance)`contains()`

: is shape contained within`other`

`intersects()`

: does shape intersect`other`

## GeoDataFrame#

A `GeoDataFrame`

is a tabular data structure that contains a `GeoSeries`

.

The most important property of a `GeoDataFrame`

is that it always has one `GeoSeries`

column that
holds a special status - the “active geometry column”. When a spatial method is applied to a
`GeoDataFrame`

(or a spatial attribute like `area`

is called), these operations will always act on the
active geometry column.

The active geometry column – no matter the name of the corresponding `GeoSeries`

–
can be accessed through the `geometry`

attribute (`gdf.geometry`

),
and the name of the `geometry`

column can be found by typing `gdf.geometry.name`

or `gdf.active_geometry_name`

.

A `GeoDataFrame`

may also contain other columns with geometrical (shapely) objects, but only one column can be the active geometry at a time. To change which column is the active geometry column, use the `GeoDataFrame.set_geometry()`

method.

An example using the `geoda.malaria`

dataset from `geodatasets`

containing the counties of Colombia:

```
In [1]: import geodatasets
In [2]: colombia = geopandas.read_file(geodatasets.get_path('geoda.malaria'))
In [3]: colombia.head()
Out[3]:
ID ADM0 ... RP2005 geometry
0 1 COLOMBIA ... 61773 POLYGON ((-71.32639 11.84789, -71.33579 11.855...
1 2 COLOMBIA ... 36465 POLYGON ((-72.42191 11.79824, -72.4198 11.795,...
2 3 COLOMBIA ... 18368 POLYGON ((-72.1891 11.5242, -72.1833 11.5323, ...
3 4 COLOMBIA ... 7566 POLYGON ((-72.638 11.3679, -72.6259 11.3499, -...
4 5 COLOMBIA ... 9343 POLYGON ((-74.77489 10.93158, -74.7753 10.9338...
[5 rows x 51 columns]
# Plot countries
In [4]: colombia.plot(markersize=.5);
```

Currently, the column named “geometry” with county borders is the active geometry column:

```
In [5]: colombia.geometry.name
Out[5]: 'geometry'
```

You can also rename this column to “borders”:

```
In [6]: colombia = colombia.rename_geometry('borders')
In [7]: colombia.geometry.name
Out[7]: 'borders'
```

Now, you create centroids and make it the geometry:

```
In [8]: colombia['centroid_column'] = colombia.centroid
In [9]: colombia = colombia.set_geometry('centroid_column')
In [10]: colombia.plot();
```

**Note:** A `GeoDataFrame`

keeps track of the active column by name, so if you rename the active geometry column, you must also reset the geometry:

```
gdf = gdf.rename(columns={'old_name': 'new_name'}).set_geometry('new_name')
```

**Note 2:** Somewhat confusingly, by default when you use the `read_file()`

command, the column containing spatial objects from the file is named “geometry” by default, and will be set as the active geometry column. However, despite using the same term for the name of the column and the name of the special attribute that keeps track of the active column, they are distinct. You can easily shift the active geometry column to a different `GeoSeries`

with the `set_geometry()`

command. Further, `gdf.geometry`

will always return the active geometry column, *not* the column named `geometry`

. If you wish to call a column named “geometry”, and a different column is the active geometry column, use `gdf['geometry']`

, not `gdf.geometry`

.

### Attributes and methods#

Any of the attributes calls or methods described for a `GeoSeries`

will work on a `GeoDataFrame`

– they are just applied to the active geometry column `GeoSeries`

.

However, `GeoDataFrames`

also have a number few extra methods for:

## Display options#

GeoPandas has an `options`

attribute with global configuration attributes:

```
In [11]: import geopandas
In [12]: geopandas.options
Out[12]:
Options(
display_precision: None [default: None]
The precision (maximum number of decimals) of the coordinates in the
WKT representation in the Series/DataFrame display. By default (None),
it tries to infer and use 3 decimals for projected coordinates and 5
decimals for geographic coordinates.
use_pygeos: False [default: False]
Deprecated option previously used to enable PyGEOS. It will be removed
in GeoPandas 1.1.
io_engine: None [default: None]
The default engine for ``read_file`` and ``to_file``. Options are
'pyogrio' and 'fiona'.
)
```

The `geopandas.options.display_precision`

option can control the number of
decimals to show in the display of coordinates in the geometry column.
In the `colombia`

example of above, the default is to show 5 decimals for
geographic coordinates:

```
In [13]: colombia['centroid_column'].head()
Out[13]:
0 POINT (-71.74594 12.00885)
1 POINT (-72.56514 11.58174)
2 POINT (-72.35203 11.32204)
3 POINT (-73.14121 11.15251)
4 POINT (-74.64555 10.88454)
Name: centroid_column, dtype: geometry
```

If you want to change this, for example to see more decimals, you can do:

```
In [14]: geopandas.options.display_precision = 9
In [15]: colombia['centroid_column'].head()
Out[15]:
0 POINT (-71.745940217 12.008854228)
1 POINT (-72.565144214 11.581744777)
2 POINT (-72.352030378 11.322036612)
3 POINT (-73.1412073 11.152507044)
4 POINT (-74.645551117 10.884543716)
Name: centroid_column, dtype: geometry
```

## Source: https://geopandas.org/en/stable/docs/user_guide/io.html

# Reading and writing files#

## Reading spatial data#

GeoPandas can read almost any vector-based spatial data format including ESRI
shapefile, GeoJSON files and more using the `geopandas.read_file()`

command:

```
geopandas.read_file(...)
```

which returns a GeoDataFrame object. This is possible because GeoPandas makes use of the massive open-source program called GDAL/OGR designed to facilitate spatial data transformations, through the Python packages Pyogrio or Fiona, which both provide bindings to GDAL.

Any arguments passed to `geopandas.read_file()`

after the file name will be
passed directly to `pyogrio.read_dataframe()`

or `fiona.open()`

, which
does the actual data importation.
In general, `geopandas.read_file()`

is pretty smart and should do what you want
without extra arguments, but for more help, type:

```
import pyogrio; help(pyogrio.read_dataframe)
import fiona; help(fiona.open)
```

Note

For faster data reading, pass `use_arrow=True`

when using the default pyogrio engine. This can be 2-4 times faster than the default reading behavior and works with all drivers. See pyogrio.read_dataframe for full details.

Note that this requires the `pyarrow`

dependency to exist in your environment.

Among other things, one can explicitly set the driver (shapefile, GeoJSON) with
the `driver`

keyword, or pick a single layer from a multi-layered file with
the `layer`

keyword:

```
countries_gdf = geopandas.read_file("package.gpkg", layer='countries')
```

If you have a file with multiple layers, you can list them using
`geopandas.list_layers()`

. Note that this function requires Pyogrio.

GeoPandas can also load resources directly from a web URL, for example for GeoJSON files from geojson.xyz:

```
url = "http://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"
df = geopandas.read_file(url)
```

You can also load ZIP files that contain your data:

```
zipfile = "zip:///Users/name/Downloads/cb_2017_us_state_500k.zip"
states = geopandas.read_file(zipfile)
```

If the dataset is in a folder in the ZIP file, you have to append its name:

```
zipfile = "zip:///Users/name/Downloads/gadm36_AFG_shp.zip!data"
```

If there are multiple datasets in a folder in the ZIP file, you also have to specify the filename:

```
zipfile = "zip:///Users/name/Downloads/gadm36_AFG_shp.zip!data/gadm36_AFG_1.shp"
```

It is also possible to read any file-like objects with a `read()`

method, such
as a file handler (e.g. via built-in `open()`

function) or `StringIO`

:

```
filename = "test.geojson"
file = open(filename)
df = geopandas.read_file(file)
```

File-like objects from fsspec can also be used to read data, allowing for any combination of storage backends and caching supported by that project:

```
path = "simplecache::http://download.geofabrik.de/antarctica-latest-free.shp.zip"
with fsspec.open(path) as file:
df = geopandas.read_file(file)
```

You can also read path objects:

```
import pathlib
path_object = pathlib.Path(filename)
df = geopandas.read_file(path_object)
```

### Using Arrow for faster reading#

For faster data reading, pass `use_arrow=True`

when using the default pyogrio engine. This can be 2-4 times faster than the default reading behavior and works with all drivers. See pyogrio.read_dataframe for full details.

It is also possible to enable this by default by setting the environment variable `PYOGRIO_USE_ARROW=1`

(which will also enable writing data using arrow).

Note that this requires the `pyarrow`

dependency to exist in your environment.

### Reading subsets of the data#

Since geopandas is powered by GDAL, you can take advantage of pre-filtering when loading
in larger datasets. This can be done geospatially with a geometry or bounding box. You
can also filter rows loaded with a slice. Read more at `geopandas.read_file()`

.

#### Geometry filter#

The geometry filter only loads data that intersects with the geometry.

```
import geodatasets
gdf_mask = geopandas.read_file(
geodatasets.get_path("geoda.nyc")
)
gdf = geopandas.read_file(
geodatasets.get_path("geoda.nyc education"),
mask=gdf_mask[gdf_mask.name=="Coney Island"],
)
```

#### Bounding box filter#

The bounding box filter only loads data that intersects with the bounding box.

```
bbox = (
1031051.7879884212, 224272.49231459625, 1047224.3104931959, 244317.30894023244
)
gdf = geopandas.read_file(
geodatasets.get_path("nybb"),
bbox=bbox,
)
```

#### Row filter#

Filter the rows loaded in from the file using an integer (for the first n rows) or a slice object.

```
gdf = geopandas.read_file(
geodatasets.get_path("geoda.nyc"),
rows=10,
)
gdf = geopandas.read_file(
geodatasets.get_path("geoda.nyc"),
rows=slice(10, 20),
)
```

#### Field/column filters#

Load in a subset of fields from the file using the `columns`

keyword
(this requires pyogrio or Fiona 1.9+):

```
gdf = geopandas.read_file(
geodatasets.get_path("geoda.nyc"),
columns=["name", "rent2008", "kids2000"],
)
```

Skip loading geometry from the file:

Note

Returns `pandas.DataFrame`

```
pdf = geopandas.read_file(
geodatasets.get_path("geoda.nyc"),
ignore_geometry=True,
)
```

#### SQL WHERE filter#

Added in version 0.12.

Load in a subset of data with a SQL WHERE clause.

Note

Requires Fiona 1.9+ or the pyogrio engine.

```
gdf = geopandas.read_file(
geodatasets.get_path("geoda.nyc"),
where="subborough='Coney Island'",
)
```

### Supported drivers / file formats#

When using pyogrio, all drivers supported by the GDAL installation are enabled, and you can check those with:

```
import pyogrio; pyogrio.list_drivers()
```

where the values indicate whether reading, writing or both are supported for a given driver. Fiona only exposes a default subset of drivers. To display those, type:

```
import fiona; fiona.supported_drivers
```

There is a list of available drivers which are unexposed by default but may be supported (depending on the GDAL-build). You can activate these at runtime by updating the supported_drivers dictionary like:

```
fiona.supported_drivers["NAS"] = "raw"
```

## Writing spatial data#

GeoDataFrames can be exported to many different standard formats using the
`geopandas.GeoDataFrame.to_file()`

method.
For a full list of supported formats, type `import pyogrio; pyogrio.list_drivers()`

.

In addition, GeoDataFrames can be uploaded to PostGIS database (starting with GeoPandas 0.8)
by using the `geopandas.GeoDataFrame.to_postgis()`

method.

Note

For faster data writing, pass `use_arrow=True`

when using the default pyogrio engine. This can be 2-4 times faster than the default writing behavior and works with all drivers. See pyogrio.write_dataframe for full details.

Note that this requires the `pyarrow`

dependency to exist in your environment.

Note

GeoDataFrame can contain more field types than supported by most of the file formats. For example tuples or lists can be easily stored in the GeoDataFrame, but saving them to e.g. GeoPackage or Shapefile will raise a ValueError. Before saving to a file, they need to be converted to a format supported by a selected driver.

Note

One GeoDataFrame can contain multiple geometry (GeoSeries) columns, but most standard GIS file formats, e.g. GeoPackage or ESRI Shapefile, support only a single geometry column. To store multiple geometry columns, non-active GeoSeries need to be converted to an alternative representation like well-known text (WKT) or well-known binary (WKB) before saving to file. Alternatively, they can be saved as an Apache (Geo)Parquet or Feather file, both of which support multiple geometry columns natively.

**Writing to Shapefile**:

```
countries_gdf.to_file("countries.shp")
```

**Writing to Shapefile with via Arrow**:

```
countries_gdf.to_file("countries.shp", use_arrow=True)
```

**Writing to GeoJSON**:

```
countries_gdf.to_file("countries.geojson", driver='GeoJSON')
```

**Writing to GeoPackage**:

```
countries_gdf.to_file("package.gpkg", layer='countries', driver="GPKG")
cities_gdf.to_file("package.gpkg", layer='cities', driver="GPKG")
```

**Writing with multiple geometry columns**:

```
countries_gdf["country_center"] = countries_gdf["geometry"].centroid
# Line below fails because GeoJSON can't contain multiple geometry columns
# countries_gdf.to_file("countries.geojson", driver='GeoJSON')
countries_gdf["country_center"] = countries_gdf["country_center"].to_wkt()
countries_gdf.to_file("countries.geojson", driver='GeoJSON')
```

For multi-layer formats such as GeoPackage, it is possible to write additional geometry columns to separate layers instead of saving them as WKT or WKB within a single layer.

## Spatial databases#

GeoPandas can also get data from a PostGIS database using the
`geopandas.read_postgis()`

command.

Writing to PostGIS:

```
from sqlalchemy import create_engine
db_connection_url = "postgresql://myusername:mypassword@myhost:5432/mydatabase";
engine = create_engine(db_connection_url)
countries_gdf.to_postgis("countries_table", con=engine)
```

## Apache Parquet and Feather file formats#

Added in version 0.8.0.

GeoPandas supports writing and reading the Apache Parquet (GeoParquet) and Feather file formats.

Apache Parquet is an efficient, columnar storage format (originating from the Hadoop ecosystem). It is a widely used binary file format for tabular data. The Feather file format is the on-disk representation of the Apache Arrow memory format, an open standard for in-memory columnar data.

The `geopandas.read_parquet()`

, `geopandas.read_feather()`

,
`geopandas.GeoDataFrame.to_parquet()`

and `geopandas.GeoDataFrame.to_feather()`

methods
enable fast roundtrip from GeoPandas to those binary file formats, preserving
the spatial information.

Note

The GeoParquet specification is developed at: opengeospatial/geoparquet.

By default, the latest
version is used when writing files, but older versions can be specified using
the `schema_version`

keyword. GeoPandas supports reading files
encoded using any GeoParquet version.

## Source: https://geopandas.org/en/stable/docs/user_guide/indexing.html

# Indexing and selecting data#

GeoPandas inherits the standard pandas methods for indexing/selecting data. This includes label based indexing with `loc`

and integer position based indexing with `iloc`

, which apply to both `GeoSeries`

and `GeoDataFrame`

objects. For more information on indexing/selecting, see the pandas documentation.

In addition to the standard pandas methods, GeoPandas also provides
coordinate based indexing with the `cx`

indexer, which slices using a bounding
box. Geometries in the `GeoSeries`

or `GeoDataFrame`

that intersect the
bounding box will be returned.

Using the `geoda.chile_labor`

dataset, you can use this functionality to quickly select parts
of Chile whose boundaries extend south of the -50 degrees latitude. You can first check the original GeoDataFrame.

```
In [1]: import geodatasets
In [2]: chile = geopandas.read_file(geodatasets.get_path('geoda.chile_labor'))
In [3]: chile.plot(figsize=(8, 8));
```

And then select only the southern part of the country.

```
In [4]: southern_chile = chile.cx[:, :-50]
In [5]: southern_chile.plot(figsize=(8, 8));
```

## Source: https://geopandas.org/en/stable/docs/user_guide/mapping.html

# Mapping and plotting tools#

GeoPandas provides a high-level interface to the matplotlib library for making maps. Mapping shapes is as easy as using the `plot()`

method on a `GeoSeries`

or `GeoDataFrame`

.

Loading some example data:

```
In [1]: import geodatasets
In [2]: chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
In [3]: groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))
```

You can now plot those GeoDataFrames:

```
# Examine the chicago GeoDataFrame
In [4]: chicago.head()
Out[4]:
community ... geometry
0 DOUGLAS ... MULTIPOLYGON (((-87.609140876 41.844692503, -8...
1 OAKLAND ... MULTIPOLYGON (((-87.592152839 41.816929346, -8...
2 FULLER PARK ... MULTIPOLYGON (((-87.628798237 41.801893034, -8...
3 GRAND BOULEVARD ... MULTIPOLYGON (((-87.606708126 41.816813771, -8...
4 KENWOOD ... MULTIPOLYGON (((-87.592152839 41.816929346, -8...
[5 rows x 9 columns]
# Basic plot, single color
In [5]: chicago.plot();
```

Note that in general, any options one can pass to pyplot in matplotlib (or style options that work for lines) can be passed to the `plot()`

method.

## Choropleth maps#

GeoPandas makes it easy to create Choropleth maps (maps where the color of each shape is based on the value of an associated variable). Simply use the plot command with the `column`

argument set to the column whose values you want used to assign colors.

```
# Plot by population
In [6]: chicago.plot(column="POP2010");
```

### Creating a legend#

When plotting a map, one can enable a legend using the `legend`

argument:

```
# Plot population estimates with an accurate legend
In [7]: chicago.plot(column='POP2010', legend=True);
```

The following example plots the color bar below the map and adds its label using `legend_kwds`

:

```
# Plot population estimates with an accurate legend
In [8]: chicago.plot(
...: column="POP2010",
...: legend=True,
...: legend_kwds={"label": "Population in 2010", "orientation": "horizontal"},
...: );
...:
```

However, the default appearance of the legend and plot axes may not be desirable. One can define the plot axes (with `ax`

) and the legend axes (with `cax`

) and then pass those in to the `plot()`

call. The following example uses `mpl_toolkits`

to horizontally align the plot axes and the legend axes and change the width:

```
# Plot population estimates with an accurate legend
In [9]: import matplotlib.pyplot as plt
In [10]: from mpl_toolkits.axes_grid1 import make_axes_locatable
In [11]: fig, ax = plt.subplots(1, 1)
In [12]: divider = make_axes_locatable(ax)
In [13]: cax = divider.append_axes("bottom", size="5%", pad=0.1)
In [14]: chicago.plot(
....: column="POP2010",
....: ax=ax,
....: legend=True,
....: cax=cax,
....: legend_kwds={"label": "Population in 2010", "orientation": "horizontal"},
....: );
....:
```

### Choosing colors#

You can also modify the colors used by `plot()`

with the `cmap`

option. For a full list of colormaps, see Choosing Colormaps in Matplotlib.

```
In [15]: chicago.plot(column='POP2010', cmap='OrRd');
```

To make the color transparent for when you just want to show the boundary, you have two options. One option is to do `chicago.plot(facecolor="none", edgecolor="black")`

. However, this can cause a lot of confusion because `"none"`

and `None`

are different in the context of using `facecolor`

and they do opposite things. `None`

does the “default behavior” based on matplotlib, and if you use it for `facecolor`

, it actually adds a color. The second option is to use `chicago.boundary.plot()`

. This option is more explicit and clear.:

```
In [16]: chicago.boundary.plot();
```

The way color maps are scaled can also be manipulated with the `scheme`

option (if you have `mapclassify`

installed, which can be accomplished via `conda install -c conda-forge mapclassify`

). The `scheme`

option can be set to any scheme provided by mapclassify (e.g. ‘box_plot’, ‘equal_interval’,
‘fisher_jenks’, ‘fisher_jenks_sampled’, ‘headtail_breaks’, ‘jenks_caspall’, ‘jenks_caspall_forced’, ‘jenks_caspall_sampled’, ‘max_p_classifier’, ‘maximum_breaks’, ‘natural_breaks’, ‘quantiles’, ‘percentiles’, ‘std_mean’ or ‘user_defined’). Arguments can be passed in classification_kwds dict. See the mapclassify documentation for further details about these map classification schemes.

```
In [17]: chicago.plot(column='POP2010', cmap='OrRd', scheme='quantiles');
```

### Missing data#

In some cases one may want to plot data which contains missing values - for some features one simply does not know the value. Geopandas (from the version 0.7) by defaults ignores such features.

```
In [18]: import numpy as np
In [19]: chicago.loc[np.random.choice(chicago.index, 30), 'POP2010'] = np.nan
In [20]: chicago.plot(column='POP2010');
```

However, passing `missing_kwds`

one can specify the style and label of features containing None or NaN.

```
In [21]: chicago.plot(column='POP2010', missing_kwds={'color': 'lightgrey'});
In [22]: chicago.plot(
....: column="POP2010",
....: legend=True,
....: scheme="quantiles",
....: figsize=(15, 10),
....: missing_kwds={
....: "color": "lightgrey",
....: "edgecolor": "red",
....: "hatch": "///",
....: "label": "Missing values",
....: },
....: );
....:
```

### Other map customizations#

Maps usually do not have to have axis labels. You can turn them off using `set_axis_off()`

or `axis("off")`

axis methods.

```
In [23]: ax = chicago.plot()
In [24]: ax.set_axis_off();
```

## Maps with layers#

There are two strategies for making a map with multiple layers – one more succinct, and one that is a little more flexible.

Before combining maps, however, remember to always ensure they share a common CRS (so they will align).

```
# Look at capitals
# Note use of standard `pyplot` line style options
In [25]: groceries.plot(marker='*', color='green', markersize=5);
# Check crs
In [26]: groceries = groceries.to_crs(chicago.crs)
# Now you can overlay over the outlines
```

**Method 1**

```
In [27]: base = chicago.plot(color='white', edgecolor='black')
In [28]: groceries.plot(ax=base, marker='o', color='red', markersize=5);
```

**Method 2: Using matplotlib objects**

```
In [29]: fig, ax = plt.subplots()
In [30]: chicago.plot(ax=ax, color='white', edgecolor='black')
Out[30]: <Axes: >
In [31]: groceries.plot(ax=ax, marker='o', color='red', markersize=5)
Out[31]: <Axes: >
In [32]: plt.show();
```

### Control the order of multiple layers in a plot#

When plotting multiple layers, use `zorder`

to take control of the order of layers being plotted.
The lower the `zorder`

is, the lower the layer is on the map and vice versa.

Without specified `zorder`

, cities (Points) gets plotted below world (Polygons), following the default order based on geometry types.

```
In [33]: ax = groceries.plot(color='k')
In [34]: chicago.plot(ax=ax);
```

You can set the `zorder`

for cities higher than for world to move it of top.

```
In [35]: ax = groceries.plot(color='k', zorder=2)
In [36]: chicago.plot(ax=ax, zorder=1);
```

## Pandas plots#

Plotting methods also allow for different plot styles from pandas
along with the default `geo`

plot. These methods can be accessed using
the `kind`

keyword argument in `plot()`

, and include:

`geo`

for mapping`line`

for line plots`bar`

or`barh`

for bar plots`hist`

for histogram`box`

for boxplot`kde`

or`density`

for density plots`area`

for area plots`scatter`

for scatter plots`hexbin`

for hexagonal bin plots`pie`

for pie plots

```
In [37]: chicago.plot(kind="scatter", x="POP2010", y="POP2000")
Out[37]: <Axes: xlabel='POP2010', ylabel='POP2000'>
```

You can also create these other plots using the `GeoDataFrame.plot.<kind>`

accessor methods instead of providing the `kind`

keyword argument.
For example, `hist`

, can be used to plot histograms of population for two different years from the Chicago dataset.

```
In [38]: chicago[["POP2000", "POP2010", "geometry"]].plot.hist(alpha=.4)
Out[38]: <Axes: ylabel='Frequency'>
```

For more information, see Chart visualization in the pandas documentation.

## Other resources#

Links to Jupyter Notebooks for different mapping tasks:

## Source: https://geopandas.org/en/stable/docs/user_guide/interactive_mapping.html

Note

# Interactive mapping#

Alongside static plots, `geopandas`

can create interactive maps based on the folium library.

Creating maps for interactive exploration mirrors the API of static plots in an explore() method of a GeoSeries or GeoDataFrame.

Loading some example data:

```
[1]:
```

```
import geopandas
import geodatasets
nybb = geopandas.read_file(geodatasets.get_path("nybb"))
chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries")).explode(ignore_index=True)
```

The simplest option is to use `GeoDataFrame.explore()`

:

```
[2]:
```

```
nybb.explore()
```

```
[2]:
```

Interactive plotting offers largely the same customisation as static one plus some features on top of that. Check the code below which plots a customised choropleth map. You can use `"BoroName"`

column with NY boroughs names as an input of the choropleth, show (only) its name in the tooltip on hover but show all values on click. You can also pass custom background tiles (either a name supported by folium, a name recognized by `xyzservices.providers.query_name()`

, XYZ URL or
`xyzservices.TileProvider`

object), specify colormap (all supported by `matplotlib`

) and specify black outline.

Note

Note that the GeoDataFrame needs to have a CRS set if you want to use background tiles.

```
[3]:
```

```
nybb.explore(
column="BoroName", # make choropleth based on "BoroName" column
tooltip="BoroName", # show "BoroName" value in tooltip (on hover)
popup=True, # show all values in popup (on click)
tiles="CartoDB positron", # use "CartoDB positron" tiles
cmap="Set1", # use "Set1" matplotlib colormap
style_kwds=dict(color="black"), # use black outline
)
```

```
[3]:
```

The `explore()`

method returns a `folium.Map`

object, which can also be passed directly (as you do with `ax`

in `plot()`

). You can then use folium functionality directly on the resulting map. In the example below, you can plot two GeoDataFrames on the same map and add layer control using folium. You can also add additional tiles allowing you to change the background directly in the map.

```
[4]:
```

```
import folium
m = chicago.explore(
column="POP2010", # make choropleth based on "POP2010" column
scheme="naturalbreaks", # use mapclassify's natural breaks scheme
legend=True, # show legend
k=10, # use 10 bins
tooltip=False, # hide tooltip
popup=["POP2010", "POP2000"], # show popup (on-click)
legend_kwds=dict(colorbar=False), # do not use colorbar
name="chicago", # name of the layer in the map
)
groceries.explore(
m=m, # pass the map object
color="red", # use red color on all points
marker_kwds=dict(radius=5, fill=True), # make marker radius 10px with fill
tooltip="Address", # show "name" column in the tooltip
tooltip_kwds=dict(labels=False), # do not show column label in the tooltip
name="groceries", # name of the layer in the map
)
folium.TileLayer("CartoDB positron", show=False).add_to(
m
) # use folium to add alternative tiles
folium.LayerControl().add_to(m) # use folium to add layer control
m # show map
```

```
[4]:
```

## Source: https://geopandas.org/en/stable/docs/user_guide/projections.html

# Projections#

## Coordinate reference systems#

The coordinate reference system (CRS) is important because the geometric shapes in a GeoSeries or GeoDataFrame object are simply a collection of coordinates in an arbitrary space. A CRS tells Python how those coordinates relate to places on the Earth.

For reference codes of the most commonly used projections, see spatialreference.org.

The same CRS can often be referred to in many ways. For example, one of the most
commonly used CRS is the WGS84 latitude-longitude projection. This can be
referred to using the authority code `"EPSG:4326"`

.

GeoPandas can accept anything accepted by `pyproj.CRS.from_user_input()`

:

CRS WKT string

An authority string (i.e. “epsg:4326”)

An EPSG integer code (i.e. 4326)

An object with a to_wkt method.

PROJ string

Dictionary of PROJ parameters

PROJ keyword arguments for parameters

JSON string with PROJ parameters

For reference, a few very common projections and their EPSG codes:

WGS84 Latitude/Longitude: EPSG:4326

UTM Zones (North): EPSG:32633

UTM Zones (South): EPSG:32733

## What is the best format to store the CRS information?#

Generally, WKT or SRID’s are preferred over PROJ strings as they can contain more information about a given CRS. Conversions between WKT and PROJ strings will in most cases cause a loss of information, potentially leading to erroneous transformations. If possible WKT2 should be used.

For more details, see What is the best format for describing coordinate reference systems.

## Setting a projection#

There are two relevant operations for projections: setting a projection and re-projecting.

Setting a projection may be necessary when for some reason GeoPandas has coordinate data (x-y values), but no information about how those coordinates refer to locations in the real world. Setting a projection is how one tells GeoPandas how to interpret coordinates. If no CRS is set, GeoPandas geometry operations will still work, but coordinate transformations will not be possible and exported files may not be interpreted correctly by other software.

Be aware that **most of the time** you don’t have to set a projection. Data loaded from a reputable source (using the `geopandas.read_file()`

command) *should* always include projection information. You can see an objects current CRS through the `GeoSeries.crs`

attribute.

From time to time, however, you may get data that does not include a projection. In this situation, you have to set the CRS so GeoPandas knows how to interpret the coordinates.

For example, if you convert a spreadsheet of latitudes and longitudes into a
GeoSeries by hand, you would set the projection by passing the WGS84
latitude-longitude CRS to the `GeoSeries.set_crs()`

method (or by setting
the `GeoSeries.crs`

attribute):

```
my_geoseries = my_geoseries.set_crs("EPSG:4326")
my_geoseries = my_geoseries.set_crs(epsg=4326)
```

## Re-projecting#

Re-projecting is the process of changing the representation of locations from one coordinate system to another. All projections of locations on the Earth into a two-dimensional plane have distortions. See Which projection is best for more information. The projection that is best for your application may be different from the projection associated with the data you import. In these cases, data can be re-projected using the `GeoDataFrame.to_crs()`

command:

```
In [1]: import geodatasets
# load example data
In [2]: usa = geopandas.read_file(geodatasets.get_path('geoda.natregimes'))
# Check original projection
# (it's Plate Carrée! x-y are long and lat)
In [3]: usa.crs
Out[3]:
<Geographic 2D CRS: EPSG:4326>
Name: WGS 84
Axis Info [ellipsoidal]:
- Lat[north]: Geodetic latitude (degree)
- Lon[east]: Geodetic longitude (degree)
Area of Use:
- name: World.
- bounds: (-180.0, -90.0, 180.0, 90.0)
Datum: World Geodetic System 1984 ensemble
- Ellipsoid: WGS 84
- Prime Meridian: Greenwich
# Visualize
In [4]: ax = usa.plot()
In [5]: ax.set_title("WGS84 (lat/lon)");
# Reproject to Albers contiguous USA
In [6]: usa = usa.to_crs("ESRI:102003")
In [7]: ax = usa.plot()
In [8]: ax.set_title("NAD 1983 Albers contiguous USA");
```

## Projection for multiple geometry columns#

GeoPandas 0.8 implements support for different projections assigned to different geometry columns of the same GeoDataFrame. The projection is now stored together with geometries per column (directly on the GeometryArray level).

Note that if GeometryArray has an assigned projection, it cannot be overridden by an another inconsistent projection during the creation of a GeoSeries or GeoDataFrame:

```
>>> array.crs
<Geographic 2D CRS: EPSG:4326>
Name: WGS 84
Axis Info [ellipsoidal]:
- Lat[north]: Geodetic latitude (degree)
- Lon[east]: Geodetic longitude (degree)
...
>>> GeoSeries(array, crs=4326) # crs=4326 is okay, as it matches the existing CRS
>>> GeoSeries(array, crs=3395) # crs=3395 is forbidden as array already has CRS
ValueError: CRS mismatch between CRS of the passed geometries and 'crs'. Use 'GeoSeries.set_crs(crs, allow_override=True)' to overwrite CRS or 'GeoSeries.to_crs(crs)' to reproject geometries.
GeoSeries(array, crs=3395).crs
```

If you want to overwrite the projection, you can then assign it to the GeoSeries
manually or re-project geometries to the target projection using either
`GeoSeries.set_crs(epsg=3395, allow_override=True)`

or
`GeoSeries.to_crs(epsg=3395)`

.

All GeometryArray-based operations preserve projection; however, if you loop over a column containing geometry, this information might be lost.

## Upgrading to GeoPandas 0.7 with pyproj > 2.2 and PROJ > 6#

Starting with GeoPandas 0.7, the .crs attribute of a GeoSeries or GeoDataFrame
stores the CRS information as a `pyproj.CRS`

, and no longer as a proj4 string
or dict.

Before, you might have seen this:

```
>>> gdf.crs
{'init': 'epsg:4326'}
```

while now you will see something like this:

```
>>> gdf.crs
<Geographic 2D CRS: EPSG:4326>
Name: WGS 84
Axis Info [ellipsoidal]:
- Lat[north]: Geodetic latitude (degree)
- Lon[east]: Geodetic longitude (degree)
...
>>> type(gdf.crs)
pyproj.crs.CRS
```

This gives a better user interface and integrates improvements from pyproj and PROJ 6, but might also require some changes in your code. See this blogpost for some more information. The subsections below cover different possible migration issues.

See the pyproj documentation for more on
the `pyproj.CRS`

object.

### Importing data from files#

When reading geospatial files with `geopandas.read_file()`

, things should
mostly work out of the box. For example, reading the example countries dataset
yields a proper CRS:

```
In [9]: df = geopandas.read_file(geodatasets.get_path('naturalearth.land'))
In [10]: df.crs
Out[10]:
<Geographic 2D CRS: EPSG:4326>
Name: WGS 84
Axis Info [ellipsoidal]:
- Lat[north]: Geodetic latitude (degree)
- Lon[east]: Geodetic longitude (degree)
Area of Use:
- name: World.
- bounds: (-180.0, -90.0, 180.0, 90.0)
Datum: World Geodetic System 1984 ensemble
- Ellipsoid: WGS 84
- Prime Meridian: Greenwich
```

However, in certain cases (with older CRS formats), the resulting CRS object might not be fully as expected. See the section below for possible reasons and how to solve it.

### Manually specifying the CRS#

When specifying the CRS manually in your code (e.g., because your data has not yet a CRS, or when converting to another CRS), this might require a change in your code.

**“init” proj4 strings/dicts**

Currently, a lot of people (and also the GeoPandas docs showed that before) specify the EPSG code using the “init” proj4 string:

```
## OLD
GeoDataFrame(..., crs={'init': 'epsg:4326'})
# or
gdf.crs = {'init': 'epsg:4326'}
# or
gdf.to_crs({'init': 'epsg:4326'})
```

The above will now raise a deprecation warning from pyproj, and instead of the “init” proj4 string, you should use only the EPSG code itself as follows:

```
## NEW
GeoDataFrame(..., crs="EPSG:4326")
# or
gdf.crs = "EPSG:4326"
# or
gdf.to_crs("EPSG:4326")
```

**proj4 strings/dicts**

Although a full proj4 string is not deprecated (as opposed to the “init” string above), it is still recommended to change it with an EPSG code if possible.

For example, *if* you know the EPSG code for the projection you are using, instead of:

```
gdf.crs = "+proj=laea +lat_0=45 +lon_0=-100 +x_0=0 +y_0=0 +a=6370997 +b=6370997 +units=m +no_defs"
```

this is recommended:

```
gdf.crs = "EPSG:2163"
```

One possible way to find out the EPSG code is using pyproj for this:

```
>>> import pyproj
>>> crs = pyproj.CRS("+proj=laea +lat_0=45 +lon_0=-100 +x_0=0 +y_0=0 +a=6370997 +b=6370997 +units=m +no_defs")
>>> crs.to_epsg()
2163
```

(you might need to set the `min_confidence`

keyword of `to_epsg`

to a lower
value if the match is not perfect)

Further, on websites such as Spatial Reference and epsg.org the descriptions of many CRS can be found including their EPSG codes and proj4 string definitions.

**Other formats**

CRS: an actual `pyproj.CRS`

object, a WKT string, a PROJ JSON string, etc.
Anything that is accepted by `pyproj.CRS.from_user_input()`

can by specified
to the `crs`

keyword/attribute in GeoPandas.

Also compatible CRS objects, such as from the `rasterio`

package, can be
passed directly to GeoPandas.

### The axis order of a CRS#

Starting with PROJ 6 / pyproj 2, the axis order of the official EPSG definition is honoured. For example, when using geographic coordinates (degrees of longitude and latitude) in the standard EPSG:4326, the CRS will look like:

```
>>> pyproj.CRS(3EPSG:4326")
<Geographic 2D CRS: EPSG:4326>
...
Axis Info [ellipsoidal]:
- Lat[north]: Geodetic latitude (degree)
- Lon[east]: Geodetic longitude (degree)
...
```

This mentions the order as (lat, lon), as that is the official order of coordinates in EPSG:4326. In GeoPandas, however, the coordinates are always stored as (x, y), and thus as (lon, lat) order, regardless of the CRS (i.e. the “traditional” order used in GIS). When reprojecting, GeoPandas and pyproj will under the hood take care of this difference in axis order, so the user doesn’t need to care about this.

### Why is it not properly recognizing my CRS?#

There are many file sources and CRS definitions out there “in the wild” that
might have a CRS description that does not fully conform to the new standards of
PROJ > 6 (proj4 strings, older WKT formats, …). In such cases, you will get a
`pyproj.CRS`

object that might not be fully what you expected (e.g. not equal
to the expected EPSG code). Below is a list of a few possible cases.

#### I get a “Bound CRS”?#

Some CRS definitions include a *“towgs84” clause*, which can give problems in
recognizing the actual CRS.

For example, both the proj4 and WKT representations for EPSG:31370 (the local projection used in Belgium) as can be found at EPSG:31370 include this clause. When taking one of those definitions from that site, and creating a CRS object:

```
>>> import pyproj
>>> crs = pyproj.CRS("+proj=lcc +lat_1=51.16666723333333 +lat_2=49.8333339 +lat_0=90 +lon_0=4.367486666666666 +x_0=150000.013 +y_0=5400088.438 +ellps=intl +towgs84=106.869,-52.2978,103.724,-0.33657,0.456955,-1.84218,1 +units=m +no_defs")
>>> crs
<Bound CRS: +proj=lcc +lat_1=51.16666723333333 +lat_2=49.83333 ...>
Name: unknown
Axis Info [cartesian]:
- E[east]: Easting (metre)
- N[north]: Northing (metre)
Area of Use:
- undefined
Coordinate Operation:
- name: Transformation from unknown to WGS84
- method: Position Vector transformation (geog2D domain)
Datum: Unknown based on International 1909 (Hayford) ellipsoid
- Ellipsoid: International 1909 (Hayford)
- Prime Meridian: Greenwich
Source CRS: unknown
```

You notice that the above is a not a “Projected CRS” as expected, but a “Bound CRS”. This is because it is “bound” to a conversion to WGS84, and will always use this when reprojecting instead of letting PROJ determine the best conversion.

To get the actual underlying projected CRS, you can use the `.source_crs`

attribute:

```
>>> crs.source_crs
<Projected CRS: PROJCRS["unknown",BASEGEOGCRS["unknown",DATUM["Unk ...>
Name: unknown
...
```

Now you have a “Projected CRS”, and now it will also recognize the correct EPSG number:

```
>>> crs.to_epsg()
>>> crs.source_crs.to_epsg()
31370
```

#### I have a different axis order?#

As mentioned above, pyproj now honours the axis order of the EPSG definition. However, proj4 strings or older WKT versions don’t specify this correctly, which can be a reason that the CRS object is not equal to the expected EPSG code.

Consider the following example of a Canadian projected CRS EPSG:2953. When constructing the CRS object from the WKT string as provided on EPSG:2953:

```
>>> crs = pyproj.CRS("""PROJCS["NAD83(CSRS) / New Brunswick Stereographic",
... GEOGCS["NAD83(CSRS)",
... DATUM["NAD83_Canadian_Spatial_Reference_System",
... SPHEROID["GRS 1980",6378137,298.257222101,
... AUTHORITY["EPSG","7019"]],
... AUTHORITY["EPSG","6140"]],
... PRIMEM["Greenwich",0,
... AUTHORITY["EPSG","8901"]],
... UNIT["degree",0.0174532925199433,
... AUTHORITY["EPSG","9122"]],
... AUTHORITY["EPSG","4617"]],
... PROJECTION["Oblique_Stereographic"],
... PARAMETER["latitude_of_origin",46.5],
... PARAMETER["central_meridian",-66.5],
... PARAMETER["scale_factor",0.999912],
... PARAMETER["false_easting",2500000],
... PARAMETER["false_northing",7500000],
... UNIT["metre",1,
... AUTHORITY["EPSG","9001"]],
... AUTHORITY["EPSG","2953"]]""")
>>> crs
<Projected CRS: PROJCS["NAD83(CSRS) / New Brunswick Stereographic" ...>
Name: NAD83(CSRS) / New Brunswick Stereographic
Axis Info [cartesian]:
- E[east]: Easting (metre)
- N[north]: Northing (metre)
...
```

Although this is the WKT string as found online for “EPSG:2953”, this CRS object does not evaluate equal to this EPSG code:

```
>>> crs == "EPSG:2953"
False
```

If you construct the CRS object from the EPSG code (truncated output):

```
>>> pyproj.CRS("EPSG:2953")
<Projected CRS: EPSG:2953>
Name: NAD83(CSRS) / New Brunswick Stereographic
Axis Info [cartesian]:
- N[north]: Northing (metre)
- E[east]: Easting (metre)
...
```

You can see that the CRS object constructed from the WKT string has a “Easting, Northing” (i.e. x, y) axis order, while the CRS object constructed from the EPSG code has a (Northing, Easting) axis order.

Only having this difference in axis order is no problem when using the CRS in GeoPandas, since GeoPandas always uses a (x, y) order to store the data regardless of the CRS definition. But, you might still want to verify it is equivalent to the expected EPSG code. By lowering the min_confidence, the axis order will be ignored:

```
>>> crs.to_epsg()
>>> crs.to_epsg(min_confidence=20)
2953
```

### The `.crs`

attribute is no longer a dict or string#

If you relied on the `.crs`

object being a dict or a string, such code can
be broken given it is now a `pyproj.CRS`

object. But this object actually
provides a more robust interface to get information about the CRS.

For example, if you used the following code to get the EPSG code:

```
gdf.crs['init']
```

This will no longer work. To get the EPSG code from a `crs`

object, you can use
the `to_epsg()`

method.

Or to check if a CRS was a certain UTM zone:

```
'+proj=utm ' in gdf.crs
```

could be replaced with the more robust check (requires pyproj 2.6+):

```
gdf.crs.utm_zone is not None
```

And there are many other methods available on the `pyproj.CRS`

class to get
information about the CRS.

## Source: https://geopandas.org/en/stable/docs/user_guide/geometric_manipulations.html

# Geometric manipulations#

GeoPandas makes available all the tools for geometric manipulations in the Shapely library.

Note that documentation for all set-theoretic tools for creating new shapes using the relationship between two different spatial datasets – like creating intersections, or differences – can be found at Set operations with overlay.

## Constructive methods#

-
GeoSeries.buffer(
*distance*,*resolution=16*)# Returns a

`GeoSeries`

of geometries representing all points within a given distance of each geometric object.

- GeoSeries.boundary#
Returns a

`GeoSeries`

of lower dimensional objects representing each geometry’s set-theoretic boundary.

- GeoSeries.concave_hull#
Returns a

`GeoSeries`

of geometries representing the smallest concave Polygon containing all the points in each object unless the number of points in the object is less than three. For two points, the concave hull collapses to a LineString; for 1, a Point.

- GeoSeries.convex_hull#
Returns a

`GeoSeries`

of geometries representing the smallest convex Polygon containing all the points in each object unless the number of points in the object is less than three. For two points, the convex hull collapses to a LineString; for 1, a Point.

- GeoSeries.constrained_delaunay_triangles()#
Returns a

`GeoSeries`

with the constrained Delaunay triangulation of polygons. A constrained Delaunay triangulation requires the edges of the input polygon(s) to be in the set of resulting triangle edges. An unconstrained delaunay triangulation only triangulates based on the vertices, hence triangle edges could cross polygon boundaries.

-
GeoSeries.delaunay_triangles(
*tolerance*,*preserve_topology=True*)# Returns a

`GeoSeries`

consisting of polygons (default) or linestrings (only_edges=True) representing the computed Delaunay triangulation around the vertices of an input geometry.

- GeoSeries.envelope#
Returns a

`GeoSeries`

of geometries representing the point or smallest rectangular polygon (with sides parallel to the coordinate axes) that contains each object.

- GeoSeries.extract_unique_points()#
Returns a

`GeoSeries`

of geometries containing all distinct vertices of each input geometry as a multipoint.

-
GeoSeries.offset_curve(
*distance*,*quad_segs=8*,*join_style='round'*,*mitre_limit=5.0*)# Returns a

`GeoSeries`

containing a Linestring or MultiLineString geometry at a distance from the object on its right or its left side.

- GeoSeries.remove_repeated_points()#
Returns a

`GeoSeries`

containing a copy of the input geometry with repeated points removed.

-
GeoSeries.simplify(
*tolerance*,*preserve_topology=True*)# Returns a

`GeoSeries`

containing a simplified representation of each object.

## Affine transformations#

-
GeoSeries.affine_transform(
*self*,*matrix*)# Transform the geometries of the

`GeoSeries`

using an affine transformation matrix

-
GeoSeries.rotate(
*self*,*angle*,*origin='center'*,*use_radians=False*)# Rotate the coordinates of the

`GeoSeries`

.

-
GeoSeries.scale(
*self*,*xfact=1.0*,*yfact=1.0*,*zfact=1.0*,*origin='center'*)# Scale the geometries of the

`GeoSeries`

along each (x, y, z) dimension.

## Examples of geometric manipulations#

```
>>> import geopandas
>>> from geopandas import GeoSeries
>>> from shapely.geometry import Polygon
>>> p1 = Polygon([(0, 0), (1, 0), (1, 1)])
>>> p2 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
>>> p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
>>> g = GeoSeries([p1, p2, p3])
>>> g
0 POLYGON ((0 0, 1 0, 1 1, 0 0))
1 POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))
2 POLYGON ((2 0, 3 0, 3 1, 2 1, 2 0))
dtype: geometry
```

Some geographic operations return normal pandas objects. The `area`

property of a `GeoSeries`

will return a `pandas.Series`

containing the area of each item in the `GeoSeries`

:

```
>>> print(g.area)
0 0.5
1 1.0
2 1.0
dtype: float64
```

Other operations return GeoPandas objects:

```
>>> g.buffer(0.5)
0 POLYGON ((-0.3535533905932737 0.35355339059327...
1 POLYGON ((-0.5 0, -0.5 1, -0.4975923633360985 ...
2 POLYGON ((1.5 0, 1.5 1, 1.502407636663901 1.04...
dtype: geometry
```

GeoPandas objects also know how to plot themselves. GeoPandas uses matplotlib for plotting. To generate a plot of a `GeoSeries`

, use:

```
>>> g.plot()
```

GeoPandas also implements alternate constructors that can read any data format recognized by Pyogrio. To read a zip file containing an ESRI shapefile with the borough boundaries of New York City (provided by the `geodatasets`

package):

```
>>> import geodatasets
>>> nybb_path = geodatasets.get_path('nybb')
>>> boros = geopandas.read_file(nybb_path)
>>> boros.set_index('BoroCode', inplace=True)
>>> boros.sort_index(inplace=True)
>>> boros
BoroName Shape_Leng Shape_Area \
BoroCode
1 Manhattan 359299.096471 6.364715e+08
2 Bronx 464392.991824 1.186925e+09
3 Brooklyn 741080.523166 1.937479e+09
4 Queens 896344.047763 3.045213e+09
5 Staten Island 330470.010332 1.623820e+09
geometry
BoroCode
1 MULTIPOLYGON (((981219.0557861328 188655.31579...
2 MULTIPOLYGON (((1012821.805786133 229228.26458...
3 MULTIPOLYGON (((1021176.479003906 151374.79699...
4 MULTIPOLYGON (((1029606.076599121 156073.81420...
5 MULTIPOLYGON (((970217.0223999023 145643.33221...
```

```
>>> boros['geometry'].convex_hull
BoroCode
1 POLYGON ((977855.4451904297 188082.3223876953,...
2 POLYGON ((1017949.977600098 225426.8845825195,...
3 POLYGON ((988872.8212280273 146772.0317993164,...
4 POLYGON ((1000721.531799316 136681.776184082, ...
5 POLYGON ((915517.6877458114 120121.8812543372,...
dtype: geometry
```

To demonstrate a more complex operation, generate a
`GeoSeries`

containing 2000 random points:

```
>>> import numpy as np
>>> from shapely.geometry import Point
>>> xmin, xmax, ymin, ymax = 900000, 1080000, 120000, 280000
>>> xc = (xmax - xmin) * np.random.random(2000) + xmin
>>> yc = (ymax - ymin) * np.random.random(2000) + ymin
>>> pts = GeoSeries([Point(x, y) for x, y in zip(xc, yc)])
```

Now draw a circle with fixed radius around each point:

```
>>> circles = pts.buffer(2000)
```

You can collapse these circles into a single `MultiPolygon`

geometry with

```
>>> mp = circles.union_all()
```

To extract the part of this geometry contained in each borough, you can just use:

```
>>> holes = boros['geometry'].intersection(mp)
```

and to get the area outside of the holes:

```
>>> boros_with_holes = boros['geometry'].difference(mp)
```

Note that this can be simplified a bit, since `geometry`

is
available as an attribute on a `GeoDataFrame`

, and the
`intersection()`

and `difference()`

methods are implemented with the
“&” and “-” operators, respectively. For example, the latter could
have been expressed simply as `boros.geometry - mp`

.

It’s easy to do things like calculate the fractional area in each borough that are in the holes:

```
>>> holes.area / boros.geometry.area
BoroCode
1 0.579939
2 0.586833
3 0.608174
4 0.582172
5 0.558075
dtype: float64
```

## Source: https://geopandas.org/en/stable/docs/user_guide/set_operations.html

# Set operations with overlay#

When working with multiple spatial datasets – especially multiple *polygon* or
*line* datasets – users often wish to create new shapes based on places where
those datasets overlap (or don’t overlap). These manipulations are often
referred using the language of sets – intersections, unions, and differences.
These types of operations are made available in the GeoPandas library through
the `overlay()`

method.

The basic idea is demonstrated by the graphic below but keep in mind that
overlays operate at the DataFrame level, not on individual geometries, and the
properties from both are retained. In effect, for every shape in the left
`GeoDataFrame`

, this operation is executed against every other shape in the right
`GeoDataFrame`

:

**Source: QGIS documentation**

Note

Note to users familiar with the *shapely* library: `overlay()`

can be thought
of as offering versions of the standard *shapely* set operations that deal with
the complexities of applying set operations to two *GeoSeries*. The standard
*shapely* set operations are also available as `GeoSeries`

methods.

## The different overlay operations#

First, create some example data:

```
In [1]: from shapely.geometry import Polygon
In [2]: polys1 = geopandas.GeoSeries([Polygon([(0,0), (2,0), (2,2), (0,2)]),
...: Polygon([(2,2), (4,2), (4,4), (2,4)])])
...:
In [3]: polys2 = geopandas.GeoSeries([Polygon([(1,1), (3,1), (3,3), (1,3)]),
...: Polygon([(3,3), (5,3), (5,5), (3,5)])])
...:
In [4]: df1 = geopandas.GeoDataFrame({'geometry': polys1, 'df1':[1,2]})
In [5]: df2 = geopandas.GeoDataFrame({'geometry': polys2, 'df2':[1,2]})
```

These two GeoDataFrames have some overlapping areas:

```
In [6]: ax = df1.plot(color='red');
In [7]: df2.plot(ax=ax, color='green', alpha=0.5);
```

The above example illustrates the different overlay modes.
The `overlay()`

method will determine the set of all individual geometries
from overlaying the two input GeoDataFrames. This result covers the area covered
by the two input GeoDataFrames, and also preserves all unique regions defined by
the combined boundaries of the two GeoDataFrames.

Note

For historical reasons, the overlay method is also available as a top-level function `overlay()`

.
It is recommended to use the method as the function may be deprecated in the future.

When using `how='union'`

, all those possible geometries are returned:

```
In [8]: res_union = df1.overlay(df2, how='union')
In [9]: res_union
Out[9]:
df1 df2 geometry
0 1.0 1.0 POLYGON ((2 2, 2 1, 1 1, 1 2, 2 2))
1 2.0 1.0 POLYGON ((2 2, 2 3, 3 3, 3 2, 2 2))
2 2.0 2.0 POLYGON ((4 4, 4 3, 3 3, 3 4, 4 4))
3 1.0 NaN POLYGON ((2 0, 0 0, 0 2, 1 2, 1 1, 2 1, 2 0))
4 2.0 NaN MULTIPOLYGON (((3 4, 3 3, 2 3, 2 4, 3 4)), ((4...
5 NaN 1.0 MULTIPOLYGON (((2 3, 2 2, 1 2, 1 3, 2 3)), ((3...
6 NaN 2.0 POLYGON ((3 5, 5 5, 5 3, 4 3, 4 4, 3 4, 3 5))
In [10]: ax = res_union.plot(alpha=0.5, cmap='tab10')
In [11]: df1.plot(ax=ax, facecolor='none', edgecolor='k');
In [12]: df2.plot(ax=ax, facecolor='none', edgecolor='k');
```

The other `how`

operations will return different subsets of those geometries.
With `how='intersection'`

, it returns only those geometries that are contained
by both GeoDataFrames:

```
In [13]: res_intersection = df1.overlay(df2, how='intersection')
In [14]: res_intersection
Out[14]:
df1 df2 geometry
0 1 1 POLYGON ((2 2, 2 1, 1 1, 1 2, 2 2))
1 2 1 POLYGON ((2 2, 2 3, 3 3, 3 2, 2 2))
2 2 2 POLYGON ((4 4, 4 3, 3 3, 3 4, 4 4))
In [15]: ax = res_intersection.plot(cmap='tab10')
In [16]: df1.plot(ax=ax, facecolor='none', edgecolor='k');
In [17]: df2.plot(ax=ax, facecolor='none', edgecolor='k');
```

`how='symmetric_difference'`

is the opposite of `'intersection'`

and returns
the geometries that are only part of one of the GeoDataFrames but not of both:

```
In [18]: res_symdiff = df1.overlay(df2, how='symmetric_difference')
In [19]: res_symdiff
Out[19]:
df1 df2 geometry
0 1.0 NaN POLYGON ((2 0, 0 0, 0 2, 1 2, 1 1, 2 1, 2 0))
1 2.0 NaN MULTIPOLYGON (((3 4, 3 3, 2 3, 2 4, 3 4)), ((4...
2 NaN 1.0 MULTIPOLYGON (((2 3, 2 2, 1 2, 1 3, 2 3)), ((3...
3 NaN 2.0 POLYGON ((3 5, 5 5, 5 3, 4 3, 4 4, 3 4, 3 5))
In [20]: ax = res_symdiff.plot(cmap='tab10')
In [21]: df1.plot(ax=ax, facecolor='none', edgecolor='k');
In [22]: df2.plot(ax=ax, facecolor='none', edgecolor='k');
```

To obtain the geometries that are part of `df1`

but are not contained in
`df2`

, you can use `how='difference'`

:

```
In [23]: res_difference = df1.overlay(df2, how='difference')
In [24]: res_difference
Out[24]:
geometry df1
0 POLYGON ((2 0, 0 0, 0 2, 1 2, 1 1, 2 1, 2 0)) 1
1 MULTIPOLYGON (((3 4, 3 3, 2 3, 2 4, 3 4)), ((4... 2
In [25]: ax = res_difference.plot(cmap='tab10')
In [26]: df1.plot(ax=ax, facecolor='none', edgecolor='k');
In [27]: df2.plot(ax=ax, facecolor='none', edgecolor='k');
```

Finally, with `how='identity'`

, the result consists of the surface of `df1`

,
but with the geometries obtained from overlaying `df1`

with `df2`

:

```
In [28]: res_identity = df1.overlay(df2, how='identity')
In [29]: res_identity
Out[29]:
df1 df2 geometry
0 1 1.0 POLYGON ((2 2, 2 1, 1 1, 1 2, 2 2))
1 2 1.0 POLYGON ((2 2, 2 3, 3 3, 3 2, 2 2))
2 2 2.0 POLYGON ((4 4, 4 3, 3 3, 3 4, 4 4))
3 1 NaN POLYGON ((2 0, 0 0, 0 2, 1 2, 1 1, 2 1, 2 0))
4 2 NaN MULTIPOLYGON (((3 4, 3 3, 2 3, 2 4, 3 4)), ((4...
In [30]: ax = res_identity.plot(cmap='tab10')
In [31]: df1.plot(ax=ax, facecolor='none', edgecolor='k');
In [32]: df2.plot(ax=ax, facecolor='none', edgecolor='k');
```

## Overlay groceries example#

First, load the Chicago community areas and groceries example datasets and select :

```
In [33]: import geodatasets
In [34]: chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
In [35]: groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))
# Project to crs that uses meters as distance measure
In [36]: chicago = chicago.to_crs("ESRI:102003")
In [37]: groceries = groceries.to_crs("ESRI:102003")
```

To illustrate the `overlay()`

method, consider the following case in which one
wishes to identify the “served” portion of each area – defined as areas within
1km of a grocery store – using a `GeoDataFrame`

of community areas and a
`GeoDataFrame`

of groceries.

```
# Look at Chicago:
In [38]: chicago.plot();
# Now buffer groceries to find area within 1km.
# Check CRS -- USA Contiguous Albers Equal Area, units of meters.
In [39]: groceries.crs
Out[39]:
<Projected CRS: ESRI:102003>
Name: USA_Contiguous_Albers_Equal_Area_Conic
Axis Info [cartesian]:
- E[east]: Easting (metre)
- N[north]: Northing (metre)
Area of Use:
- name: United States (USA) - CONUS onshore - Alabama; Arizona; Arkansas; California; Colorado; Connecticut; Delaware; Florida; Georgia; Idaho; Illinois; Indiana; Iowa; Kansas; Kentucky; Louisiana; Maine; Maryland; Massachusetts; Michigan; Minnesota; Mississippi; Missouri; Montana; Nebraska; Nevada; New Hampshire; New Jersey; New Mexico; New York; North Carolina; North Dakota; Ohio; Oklahoma; Oregon; Pennsylvania; Rhode Island; South Carolina; South Dakota; Tennessee; Texas; Utah; Vermont; Virginia; Washington; West Virginia; Wisconsin; Wyoming.
- bounds: (-124.79, 24.41, -66.91, 49.38)
Coordinate Operation:
- name: USA_Contiguous_Albers_Equal_Area_Conic
- method: Albers Equal Area
Datum: North American Datum 1983
- Ellipsoid: GRS 1980
- Prime Meridian: Greenwich
# make 1km buffer
In [40]: groceries['geometry']= groceries.buffer(1000)
In [41]: groceries.plot();
```

To select only the portion of community areas within 1km of a grocery, specify the `how`

option to be “intersect”, which creates a new set of polygons where these two layers overlap:

```
In [42]: chicago_cores = chicago.overlay(groceries, how='intersection')
In [43]: chicago_cores.plot(alpha=0.5, edgecolor='k', cmap='tab10');
```

Changing the `how`

option allows for different types of overlay operations. For example, if you were interested in the portions of Chicago *far* from groceries (the peripheries), you would compute the difference of the two.

```
In [44]: chicago_peripheries = chicago.overlay(groceries, how='difference')
In [45]: chicago_peripheries.plot(alpha=0.5, edgecolor='k', cmap='tab10');
```

## keep_geom_type keyword#

In default settings, `overlay()`

returns only geometries of the same geometry type as GeoDataFrame
(left one) has, where Polygon and MultiPolygon is considered as a same type (other types likewise).
You can control this behavior using `keep_geom_type`

option, which is set to
True by default. Once set to False, `overlay`

will return all geometry types resulting from
selected set-operation. Different types can result for example from intersection of touching geometries,
where two polygons intersects in a line or a point.

## More examples#

A larger set of examples of the use of `overlay()`

can be found here

## Source: https://geopandas.org/en/stable/docs/user_guide/aggregation_with_dissolve.html

# Aggregation with dissolve#

Spatial data are often more granular than needed. For example, you might have data on sub-national units, but you’re actually interested in studying patterns at the level of countries.

In a non-spatial setting, when you need summary statistics of the data, you can aggregate data using the `groupby()`

function. But for spatial data, you sometimes also need to aggregate geometric features. In the GeoPandas library, you can aggregate geometric features using the `dissolve()`

function.

`dissolve()`

can be thought of as doing three things:

it dissolves all the geometries within a given group together into a single geometric feature (using the

`union_all()`

method), andit aggregates all the rows of data in a group using groupby.aggregate, and

it combines those two results.

`dissolve()`

Example#

Take example of administrative areas in Nepal. You have districts, which are smaller, and zones, which are larger. A group of districts always compose a single zone. Suppose you are interested in Nepalese zone, but you only have Nepalese district-level data like the geoda.nepal dataset included in geodatasets. You can easily convert this to a zone-level dataset.

First, let’s look at the most simple case where you just want zone shapes and names.

```
In [1]: import geodatasets
In [2]: nepal = geopandas.read_file(geodatasets.get_path('geoda.nepal'))
In [3]: nepal = nepal.rename(columns={"name_2": "zone"}) # rename to remember the column
In [4]: nepal[["zone", "geometry"]].head()
Out[4]:
zone geometry
0 Dhaualagiri POLYGON ((83.10834 28.6202, 83.1056 28.60976, ...
1 Dhaualagiri POLYGON ((83.99726 29.31675, 84 29.31576, 84 2...
2 Dhaualagiri POLYGON ((83.50688 28.79306, 83.51024 28.78809...
3 Dhaualagiri POLYGON ((83.70261 28.39837, 83.70435 28.39452...
4 Bagmati POLYGON ((85.52173 27.71822, 85.52359 27.71375...
```

By default, `dissolve()`

will pass `'first'`

to groupby.aggregate.

```
In [5]: nepal_zone = nepal[['zone', 'geometry']]
In [6]: zones = nepal_zone.dissolve(by='zone')
In [7]: zones.plot();
In [8]: zones.head()
Out[8]:
geometry
zone
Bagmati POLYGON ((85.87653 27.61234, 85.87355 27.60861...
Bheri POLYGON ((81.75089 28.31038, 81.75562 28.3074,...
Dhaualagiri POLYGON ((83.70647 28.39278, 83.70721 28.38781...
Gandaki POLYGON ((84.49995 28.74099, 84.50443 28.7441,...
Janakpur POLYGON ((86.26166 26.91417, 86.2588 26.91144,...
```

If you are interested in aggregate populations, however, you can pass different functions to the `dissolve()`

method to aggregate populations using the `aggfunc =`

argument:

```
In [9]: nepal_pop = nepal[['zone', 'geometry', 'population']]
In [10]: zones = nepal_pop.dissolve(by='zone', aggfunc='sum')
In [11]: zones.plot(column = 'population', scheme='quantiles', cmap='YlOrRd');
In [12]: zones.head()
Out[12]:
geometry population
zone
Bagmati POLYGON ((85.87653 27.61234, 85.87355 27.60861... 3750441
Bheri POLYGON ((81.75089 28.31038, 81.75562 28.3074,... 1463510
Dhaualagiri POLYGON ((83.70647 28.39278, 83.70721 28.38781... 516905
Gandaki POLYGON ((84.49995 28.74099, 84.50443 28.7441,... 1530310
Janakpur POLYGON ((86.26166 26.91417, 86.2588 26.91144,... 2818356
```

## Dissolve arguments#

The `aggfunc =`

argument defaults to ‘first’ which means that the first row of attributes values found in the dissolve routine will be assigned to the resultant dissolved geodataframe.
However it also accepts other summary statistic options as allowed by `pandas.groupby`

including:

‘first’

‘last’

‘min’

‘max’

‘sum’

‘mean’

‘median’

function

string function name

list of functions and/or function names, e.g. [np.sum, ‘mean’]

dict of axis labels -> functions, function names or list of such.

For example, to get the number of countries on each continent,
as well as the populations of the largest and smallest country of each,
you can aggregate the `'name'`

column using `'count'`

,
and the `'pop_est'`

column using `'min'`

and `'max'`

:

```
In [13]: zones = nepal.dissolve(
....: by="zone",
....: aggfunc={
....: "district": "count",
....: "population": ["min", "max"],
....: },
....: )
....: zones.head()
....:
Out[13]:
geometry ... (population, max)
zone ...
Bagmati POLYGON ((85.87653 27.61234, 85.87355 27.60861... ... 1688131
Bheri POLYGON ((81.75089 28.31038, 81.75562 28.3074,... ... 422812
Dhaualagiri POLYGON ((83.70647 28.39278, 83.70721 28.38781... ... 250065
Gandaki POLYGON ((84.49995 28.74099, 84.50443 28.7441,... ... 480851
Janakpur POLYGON ((86.26166 26.91417, 86.2588 26.91144,... ... 765959
[5 rows x 4 columns]
```

## Source: https://geopandas.org/en/stable/docs/user_guide/mergingdata.html

# Merging data#

There are two ways to combine datasets in GeoPandas – attribute joins and spatial joins.

In an attribute join, a `GeoSeries`

or `GeoDataFrame`

is
combined with a regular `pandas.Series`

or `pandas.DataFrame`

based on a
common variable. This is analogous to normal merging or joining in *pandas*.

In a spatial join, observations from two `GeoSeries`

or `GeoDataFrame`

are combined based on their spatial relationship to one another.

In the following examples, these datasets are used:

```
In [1]: import geodatasets
In [2]: chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
In [3]: groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))
# For attribute join
In [4]: chicago_shapes = chicago[['geometry', 'NID']]
In [5]: chicago_names = chicago[['community', 'NID']]
# For spatial join
In [6]: chicago = chicago[['geometry', 'community']].to_crs(groceries.crs)
```

## Appending#

Appending `GeoDataFrame`

and `GeoSeries`

uses pandas `concat()`

function.
Keep in mind, that appended geometry columns needs to have the same CRS.

```
# Appending GeoSeries
In [7]: joined = pd.concat([chicago.geometry, groceries.geometry])
# Appending GeoDataFrames
In [8]: douglas = chicago[chicago.community == 'DOUGLAS']
In [9]: oakland = chicago[chicago.community == 'OAKLAND']
In [10]: douglas_oakland = pd.concat([douglas, oakland])
```

## Attribute joins#

Attribute joins are accomplished using the `merge()`

method. In general, it is recommended
to use the `merge()`

method called from the spatial dataset. With that said, the stand-alone
`pandas.merge()`

function will work if the `GeoDataFrame`

is in the `left`

argument;
if a `DataFrame`

is in the `left`

argument and a `GeoDataFrame`

is in the `right`

position, the result will no longer be a `GeoDataFrame`

.

For example, consider the following merge that adds full names to a `GeoDataFrame`

that initially has only area ID for each geometry by merging it with a `DataFrame`

.

```
# `chicago_shapes` is GeoDataFrame with community shapes and area IDs
In [11]: chicago_shapes.head()
Out[11]:
geometry NID
0 MULTIPOLYGON (((-87.609140876 41.844692503, -8... 35
1 MULTIPOLYGON (((-87.592152839 41.816929346, -8... 36
2 MULTIPOLYGON (((-87.628798237 41.801893034, -8... 37
3 MULTIPOLYGON (((-87.606708126 41.816813771, -8... 38
4 MULTIPOLYGON (((-87.592152839 41.816929346, -8... 39
# `chicago_names` is DataFrame with community names and area ID
In [12]: chicago_names.head()
Out[12]:
community NID
0 DOUGLAS 35
1 OAKLAND 36
2 FULLER PARK 37
3 GRAND BOULEVARD 38
4 KENWOOD 39
# Merge with `merge` method on shared variable (area ID):
In [13]: chicago_shapes = chicago_shapes.merge(chicago_names, on='NID')
In [14]: chicago_shapes.head()
Out[14]:
geometry NID community
0 MULTIPOLYGON (((-87.609140876 41.844692503, -8... 35 DOUGLAS
1 MULTIPOLYGON (((-87.592152839 41.816929346, -8... 36 OAKLAND
2 MULTIPOLYGON (((-87.628798237 41.801893034, -8... 37 FULLER PARK
3 MULTIPOLYGON (((-87.606708126 41.816813771, -8... 38 GRAND BOULEVARD
4 MULTIPOLYGON (((-87.592152839 41.816929346, -8... 39 KENWOOD
```

## Spatial joins#

In a spatial join, two geometry objects are merged based on their spatial relationship to one another.

```
# One GeoDataFrame of communities, one of grocery stores.
# Want to merge to get each grocery's community.
In [15]: chicago.head()
Out[15]:
geometry community
0 MULTIPOLYGON (((1181573.249800048 1886828.0393... DOUGLAS
1 MULTIPOLYGON (((1186289.355600054 1876750.7332... OAKLAND
2 MULTIPOLYGON (((1176344.998000037 1871187.5456... FULLER PARK
3 MULTIPOLYGON (((1182322.042900046 1876674.7304... GRAND BOULEVARD
4 MULTIPOLYGON (((1186289.355600054 1876750.7332... KENWOOD
In [16]: groceries.head()
Out[16]:
OBJECTID ... geometry
0 16 ... MULTIPOINT ((1168268.671671558 1933554.3504257...
1 18 ... MULTIPOINT ((1162302.617919334 1832900.2240279...
2 22 ... MULTIPOINT ((1173317.042329894 1895425.4259547...
3 23 ... MULTIPOINT ((1168996.475130927 1898801.4056401...
4 27 ... MULTIPOINT ((1176991.988724414 1847262.4228848...
[5 rows x 8 columns]
# Execute spatial join
In [17]: groceries_with_community = groceries.sjoin(chicago, how="inner", predicate='intersects')
In [18]: groceries_with_community.head()
Out[18]:
OBJECTID Ycoord ... index_right community
0 16 41.973266 ... 30 UPTOWN
1 18 41.696367 ... 73 MORGAN PARK
2 22 41.868634 ... 28 NEAR WEST SIDE
3 23 41.877590 ... 28 NEAR WEST SIDE
4 27 41.737696 ... 39 CHATHAM
[5 rows x 10 columns]
```

GeoPandas provides two spatial-join functions:

`GeoDataFrame.sjoin()`

: joins based on binary predicates (intersects, contains, etc.)`GeoDataFrame.sjoin_nearest()`

: joins based on proximity, with the ability to set a maximum search radius.

Note

For historical reasons, both methods are also available as top-level functions `sjoin()`

and `sjoin_nearest()`

.
It is recommended to use methods as the functions may be deprecated in the future.

### Binary predicate joins#

Binary predicate joins are available via `GeoDataFrame.sjoin()`

.

`GeoDataFrame.sjoin()`

has two core arguments: `how`

and `predicate`

.

**predicate**

The `predicate`

argument specifies how GeoPandas decides whether or not to join the attributes of one
object to another, based on their geometric relationship.

The values for `predicate`

correspond to the names of geometric binary predicates and depend on the spatial
index implementation.

The default spatial index in GeoPandas currently supports the following values for `predicate`

which are
defined in the
Shapely documentation:

intersects

contains

within

touches

crosses

overlaps

**how**

The how argument specifies the type of join that will occur and which geometry is retained in the resultant
`GeoDataFrame`

. It accepts the following options:

`left`

: use the index from the first (or left_df)`GeoDataFrame`

that you provide to`GeoDataFrame.sjoin()`

; retain only the left_df geometry column`right`

: use index from second (or right_df); retain only the right_df geometry column`inner`

: use intersection of index values from both`GeoDataFrame`

; retain only the left_df geometry column

Note more complicated spatial relationships can be studied by combining geometric operations with spatial join.
To find all polygons within a given distance of a point, for example, one can first use the `buffer()`

method to expand each
point into a circle of appropriate radius, then intersect those buffered circles with the polygons in question.

### Nearest joins#

Proximity-based joins can be done via `GeoDataFrame.sjoin_nearest()`

.

`GeoDataFrame.sjoin_nearest()`

shares the `how`

argument with `GeoDataFrame.sjoin()`

, and
includes two additional arguments: `max_distance`

and `distance_col`

.

**max_distance**

The `max_distance`

argument specifies a maximum search radius for matching geometries. This can have a considerable performance impact in some cases.
If you can, it is highly recommended that you use this parameter.

**distance_col**

If set, the resultant GeoDataFrame will include a column with this name containing the computed distances between an input geometry and the nearest geometry.

## Source: https://geopandas.org/en/stable/docs/user_guide/geocoding.html

# Geocoding#

GeoPandas supports geocoding (i.e., converting place names to location on Earth) through geopy, an optional dependency of GeoPandas. The following example shows how to get the locations of boroughs in New York City, and plots those locations along with the detailed borough boundary file included within GeoPandas.

```
In [1]: import geodatasets
In [2]: boros = geopandas.read_file(geodatasets.get_path("nybb"))
In [3]: boros.BoroName
Out[3]:
0 Staten Island
1 Queens
2 Brooklyn
3 Manhattan
4 Bronx
Name: BoroName, dtype: str
In [4]: boro_locations = geopandas.tools.geocode(boros.BoroName)
In [5]: boro_locations
Out[5]:
geometry address
0 POINT (-74.1496048 40.5834557) Staten Island, New York, New York, United States
1 POINT (-73.8283132 40.7135078) Queens, New York, New York, United States
2 POINT (-73.9497211 40.6526006) Brooklyn, New York, New York, United States
3 POINT (-73.9855319 40.7579554) Manhattan, New York, New York, United States
4 POINT (-73.8785937 40.8466508) The Bronx, New York, New York, United States
In [6]: import matplotlib.pyplot as plt
In [7]: fig, ax = plt.subplots()
In [8]: boros.to_crs("EPSG:4326").plot(ax=ax, color="white", edgecolor="black");
In [9]: boro_locations.plot(ax=ax, color="red");
```

By default, the `geocode()`

function uses the
Photon geocoding API.
But a different geocoding service can be specified with the
`provider`

keyword.

The argument to `provider`

can either be a string referencing geocoding
services, such as `'google'`

, `'bing'`

, `'yahoo'`

, and
`'openmapquest'`

, or an instance of a `Geocoder`

from `geopy`

. See
`geopy.geocoders.SERVICE_TO_GEOCODER`

for the full list.
For many providers, parameters such as API keys need to be passed as
`**kwargs`

in the `geocode()`

call.

For example, to use the OpenStreetMap Nominatim geocoder, you need to specify a user agent:

```
geopandas.tools.geocode(boros.BoroName, provider='nominatim', user_agent="my-application")
```

Attention

Please consult the Terms of Service for the chosen provider. The example
above uses `'photon'`

(the default), which expects fair usage
- extensive usage will be throttled.
(Photon’s Terms of Use).

## Source: https://geopandas.org/en/stable/docs/user_guide/sampling.html

Note

# Sampling Points#

Learn how to sample random points using GeoPandas.

The example below shows you how to sample random locations from shapes in GeoPandas GeoDataFrames.

## Import Packages#

To begin with, we need to import packages we’ll use:

```
[1]:
```

```
import geopandas
import geodatasets
```

For this example, we will use the New York Borough example data (`nybb`

) provided by geodatasets.

```
[2]:
```

```
nybb = geopandas.read_file(geodatasets.get_path("nybb"))
# simplify geometry to save space when rendering many interactive maps
nybb.geometry = nybb.simplify(200)
```

To see what this looks like, visualize the data:

```
[3]:
```

```
nybb.explore()
```

```
[3]:
```

## Sampling random points#

To sample points from within a GeoDataFrame, use the `sample_points()`

method. To specify the sample sizes, provide an explicit number of points to sample. For example, we can sample 200 points randomly from each feature:

```
[4]:
```

```
n200_sampled_points = nybb.sample_points(200)
m = nybb.explore()
n200_sampled_points.explore(m=m, color='red')
```

```
[4]:
```

This functionality also works for line geometries. For example, let’s look only at the boundary of Manhattan Island:

```
[5]:
```

```
manhattan_parts = nybb.iloc[[3]].explode(ignore_index=True)
manhattan_island = manhattan_parts.iloc[[30]]
manhattan_island.boundary.explore()
```

```
[5]:
```

Sampling randomly from along this boundary can use the same `sample_points()`

method:

```
[6]:
```

```
manhattan_border_points = manhattan_island.boundary.sample_points(200)
m = manhattan_island.explore()
manhattan_border_points.explore(m=m, color='red')
```

```
[6]:
```

Keep in mind that sampled points are returned as a single multi-part geometry, and that the distances over the line segments are calculated *along* the line.

```
[7]:
```

```
manhattan_border_points
```

```
[7]:
```

```
30 MULTIPOINT ((978995.392 196739.185), (979054.9...
Name: sampled_points, dtype: geometry
```

If you want to separate out the individual sampled points, use the `.explode()`

method on the dataframe:

```
[8]:
```

```
manhattan_border_points.explode(ignore_index=True).head()
```

```
[8]:
```

```
0 POINT (978995.392 196739.185)
1 POINT (979054.948 196856.485)
2 POINT (979414.89 199633.108)
3 POINT (979587.506 200872.958)
4 POINT (979598.418 200951.336)
Name: sampled_points, dtype: geometry
```

## Variable number of points#

You can also sample different number of points from different geometries if you pass an array specifying the size of the sample per geometry.

```
[9]:
```

```
variable_size = nybb.sample_points([10, 50, 100, 200, 500])
m = nybb.explore()
variable_size.explore(m=m, color='red')
```

```
[9]:
```

## Sampling from more complicated point pattern processes#

Finally, the `sample_points()`

method can use different sampling processes than those described above, so long as they are implemented in the `pointpats`

package for spatial point pattern analysis. For example, a “cluster-poisson” process is a spatially-random cluster process where the “seeds” of clusters are chosen randomly, and then points around these clusters are distributed according again randomly.

To see what this looks like, consider the following, where ten points will be distributed around five seeds within each of the boroughs in New York City:

```
[10]:
```

```
sample_t = nybb.sample_points(method='cluster_poisson', size=50, n_seeds=5, cluster_radius=7500)
```

```
[11]:
```

```
m = nybb.explore()
sample_t.explore(m=m, color='red')
```

```
[11]:
```

## Source: https://geopandas.org/en/stable/docs/user_guide/how_to.html

# How to…#

## Drop duplicate geometry in all situations#

Using the standard Pandas `drop_duplicates()`

function on a geometry column can lead to some duplicate
geometries not being dropped, in certain circumstances. When used on a geometry columnm, the Pandas function compares the
WKB of each geometry object. This is sensitive to the orders of various components of the geometry - for example, a line
with co-ordinates in the order left-to-right should be equal to a line with the same co-ordinates in the order right-to-left,
but the WKB representations will be different. The same applies for the order of rings of polygons and parts in multipart
geometries.

To deal with this problem, use the `normalize()`

method first to order the co-ordinates in a canonincal form,
and then use the standard `drop_duplicates()`

method:

```
gdf["geometry"] = gdf.normalize()
gdf.drop_duplicates()
```

The effect of the `normalize()`

method can be seen in the following example:

```
>>> geopandas.GeoSeries([
... shapely.LineString([(0, 0), (1, 0), (2, 0)]),
... shapely.LineString([(2, 0), (1, 0), (0, 0)]),
... ]).normalize().to_wkt()
0 LINESTRING (0 0, 1 0, 2 0)
1 LINESTRING (0 0, 1 0, 2 0)
dtype: object
```

## Source: https://geopandas.org/en/stable/docs/user_guide/spatial_indexing.html

Note

# Spatial indexing#

When you want to know a spatial relationship (known as a spatial predicate) between a set of geometries A and a geometry B (or a set of them), you can compare geometry B against any geometry in a set A. However, that is not the most performant approach in most cases. A spatial index is a more efficient method for pre-filtering comparisons of geometries before using more computationally expensive spatial predicates. GeoPandas exposes the Sort-Tile-Recursive R-tree from shapely on any GeoDataFrame and GeoSeries using the GeoSeries.sindex property. This page outlines its options and common usage patterns.

Note that for many operations where a spatial index provides significant performance benefits, GeoPandas already uses it automatically (like sjoin(), overlay(), or clip()). However, more advanced use cases may require a direct interaction with the index.

```
[1]:
```

```
import geopandas
import matplotlib.pyplot as plt
import shapely
from geodatasets import get_path
```

Load data on New York City subboroughs to illustrate the spatial indexing.

```
[2]:
```

```
nyc = geopandas.read_file(get_path("geoda nyc"))
```

```
Downloading file 'nyc.zip' from 'https://geodacenter.github.io/data-and-lab///data/nyc.zip' to '/home/docs/.cache/geodatasets'.
```

## R-tree principle#

In principle, any R-tree index builds a hierarchical collection of bounding boxes (envelopes) representing first individual geometries and then their most efficient combinations (from a spatial query perspective). When creating one, you can imagine that your geometries are represented by their envelopes, as illustrated below.

```
[3]:
```

```
fig, axs = plt.subplots(1, 2, sharey=True, figsize=(8, 4))
nyc.plot(ax=axs[0], edgecolor="black", linewidth=1)
nyc.envelope.boundary.plot(ax=axs[1], color='black');
```

The left side of the figure shows the original geometries, while the right side their bounding boxes, extracted using the envelope property. Typically, the index works on top of those.

Let’s generate two points now, both intersecting at least one bounding box but only one intersecting the actual geometry.

```
[4]:
```

```
point_inside = shapely.Point(950000, 155000)
point_outside = shapely.Point(1050000, 150000)
points = geopandas.GeoSeries([point_inside, point_outside], crs=nyc.crs)
```

You can verify that visually.

```
[5]:
```

```
fig, axs = plt.subplots(1, 2, sharey=True, figsize=(8, 4))
nyc.plot(ax=axs[0], edgecolor="black", linewidth=1)
nyc.envelope.boundary.plot(ax=axs[1], color='black')
points.plot(ax=axs[0], color="limegreen")
points.plot(ax=axs[1], color="limegreen");
```

## Querying the index#

### Scalar query#

You can now use the sindex property to query the index. The query() method, by default, returns positions of all geometries whose bounding boxes intersect the bounding box of the input geometry.

```
[6]:
```

```
bbox_query_inside = nyc.sindex.query(point_inside)
bbox_query_outside = nyc.sindex.query(point_outside)
bbox_query_inside, bbox_query_outside
```

```
[6]:
```

```
(array([1]), array([16]))
```

Both the point we know is inside a geometry and the one that is outside a geometry return one hit as each intersects one bounding box in the tree.

```
[7]:
```

```
fig, axs = plt.subplots(1, 2, sharey=True, figsize=(8, 4))
nyc.plot(ax=axs[0], edgecolor="black", linewidth=1)
nyc.envelope.boundary.plot(ax=axs[1], color='black')
points.plot(ax=axs[0], color="limegreen", zorder=3, edgecolor="black", linewidth=.5)
points.plot(ax=axs[1], color="limegreen", zorder=3, edgecolor="black", linewidth=.5)
nyc.iloc[bbox_query_inside].plot(ax=axs[0], color='orange')
nyc.iloc[bbox_query_outside].plot(ax=axs[0], color='orange')
nyc.envelope.iloc[bbox_query_inside].plot(ax=axs[1], color='orange')
nyc.envelope.iloc[bbox_query_outside].plot(ax=axs[1], color='orange');
```

The image above provides a clear illustration of what happens. While you can see on the left image that only one intersects an orange geometry marked as a *hit*, the hits are quite clear when looking at the bounding box.

Thankfully, the spatial index allows for further filtering based on the actual geometry. In this case, the tree is first queried as above but afterwards, each of the possible hits is checked using a spatial predicate.

```
[8]:
```

```
pred_inside = nyc.sindex.query(point_inside, predicate="intersects")
pred_outside = nyc.sindex.query(point_outside, predicate="intersects")
pred_inside, pred_outside
```

```
[8]:
```

```
(array([1]), array([], dtype=int64))
```

When you specify `predicate="intersects"`

, the result is indeed different and the output of the query using the point that lies outside of any geometry is empty.

```
[9]:
```

```
fig, axs = plt.subplots(1, 2, sharey=True, figsize=(8, 4))
nyc.plot(ax=axs[0], edgecolor="black", linewidth=1)
nyc.envelope.boundary.plot(ax=axs[1], color='black')
points.plot(ax=axs[0], color="limegreen", zorder=3, edgecolor="black", linewidth=.5)
points.plot(ax=axs[1], color="limegreen", zorder=3, edgecolor="black", linewidth=.5)
nyc.iloc[pred_inside].plot(ax=axs[0], color='orange')
nyc.envelope.iloc[pred_inside].plot(ax=axs[1], color='orange');
```

You can use any of the predicates available in valid_query_predicates:

```
[10]:
```

```
nyc.sindex.valid_query_predicates
```

```
[10]:
```

```
{None,
'contains',
'contains_properly',
'covered_by',
'covers',
'crosses',
'dwithin',
'intersects',
'overlaps',
'touches',
'within'}
```

### Array query#

Checking a single geometry against the tree is nice but not that efficient if you are interested in many-to-many relationships. The query() method allows passing any 1-D array of geometries to be checked against the tree. If you do so, the output structure is slightly different:

```
[11]:
```

```
bbox_array_query = nyc.sindex.query(points)
bbox_array_query
```

```
[11]:
```

```
array([[ 0, 1],
[ 1, 16]])
```

By default, the method returns a 2-D array of indices where the query found a hit where the subarrays correspond to the indices of the input geometries and indices of the tree geometries associated with each. In the example above, the 0-th geometry in the `points`

GeoSeries intersects the bounding box of the geometry at the position 1 from the `nyc`

GeoDataFrame, while the geometry 1 in the `points`

matches geometry 16 in the `nyc`

. You may notice that these are the same indices as
you’ve seen above.

The other option is to return a boolean array with shape `(len(tree), n)`

with boolean values marking whether the bounding box of a geometry in the tree intersects a bounding box of a given geometry. This can be either a dense numpy array, or a sparse scipy array. Keep in mind that the output will be, in most cases, mostly filled with `False`

and the array can become really large, so it is recommended to use the sparse format, if possible.

You can specify each using the `output_format`

keyword:

```
[12]:
```

```
bbox_array_query_dense = nyc.sindex.query(points, output_format="dense")
bbox_array_query_dense
```

```
[12]:
```

```
array([[False, False],
[ True, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, True],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False],
[False, False]])
```

The dense array above has rows aligned with the rows of `nyc`

and columns aligned with the rows of `points`

and indicates all pairs where a *hit* was found.

The same array can be represented as a `scipy.sparse.coo_array`

:

```
[13]:
```

```
bbox_array_query_sparse = nyc.sindex.query(points, output_format="sparse")
bbox_array_query_sparse
```

```
[13]:
```

```
<COOrdinate sparse array of dtype 'bool'
with 2 stored elements and shape (55, 2)>
```

For example, to find the number of neighboring geometries for each subborough, you can use the spatial index to compare all geometries against each other. Since you are using `nyc`

on both sides of the query here, the resulting array is square-shaped with diagonal filled with `True`

.

```
[14]:
```

```
neighbors = nyc.sindex.query(nyc.geometry, predicate="intersects", output_format="dense")
neighbors
```

```
[14]:
```

```
array([[ True, True, False, ..., False, False, False],
[ True, True, True, ..., False, False, False],
[False, True, True, ..., False, False, False],
...,
[False, False, False, ..., True, True, True],
[False, False, False, ..., True, True, True],
[False, False, False, ..., True, True, True]], shape=(55, 55))
```

Getting the sum along one axis can then give you the answer. Note that since a geometry always intersects itself, you need to subtract one.

```
[15]:
```

```
n_neighbors = neighbors.sum(axis=1) - 1
n_neighbors
```

```
[15]:
```

```
array([1, 2, 1, 2, 4, 3, 7, 7, 3, 3, 6, 7, 4, 3, 4, 4, 1, 4, 2, 4, 3, 7,
4, 3, 4, 3, 3, 4, 7, 3, 4, 4, 2, 4, 3, 4, 5, 4, 5, 5, 5, 5, 6, 5,
7, 5, 6, 4, 4, 4, 5, 7, 5, 4, 3])
```

The result is a numpy array you can directly plot on a map.

```
[16]:
```

```
nyc.plot(n_neighbors, legend=True);
```

### Nearest geometry query#

While checking the spatial predicate using the spatial index is indeed extremely useful, GeoPandas also allows you to use the spatial index to find the nearest geometry. The API is similar as above:

```
[17]:
```

```
nearest_indices = nyc.sindex.nearest(points)
nearest_indices
```

```
[17]:
```

```
array([[ 0, 1],
[ 1, 16]])
```

You can see that the nearest query returns the indices representation. If you are interested in how “near” the geometries actually are, the method can also return distances. In this case, the return format is a tuple of arrays.

```
[18]:
```

```
nearest_indices, distance = nyc.sindex.nearest(points, return_distance=True)
distance
```

```
[18]:
```

```
array([ 0. , 4413.99923494])
```

## Source: https://geopandas.org/en/stable/docs/user_guide/missing_empty.html

# Missing and empty geometries#

GeoPandas supports, just like in pandas, the concept of missing values (NA or null values). But for geometry values, there is an additional concept of empty geometries:

**Empty geometries**are actual geometry objects but that have no coordinates (and thus also no area, for example). They can for example originate from taking the intersection of two polygons that have no overlap. The scalar object (when accessing a single element of a GeoSeries) is still a Shapely geometry object.**Missing geometries**are unknown values in a GeoSeries. They will typically be propagated in operations (for example in calculations of the area or of the intersection), or ignored in reductions such as`union_all()`

. The scalar object (when accessing a single element of a GeoSeries) is the Python`None`

object.

Warning

Starting from GeoPandas v0.6.0, those two concepts are more consistently separated. See below for more details on what changed compared to earlier versions.

Consider the following example GeoSeries with one polygon, one missing value and one empty polygon:

```
In [1]: from shapely.geometry import Polygon
In [2]: s = geopandas.GeoSeries([Polygon([(0, 0), (1, 1), (0, 1)]), None, Polygon([])])
In [3]: s
Out[3]:
0 POLYGON ((0 0, 1 1, 0 1, 0 0))
1 None
2 POLYGON EMPTY
dtype: geometry
```

In spatial operations, missing geometries will typically propagate (be missing in the result as well), while empty geometries are treated as a geometry and the result will depend on the operation:

```
In [4]: s.area
Out[4]:
0 0.5
1 NaN
2 0.0
dtype: float64
In [5]: s.union(Polygon([(0, 0), (0, 1), (1, 1), (1, 0)]))
Out[5]:
0 POLYGON ((1 1, 1 0, 0 0, 0 1, 1 1))
1 None
2 POLYGON ((0 1, 1 1, 1 0, 0 0, 0 1))
dtype: geometry
In [6]: s.intersection(Polygon([(0, 0), (0, 1), (1, 1), (1, 0)]))
Out[6]:
0 POLYGON ((0 0, 0 1, 1 1, 0 0))
1 None
2 POLYGON EMPTY
dtype: geometry
```

The `GeoSeries.isna()`

method will only check for missing values and not
for empty geometries:

```
In [7]: s.isna()
Out[7]:
0 False
1 True
2 False
dtype: bool
```

On the other hand, if you want to know which values are empty geometries,
you can use the `GeoSeries.is_empty`

attribute:

```
In [8]: s.is_empty
Out[8]:
0 False
1 False
2 True
dtype: bool
```

To get only the actual geometry objects that are neither missing nor empty, you can use a combination of both:

```
In [9]: s.is_empty | s.isna()
Out[9]:
0 False
1 True
2 True
dtype: bool
In [10]: s[~(s.is_empty | s.isna())]
Out[10]:
0 POLYGON ((0 0, 1 1, 0 1, 0 0))
dtype: geometry
```

## Changes since GeoPandas v0.6.0#

In GeoPandas v0.6.0, the missing data handling was refactored and made more consistent across the library.

Historically, missing (“NA”) values in a GeoSeries could be represented by empty
geometric objects, in addition to standard representations such as `None`

and
`np.nan`

. At least, this was the case in `GeoSeries.isna()`

or when a
GeoSeries got aligned in geospatial operations. But, other methods like
`dropna()`

and `fillna()`

did not follow this
approach and did not consider empty geometries as missing.

In GeoPandas v0.6.0, the most important change is `GeoSeries.isna()`

no
longer treating empty as missing:

Using the small example from above, the old behaviour treated both the empty as missing geometry as “missing”:

>>> s 0 POLYGON ((0 0, 1 1, 0 1, 0 0)) 1 None 2 GEOMETRYCOLLECTION EMPTY dtype: object >>> s.isna() 0 False 1 True 2 True dtype: bool

Starting from GeoPandas v0.6.0, it will now only see actual missing values as missing:

In [11]: s.isna() Out[11]: 0 False 1 True 2 False dtype: bool

For now, when

`isna()`

is called on a GeoSeries with empty geometries, a warning is raised to alert the user of the changed behaviour with an indication how to solve this.

Additionally, the behaviour of `GeoSeries.align()`

changed to use
missing values instead of empty geometries to fill non-matching indexes.
Consider the following small toy example:

```
In [12]: from shapely.geometry import Point
In [13]: s1 = geopandas.GeoSeries([Point(0, 0), Point(1, 1)], index=[0, 1])
In [14]: s2 = geopandas.GeoSeries([Point(1, 1), Point(2, 2)], index=[1, 2])
In [15]: s1
Out[15]:
0 POINT (0 0)
1 POINT (1 1)
dtype: geometry
In [16]: s2
Out[16]:
1 POINT (1 1)
2 POINT (2 2)
dtype: geometry
```

Previously, the

`align`

method would use empty geometries to fill values:>>> s1_aligned, s2_aligned = s1.align(s2) >>> s1_aligned 0 POINT (0 0) 1 POINT (1 1) 2 GEOMETRYCOLLECTION EMPTY dtype: object >>> s2_aligned 0 GEOMETRYCOLLECTION EMPTY 1 POINT (1 1) 2 POINT (2 2) dtype: object

This method is used under the hood when performing spatial operations on mis-aligned GeoSeries objects:

>>> s1.intersection(s2) 0 GEOMETRYCOLLECTION EMPTY 1 POINT (1 1) 2 GEOMETRYCOLLECTION EMPTY dtype: object

Starting from GeoPandas v0.6.0,

`GeoSeries.align()`

will use missing values to fill in the non-aligned indices, to be consistent with the behaviour in pandas:In [17]: s1_aligned, s2_aligned = s1.align(s2) In [18]: s1_aligned Out[18]: 0 POINT (0 0) 1 POINT (1 1) 2 None dtype: geometry In [19]: s2_aligned Out[19]: 0 None 1 POINT (1 1) 2 POINT (2 2) dtype: geometry

This has the consequence that spatial operations will also use missing values instead of empty geometries, which can have a different behaviour depending on the spatial operation:

In [20]: s1.intersection(s2) Out[20]: 0 None 1 POINT (1 1) 2 None dtype: geometry

## Source: https://geopandas.org/en/stable/docs/user_guide/reproject_fiona.html

# Re-projecting using GDAL with Rasterio and Fiona#

The simplest method of re-projecting is `GeoDataFrame.to_crs()`

.
It uses pyproj as the engine and transforms the points within the geometries.

These examples demonstrate how to use Fiona or rasterio as the engine to re-project your data. Fiona and rasterio are powered by GDAL and with algorithms that consider the geometry instead of just the points the geometry contains. This is particularly useful for antimeridian cutting. However, this also means the transformation is not as fast.

## Fiona example#

```
from functools import partial
import fiona
import geopandas
from fiona.transform import transform_geom
from packaging import version
from pyproj import CRS
from pyproj.enums import WktVersion
from shapely.geometry import mapping, shape
# set up Fiona transformer
def crs_to_fiona(proj_crs):
proj_crs = CRS.from_user_input(proj_crs)
if version.parse(fiona.__gdal_version__) < version.parse("3.0.0"):
fio_crs = proj_crs.to_wkt(WktVersion.WKT1_GDAL)
else:
# GDAL 3+ can use WKT2
fio_crs = proj_crs.to_wkt()
return fio_crs
def base_transformer(geom, src_crs, dst_crs):
return shape(
transform_geom(
src_crs=crs_to_fiona(src_crs),
dst_crs=crs_to_fiona(dst_crs),
geom=mapping(geom),
antimeridian_cutting=True,
)
)
# load natural earth land data
world = geopandas.read_file("https://naciscdn.org/naturalearth/110m/physical/ne_110m_land.zip")
destination_crs = "EPSG:3395"
forward_transformer = partial(base_transformer, src_crs=world.crs, dst_crs=destination_crs)
# Reproject to Mercator (after dropping Antartica)
world = world.drop(7)
with fiona.Env(OGR_ENABLE_PARTIAL_REPROJECTION="YES"):
mercator_world = world.set_geometry(world.geometry.apply(forward_transformer), crs=destination_crs)
```

## Rasterio example#

This example requires rasterio 1.2+ and GDAL 3+.

```
import geopandas
import rasterio.warp
from shapely.geometry import shape
# load example data
world = geopandas.read_file("https://naciscdn.org/naturalearth/110m/physical/ne_110m_land.zip")
# Reproject to Mercator (after dropping Antartica)
world = world.drop(7)
destination_crs = "EPSG:3395"
geometry = rasterio.warp.transform_geom(
src_crs=world.crs,
dst_crs=destination_crs,
geom=world.geometry.values,
)
mercator_world = world.set_geometry(
[shape(geom) for geom in geometry],
crs=destination_crs,
)
```

## Source: https://geopandas.org/en/stable/docs/user_guide/pygeos_to_shapely.html

# Migration from PyGEOS geometry backend to Shapely 2.0#

Since the 0.8 version, GeoPandas includes an experimental support of PyGEOS as an alternative geometry backend to Shapely. Recently, PyGEOS codebase was merged into the Shapely project and released as part of Shapely 2.0. GeoPandas will therefore deprecate support of the PyGEOS backend and will go forward with Shapely 2.0 as the only geometry engine exposing GEOS functionality.

Given that historically the PyGEOS engine was automatically used if the package is installed (this behaviour will changed in GeoPandas 0.14 where Shapely 2.0 is used by default if installed), some downstream code may depend on
PyGEOS geometries being available as underlying data of a `GeometryArray`

.

This guide outlines the migration from the PyGEOS-based code to the Shapely-based code.

## Migration period#

The migration is planned for three releases spanning approximately one year, starting with 0.13 released in the second quarter of 2023.

### GeoPandas 0.13#

PyGEOS is still used as a default backend over Shapely (1.8 or 2.0) if installed, with a

`FutureWarning`

warning about upcoming changes.

### GeoPandas 0.14#

The default backend is Shapely 2.0 and the PyGEOS is used only if Shapely 1.8 is installed instead of 2.0 or newer. The PyGEOS backend is still supported, but a user needs to opt in using the environment variable

`USE_PYGEOS`

as explained in the installation instructions.

### GeoPandas 1.0#

GeoPandas will remove support of both PyGEOS and Shapely<2.

## How to prepare your code for transition#

If you don’t use PyGEOS explicitly, there nothing to be done as GeoPandas internals will
take care of the transition. If you use PyGEOS directly and access an array of PyGEOS
geometries using `GeoSeries.values.data`

, you will need to make some changes to avoid
code breakage.

The recommended way is using Shapely vectorized operations on the `GeometryArray`

instead of accessing the NumPy array of geometries and using PyGEOS/Shapely operations
on the array.

This is a common pattern used with GeoPandas 0.12 (or earlier), that should now be avoided in new code:

```
>>> import pygeos
>>> geometries = gdf.geometry.values.data
>>> mrr = pygeos.minimum_rotated_rectangle(geometries)
```

The recommended way of refactoring this code would look like this (with Geopandas 0.12 or later):

```
>>> import shapely # shapely 2.0
>>> mrr = shapely.minimum_rotated_rectangle(gdf.geometry.array)
```

This code will work no matter which geometry backend GeoPandas actually uses, because on
the `GeometryArray`

level, it always returns Shapely geometry. Although keep in mind, that
it may involve additional overhead cost of converting PyGEOS geometry to Shapely
geometry.

Note that while in most cases, a simple replacement of `pygeos`

with `shapely`

together with a change of `gdf.geometry.values.data`

to `gdf.geometry.values`

or
analogous `gdf.geometry.array`

should work, there are some differences between the
API of PyGEOS and that of Shapely. Please consult the
Migrating from PyGEOS
document for details.

## Source: https://geopandas.org/en/stable/docs/user_guide/fiona_to_pyogrio.html

# Migration from the Fiona to the Pyogrio read/write engine#

Since version 0.11, GeoPandas started supporting two engines to read and write files: Fiona and Pyogrio.

It became possible to choose the engine using the `engine=`

parameter in
`geopandas.read_file()`

and `geopandas.GeoDataFrame.to_file()`

. It became also
possible to change the default engine globally with:

```
geopandas.options.io_engine = "pyogrio"
```

For Geopandas versions <1.0, GeoPandas defaulted to use Fiona. Starting from GeoPandas version 1.0, the global default has changed from Fiona to Pyogrio.

The main reason for this change is performance. Pyogrio is optimized for the use case relevant for GeoPandas: reading and writing in bulk. Because of this, in many cases speedups >5-20x can be observed.

This guide outlines the (known) functional differences between both, so you can account for them when switching to Pyogrio.

## Write an attribute table to a file#

Using the Fiona engine, it was possible to write an attribute table (a table without
geometry column) to a file using the `schema`

parameter to specify that the “geometry”
column of a GeoDataFrame should be ignored.

With Pyogrio you can write an attribute table by using `pyogrio.write_dataframe()`

and passing a pandas DataFrame to it:

```
>>> import pyogrio
>>> df = pd.DataFrame({"data_column": [1, 2, 3]})
>>> pyogrio.write_dataframe(df, "test_attribute_table.gpkg")
```

## No support for `schema`

parameter to write files#

Pyogrio does not support specifying the schema parameter to write files. This means it is not possible to specify the types of attributes being written explicitly.

## Writing EMPTY geometries#

Pyogrio writes EMPTY and None geometries as such to e.g. GPKG files, Fiona writes both as None.

```
In [1]: import shapely
In [2]: gdf = geopandas.GeoDataFrame(geometry=[shapely.Polygon(), None], crs=31370)
In [3]: gdf.to_file("test_fiona.gpkg", engine="fiona")
In [4]: gdf.to_file("test_pyogrio.gpkg", engine="pyogrio")
In [5]: geopandas.read_file("test_fiona.gpkg").head()
Out[5]:
geometry
0 None
1 None
In [6]: geopandas.read_file("test_pyogrio.gpkg").head()
Out[6]:
geometry
0 POLYGON EMPTY
1 None
```
