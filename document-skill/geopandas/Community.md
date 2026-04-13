## Source: https://geopandas.org/en/stable/community.html

# Community#

GeoPandas is a community-led project written, used and supported by a wide range of people from all around of world of a large variety of backgrounds. Everyone is welcome, each small contribution, no matter if it is a fix of a typo in the documentation, bug report, an idea, or a question, is valuable. As a member of our community, you should adhere to the principles presented in the Code of Conduct.

If you’d like to contribute, please read the Contributing guide. It will help you to understand the way GeoPandas development works and us to review your contribution.

GeoPandas is a part of the broader Python ecosystem. It depends on a range of great tools, and various packages are built on top of GeoPandas addressing specific needs in geospatial data processing, analysis and visualization.

# GeoPandas Project Code of Conduct#

Behind the GeoPandas Project is an engaged and respectful community made up of people from all over the world and with a wide range of backgrounds. Naturally, this implies diversity of ideas and perspectives on often complex problems. Disagreement and healthy discussion of conflicting viewpoints is welcome: the best solutions to hard problems rarely come from a single angle. But disagreement is not an excuse for aggression: humans tend to take disagreement personally and easily drift into behavior that ultimately degrades a community. This is particularly acute with online communication across language and cultural gaps, where many cues of human behavior are unavailable. We are outlining here a set of principles and processes to support a healthy community in the face of these challenges.

Fundamentally, we are committed to fostering a productive, harassment-free environment for everyone. Rather than considering this code an exhaustive list of things that you can’t do, take it in the spirit it is intended - a guide to make it easier to enrich all of us and the communities in which we participate.

Importantly: as a member of our community, *you are also a steward of these
values*. Not all problems need to be resolved via formal processes, and often
a quick, friendly but clear word on an online forum or in person can help
resolve a misunderstanding and de-escalate things.

However, sometimes these informal processes may be inadequate: they fail to work, there is urgency or risk to someone, nobody is intervening publicly and you don’t feel comfortable speaking in public, etc. For these or other reasons, structured follow-up may be necessary and here we provide the means for that: we welcome reports by emailing geopandas-conduct@googlegroups.com or by filling out this form.

This code applies equally to founders, developers, mentors and new community members, in all spaces managed by the GeoPandas Project. This includes the mailing lists, our GitHub organization, our chat room, in-person events, and any other forums created by the project team. In addition, violations of this code outside these spaces may affect a person’s ability to participate within them.

By embracing the following principles, guidelines and actions to follow or avoid, you will help us make Jupyter a welcoming and productive community. Feel free to contact the Code of Conduct Committee at geopandas-conduct@googlegroups.com with any questions.

**Be friendly and patient**.**Be welcoming**. We strive to be a community that welcomes and supports people of all backgrounds and identities. This includes, but is not limited to, members of any race, ethnicity, culture, national origin, color, immigration status, social and economic class, educational level, sex, sexual orientation, gender identity and expression, age, physical appearance, family status, technological or professional choices, academic discipline, religion, mental ability, and physical ability.**Be considerate**. Your work will be used by other people, and you in turn will depend on the work of others. Any decision you take will affect users and colleagues, and you should take those consequences into account when making decisions. Remember that we’re a world-wide community. You may be communicating with someone with a different primary language or cultural background.**Be respectful**. Not all of us will agree all the time, but disagreement is no excuse for poor behavior or poor manners. We might all experience some frustration now and then, but we cannot allow that frustration to turn into a personal attack. It’s important to remember that a community where people feel uncomfortable or threatened is not a productive one.**Be careful in the words that you choose**. Be kind to others. Do not insult or put down other community members. Harassment and other exclusionary behavior are not acceptable. This includes, but is not limited to:Violent threats or violent language directed against another person

Discriminatory jokes and language

Posting sexually explicit or violent material

Posting (or threatening to post) other people’s personally identifying information (“doxing”)

