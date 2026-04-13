## Source: https://geopandas.org/en/stable/docs/reference.html

# API reference#

The API reference provides an overview of all public objects, functions and methods implemented in GeoPandas. All classes and function exposed in `geopandas.*`

namespace plus those listed in the reference are public.

Warning

The `geopandas.array`

and `geopandas.base`

modules are private. Stable functionality in such modules is not guaranteed.

- GeoSeries
- Constructor
- General methods and attributes
- Unary predicates
- Binary predicates
- Set-theoretic methods
- Constructive methods and attributes
- Affine transformations
- Linestring operations
- Aggregating and exploding
- Serialization / IO / conversion
- Projection handling
- Missing values
- Overlay operations
- Plotting
- Spatial index
- Indexing
- Interface

- GeoDataFrame
- Input/output
- Tools
- Spatial index
- Testing

## Source: https://geopandas.org/en/stable/docs/reference/geoseries.html

# GeoSeries#

## Constructor#

|
A Series object designed to store shapely geometry objects. |

## General methods and attributes#

Return a |
|
Return a |
|
Return a |
|
Return a tuple containing |
|
Return a |
|
Returns a |
|
|
Return a |
|
Return a |
|
Return a |
|
Return a |
Return a |
|
Return a |
|
Return a |
|
Return a Series of the radii of the minimum bounding circles that enclose each geometry. |
|
Return a |
|
Return the x location of point geometries in a GeoSeries. |
|
Return the y location of point geometries in a GeoSeries. |
|
Return the z location of point geometries in a GeoSeries. |
|
Return the m coordinate of point geometries in a GeoSeries. |
|
|
|
Return a |
|
Return a |
|
Return a |
|
|
Return a |
Return a |
|
|
Return the n-th geometry from a collection of geometries. |

## Unary predicates#

Return a |
|
Returns a |
|
Return a |
|
Return a |
|
Return a |
|
Return a |
|
|
Return a |
|
Return a |
Return a |
|
Return a |
|
Return a |

## Binary predicates#

|
Return a |
|
Return a |
|
Return a |
|
Return a |
|
Return a |
|
Return a |
|
Return True for all geometries that equal aligned |
|
Return True for all geometries that are identical aligned |
|
Return a |
|
Return True for all aligned geometries that overlap |
|
Return a |
|
Return a |
|
Return a |
|
Return a |
|
Return the DE-9IM intersection matrices for the geometries. |
|
Return True if the DE-9IM string code for the relationship between the geometries satisfies the pattern, else False. |

## Set-theoretic methods#

|
Return a |
|
Return a |
|
Return a |
|
Return a |
|
Return a |

## Constructive methods and attributes#

Return a |
|
|
Return a |
Return a |
|
|
Return a |
Return a |
|
Return a |
|
Return a |
|
Force the dimensionality of a geometry to 2D. |
|
|
Force the dimensionality of a geometry to 3D. |
|
Repairs invalid geometries. |
Return a |
|
|
Return a |
Return a |
|
Return a |
|
Return a |
|
Return a |
|
|
Return a |
|
Return a |
Return a |
|
|
Sample points from each geometry. |
|
Return a |
|
Return the shortest two-point line between two geometries. |
|
Return a |
|
Return a |
|
Snap the vertices and segments of the geometry to vertices of the reference. |
|
Return a |

## Affine transformations#

|
Return a |
|
Return a |
|
Return a |
|
Return a |
|
Return a |

## Linestring operations#

|
Return a point at the specified distance along each geometry. |
|
Return (Multi)LineStrings formed by combining the lines in a MultiLineString. |
|
Return the distance along each geometry nearest to |
|
Return the shared paths between two geometries. |

## Aggregating and exploding#

|
Create an areal geometry formed by the constituent linework. |
Return a |
|
|
Return a |
|
Explode multi-part geometries into multiple single geometries. |
Return a geometry containing the intersection of all geometries in the |
|
|
Create polygons formed from the linework of a GeoSeries. |
|
Return a geometry containing the union of all geometries in the |
|
Return a |

## Serialization / IO / conversion#

|
Construct a GeoSeries from an Arrow array object with a GeoArrow extension type. |
|
Alternate constructor to create a |
|
Alternate constructor to create a |
|
Alternate constructor to create a |
|
Alternate constructor to create a |
|
Encode a GeoSeries to GeoArrow format. |
|
Write the |
|
Return a GeoJSON string representation of the GeoSeries. |
|
Convert GeoSeries geometries to WKB. |
|
Convert GeoSeries geometries to WKT. |

## Projection handling#

The Coordinate Reference System (CRS) as a |
|
|
|
|
Return a |
|
Return the estimated UTM CRS based on the bounds of the dataset. |

## Missing values#

|
Fill NA values with geometry (or geometries). |
Detect missing values. |
|
Detect non-missing values. |

## Overlay operations#

|
Clip points, lines, or polygon geometries to the mask extent. |

## Plotting#

|
Plot a GeoSeries. |
|
Explore with an interactive map based on folium/leaflet.js.Interactive map based on GeoPandas and folium/leaflet.js. |

## Spatial index#

Generate the spatial index. |
|
Check the existence of the spatial index without generating it. |

## Indexing#

Coordinate based indexer to select by intersection with bounding box. |

## Interface#

Returns a |

Methods of pandas `Series`

objects are also available, although not
all are applicable to geometric objects and some may return a
`Series`

rather than a `GeoSeries`

result when appropriate. The methods
`isna()`

and `fillna()`

have been
implemented specifically for `GeoSeries`

and are expected to work
correctly.

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.html

# geopandas.GeoSeries#

-
class geopandas.GeoSeries(
*data=None*,*index=None*,*crs=None*,***kwargs*)[source]# A Series object designed to store shapely geometry objects.

- Parameters:
**data**array-like, dict, scalar valueThe geometries to store in the GeoSeries.

**index**array-like or IndexThe index for the GeoSeries.

**crs**value (optional)Coordinate Reference System of the geometry objects. Can be anything accepted by

`pyproj.CRS.from_user_input()`

, such as an authority string (eg “EPSG:4326”) or a WKT string.**kwargs**- Additional arguments passed to the Series constructor,
e.g.

`name`

.

See also

Examples

>>> from shapely.geometry import Point >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)]) >>> s 0 POINT (1 1) 1 POINT (2 2) 2 POINT (3 3) dtype: geometry

>>> s = geopandas.GeoSeries( ... [Point(1, 1), Point(2, 2), Point(3, 3)], crs="EPSG:3857" ... ) >>> s.crs <Projected CRS: EPSG:3857> Name: WGS 84 / Pseudo-Mercator Axis Info [cartesian]: - X[east]: Easting (metre) - Y[north]: Northing (metre) Area of Use: - name: World - 85°S to 85°N - bounds: (-180.0, -85.06, 180.0, 85.06) Coordinate Operation: - name: Popular Visualisation Pseudo-Mercator - method: Popular Visualisation Pseudo Mercator Datum: World Geodetic System 1984 - Ellipsoid: WGS 84 - Prime Meridian: Greenwich

