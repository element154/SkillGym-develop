## Source: https://docs.astropy.org/en/stable/utils/iers.html

# IERS data access (`astropy.utils.iers`

)#

## Introduction#

The `iers`

package provides access to the tables provided by the
International Earth Rotation and Reference Systems
(IERS) service, in particular the Earth Orientation data
allowing interpolation of published UT1-UTC and polar motion values for given
times. The UT1-UTC values are used in Time and Dates (astropy.time) to provide UT1 values, and
the polar motions are used in `astropy.coordinates`

to determine Earth
orientation for celestial-to-terrestrial coordinate transformations.

Note

The package also provides machinery to track leap seconds. Since it
generally should not be necessary to deal with those by hand, this
is not discussed below. For details, see the documentation of
`LeapSeconds`

.

There are two IERS data products that we discuss here:

**Bulletin A**(`IERS_A`

) is updated weekly and has historical data starting from 1973 and predictive data for 1 year into the future. It contains Earth orientation parameters x/y pole, UT1-UTC and their errors at daily intervals.**Bulletin B**(`IERS_B`

) is updated monthly and has data from 1962 up to the time when it is generated. This file contains Earth’s orientation in the IERS Reference System including Universal Time, coordinates of the terrestrial pole, and celestial pole offsets.

Since `astropy`

v6.0, both files are provided by the astropy-iers-data package, which is automatically
installed when `astropy`

itself is installed.

## Getting started#

By default, files are used from the astropy-iers-data package which is regularly updated.

In some cases, the latest IERS-A values (which include approximately one year of
predictive values) may be automatically downloaded from the IERS service as
required. This happens when a time or coordinate transformation needs a value
which is not already available via existing files in astropy-iers-data. In most
cases there is no need for invoking the `iers`

classes oneself,
but it is useful to understand the situations when a download will occur and how
this can be controlled.

### Basic usage#

By default, the IERS data are managed via instances of the
`IERS_Auto`

class. These instances are created
internally within the relevant time and coordinate objects during
transformations. If the bundled files or the astropy data cache are not recent
enough then astropy will request the file from the IERS service. Here is an
example that shows the typical download progress bar:

```
>>> from astropy.time import Time
>>> t = Time('2016:001')
>>> t.ut1
Downloading https://maia.usno.navy.mil/ser7/finals2000A.all
|==================================================================| 3.0M/3.0M (100.00%) 6s
<Time object: scale='ut1' format='yday' value=2016:001:00:00:00.082>
```

Note that you can forcibly clear the download cache as follows:

```
>>> from astropy.utils.data import clear_download_cache
>>> clear_download_cache()
```

The default IERS-A data used automatically is updated by the service every 7 days and includes transforms dating back to 1973-01-01.

Note

The `IERS_Auto`

class contains machinery
to ensure that the IERS table is kept up to date by auto-downloading the
latest version as needed. This means that the IERS table is assured of
having the state-of-the-art definitive and predictive values for Earth
rotation. As a user it is **your responsibility** to understand the
accuracy of IERS predictions if your science depends on that. If you
request `UT1-UTC`

or polar motions for times beyond the range of IERS
table data then the nearest available values will be provided.

### Configuration parameters#

There are a number of IERS configuration parameters in `astropy.utils.iers.Conf`

that relate to automatic IERS downloading. Four of the most
important to consider are the following:

- auto_download:
Enable auto-downloading of the latest IERS-A data. If set to

`False`

then the bundled IERS-A file will be used by default (even if a newer versions of the IERS-A file was already downloaded and cached). This parameter also controls whether internet resources will be queried to update the leap second table if the installed version is out of date.- auto_max_age:
Maximum age of predictive data before auto-downloading (days). See next section for details. (default=30)

- remote_timeout:
Remote timeout downloading IERS file data (seconds)

- iers_degraded_accuracy:
Some time conversions like UTC -> UT1 require IERS-A Earth rotation data for full accuracy. This parameter controls the behavior when computations use only the IERS-B data and full accuracy is not possible.

`'error'`

(the default) will raise an exception,`'warn'`

will issue a warning, and`'ignore'`

will ignore the problem (i.e., the inaccuracy is acceptable).

### Auto refresh behavior#

The first time that one attempts a time or coordinate transformation that requires IERS data, if the bundled versions of the files in astropy-iers-data are not recent enough, the latest version of the IERS table (from 1973 through one year into the future) will be downloaded and stored in the astropy cache.

Transformations will then use the cached data file if possible. However, the
`IERS_Auto`

table is automatically updated in place from the network if the
following two conditions a met when the table is queried for `UT1-UTC`