Personal insults, especially those using racist, sexist, and xenophobic terms

Unwelcome sexual attention

Advocating for, or encouraging, any of the above behavior

Repeated harassment of others. In general, if someone asks you to stop, then stop

**Moderate your expectations**. Please respect that community members choose how they spend their time in the project. A thoughtful question about your expectations is preferable to demands for another person’s time.**When we disagree, try to understand why**. Disagreements, both social and technical, happen all the time and the GeoPandas Project is no exception. Try to understand where others are coming from, as seeing a question from their viewpoint may help find a new path forward. And don’t forget that it is human to err: blaming each other doesn’t get us anywhere, while we can learn from mistakes to find better solutions.**A simple apology can go a long way**. It can often de-escalate a situation, and telling someone that you are sorry is an act of empathy that doesn’t automatically imply an admission of guilt.

## Reporting#

If you believe someone is violating the code of conduct, please report this in a timely manner. Code of conduct violations reduce the value of the community for everyone and we take them seriously.

You can file a report by emailing geopandas-conduct@googlegroups.com or by filing out this form.

The online form gives you the option to keep your report anonymous or request that we follow up with you directly. While we cannot follow up on an anonymous report, we will take appropriate action.

Messages sent to the e-mail address or through the form will be sent only to the Code of Conduct Committee, which currently consists of:

Hannah Aizenman

Joris Van den Bossche

Martin Fleischmann

## Enforcement#

Enforcement procedures within the GeoPandas Project follow Project Jupyter’s Enforcement Manual. For information on enforcement, please view the original manual.

Original text courtesy of the Speak Up!, Django and Jupyter Projects, modified by the GeoPandas Project. We are grateful to those projects for contributing these materials under open licensing terms for us to easily reuse.

All content on this page is licensed under a Creative Commons Attribution license.

## Source: https://geopandas.org/en/stable/community/ecosystem.html

# Ecosystem#

## GeoPandas dependencies#

GeoPandas brings together the full capability of `pandas`

and the open-source geospatial
tools `Shapely`

, which brings manipulation and analysis of geometric objects backed by
`GEOS`

library, `pyogrio`

, allowing us to read and write
geographic data files using `GDAL`

, and `pyproj`

, a library for
cartographic projections and coordinate transformations, which is a Python interface to
`PROJ`

.

Furthermore, GeoPandas has several optional dependencies as
`mapclassify`

, or `geopy`

.

### Required dependencies#

#### pandas#

`pandas`

is a Python package that provides fast, flexible, and expressive data
structures designed to make working with structured (tabular, multidimensional,
potentially heterogeneous) and time series data both easy and intuitive. It aims to be
the fundamental high-level building block for doing practical, real world data analysis
in Python. Additionally, it has the broader goal of becoming the most powerful and
flexible open source data analysis / manipulation tool available in any language. It is
already well on its way toward this goal.

#### Shapely#

`Shapely`

is a BSD-licensed Python package for manipulation and analysis of planar
geometric objects. It is based on the widely deployed `GEOS`

(the engine of PostGIS) and
`JTS`

(from which `GEOS`

is ported) libraries. `Shapely`

is not concerned with data
formats or coordinate systems, but can be readily integrated with packages that are.

#### pyogrio#

Pyogrio provides a GeoPandas-oriented API to OGR vector data sources, such as ESRI Shapefile, GeoPackage, and GeoJSON. Vector data sources have geometries, such as points, lines, or polygons, and associated records with potentially many columns worth of data.

#### pyproj#

`pyproj`

is a Python interface to `PROJ`

(cartographic projections and coordinate
transformations library). GeoPandas uses a `pyproj.crs.CRS`

object to keep track of the
projection of each `GeoSeries`

and its `Transformer`

object to manage re-projections.

### Optional dependencies#

#### mapclassify#

`mapclassify`