>>> s = geopandas.GeoSeries( ... [Point(1, 1), Point(2, 2), Point(3, 3)], index=["a", "b", "c"], crs=4326 ... ) >>> s a POINT (1 1) b POINT (2 2) c POINT (3 3) dtype: geometry

>>> s.crs <Geographic 2D CRS: EPSG:4326> Name: WGS 84 Axis Info [ellipsoidal]: - Lat[north]: Geodetic latitude (degree) - Lon[east]: Geodetic longitude (degree) Area of Use: - name: World. - bounds: (-180.0, -90.0, 180.0, 90.0) Datum: World Geodetic System 1984 ensemble - Ellipsoid: WGS 84 - Prime Meridian: Greenwich

Methods

`__init__`

([data, index, crs])`abs`

()Return a Series/DataFrame with absolute numeric value of each element.

`add`

(other[, level, fill_value, axis])Return Addition of series and other, element-wise (binary operator add).

`add_prefix`

(prefix[, axis])Prefix labels with string prefix.

`add_suffix`

(suffix[, axis])Suffix labels with string suffix.

`affine_transform`

(matrix)Return a

`GeoSeries`

with translated geometries.`agg`

([func, axis])Aggregate using one or more operations over the specified axis.

`aggregate`

([func, axis])Aggregate using one or more operations over the specified axis.

`align`

(other[, join, axis, level, copy, ...])Align two objects on their axes with the specified join method.

`all`

(*[, axis, bool_only, skipna])Return whether all elements are True, potentially over an axis.

`any`

(*[, axis, bool_only, skipna])Return whether any element is True, potentially over an axis.

`apply`

(func[, convert_dtype, args])One-dimensional ndarray with axis labels (including time series).

`argmax`

([axis, skipna])Return int position of the largest value in the Series.

`argmin`

([axis, skipna])Return int position of the smallest value in the Series.

`argsort`

([axis, kind, order, stable])Return the integer indices that would sort the Series values.

`asfreq`

(freq[, method, how, normalize, ...])Convert time series to specified frequency.

`asof`

(where[, subset])Return the last row(s) without any NaNs before where.

`astype`

(dtype[, copy, errors])Cast a pandas object to a specified dtype

`dtype`

.`at_time`

(time[, asof, axis])Select values at particular time of day (e.g., 9:30AM).

`autocorr`

([lag])Compute the lag-N autocorrelation.

`between`

(left, right[, inclusive])Return boolean Series equivalent to left <= series <= right.

`between_time`

(start_time, end_time[, ...])Select values between particular times of the day (e.g., 9:00-9:30 AM).

`bfill`

(*[, axis, inplace, limit, limit_area])Fill NA/NaN values by using the next valid observation to fill the gap.

`buffer`

(distance[, resolution, cap_style, ...])Return a

`GeoSeries`

of geometries representing all points within a given`distance`

of each geometric object.`build_area`

([node])Create an areal geometry formed by the constituent linework.

`case_when`

(caselist)Replace values where the conditions are True.

`clip`

(mask[, keep_geom_type, sort])Clip points, lines, or polygon geometries to the mask extent.

`clip_by_rect`

(xmin, ymin, xmax, ymax)Return a

`GeoSeries`

of the portions of geometry within the given rectangle.`combine`

(other, func[, fill_value])Combine the Series with a Series or scalar according to func.

`combine_first`

(other)Update null elements with value in the same location in 'other'.

`compare`

(other[, align_axis, keep_shape, ...])Compare to another Series and show the differences.

`concave_hull`

([ratio, allow_holes])Return a

`GeoSeries`

of geometries representing the concave hull of vertices of each geometry.Return a

`GeoSeries`

with the constrained Delaunay triangulation of polygons.`contains`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that contains other.`contains_properly`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that is completely inside`other`

, with no common boundary points.`convert_dtypes`

([infer_objects, ...])Convert columns from numpy dtypes to the best dtypes that support

`pd.NA`

.`copy`

([deep])Make a copy of this object's indices and data.

`corr`

(other[, method, min_periods])Compute correlation with other Series, excluding missing values.

`count`

()Return number of non-NA/null observations in the Series.

Return a

`Series`

containing the count of the number of coordinate pairs in each geometry.Return a

`Series`

containing the count of geometries in each multi-part geometry.Return a

`Series`

containing the count of the number of interior rings in a polygonal geometry.`cov`

(other[, min_periods, ddof])Compute covariance with Series, excluding missing values.

`covered_by`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that is entirely covered by other.`covers`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that is entirely covering other.`crosses`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that cross other.`cummax`

([axis, skipna])Return cumulative maximum over a Series.

`cummin`

([axis, skipna])Return cumulative minimum over a Series.

`cumprod`

([axis, skipna])Return cumulative product over a Series.

`cumsum`

([axis, skipna])Return cumulative sum over a Series.

`delaunay_triangles`

([tolerance, only_edges])Return a

`GeoSeries`

consisting of objects representing the computed Delaunay triangulation between the vertices of an input geometry.`describe`

([percentiles, include, exclude])Generate descriptive statistics.

`diff`

([periods])First discrete difference of Series elements.

`difference`

(other[, align])Return a

`GeoSeries`

of the points in each aligned geometry that are not in other.`disjoint`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry disjoint to other.`distance`

(other[, align])Return a

`Series`

containing the distance to aligned other.`div`

(other[, level, fill_value, axis])Return Floating division of series and other, element-wise (binary operator truediv).

`divide`

(other[, level, fill_value, axis])Return Floating division of series and other, element-wise (binary operator truediv).

`divmod`

(other[, level, fill_value, axis])Return Integer division and modulo of series and other, element-wise (binary operator divmod).

`dot`

(other)Compute the dot product between the Series and the columns of other.

`drop`

([labels, axis, index, columns, level, ...])Return Series with specified index labels removed.

`drop_duplicates`

(*[, keep, inplace, ignore_index])Return Series with duplicate values removed.

`droplevel`

(level[, axis])Return Series/DataFrame with requested index / column level(s) removed.

`dropna`

(*[, axis, inplace, how, ignore_index])Return a new Series with missing values removed.

`duplicated`

([keep])Indicate duplicate Series values.

`dwithin`