or
polar motion values:

Any of the requested IERS values are

*predictive*, meaning that they have been extrapolated into the future with a model that is fit to measured data. The IERS table contains approximately one year of predictive data from the time it is created.The first predictive values in the table are at least

`conf.auto_max_age days`

old relative to the current actual time (i.e.`Time.now()`

). This means that the IERS table is out of date and a newer version can be found on the IERS service.

The IERS Service provides the default online table
(set by `astropy.utils.iers.IERS_A_URL`

) and updates the content
once each 7 days. The default value of `auto_max_age`

is 30 days to avoid
unnecessary network access, but one can reduce this to as low as 10 days.

### Working offline#

If you are working without an internet connection and doing transformations that require IERS data, there are a couple of options.

**Ensure astropy-iers-data is up to date**

If you are planning to work without an internet connection, we recommend updating
the astropy-iers-data package to the latest available version, using e.g., `pip`

or `conda`

, as this will ensure that you have the most recent IERS and leap
second data.

**Disable auto downloading**

Here you can do:

```
>>> from astropy.utils import iers
>>> iers.conf.auto_download = False
```

In this case any transforms will use the bundled IERS data which are included in the astropy-iers-data package and include data up to the release date of that package (which is why it is important to ensure that package is up to date as described above). Any transforms outside of this range will not be allowed.

**Set the auto-download max age parameter**

*Only do this if you understand what you are doing, THIS CAN GIVE INACCURATE
ANSWERS!* Assuming you have previously been connected to the internet and have
downloaded and cached the IERS auto values previously, then do the following:

```
>>> iers.conf.auto_max_age = None
```

This disables the check of whether the IERS values are sufficiently recent, and all the transformations (even those outside the time range of available IERS data) will succeed with at most warnings.

**Allow degraded accuracy**

*Only do this if you understand what you are doing, THIS CAN GIVE INACCURATE
ANSWERS!*

Set `astropy.utils.iers.conf.iers_degraded_accuracy`

to either `'warn'`

or `'ignore'`

. These prevent the normal exception that occurs if a
time conversion falls outside the bounds of available local IERS-B data.

### Direct table access#

In most cases the automatic interface will suffice, but you may need to directly load and manipulate IERS tables. IERS-B values are provided as part of astropy and can be used to calculate time offsets and polar motion directly, or set up for internal use in further time and coordinate transformations. For example:

```
>>> from astropy.utils import iers
>>> t = Time('2010:001')
>>> iers_b = iers.IERS_B.open()
>>> iers_b.ut1_utc(t)
<Quantity 0.1141359 s>
>>> iers.earth_orientation_table.set(iers_b)
<ScienceState earth_orientation_table: <IERS_B length=...>...>
>>> t.ut1.iso
'2010-01-01 00:00:00.114'
```

Instead of local copies of IERS files, one can also download them, using
`iers.IERS_A_URL`

(or `iers.IERS_A_URL_MIRROR`

) and `iers.IERS_B_URL`

,
and then use those for future time and coordinate transformations (in this
example, just for a single calculation, by using
`earth_orientation_table`

as a context manager):

```
>>> iers_a = iers.IERS_A.open(iers.IERS_A_URL)
>>> with iers.earth_orientation_table.set(iers_a):
... print(t.ut1.iso)
2010-01-01 00:00:00.114
```

To reset to the default, pass in `None`

(which is equivalent to passing in
`iers.IERS_Auto.open()`

):

```
>>> iers.earth_orientation_table.set(None)
<ScienceState earth_orientation_table: <IERS...>...>
```

To see the internal IERS data that gets used in astropy you can do the following:

```
>>> dat = iers.earth_orientation_table.get()
>>> type(dat)
<class 'astropy.utils.iers.iers.IERS...'>
>>> dat
<IERS_Auto length=16196>
year month day MJD PolPMFlag_A ... UT1Flag PM_x PM_y PolPMFlag
d ... arcsec arcsec
int64 int64 int64 float64 str1 ... unicode1 float64 float64 unicode1
----- ----- ----- ------- ----------- ... -------- -------- -------- ---------
73 1 2 41684.0 I ... B 0.143 0.137 B
73 1 3 41685.0 I ... B 0.141 0.134 B
73 1 4 41686.0 I ... B 0.139 0.131 B
73 1 5 41687.0 I ... B 0.137 0.128 B
... ... ... ... ... ... ... ... ... ...
17 5 2 57875.0 P ... P 0.007211 0.44884 P
17 5 3 57876.0 P ... P 0.008757 0.450321 P
17 5 4 57877.0 P ... P 0.010328 0.451777 P
17 5 5 57878.0 P ... P 0.011924 0.453209 P
17 5 6 57879.0 P ... P 0.013544 0.454617 P
```