provides functionality for Choropleth map classification. Currently,
fifteen different classification schemes are available, including a highly-optimized
implementation of Fisher-Jenks optimal classification. Each scheme inherits a common
structure that ensures computations are scalable and supports applications in streaming
contexts.

#### geopy#

`geopy`

is a Python client for several popular geocoding web services. `geopy`

makes it
easy for Python developers to locate the coordinates of addresses, cities, countries,
and landmarks across the globe using third-party geocoders and other data sources.

#### matplotlib#

`Matplotlib`

is a comprehensive library for creating static, animated, and interactive
visualizations in Python. Matplotlib produces publication-quality figures in a variety
of hardcopy formats and interactive environments across platforms. Matplotlib can be
used in Python scripts, the Python and IPython shell, web application servers, and
various graphical user interface toolkits.

#### Fiona#

`Fiona`

is `GDAL’s`

neat and nimble vector API for Python programmers. Fiona is designed
to be simple and dependable. It focuses on reading and writing data in standard Python
IO style and relies upon familiar Python types and protocols such as files,
dictionaries, mappings, and iterators instead of classes specific to `OGR`

. Fiona can
read and write real-world data using multi-layered GIS formats and zipped virtual file
systems and integrates readily with other Python GIS packages such as `pyproj`

, `Rtree`

,
and `Shapely`

.

## GeoPandas ecosystem#

Various packages are built on top of GeoPandas addressing specific geospatial data processing needs, analysis, and visualization. Below is an incomplete list (in no particular order) of tools which form the GeoPandas-related Python ecosystem.

### Spatial analysis and Machine Learning#

#### PySAL#

`PySAL`

, the Python spatial analysis library, is an open source cross-platform library
for geospatial data science with an emphasis on geospatial vector data written in
Python. `PySAL`

is a family of packages, some of which are listed below.

##### libpysal#

`libpysal`

provides foundational algorithms and data structures that support the rest of
the library. This currently includes the following modules: input/output (`io`

), which
provides readers and writers for common geospatial file formats; weights (`weights`

),
which provides the main class to store spatial weights matrices, as well as several
utilities to manipulate and operate on them; computational geometry (`cg`

), with several
algorithms, such as Voronoi tessellations or alpha shapes that efficiently process
geometric shapes; and an additional module with example data sets (`examples`

).

##### esda#

`esda`

implements methods for the analysis of both global (map-wide) and local (focal)
spatial autocorrelation, for both continuous and binary data. In addition, the package
increasingly offers cutting-edge statistics about boundary strength and measures of
aggregation error in statistical analyses.

##### segregation#

`segregation`

package calculates over 40 different segregation indices and provides a
suite of additional features for measurement, visualization, and hypothesis testing that
together represent the state of the art in quantitative segregation analysis.

##### mgwr#

`mgwr`

provides scalable algorithms for estimation, inference, and prediction using
single- and multi-scale geographically weighted regression models in a variety of
generalized linear model frameworks, as well as model diagnostics tools.

##### tobler#

`tobler`

provides functionality for areal interpolation and dasymetric mapping.
`tobler`

includes functionality for interpolating data using area-weighted approaches,
regression model-based approaches that leverage remotely-sensed raster data as auxiliary
information, and hybrid approaches.

#### movingpandas#

`MovingPandas`

is a package for dealing with movement data. `MovingPandas`

implements a
`Trajectory`

class and corresponding methods based on GeoPandas. A trajectory has a
time-ordered series of point geometries. These points and associated attributes are
stored in a `GeoDataFrame`

. `MovingPandas`

implements spatial and temporal data access
and analysis functions as well as plotting functions.

#### momepy#

`momepy`

is a library for quantitative analysis of urban form - urban morphometrics. It
is built on top of `GeoPandas`

, `PySAL`

and `networkX`

. `momepy`

aims to provide a wide
range of tools for a systematic and exhaustive analysis of urban form. It can work with
a wide range of elements, while focused on building footprints and street networks.