(other, distance[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that is within a set distance from`other`

.`eq`

(other[, level, fill_value, axis])Return Equal to of series and other, element-wise (binary operator eq).

`equals`

(other)Test whether two objects contain the same elements.

`estimate_utm_crs`

([datum_name])Return the estimated UTM CRS based on the bounds of the dataset.

`ewm`

([com, span, halflife, alpha, ...])Provide exponentially weighted (EW) calculations.

`expanding`

([min_periods, method])Provide expanding window calculations.

`explode`

([ignore_index, index_parts])Explode multi-part geometries into multiple single geometries.

`explore`

(*args, **kwargs)Explore with an interactive map based on folium/leaflet.js.Interactive map based on GeoPandas and folium/leaflet.js.

Return a

`GeoSeries`

of MultiPoints representing all distinct vertices of an input geometry.`factorize`

([sort, use_na_sentinel])Encode the object as an enumerated type or categorical variable.

`ffill`

(*[, axis, inplace, limit, limit_area])Fill NA/NaN values by propagating the last valid observation to next valid.

`fillna`

([value, inplace, limit])Fill NA values with geometry (or geometries).

`filter`

([items, like, regex, axis])Subset the DataFrame or Series according to the specified index labels.

`first_valid_index`

()Return index for first non-missing value or None, if no value is found.

`floordiv`

(other[, level, fill_value, axis])Return Integer division of series and other, element-wise (binary operator floordiv).

`force_2d`

()Force the dimensionality of a geometry to 2D.

`force_3d`

([z])Force the dimensionality of a geometry to 3D.

`frechet_distance`

(other[, align, densify])Return a

`Series`

containing the Frechet distance to aligned other.`from_arrow`

(arr, **kwargs)Construct a GeoSeries from an Arrow array object with a GeoArrow extension type.

`from_file`

(filename, **kwargs)Alternate constructor to create a

`GeoSeries`

from a file.`from_wkb`

(data[, index, crs, on_invalid])Alternate constructor to create a

`GeoSeries`

from a list or array of WKB objects.`from_wkt`

(data[, index, crs, on_invalid])Alternate constructor to create a

`GeoSeries`

from a list or array of WKT objects.`from_xy`

(x, y[, z, index, crs])Alternate constructor to create a

`GeoSeries`

of Point geometries from lists or arrays of x, y(, z) coordinates.`ge`

(other[, level, fill_value, axis])Return Greater than or equal to of series and other, element-wise (binary operator ge).

`geom_equals`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry equal to other.`geom_equals_exact`

(other, tolerance[, align])Return True for all geometries that equal aligned

*other*to a given tolerance, else False.`geom_equals_identical`

(other[, align])Return True for all geometries that are identical aligned

*other*, else False.`get`

(key[, default])Get item from object for given key (ex: DataFrame column).

`get_coordinates`

([include_z, ignore_index, ...])`get_geometry`

(index)Return the n-th geometry from a collection of geometries.

Return a

`Series`

of the precision of each geometry.`groupby`

([by, level, as_index, sort, ...])Group Series using a mapper or by a Series of columns.

`gt`

(other[, level, fill_value, axis])Return Greater than of series and other, element-wise (binary operator gt).

`hausdorff_distance`

(other[, align, densify])Return a

`Series`

containing the Hausdorff distance to aligned other.`head`

([n])Return the first n rows.

`hilbert_distance`

([total_bounds, level])Calculate the distance along a Hilbert curve.

`hist`

([by, ax, grid, xlabelsize, xrot, ...])Draw histogram of the input series using matplotlib.

`idxmax`

([axis, skipna])Return the row label of the maximum value.

`idxmin`

([axis, skipna])Return the row label of the minimum value.

`infer_objects`

([copy])Attempt to infer better dtypes for object columns.

`info`

([verbose, buf, max_cols, memory_usage, ...])Print a concise summary of a Series.

`interpolate`

(distance[, normalized])Return a point at the specified distance along each geometry.

`intersection`

(other[, align])Return a

`GeoSeries`

of the intersection of points in each aligned geometry with other.Return a geometry containing the intersection of all geometries in the

`GeoSeries`

.`intersects`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that intersects other.`invalid_coverage_edges`

(*[, gap_width])Return a

`GeoSeries`

containing edges causing invalid polygonal coverage.`is_valid_coverage`

(*[, gap_width])Return a

`bool`

indicating whether a`GeoSeries`

forms a valid coverage.Return a

`Series`

of strings with the reason for invalidity of each geometry.`isin`

(values)Whether elements in Series are contained in values.

`isna`

()Detect missing values.

`isnull`

()Alias for isna method.

`item`

()Return the first element of the underlying data as a Python scalar.

`items`

()Lazily iterate over (index, value) tuples.

`keys`

()Return alias for index.

`kurt`

(*[, axis, skipna, numeric_only])Return unbiased kurtosis over requested axis.

`kurtosis`

(*[, axis, skipna, numeric_only])Return unbiased kurtosis over requested axis.

`last_valid_index`

()Return index for last non-missing value or None, if no value is found.

`le`

(other[, level, fill_value, axis])Return Less than or equal to of series and other, element-wise (binary operator le).

`line_merge`

([directed])Return (Multi)LineStrings formed by combining the lines in a MultiLineString.

`lt`

(other[, level, fill_value, axis])Return Greater than of series and other, element-wise (binary operator lt).

`make_valid`

(*[, method, keep_collapsed])Repairs invalid geometries.

`map`

([func, na_action, engine])Map values of Series according to an input mapping or function.

`mask`

(cond[, other, inplace, axis, level])Replace values where the condition is True.

`max`

(*[, axis, skipna, numeric_only])Return the maximum of the values over the requested axis.

`maximum_inscribed_circle`

(*[, tolerance])Return a

`GeoSeries`

of geometries representing the largest circle that is fully contained within the input geometry.`mean`

(*[, axis, skipna, numeric_only])Return the mean of the values over the requested axis.

`median`

(*[, axis, skipna, numeric_only])Return the median of the values over the requested axis.

`memory_usage`

([index, deep])Return the memory usage of the Series.

`min`

(*[, axis, skipna, numeric_only])Return the minimum of the values over the requested axis.

Return a

`GeoSeries`

of geometries representing the minimum bounding circle that encloses each geometry.Return a Series of the radii of the minimum bounding circles that enclose each geometry.

Return a

`Series`

containing the minimum clearance distance, which is the smallest distance by which a vertex of the geometry could be moved to produce an invalid geometry.Return a

`GeoSeries`

of linestrings whose endpoints define the minimum clearance.Return a

`GeoSeries`

of the general minimum bounding rectangle that contains the object.`mod`

(other[, level, fill_value, axis])Return Modulo of series and other, element-wise (binary operator mod).

`mode`

([dropna])Return the mode(s) of the Series.

`mul`

(other[, level, fill_value, axis])Return Multiplication of series and other, element-wise (binary operator mul).

`multiply`

(other[, level, fill_value, axis])Return Multiplication of series and other, element-wise (binary operator mul).

`ne`

(other[, level, fill_value, axis])Return Not equal to of series and other, element-wise (binary operator ne).

`nlargest`

([n, keep])Return the largest n elements.

Return a

`GeoSeries`

of normalized geometries to normal form (or canonical form).`notna`

()Detect non-missing values.

`notnull`

()Alias for notna method.

`nsmallest`

([n, keep])Return the smallest n elements.

`nunique`

([dropna])Return number of unique elements in the object.

`offset_curve`

(distance[, quad_segs, ...])Return a

`LineString`

or`MultiLineString`

geometry at a distance from the object on its right or its left side.`orient_polygons`

(*[, exterior_cw])Return a

`GeoSeries`

of geometries with enforced ring orientation.`overlaps`

(other[, align])Return True for all aligned geometries that overlap

*other*, else False.`pct_change`

([periods, fill_method, freq])Fractional change between the current and a prior element.

`pipe`

(func, *args, **kwargs)Apply chainable functions that expect Series or DataFrames.

`plot`

(*args, **kwargs)Plot a GeoSeries.

`polygonize`

([node, full])Create polygons formed from the linework of a GeoSeries.

`pop`

(item)Return item and drops from series.

`pow`

(other[, level, fill_value, axis])Return Exponential power of series and other, element-wise (binary operator pow).

`prod`

(*[, axis, skipna, numeric_only, min_count])Return the product of the values over the requested axis.

`product`

(*[, axis, skipna, numeric_only, ...])Return the product of the values over the requested axis.

`project`

(other[, normalized, align])Return the distance along each geometry nearest to

*other*.`quantile`

([q, interpolation])Return value at the given quantile.

`radd`

(other[, level, fill_value, axis])Return Addition of series and other, element-wise (binary operator radd).

`rank`

([axis, method, numeric_only, ...])Compute numerical data ranks (1 through n) along axis.

`rdiv`

(other[, level, fill_value, axis])Return Floating division of series and other, element-wise (binary operator rtruediv).

`rdivmod`

(other[, level, fill_value, axis])Return Integer division and modulo of series and other, element-wise (binary operator rdivmod).

`reindex`

([index, axis, method, copy, level, ...])Conform Series to new index with optional filling logic.

`reindex_like`

(other[, method, copy, limit, ...])Return an object with matching indices as other object.

`relate`

(other[, align])Return the DE-9IM intersection matrices for the geometries.

`relate_pattern`

(other, pattern[, align])Return True if the DE-9IM string code for the relationship between the geometries satisfies the pattern, else False.

`remove_repeated_points`

([tolerance])Return a

`GeoSeries`

containing a copy of the input geometry with repeated points removed.`rename`

([index, axis, copy, inplace, level, ...])Alter Series index labels or name.

`rename_axis`

([mapper, index, axis, copy, inplace])Set the name of the axis for the index.

`reorder_levels`

(order)Rearrange index levels using input order.

`repeat`

(repeats[, axis])Repeat elements of a Series.

`replace`

([to_replace, value, inplace, regex])Replace values given in to_replace with value.

Return a

`GeoSeries`

of (cheaply computed) points that are guaranteed to be within each geometry.`resample`

(rule[, closed, label, convention, ...])Resample time-series data.

`reset_index`

([level, drop, name, inplace, ...])Generate a new DataFrame or Series with the index reset.

`reverse`

()Return a

`GeoSeries`

with the order of coordinates reversed.`rfloordiv`

(other[, level, fill_value, axis])Return Integer division of series and other, element-wise (binary operator rfloordiv).

`rmod`

(other[, level, fill_value, axis])Return Modulo of series and other, element-wise (binary operator rmod).

`rmul`

(other[, level, fill_value, axis])Return Multiplication of series and other, element-wise (binary operator rmul).

`rolling`

(window[, min_periods, center, ...])Provide rolling window calculations.

`rotate`

(angle[, origin, use_radians])Return a

`GeoSeries`

with rotated geometries.`round`

([decimals])Round each value in a Series to the given number of decimals.

`rpow`

(other[, level, fill_value, axis])Return Exponential power of series and other, element-wise (binary operator rpow).

`rsub`

(other[, level, fill_value, axis])Return Subtraction of series and other, element-wise (binary operator rsub).

`rtruediv`

(other[, level, fill_value, axis])Return Floating division of series and other, element-wise (binary operator rtruediv).

`sample`

([n, frac, replace, weights, ...])Return a random sample of items from an axis of object.

`sample_points`

(size[, method, seed, rng])Sample points from each geometry.

`scale`

([xfact, yfact, zfact, origin])Return a

`GeoSeries`

with scaled geometries.`searchsorted`

(value[, side, sorter])Find indices where elements should be inserted to maintain order.

`segmentize`

(max_segment_length)Return a

`GeoSeries`

with vertices added to line segments based on maximum segment length.`sem`

(*[, axis, skipna, ddof, numeric_only])Return unbiased standard error of the mean over requested axis.

`set_axis`

(labels, *[, axis, copy])Assign desired index to given axis.

`set_crs`

(**kwargs)`set_flags`

(*[, copy, allows_duplicate_labels])Return a new object with updated flags.

`set_precision`

(grid_size[, mode])Return a

`GeoSeries`

with the precision set to a precision grid size.`shared_paths`

(other[, align])Return the shared paths between two geometries.

`shift`

([periods, freq, axis, fill_value, suffix])Shift index by desired number of periods with an optional time freq.

`shortest_line`

(other[, align])Return the shortest two-point line between two geometries.

`simplify`

(tolerance[, preserve_topology])Return a

`GeoSeries`

containing a simplified representation of each geometry.`simplify_coverage`

(tolerance, *[, ...])Return a

`GeoSeries`

containing a simplified representation of polygonal coverage.`skew`

([xs, ys, origin, use_radians])Return a

`GeoSeries`

with skewed geometries.`snap`

(other, tolerance[, align])Snap the vertices and segments of the geometry to vertices of the reference.

`sort_index`

(*args, **kwargs)One-dimensional ndarray with axis labels (including time series).

`sort_values`

(*[, axis, ascending, inplace, ...])Sort by the values.

`squeeze`

([axis])Squeeze 1 dimensional axis objects into scalars.

`std`

(*[, axis, skipna, ddof, numeric_only])Return sample standard deviation.

`sub`

(other[, level, fill_value, axis])Return Subtraction of series and other, element-wise (binary operator sub).

`subtract`

(other[, level, fill_value, axis])Return Subtraction of series and other, element-wise (binary operator sub).

`sum`

(*[, axis, skipna, numeric_only, min_count])Return the sum of the values over the requested axis.

`swaplevel`

([i, j, copy])Swap levels i and j in a

`MultiIndex`

.`symmetric_difference`

(other[, align])Return a

`GeoSeries`

of the symmetric difference of points in each aligned geometry with other.`tail`

([n])Return the last n rows.

`take`

(*args, **kwargs)One-dimensional ndarray with axis labels (including time series).

`to_arrow`

([geometry_encoding, interleaved, ...])Encode a GeoSeries to GeoArrow format.

`to_clipboard`

(*[, excel, sep])Copy object to the system clipboard.

`to_crs`

([crs, epsg])Return a

`GeoSeries`

with all geometries transformed to a new coordinate reference system.`to_csv`

([path_or_buf, sep, na_rep, ...])Write object to a comma-separated values (csv) file.

`to_dict`

(*[, into])Convert Series to {label -> value} dict or dict-like object.

`to_excel`

(excel_writer, *[, sheet_name, ...])Write object to an Excel sheet.

`to_file`

(filename[, driver, index])Write the

`GeoSeries`

to a file.`to_frame`

([name])Convert Series to DataFrame.

`to_hdf`

(path_or_buf, *, key[, mode, ...])Write the contained data to an HDF5 file using HDFStore.

`to_json`

([show_bbox, drop_id, to_wgs84])Return a GeoJSON string representation of the GeoSeries.

`to_latex`

([buf, columns, header, index, ...])Render object to a LaTeX tabular, longtable, or nested table.

`to_list`

()Return a list of the values.

`to_markdown`

([buf, mode, index, storage_options])Print Series in Markdown-friendly format.

`to_numpy`

([dtype, copy, na_value])A NumPy ndarray representing the values in this Series or Index.

`to_period`

([freq, copy])Convert Series from DatetimeIndex to PeriodIndex.

`to_pickle`

(path, *[, compression, protocol, ...])Pickle (serialize) object to file.

`to_sql`

(name, con, *[, schema, if_exists, ...])Write records stored in a DataFrame to a SQL database.

`to_string`

([buf, na_rep, float_format, ...])Render a string representation of the Series.

`to_timestamp`

([freq, how, copy])Cast to DatetimeIndex of Timestamps, at

*beginning*of period.`to_wkb`

([hex])Convert GeoSeries geometries to WKB.

`to_wkt`

(**kwargs)Convert GeoSeries geometries to WKT.

`to_xarray`

()Return an xarray object from the pandas object.

`tolist`

()Return a list of the values.

`touches`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that touches other.`transform`

(transformation[, include_z])Return a

`GeoSeries`

with the transformation function applied to the geometry coordinates.`translate`

([xoff, yoff, zoff])Return a

`GeoSeries`

with translated geometries.`transpose`

(*args, **kwargs)Return the transpose, which is by definition self.

`truediv`

(other[, level, fill_value, axis])Return Floating division of series and other, element-wise (binary operator truediv).

`truncate`

([before, after, axis, copy])Truncate a Series or DataFrame before and after some index value.

`tz_convert`

(tz[, axis, level, copy])Convert tz-aware axis to target time zone.

`tz_localize`

(tz[, axis, level, copy, ...])Localize time zone naive index of a Series or DataFrame to target time zone.

`union`

(other[, align])Return a

`GeoSeries`

of the union of points in each aligned geometry with other.`union_all`

([method, grid_size])Return a geometry containing the union of all geometries in the

`GeoSeries`

.`unique`

()Return unique values of Series object.

`unstack`

([level, fill_value, sort])Unstack, also known as pivot, Series with MultiIndex to produce DataFrame.

`update`

(other)Modify Series in place using values from passed Series.

`value_counts`

([normalize, sort, ascending, ...])Return a Series containing counts of unique values.

`var`

(*[, axis, skipna, ddof, numeric_only])Return unbiased variance over requested axis.

`voronoi_polygons`

([tolerance, extend_to, ...])Return a

`GeoSeries`

consisting of objects representing the computed Voronoi diagram around the vertices of an input geometry.`where`

(cond[, other, inplace, axis, level])Replace values where the condition is False.

`within`

(other[, align])Return a

`Series`

of`dtype('bool')`

with value`True`

for each aligned geometry that is within other.`xs`

(key[, axis, level, drop_level])Return cross-section from the Series/DataFrame.

Attributes

`T`

Return the transpose, which is by definition self.

Return a

`Series`

containing the area of each geometry in the`GeoSeries`

expressed in the units of the CRS.`array`

The ExtensionArray of the data backing this Series or Index.

`at`

Access a single value for a row/column label pair.

`attrs`

Dictionary of global attributes of this dataset.

`axes`

Return a list of the row axis labels.

Return a

`GeoSeries`

of lower dimensional objects representing each geometry's set-theoretic boundary.Return a

`DataFrame`

with columns`minx`

,`miny`

,`maxx`

,`maxy`

values containing the bounds for each geometry.Return a

`GeoSeries`

of points representing the centroid of each geometry.Return a

`GeoSeries`

of geometries representing the convex hull of each geometry.The Coordinate Reference System (CRS) as a

`pyproj.CRS`

object.Coordinate based indexer to select by intersection with bounding box.

`dtype`

Return the dtype object of the underlying data.

`dtypes`

Return the dtype object of the underlying data.

`empty`

Indicator whether Index is empty.

Return a

`GeoSeries`

of geometries representing the envelope of each geometry.Return a

`GeoSeries`

of LinearRings representing the outer boundary of each polygon in the GeoSeries.`flags`

Get the properties associated with this pandas object.

Returns a

`Series`

of strings specifying the Geometry Type of each object.`geometry`

Return a

`Series`

of`dtype('bool')`

with value`True`

for features that have a m-component.Check the existence of the spatial index without generating it.

Return a

`Series`

of`dtype('bool')`

with value`True`

for features that have a z-component.`hasnans`

Return True if there are any NaNs.

`iat`

Access a single value for a row/column pair by integer position.

`iloc`

Purely integer-location based indexing for selection by position.

`index`

The index (axis labels) of the Series.

Return a

`Series`

of List representing the inner rings of each polygon in the GeoSeries.Return a

`Series`

of`dtype('bool')`

with value`True`

if a LineString or LinearRing is counterclockwise.Return a

`Series`

of`dtype('bool')`

with value`True`

if a LineString's or LinearRing's first and last points are equal.Returns a

`Series`

of`dtype('bool')`

with value`True`

for empty geometries.`is_monotonic_decreasing`

Return True if values in the object are monotonically decreasing.

`is_monotonic_increasing`

Return True if values in the object are monotonically increasing.

Return a

`Series`

of`dtype('bool')`

with value`True`

for features that are closed.Return a

`Series`

of`dtype('bool')`

with value`True`

for geometries that do not cross themselves.`is_unique`

Return True if values in the object are unique.

Return a

`Series`

of`dtype('bool')`

with value`True`

for geometries that are valid.Return a

`Series`

containing the length of each geometry expressed in the units of the CRS.`loc`

Access a group of rows and columns by label(s) or a boolean array.

Return the m coordinate of point geometries in a GeoSeries.

`name`

Return the name of the Series.

`nbytes`

Return the number of bytes in the underlying data.

`ndim`

Number of dimensions of the underlying data, by definition 1.

`shape`

Return a tuple of the shape of the underlying data.

Generate the spatial index.

`size`

Return the number of elements in the underlying data.

Return a tuple containing

`minx`

,`miny`

,`maxx`

,`maxy`

values for the bounds of the series as a whole.`type`

Return the geometry type of each geometry in the GeoSeries.

`unary_union`

Return a geometry containing the union of all geometries in the

`GeoSeries`

.`values`

Return Series as ndarray or ndarray-like depending on the dtype.

Return the x location of point geometries in a GeoSeries.

Return the y location of point geometries in a GeoSeries.

Return the z location of point geometries in a GeoSeries.

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.area.html

# geopandas.GeoSeries.area#

- property GeoSeries.area[source]#
Return a

`Series`

containing the area of each geometry in the`GeoSeries`

expressed in the units of the CRS.See also

`GeoSeries.length`

measure length

Notes

Area may be invalid for a geographic CRS using degrees as units; use

`GeoSeries.to_crs()`

to project geometries to a planar CRS before using this function.Every operation in GeoPandas is planar, i.e. the potential third dimension is not taken into account.

Examples

>>> from shapely.geometry import Polygon, LineString, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 1), (0, 1)]), ... Polygon([(10, 0), (10, 5), (0, 0)]), ... Polygon([(0, 0), (2, 2), (2, 0)]), ... LineString([(0, 0), (1, 1), (0, 1)]), ... Point(0, 1) ... ] ... ) >>> s 0 POLYGON ((0 0, 1 1, 0 1, 0 0)) 1 POLYGON ((10 0, 10 5, 0 0, 10 0)) 2 POLYGON ((0 0, 2 2, 2 0, 0 0)) 3 LINESTRING (0 0, 1 1, 0 1) 4 POINT (0 1) dtype: geometry