The explanation for most of the columns can be found in the file named
`iers.IERS_A_README`

. The important columns of this table are MJD, UT1_UTC,
UT1Flag, PM_x, PM_y, PolPMFlag:

```
>>> dat['MJD', 'UT1_UTC', 'UT1Flag', 'PM_x', 'PM_y', 'PolPMFlag']
<IERS_Auto length=16196>
MJD UT1_UTC UT1Flag PM_x PM_y PolPMFlag
d s arcsec arcsec
float64 float64 unicode1 float64 float64 unicode1
------- ---------- -------- -------- -------- ---------
41684.0 0.8075 B 0.143 0.137 B
41685.0 0.8044 B 0.141 0.134 B
41686.0 0.8012 B 0.139 0.131 B
41687.0 0.7981 B 0.137 0.128 B
... ... ... ... ... ...
57875.0 -0.6545408 P 0.007211 0.44884 P
57876.0 -0.6559528 P 0.008757 0.450321 P
57877.0 -0.6573705 P 0.010328 0.451777 P
57878.0 -0.6587712 P 0.011924 0.453209 P
57879.0 -0.660187 P 0.013544 0.454617 P
```

## Source: https://docs.astropy.org/en/stable/utils/masked/index.html

# Masked Values and Quantities (`astropy.utils.masked`

)#

Often, data sets are incomplete or corrupted and it would be handy to be able
to mask certain values. Astropy provides a `Masked`

class to help represent
such data sets.

Note

`Masked`

is similar to Numpy’s `MaskedArray`

,
but it supports subclasses much better and also has some important
differences in behaviour.

## Usage#

Astropy `Masked`

instances behave like `ndarray`

or subclasses such as
`Quantity`

but with a mask associated, which is propagated in operations such
as addition, etc.:

```
>>> import numpy as np
>>> from astropy import units as u
>>> from astropy.utils.masked import Masked
>>> ma = Masked([1., 2., 3.], mask=[False, False, True])
>>> ma
MaskedNDArray([1., 2., ——])
>>> mq = ma * u.m
>>> mq + 25 * u.cm
<MaskedQuantity [1.25, 2.25, ———] m>
```

You can get the values without the mask using
`unmasked`

, or, if you need to control what
should be substituted for any masked values, with
`filled()`

:

```
>>> mq.unmasked
<Quantity [1., 2., 3.] m>
>>> mq.filled(fill_value=-75*u.cm)
<Quantity [ 1. , 2. , -0.75] m>
```

You can mask or unmask individual elements by setting them to
`masked`

or `nomask`

:

```
>>> mq.mask
array([False, False, True])
>>> mq[:] = np.ma.nomask
>>> mq[2] = np.ma.masked
>>> mq.mask
array([False, False, True])
>>> mq
<MaskedQuantity [1., 2., ——] m>
```

These same procedures also work for higher-level classes like `Time`

and
`SkyCoord`

, which use `Masked`

under the hood.

For reductions such as sums, the mask propagates as if the sum was done directly:

```
>>> ma = Masked([[0., 1.], [2., 3.]], mask=[[False, True], [False, False]])
>>> ma.sum(axis=-1)
MaskedNDArray([——, 5.])
>>> ma.sum()
MaskedNDArray(——)
```

You might wonder why masked elements are propagated, instead of just being
skipped (as is done in `MaskedArray`

; see below). The rationale is that this leaves a
sum which is generally not useful unless one knows the number of masked
elements. In contrast, for sample properties such as the mean, for which the
number of elements are counted, it seems natural to simply omit the masked
elements from the calculation:

```
>> ma.mean(-1)
MaskedNDArray([0.0, 2.5])
```

Numpy functions work as expected on `Masked`

instances, with non-obvious
choices documented in `astropy.utils.masked.function_helpers`

(please report
numpy functions that do not work properly with `Masked`

values!). For example,
`nansum()`

does not propagate
masked elements, but instead replaces them with zero, and returns an unmasked
instance:

```
>> np.nansum(ma, axis=-1)
array([0., 5.])
```

## Differences from `MaskedArray`

#

`Masked`

differs from `MaskedArray`

in a number of ways, which we
detail below. Overall, it may be helpful to think of `Masked`

not as a
replacement of `MaskedArray`