#### geosnap#

`geosnap`

makes it easier to explore, model, analyze, and visualize the social and
spatial dynamics of neighborhoods. `geosnap`

provides a suite of tools for creating
socio-spatial datasets, harmonizing those datasets into consistent set of time-static
boundaries, modeling bespoke neighborhoods and prototypical neighborhood types, and
modeling neighborhood change using classic and spatial statistical methods. It also
provides a set of static and interactive visualization tools to help you display and
understand the critical information at each step of the process.

#### mesa-geo#

`mesa-geo`

implements a GeoSpace that can host GIS-based GeoAgents, which are like
normal Agents, except they have a shape attribute that is a `Shapely`

object. You can
use `Shapely`

directly to create arbitrary shapes, but in most cases you will want to
import your shapes from a file. Mesa-geo allows you to create GeoAgents from any vector
data file (e.g. shapefiles), valid GeoJSON objects or a GeoPandas `GeoDataFrame`

.

#### Pyspatialml#

`Pyspatialml`

is a Python module for applying `scikit-learn`

machine learning models to
‘stacks’ of raster datasets. Pyspatialml includes functions and classes for working with
multiple raster datasets and performing a typical machine learning workflow consisting
of extracting training data and applying the predict or `predict_proba`

methods of
`scikit-learn`

estimators to a stack of raster datasets. Pyspatialml is built upon the
`rasterio`

Python module for all of the heavy lifting, and is also designed for working
with vector data using the `geopandas`

module.

#### PyGMI#

`PyGMI`

stands for Python Geoscience Modelling and Interpretation. It is a modelling and
interpretation suite aimed at magnetic, gravity and other datasets.

### Visualization#

#### hvPlot#

`hvPlot`

provides interactive Bokeh-based plotting for GeoPandas
dataframes and series using the same API as the Matplotlib `.plot()`

support that comes with GeoPandas. hvPlot makes it simple to pan and zoom into
your plots, use widgets to explore multidimensional data, and render even the
largest datasets in web browsers using Datashader.

#### contextily#

`contextily`

is a small Python 3 (3.6 and above) package to retrieve tile maps from the
internet. It can add those tiles as basemap to `matplotlib`

figures or write tile maps
to disk into geospatial raster files. Bounding boxes can be passed in both WGS84
(EPSG:4326) and Spheric Mercator (EPSG:3857).

#### cartopy#

`Cartopy`

is a Python package designed to make drawing maps for data analysis and
visualisation easy. It features: object oriented projection definitions; point, line,
polygon and image transformations between projections; integration to expose advanced
mapping in `Matplotlib`

with a simple and intuitive interface; powerful vector data
handling by integrating shapefile reading with `Shapely`

capabilities.

#### bokeh#

`Bokeh`

is an interactive visualization library for modern web browsers. It provides
elegant, concise construction of versatile graphics, and affords high-performance
interactivity over large or streaming datasets. `Bokeh`

can help anyone who would like
to quickly and easily make interactive plots, dashboards, and data applications.

#### folium#

`folium`

builds on the data wrangling strengths of the Python ecosystem and the mapping
strengths of the `Leaflet.js`

library. Manipulate your data in Python, then visualize it
in a `Leaflet`

map via `folium`

.

#### kepler.gl#

`Kepler.gl`

is a data-agnostic, high-performance web-based application for visual
exploration of large-scale geolocation data sets. Built on top of Mapbox GL and
`deck.gl`

, `kepler.gl`

can render millions of points representing thousands of trips and
perform spatial aggregations on the fly.

#### geoplot#

`geoplot`

is a high-level Python geospatial plotting library. It’s an extension to
`cartopy`

and `matplotlib`

which makes mapping easy: like `seaborn`

for geospatial. It
comes with the high-level plotting API, native projection support and compatibility with
`matplotlib`

.

#### GeoViews#