>>> s.area 0 0.5 1 25.0 2 2.0 3 0.0 4 0.0 dtype: float64

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.boundary.html

# geopandas.GeoSeries.boundary#

- property GeoSeries.boundary[source]#
Return a

`GeoSeries`

of lower dimensional objects representing each geometry’s set-theoretic boundary.See also

`GeoSeries.exterior`

outer boundary (without interior rings)

Examples

>>> from shapely.geometry import Polygon, LineString, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 1), (0, 1)]), ... LineString([(0, 0), (1, 1), (1, 0)]), ... Point(0, 0), ... ] ... ) >>> s 0 POLYGON ((0 0, 1 1, 0 1, 0 0)) 1 LINESTRING (0 0, 1 1, 1 0) 2 POINT (0 0) dtype: geometry

>>> s.boundary 0 LINESTRING (0 0, 1 1, 0 1, 0 0) 1 MULTIPOINT ((0 0), (1 0)) 2 GEOMETRYCOLLECTION EMPTY dtype: geometry

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.bounds.html

# geopandas.GeoSeries.bounds#

- property GeoSeries.bounds[source]#
Return a

`DataFrame`

with columns`minx`

,`miny`

,`maxx`

,`maxy`

values containing the bounds for each geometry.See

`GeoSeries.total_bounds`