, but just as a way of marking bad
elements, as one might do without needing a different class by setting them to
NaN (not-a-number). Like those NaN, the mask just propagates, except that for
some operations like taking the mean the equivalent of `nanmean`

is
used.

### Values under masked are operated on#

A difference in usage is that most operations act on the masked values, i.e., no effort is made to preserve values. For instance, compare:

```
>>> np_ma = np.ma.MaskedArray([1., 2., 3.], mask=[False, True, False])
>>> (np_ma + 1).data
array([2., 2., 4.])
>>> (Masked(np_ma) + 1).unmasked
array([2., 3., 4.])
```

The main reason for this decision is that for some masked subclasses, like
masked `Quantity`

, keeping the original value makes no sense (e.g., consider
dividing a length by a time: if the unit of a masked quantity is changing, why
should its value not change?). But it also helps to keep the implementation
considerably simpler, as the `Masked`

class now primarily has to deal with
propagating the mask rather than deciding what to do with values.

### Masked values are not skipped in reductions#

In reductions, the mask propagates as it would have if the operations were done on the individual elements:

```
>>> np_ma.prod()
np.float64(3.0)
>>> np_ma[0] * np_ma[1] * np_ma[2]
masked
>>> Masked(np_ma).prod()
MaskedNDArray(——)
```

The rationale for this becomes clear again by thinking about subclasses like a
masked `Quantity`

. For instance, consider an array `s`

of lengths with
shape `(N, 3)`

, in which the last axis represents width, height, and depth.
With this, you could compute corresponding volumes by taking the product of
the values in the last axis, `s.prod(axis=-1)`

. But if masked elements were
skipped, the physical dimension of entries in the result would depend how many
elements were masked, which is something `Quantity`

could not represent (and
would be rather surprising!). As noted above, however, masked elements are
skipped for operations for which this is well defined, such as for getting the
mean and other sample properties such as the variance and standard deviation.

### Setting the mask attribute replaces it#

If one sets the mask attribute of a `MaskedArray`

, it will
attempt to change the mask inplace:

```
>>> np_ma = np.ma.MaskedArray([1., 2., 3.], mask=[False, True, False])
>>> np_ma_mask_ref = np_ma.mask
>>> np_ma.mask = False
>>> np_ma_mask_ref
array([False, False, False])
```

In contrast, if one sets the mask on a `Masked`

class, it just sets it:

```
>>> ma = Masked([1., 2., 3.], mask=[False, True, False])
>>> ma_mask_ref = ma.mask
>>> ma.mask = False
>>> ma.mask
array([False, False, False])
>>> ma_mask_ref
array([False, True, False])
```

This has a consequence for setting the mask on a slice: for
`MaskedArray`

it propagates back, but for `Masked`

it does not:

```
>>> np_ma = np.ma.MaskedArray([1., 2., 3.], mask=[False, True, False])
>>> np_ma_view = np_ma[2:3]
>>> np_ma_view.mask = True
>>> np_ma_view
masked_array(data=[--],
mask=[ True],
fill_value=1e+20,
dtype=float64)
>>> np_ma
masked_array(data=[1.0, --, --],
mask=[False, True, True],
fill_value=1e+20)
>>> ma = Masked([1., 2., 3.], mask=[False, True, False])
>>> ma_view = ma[2:3]
>>> ma_view.mask = True
>>> ma_view
MaskedNDArray([——])
>>> ma
MaskedNDArray([1., ——, 3.])
```

In order for the mask to be set in-place, one should do it explicitly:

```
>>> ma[1:2].mask[...] = True
>>> ma.mask
array([False, True, False])
```

The reason for not attempting to propagate is partially just that assignment
should be just that, assignment. But also that it is tricky to get right.
Indeed, also for `MaskedArray`

it does not always work:

```
>>> np_ma[0].mask = True
Traceback (most recent call last):
...
AttributeError: 'numpy.float64' object has no attribute 'mask'...
```

### Numpy functions work as expected#

For `MaskedArray`

, a number of regular numpy functions do not work
properly, and instead one has to use variants from the `np.ma`

namespace.
For `Masked`

, numpy functions do work as expected (but those under the
`np.ma`

namespace typically do not).

### Masked subclasses behave like the subclass#

A more conceptual difference is that for `MaskedArray`

, the
instance that is created is a masked version of the unmasked instance, i.e.,
`MaskedArray`

remembers that is has wrapped a subclass like
`Quantity`

, but does not share any of its methods. Hence, even though the
resulting class looks reasonable at first glance, it does not work as expected:

```
>>> q = [1., 2.] * u.m
>>> np_mq = np.ma.MaskedArray(q, mask=[False, True])
>>> np_mq
masked_Quantity(data=[1.0, --],
mask=[False, True],
fill_value=1e+20)
>>> np_mq.unit
Traceback (most recent call last):
...
AttributeError: 'MaskedArray' object has no attribute 'unit'...
>>> np_mq / u.s
<Quantity [1., 2.] 1 / s>
```

In contrast, `Masked`

is always wrapped around the data proper, i.e., a
`MaskedQuantity`

is a quantity which has masked values, but with a unit that
is never masked. Indeed, one can see this from the class hierarchy:

```
>>> mq.__class__.__mro__
(<class 'astropy.utils.masked.core.MaskedQuantity'>,
<class 'astropy.units.quantity.Quantity'>,
<class 'astropy.utils.masked.core.MaskedNDArray'>,
<class 'astropy.utils.masked.core.Masked'>,
<class 'astropy.utils.shapes.NDArrayShapeMethods'>,
<class 'numpy.ndarray'>,
<class 'object'>)
```

This choice has made the implementation much simpler: `Masked`

only has to
worry about how to deal with masked values, while `Quantity`

can worry just
about unit propagation, etc. Indeed, an experiment showed that applying
`Masked`

to `Column`

(which is a subclass of `ndarray`

),
the result is a new `MaskedColumn`

that “just works”, with no need for the
overrides and special-casing that were needed to make `MaskedArray`

work with `Column`

. (Because the behaviour does change
somewhat, however, we chose not to replace the existing implementation.)

## Reference/API#

### astropy.utils.masked Package#

Built-in mask mixin class.

The design uses `Masked`

as a factory class which automatically
generates new subclasses for any data class that is itself a
subclass of a predefined masked class, with `MaskedNDArray`

providing such a predefined class for `ndarray`

.

#### Functions#

|
Combine masks, possibly storing it in some output. |
|
Split possibly masked array into unmasked and mask. |

#### Classes#

Like ShapedLikeNDArray, but for classes that can work with masked data. |
|
|
A scalar value or array of values with associated mask. |
|
Masked version of ndarray. |

#### Class Inheritance Diagram#

### astropy.utils.masked.function_helpers Module#

Helpers for letting numpy functions interact with Masked arrays.

The module supplies helper routines for numpy functions that propagate
masks appropriately, for use in the `__array_function__`

implementation of `MaskedNDArray`

. They are not
very useful on their own, but the ones with docstrings are included in
the documentation so that there is a place to find out how the mask is
interpreted.

#### Functions#

|
Count number of occurrences of each value in array of non-negative ints. |
|
Broadcast arrays to a common shape. |
|
Broadcast array to the given shape. |
|
Construct an array from an index array and a set of arrays to choose from. |
|
Copies values from one array to another, broadcasting as necessary. |
|
Counts the number of non-zero values in the array |
|
Return a full array with the same shape and type as a given array. |
|
Insert values along the given axis before the given indices. |
|
One-dimensional linear interpolation. |
|
Perform an indirect stable sort using a sequence of keys. |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Like |
|
Return an array of ones with the same shape and type as a given array. |
|
Evaluate a piecewise-defined function. |
|
Change elements of an array based on conditional and input values. |
|
Replaces specified elements of an array with given values. |
|
Return an array drawn from elements in choicelist, depending on conditions. |
|
Return an array of zeros with the same shape and type as a given array. |

## Source: https://docs.astropy.org/en/stable/utils/index.html

# Astropy Core Package Utilities (`astropy.utils`

)#

## Introduction#

The `astropy.utils`

package contains general-purpose utility functions and
classes. Examples include data structures, tools for downloading and caching
from URLs, and version intercompatibility functions.

This functionality is not astronomy-specific, but is intended primarily for use by Astropy developers. It is all safe for users to use, but the functions and classes are typically more complicated or specific to a particular need of Astropy.

Because of the mostly standalone and grab-bag nature of these utilities, they are generally best understood through their docstrings, and hence this documentation generally does not have detailed sections like the other packages. The exceptions are below:

IERS data access (astropy.utils.iers)

Masked Values and Quantities (astropy.utils.masked)

Note

The `astropy.utils.compat`

subpackage is not included in this
documentation. It contains utility modules for compatibility with
older/newer versions of python and numpy, as well as including some
bugfixes for the stdlib that are important for `astropy`

. It is recommended
that developers at least glance over the source code for this subpackage,
but most of it cannot be reliably included here because of the large
amount of version-specific code it contains. Its content is solely for
internal use of `astropy`

and subject to changes without deprecations.
Do not use it in external packages or code.