`GeoViews`

is a Python library that makes it easy to explore and
visualize any data that includes geographic locations, with native
support for GeoPandas dataframes and series objects. It has
particularly powerful support for multidimensional meteorological and
oceanographic datasets, such as those used in weather, climate, and
remote sensing research, but is useful for almost anything that you
would want to plot on a map!

#### EarthPy#

`EarthPy`

is a python package that makes it easier to plot and work with spatial raster
and vector data using open source tools. `Earthpy`

depends upon `geopandas`

which has a
focus on vector data and `rasterio`

with facilitates input and output of raster data
files. It also requires `matplotlib`

for plotting operations. `EarthPy’s`

goal is to
make working with spatial data easier for scientists.

#### splot#

`splot`

provides statistical visualizations for spatial analysis. It methods for
visualizing global and local spatial autocorrelation (through Moran scatterplots and
cluster maps), temporal analysis of cluster dynamics (through heatmaps and rose
diagrams), and multivariate choropleth mapping (through value-by-alpha maps). A high
level API supports the creation of publication-ready visualizations

#### legendgram#

`legendgram`

is a small package that provides “legendgrams” legends that visualize the
distribution of observations by color in a given map. These distributional
visualizations for map classification schemes assist in analytical cartography and
spatial data visualization.

#### buckaroo#

`buckaroo`

is a modern data table for Jupyter that expedites the most
common exploratory data analysis tasks. It provides scrollable tables,
histograms, and summary stats. Buckaroo supports many DataFrame
libraries including `geopandas`

. It can display `GeoDataFrame`

s as
tables, it also supports rendering the Geometry as an SVG in the
table.

### Geometry manipulation#

#### TopoJSON#

`topojson`

is a library for creating a TopoJSON encoding of nearly any
geographical object in Python. With topojson it is possible to reduce the size of
your geographical data, typically by orders of magnitude. It is able to do so through
eliminating redundancy through computation of a topology, fixed-precision integer
encoding of coordinates, and simplification and quantization of arcs.

#### geocube#

Tool to convert geopandas vector data into rasterized `xarray`

data.

### Data retrieval#

#### OSMnx#

`OSMnx`

is a Python package that lets you download spatial data from OpenStreetMap and
model, project, visualize, and analyze real-world street networks. You can download and
model walkable, drivable, or bikeable urban networks with a single line of Python code
and then easily analyze and visualize them. You can just as easily download and work with
other infrastructure types, amenities/points of interest, building footprints, elevation
data, street bearings/orientations, and speed/travel time.

#### pyrosm#

`Pyrosm`

is a Python library for reading OpenStreetMap data from Protocolbuffer Binary
Format -files (`*.osm.pbf`

) into Geopandas `GeoDataFrames`

. `Pyrosm`

makes it easy to
extract various datasets from OpenStreetMap pbf-dumps including e.g. road networks,
buildings, Points of Interest (POI), landuse and natural elements. Also fully customized
queries are supported which makes it possible to parse the data from OSM with more
specific filters.

#### geobr#

`geobr`

is a computational package to download official spatial data sets of Brazil. The
package includes a wide range of geospatial data in geopackage format (like shapefiles
but better), available at various geographic scales and for various years with
harmonized attributes, projection and topology.

#### cenpy#

An interface to explore and query the US Census API and return Pandas `Dataframes`

. This
package is intended for exploratory data analysis and draws inspiration from
sqlalchemy-like interfaces and `acs.R`

. With separate APIs for application developers
and folks who only want to get their data quickly & painlessly, `cenpy`

should meet the
needs of most who aim to get US Census Data into Python.

#### pygadm#

`pygadm`

is a Python package that lets you request spatial data from GADM
without manually downloading any file. This package aims at simplifying the requests
of the data using few parameters such as the name and the subdivision levels.
Outputs are served as `GeoDataFrame`

in `epsg:4326`

.