for the limits of the entire series.Examples

>>> from shapely.geometry import Point, Polygon, LineString >>> d = {'geometry': [Point(2, 1), Polygon([(0, 0), (1, 1), (1, 0)]), ... LineString([(0, 1), (1, 2)])]} >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326") >>> gdf.bounds minx miny maxx maxy 0 2.0 1.0 2.0 1.0 1 0.0 0.0 1.0 1.0 2 0.0 1.0 1.0 2.0

You can assign the bounds to the

`GeoDataFrame`

as:>>> import pandas as pd >>> gdf = pd.concat([gdf, gdf.bounds], axis=1) >>> gdf geometry minx miny maxx maxy 0 POINT (2 1) 2.0 1.0 2.0 1.0 1 POLYGON ((0 0, 1 1, 1 0, 0 0)) 0.0 0.0 1.0 1.0 2 LINESTRING (0 1, 1 2) 0.0 1.0 1.0 2.0

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.total_bounds.html

# geopandas.GeoSeries.total_bounds#

- property GeoSeries.total_bounds[source]#
Return a tuple containing

`minx`

,`miny`

,`maxx`

,`maxy`

values for the bounds of the series as a whole.See

`GeoSeries.bounds`

for the bounds of the geometries contained in the series.Examples

>>> from shapely.geometry import Point, Polygon, LineString >>> d = {'geometry': [Point(3, -1), Polygon([(0, 0), (1, 1), (1, 0)]), ... LineString([(0, 1), (1, 2)])]} >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326") >>> gdf.total_bounds array([ 0., -1., 3., 2.])

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.length.html

# geopandas.GeoSeries.length#

- property GeoSeries.length[source]#
Return a

`Series`

containing the length of each geometry expressed in the units of the CRS.In the case of a (Multi)Polygon it measures the length of its exterior (i.e. perimeter).

See also

`GeoSeries.area`

measure area of a polygon

Notes

Length may be invalid for a geographic CRS using degrees as units; use

`GeoSeries.to_crs()`

to project geometries to a planar CRS before using this function.Every operation in GeoPandas is planar, i.e. the potential third dimension is not taken into account.

Examples

>>> from shapely.geometry import Polygon, LineString, MultiLineString, Point, GeometryCollection >>> s = geopandas.GeoSeries( ... [ ... LineString([(0, 0), (1, 1), (0, 1)]), ... LineString([(10, 0), (10, 5), (0, 0)]), ... MultiLineString([((0, 0), (1, 0)), ((-1, 0), (1, 0))]), ... Polygon([(0, 0), (1, 1), (0, 1)]), ... Point(0, 1), ... GeometryCollection([Point(1, 0), LineString([(10, 0), (10, 5), (0, 0)])]) ... ] ... ) >>> s 0 LINESTRING (0 0, 1 1, 0 1) 1 LINESTRING (10 0, 10 5, 0 0) 2 MULTILINESTRING ((0 0, 1 0), (-1 0, 1 0)) 3 POLYGON ((0 0, 1 1, 0 1, 0 0)) 4 POINT (0 1) 5 GEOMETRYCOLLECTION (POINT (1 0), LINESTRING (1... dtype: geometry

>>> s.length 0 2.414214 1 16.180340 2 3.000000 3 3.414214 4 0.000000 5 16.180340 dtype: float64

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.geom_type.html

# geopandas.GeoSeries.geom_type#

- property GeoSeries.geom_type[source]#
Returns a

`Series`

of strings specifying the Geometry Type of each object.Examples

>>> from shapely.geometry import Point, Polygon, LineString >>> d = {'geometry': [Point(2, 1), Polygon([(0, 0), (1, 1), (1, 0)]), ... LineString([(0, 0), (1, 1)])]} >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326") >>> gdf.geom_type 0 Point 1 Polygon 2 LineString dtype: object

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.offset_curve.html

# geopandas.GeoSeries.offset_curve#

-
GeoSeries.offset_curve(
*distance*,*quad_segs=8*,*join_style='round'*,*mitre_limit=5.0*)[source]# Return a

`LineString`

or`MultiLineString`

geometry at a distance from the object on its right or its left side.- Parameters:
**distance**float | array-likeSpecifies the offset distance from the input geometry. Negative for right side offset, positive for left side offset.

**quad_segs**int (optional, default 8)Specifies the number of linear segments in a quarter circle in the approximation of circular arcs.

**join_style**{‘round’, ‘bevel’, ‘mitre’}, (optional, default ‘round’)Specifies the shape of outside corners. ‘round’ results in rounded shapes. ‘bevel’ results in a beveled edge that touches the original vertex. ‘mitre’ results in a single vertex that is beveled depending on the

`mitre_limit`

parameter.**mitre_limit**float (optional, default 5.0)Crops of ‘mitre’-style joins if the point is displaced from the buffered vertex by more than this limit.

**See http://shapely.readthedocs.io/en/latest/manual.html#object.offset_curve****for details.**

Examples

>>> from shapely.geometry import LineString >>> s = geopandas.GeoSeries( ... [ ... LineString([(0, 0), (0, 1), (1, 1)]), ... ], ... crs=3857 ... ) >>> s 0 LINESTRING (0 0, 0 1, 1 1) dtype: geometry

>>> s.offset_curve(1) 0 LINESTRING (-1 0, -1 1, -0.981 1.195, -0.924 1... dtype: geometry

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.distance.html

# geopandas.GeoSeries.distance#

-
GeoSeries.distance(
*other*,*align=None*)[source]# Return a

`Series`

containing the distance to aligned other.The operation works on a 1-to-1 row-wise manner:

- Parameters:
**other**Geoseries or geometric objectThe Geoseries (elementwise) or geometric object to find the distance to.

**align**bool | None (default None)If True, automatically aligns GeoSeries based on their indices. If False, the order of elements is preserved. None defaults to True.

- Returns:
- Series (float)

Examples

>>> from shapely.geometry import Polygon, LineString, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 0), (1, 1)]), ... Polygon([(0, 0), (-1, 0), (-1, 1)]), ... LineString([(1, 1), (0, 0)]), ... Point(0, 0), ... ], ... ) >>> s2 = geopandas.GeoSeries( ... [ ... Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)]), ... Point(3, 1), ... LineString([(1, 0), (2, 0)]), ... Point(0, 1), ... ], ... index=range(1, 5), ... )

>>> s 0 POLYGON ((0 0, 1 0, 1 1, 0 0)) 1 POLYGON ((0 0, -1 0, -1 1, 0 0)) 2 LINESTRING (1 1, 0 0) 3 POINT (0 0) dtype: geometry

>>> s2 1 POLYGON ((0.5 0.5, 1.5 0.5, 1.5 1.5, 0.5 1.5, ... 2 POINT (3 1) 3 LINESTRING (1 0, 2 0) 4 POINT (0 1) dtype: geometry

We can check the distance of each geometry of GeoSeries to a single geometry:

>>> point = Point(-1, 0) >>> s.distance(point) 0 1.0 1 0.0 2 1.0 3 1.0 dtype: float64

We can also check two GeoSeries against each other, row by row. The GeoSeries above have different indices. We can either align both GeoSeries based on index values and use elements with the same index using

`align=True`

or ignore index and use elements based on their matching order using`align=False`

:>>> s.distance(s2, align=True) 0 NaN 1 0.707107 2 2.000000 3 1.000000 4 NaN dtype: float64

>>> s.distance(s2, align=False) 0 0.000000 1 3.162278 2 0.707107 3 1.000000 dtype: float64

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.hausdorff_distance.html

# geopandas.GeoSeries.hausdorff_distance#

-
GeoSeries.hausdorff_distance(
*other*,*align=None*,*densify=None*)[source]# Return a

`Series`

containing the Hausdorff distance to aligned other.The Hausdorff distance is the largest distance consisting of any point in self with the nearest point in other.

The operation works on a 1-to-1 row-wise manner:

- Parameters:
**other**GeoSeries or geometric objectThe Geoseries (elementwise) or geometric object to find the distance to.

**align**bool | None (default None)If True, automatically aligns GeoSeries based on their indices. If False, the order of elements is preserved. None defaults to True.

**densify**float (default None)A value between 0 and 1, that splits each subsegment of a line string into equal length segments, making the approximation less coarse. A densify value of 0.5 will add a point halfway between each pair of points. A densify value of 0.25 will add a point a quarter of the way between each pair of points.

- Returns:
- Series (float)

Examples

>>> from shapely.geometry import Polygon, LineString, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 0), (1, 1)]), ... Polygon([(0, 0), (-1, 0), (-1, 1)]), ... LineString([(1, 1), (0, 0)]), ... Point(0, 0), ... ], ... ) >>> s2 = geopandas.GeoSeries( ... [ ... Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)]), ... Point(3, 1), ... LineString([(1, 0), (2, 0)]), ... Point(0, 1), ... ], ... index=range(1, 5), ... )

>>> s 0 POLYGON ((0 0, 1 0, 1 1, 0 0)) 1 POLYGON ((0 0, -1 0, -1 1, 0 0)) 2 LINESTRING (1 1, 0 0) 3 POINT (0 0) dtype: geometry

>>> s2 1 POLYGON ((0.5 0.5, 1.5 0.5, 1.5 1.5, 0.5 1.5, ... 2 POINT (3 1) 3 LINESTRING (1 0, 2 0) 4 POINT (0 1) dtype: geometry

We can check the hausdorff distance of each geometry of GeoSeries to a single geometry:

>>> point = Point(-1, 0) >>> s.hausdorff_distance(point) 0 2.236068 1 1.000000 2 2.236068 3 1.000000 dtype: float64

We can also check two GeoSeries against each other, row by row. The GeoSeries above have different indices. We can either align both GeoSeries based on index values and use elements with the same index using

`align=True`

or ignore index and use elements based on their matching order using`align=False`

:>>> s.hausdorff_distance(s2, align=True) 0 NaN 1 2.121320 2 3.162278 3 2.000000 4 NaN dtype: float64

>>> s.hausdorff_distance(s2, align=False) 0 0.707107 1 4.123106 2 1.414214 3 1.000000 dtype: float64

We can also set a densify value, which is a float between 0 and 1 and signifies the fraction of the distance between each pair of points that will be used as the distance between the points when densifying.

>>> l1 = geopandas.GeoSeries([LineString([(130, 0), (0, 0), (0, 150)])]) >>> l2 = geopandas.GeoSeries([LineString([(10, 10), (10, 150), (130, 10)])]) >>> l1.hausdorff_distance(l2) 0 14.142136 dtype: float64 >>> l1.hausdorff_distance(l2, densify=0.25) 0 70.0 dtype: float64

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.frechet_distance.html

# geopandas.GeoSeries.frechet_distance#

-
GeoSeries.frechet_distance(
*other*,*align=None*,*densify=None*)[source]# Return a

`Series`

containing the Frechet distance to aligned other.The Fréchet distance is a measure of similarity: it is the greatest distance between any point in A and the closest point in B. The discrete distance is an approximation of this metric: only vertices are considered. The parameter

`densify`

makes this approximation less coarse by splitting the line segments between vertices before computing the distance.Fréchet distance sweep continuously along their respective curves and the direction of curves is significant. This makes it a better measure of similarity than Hausdorff distance for curve or surface matching.

The operation works on a 1-to-1 row-wise manner:

- Parameters:
**other**GeoSeries or geometric objectThe Geoseries (elementwise) or geometric object to find the distance to.

**align**bool | None (default None)If True, automatically aligns GeoSeries based on their indices. If False, the order of elements is preserved. None defaults to True.

**densify**float (default None)A value between 0 and 1, that splits each subsegment of a line string into equal length segments, making the approximation less coarse. A densify value of 0.5 will add a point halfway between each pair of points. A densify value of 0.25 will add a point every quarter of the way between each pair of points.

- Returns:
- Series (float)

Examples

>>> from shapely.geometry import Polygon, LineString, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 0), (1, 1)]), ... Polygon([(0, 0), (-1, 0), (-1, 1)]), ... LineString([(1, 1), (0, 0)]), ... Point(0, 0), ... ], ... ) >>> s2 = geopandas.GeoSeries( ... [ ... Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)]), ... Point(3, 1), ... LineString([(1, 0), (2, 0)]), ... Point(0, 1), ... ], ... index=range(1, 5), ... )

>>> s 0 POLYGON ((0 0, 1 0, 1 1, 0 0)) 1 POLYGON ((0 0, -1 0, -1 1, 0 0)) 2 LINESTRING (1 1, 0 0) 3 POINT (0 0) dtype: geometry

>>> s2 1 POLYGON ((0.5 0.5, 1.5 0.5, 1.5 1.5, 0.5 1.5, ... 2 POINT (3 1) 3 LINESTRING (1 0, 2 0) 4 POINT (0 1) dtype: geometry

We can check the frechet distance of each geometry of GeoSeries to a single geometry:

>>> point = Point(-1, 0) >>> s.frechet_distance(point) 0 2.236068 1 1.000000 2 2.236068 3 1.000000 dtype: float64

We can also check two GeoSeries against each other, row by row. The GeoSeries above have different indices. We can either align both GeoSeries based on index values and use elements with the same index using

`align=True`

or ignore index and use elements based on their matching order using`align=False`

:>>> s.frechet_distance(s2, align=True) 0 NaN 1 2.121320 2 3.162278 3 2.000000 4 NaN dtype: float64 >>> s.frechet_distance(s2, align=False) 0 0.707107 1 4.123106 2 2.000000 3 1.000000 dtype: float64

We can also set a

`densify`

value, which is a float between 0 and 1 and signifies the fraction of the distance between each pair of points that will be used as the distance between the points when densifying.>>> l1 = geopandas.GeoSeries([LineString([(0, 0), (10, 0), (0, 15)])]) >>> l2 = geopandas.GeoSeries([LineString([(0, 0), (20, 15), (9, 11)])]) >>> l1.frechet_distance(l2) 0 18.027756 dtype: float64 >>> l1.frechet_distance(l2, densify=0.25) 0 16.77051 dtype: float64

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.representative_point.html

# geopandas.GeoSeries.representative_point#

- GeoSeries.representative_point()[source]#
Return a

`GeoSeries`

of (cheaply computed) points that are guaranteed to be within each geometry.See also

`GeoSeries.centroid`

geometric centroid

Examples

>>> from shapely.geometry import Polygon, LineString, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 1), (0, 1)]), ... LineString([(0, 0), (1, 1), (1, 0)]), ... Point(0, 0), ... ] ... ) >>> s 0 POLYGON ((0 0, 1 1, 0 1, 0 0)) 1 LINESTRING (0 0, 1 1, 1 0) 2 POINT (0 0) dtype: geometry

>>> s.representative_point() 0 POINT (0.25 0.5) 1 POINT (1 1) 2 POINT (0 0) dtype: geometry

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.exterior.html

# geopandas.GeoSeries.exterior#

- property GeoSeries.exterior[source]#
Return a

`GeoSeries`

of LinearRings representing the outer boundary of each polygon in the GeoSeries.Applies to GeoSeries containing only Polygons. Returns

`None``

for other geometry types.See also

`GeoSeries.boundary`

complete set-theoretic boundary

`GeoSeries.interiors`

list of inner rings of each polygon

Examples

>>> from shapely.geometry import Polygon, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 1), (0, 1)]), ... Polygon([(1, 0), (2, 1), (0, 0)]), ... Point(0, 1) ... ] ... ) >>> s 0 POLYGON ((0 0, 1 1, 0 1, 0 0)) 1 POLYGON ((1 0, 2 1, 0 0, 1 0)) 2 POINT (0 1) dtype: geometry

>>> s.exterior 0 LINEARRING (0 0, 1 1, 0 1, 0 0) 1 LINEARRING (1 0, 2 1, 0 0, 1 0) 2 None dtype: geometry

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.interiors.html

# geopandas.GeoSeries.interiors#

- property GeoSeries.interiors[source]#
Return a

`Series`

of List representing the inner rings of each polygon in the GeoSeries.Applies to GeoSeries containing only Polygons.

- Returns:
- inner_rings: Series of List
Inner rings of each polygon in the GeoSeries.

See also

`GeoSeries.exterior`

outer boundary

Examples

>>> from shapely.geometry import Polygon >>> s = geopandas.GeoSeries( ... [ ... Polygon( ... [(0, 0), (0, 5), (5, 5), (5, 0)], ... [[(1, 1), (2, 1), (1, 2)], [(1, 4), (2, 4), (2, 3)]], ... ), ... Polygon([(1, 0), (2, 1), (0, 0)]), ... ] ... ) >>> s 0 POLYGON ((0 0, 0 5, 5 5, 5 0, 0 0), (1 1, 2 1,... 1 POLYGON ((1 0, 2 1, 0 0, 1 0)) dtype: geometry

>>> s.interiors 0 [LINEARRING (1 1, 2 1, 1 2, 1 1), LINEARRING (... 1 [] dtype: object

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.minimum_bounding_radius.html

# geopandas.GeoSeries.minimum_bounding_radius#

- GeoSeries.minimum_bounding_radius()[source]#
Return a Series of the radii of the minimum bounding circles that enclose each geometry.

See also

`GeoSeries.minumum_bounding_circle`

minimum bounding circle (geometry)

Examples

>>> from shapely.geometry import Point, LineString, Polygon >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 1), (0, 1), (0, 0)]), ... LineString([(0, 0), (1, 1), (1, 0)]), ... Point(0,0), ... ] ... ) >>> s 0 POLYGON ((0 0, 1 1, 0 1, 0 0)) 1 LINESTRING (0 0, 1 1, 1 0) 2 POINT (0 0) dtype: geometry

>>> s.minimum_bounding_radius() 0 0.707107 1 0.707107 2 0.000000 dtype: float64

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.minimum_clearance.html

# geopandas.GeoSeries.minimum_clearance#

- GeoSeries.minimum_clearance()[source]#
`Series`

containing the minimum clearance distance, which is the smallest distance by which a vertex of the geometry could be moved to produce an invalid geometry.If no minimum clearance exists for a geometry (for example, a single point, or an empty geometry), infinity is returned.

See also

Examples

>>> from shapely.geometry import Polygon, LineString, Point >>> s = geopandas.GeoSeries( ... [ ... Polygon([(0, 0), (1, 1), (0, 1), (0, 0)]), ... LineString([(0, 0), (1, 1), (3, 2)]), ... Point(0, 0), ... ] ... ) >>> s 0 POLYGON ((0 0, 1 1, 0 1, 0 0)) 1 LINESTRING (0 0, 1 1, 3 2) 2 POINT (0 0) dtype: geometry

>>> s.minimum_clearance() 0 0.707107 1 1.414214 2 inf dtype: float64

## Source: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.x.html

geopandas.GeoSeries.x# property GeoSeries.x[source]# Return the x location of point geometries in a GeoSeries. Returns: pandas.Series See also GeoSeries.y GeoSeries.z Examples >>> from shapely.geometry import Point >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)]) >>> s.x 0 1.0 1 2.0 2 3.0 dtype: float64
