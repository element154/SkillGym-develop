## Source: https://docs.astropy.org/en/stable/index.html

# astropy: A Community Python Library for Astronomy#

**Version**: 7.2.0 - What’s New in Astropy 7.2?

**Useful links**:
Installation |
Issues & Ideas |
Get Help |
Contribute |
About

The `astropy`

package contains key functionality and common tools needed for
performing astronomy and astrophysics with Python. It is at the core of the
Astropy Project, which aims to enable
the community to develop a robust ecosystem of affiliated packages
covering a broad range of needs for astronomical research, data
processing, and data analysis.

Important

If you use Astropy for work presented in a publication or talk please help the project via proper citation or acknowledgement. This also applies to use of software or affiliated packages that depend on the astropy core package.

New to Astropy? Check out the getting started guides. They contain an introduction to astropy’s main concepts and links to additional tutorials.

The user guide provides in-depth information on the key concepts of astropy with useful background information and explanation.

Learn how to use Python for astronomy through tutorials and guides that cover Astropy and other packages in the astronomy Python ecosystem.

The Astropy Project ecosystem includes numerous Coordinated and Affiliated packages. Coordinated packages are maintained by the Project.

Saw a typo in the documentation? Want to improve existing functionalities? The contributing guidelines will show you how to improve astropy.

What’s new in the latest release, changelog, and other project details.

## Source: https://docs.astropy.org/en/stable/wcs/index.html

# World Coordinate System (`astropy.wcs`

)#

## Introduction#

World Coordinate Systems (WCSs) describe the geometric transformations between one set of coordinates and another. A common application is to map the pixels in an image onto the celestial sphere. Another common application is to map pixels to wavelength in a spectrum.

`astropy.wcs`

contains utilities for managing World Coordinate System
(WCS) transformations defined in several elaborate FITS WCS standard conventions.
These transformations work both forward (from pixel to world) and backward
(from world to pixel).

For historical reasons and to support legacy software, `astropy.wcs`

maintains
two separate application interfaces. The `High-Level API`

should be used by
most applications. It abstracts out the underlying object and works transparently
with other packages which support the
Common Python Interface for WCS,
allowing for a more flexible approach to the problem and avoiding the limitations
of the FITS WCS standard.

The `Low Level API`

is the original `astropy.wcs`

API and originally developed as `pywcs`

.
It ties applications to the `astropy.wcs`

package and limits the transformations to the three distinct
types supported by it:

Core WCS, as defined in the FITS WCS standard, based on Mark Calabretta’s wcslib. (Also includes

`TPV`

and`TPD`

distortion, but not`SIP`

).Simple Imaging Polynomial (SIP) convention. (See note about SIP in headers.)

Table lookup distortions as defined in the FITS WCS distortion paper.

### Pixel Conventions and Definitions#

Both APIs assume that integer pixel values fall at the center of pixels (as assumed in the FITS WCS standard, see Section 2.1.4 of Greisen et al., 2002, A&A 446, 747).

However, there’s a difference in what is considered to be the first pixel. The
`High Level API`

follows the Python and C convention that the first pixel is
the 0-th one, i.e. the first pixel spans pixel values -0.5 to + 0.5. The
`Low Level API`

takes an additional `origin`

argument with values of 0 or 1
indicating whether the input arrays are 0- or 1-based.
The Low-level interface assumes Cartesian order (x, y) of the input coordinates,
however the Common Interface for World Coordinate System accepts both conventions.
The order of the pixel coordinates ((x, y) vs (row, column)) in the Common API
depends on the method or property used, and this can normally be determined from
the property or method name. Properties and methods containing “pixel” assume (x, y)
ordering, while properties and methods containing “array” assume (row, column) ordering.

## A Simple Example#

One example of the use of the high-level WCS API is to use the
`pixel_to_world`

to yield the simplest WCS
with default values, converting from pixel to world coordinates:

```
>>> from astropy.io import fits
>>> from astropy.wcs import WCS
>>> from astropy.utils.data import get_pkg_data_filename
>>> fn = get_pkg_data_filename('data/j94f05bgq_flt.fits', package='astropy.wcs.tests')
>>> f = fits.open(fn)
>>> w = WCS(f[1].header)
>>> sky = w.pixel_to_world(30, 40)
>>> print(sky)
<SkyCoord (ICRS): (ra, dec) in deg
(5.52844243, -72.05207809)>
>>> f.close()
```

Similarly, another use of the high-level API is to use the
`world_to_pixel`

to yield another simple WCS, while
converting from world to pixel coordinates:

```
>>> from astropy.io import fits
>>> from astropy.wcs import WCS
>>> from astropy.utils.data import get_pkg_data_filename
>>> fn = get_pkg_data_filename('data/j94f05bgq_flt.fits', package='astropy.wcs.tests')
>>> f = fits.open(fn)
>>> w = WCS(f[1].header)
>>> x, y = w.world_to_pixel(sky)
>>> print(x, y)
30.00000214673885 39.999999958235094
>>> f.close()
```

## Using `astropy.wcs`

#

## Examples creating a WCS programmatically#

## WCS Tools#

## Relax Constants#

## Other Information#

## Reference/API#

## See Also#

## Acknowledgments and Licenses#

wcslib is licenced under the GNU Lesser General Public License.

# Known Issues#

While most bugs and issues are managed using the astropy issue tracker, this document lists issues that are too difficult to fix, may require some intervention from the user to work around, or are caused by bugs in other projects or packages.

Issues listed on this page are grouped into two categories: The first is known
issues and shortcomings in actual algorithms and interfaces that currently do
not have fixes or workarounds, and that users should be aware of when writing
code that uses `astropy`

. Some of those issues are still platform-specific,
while others are very general. The second category is of common issues that come
up when configuring, building, or installing `astropy`

. This also includes
cases where the test suite can report false negatives depending on the context/
platform on which it was run.

## Known Deficiencies#

### Quantities Lose Their Units with Some Operations#

Quantities are subclassed from `numpy`

’s `ndarray`

and while we have
ensured that `numpy`

functions will work well with them, they do not always
work in functions from `scipy`

or other packages that use `numpy`

internally, but ignore the subclass. Furthermore, at a few places in `numpy`

itself we cannot control the behaviour. For instance, care must be taken when
setting array slices using Quantities:

```
>>> import astropy.units as u
>>> import numpy as np
>>> a = np.ones(4)
>>> a[2:3] = 2*u.kg
>>> a
array([1., 1., 2., 1.])
```

```
>>> a = np.ones(4)
>>> a[2:3] = 1*u.cm/u.m
>>> a
array([1., 1., 1., 1.])
```

Either set single array entries or use lists of Quantities:

```
>>> a = np.ones(4)
>>> a[2] = 1*u.cm/u.m
>>> a
array([1. , 1. , 0.01, 1. ])
```

```
>>> a = np.ones(4)
>>> a[2:3] = [1*u.cm/u.m]
>>> a
array([1. , 1. , 0.01, 1. ])
```

Both will throw an exception if units do not cancel, e.g.:

```
>>> a = np.ones(4)
>>> a[2] = 1*u.cm
Traceback (most recent call last):
...
TypeError: only dimensionless scalar quantities can be converted to Python scalars
```

See: astropy/astropy#7582

### Multiplying a `pandas.Series`

with an `Unit`

does not produce a `Quantity`

#

Quantities may work with certain operations on `Series`

but
this behaviour is not tested.
For example, multiplying a `Series`

instance
with a unit will *not* return a `Quantity`

. It will return a `Series`

object without any unit:

```
>>> import pandas as pd
>>> import astropy.units as u
>>> a = pd.Series([1., 2., 3.])
>>> a * u.m
0 1.0
1 2.0
2 3.0
dtype: float64
```

To avoid this, it is best to initialize the `Quantity`

directly:

```
>>> u.Quantity(a, u.m)
<Quantity [1., 2., 3.] m>
```

Note that the overrides pandas provides are not complete, and as a consequence, using the (in-place) shift operator does work:

```
>>> b = a << u.m
>>> b
<Quantity [1., 2., 3.] m>
>>> a <<= u.m
>>> a
<Quantity [1., 2., 3.] m>
```

But this is fragile as this may stop working in future versions of pandas if they decide to override the dunder methods.

### Using Numpy array creation functions to initialize Quantity#

Trying the following example will ignore the unit:

```
>>> np.full(10, 1 * u.m)
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
```

However, the following works as one would expect

```
>>> np.full(10, 1.0, like=u.Quantity([], u.m))
<Quantity [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.] m>
```

and is equivalent to:

```
>>> np.full(10, 1) << u.m
<Quantity [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.] m>
```

`zeros`

, `ones`

, and `empty`

behave similarly.

`arange`

also supports the `like`

keyword argument

```
>>> np.arange(0 * u.cm, 1 * u.cm, 1 * u.mm, like=u.Quantity([], u.cm))
<Quantity [0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] cm>
```

Also note that the unit of the output array is dictated by that of the `stop`

argument, and that, like for quantities generally, the data has a floating-point
dtype. If `stop`

is a pure number, the unit of the output will default to that
of the `like`

argument.

As with `~numpy.full`

and similar functions, one may alternatively move the
units outside of the call to `arange`

:

```
>>> np.arange(0, 10, 1) << u.mm
<Quantity [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.] mm>
```

Or use `linspace`

:

```
>>> np.linspace(0 * u.cm, 9 * u.mm, 10)
<Quantity [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.] mm>
```

### Quantities Lose Their Units When Broadcasted#

When broadcasting Quantities, it is necessary to pass `subok=True`

to
`broadcast_to`

, or else a bare `ndarray`

will be returned:

```
>>> q = u.Quantity(np.arange(10.), u.m)
>>> b = np.broadcast_to(q, (2, len(q)))
>>> b
array([[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.],
[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]])
>>> b2 = np.broadcast_to(q, (2, len(q)), subok=True)
>>> b2
<Quantity [[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.],
[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]] m>
```

This is analogous to the case of passing a Quantity to `array`

:

```
>>> a = np.array(q)
>>> a
array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
>>> a2 = np.array(q, subok=True)
>>> a2
<Quantity [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.] m>
```

See: astropy/astropy#7832

### Chained Quantity comparisons to dimensionless zero can be misleading#

When chaining comparisons using Quantities and dimensionless zero, the result may be misleading:

```
>>> 0 * u.Celsius == 0 * u.m # Correct
False
>>> 0 * u.Celsius == 0 == 0 * u.m # Misleading
np.True_
```

What the second comparison is really doing is this:

```
>>> (0 * u.Celsius == 0) and (0 == 0 * u.m)
np.True_
```

### numpy.prod cannot be applied to Quantity#

Using `numpy.prod`

function on a Quantity would result in error.
This is because correctly implementing it for Quantity is fairly
difficult, since, unlike for most numpy functions, the result unit
depends on the shape of the input (rather than only on the units
of the inputs).

```
>>> np.prod([1, 2, 3] * u.m)
Traceback (most recent call last):
...
astropy.units.errors.UnitsError: Cannot use 'reduce' method on ufunc multiply with a Quantity instance as it would change the unit.
```

### def_unit should not be used for logarithmic unit#

When defining custom unit involving logarithmic unit, `def_unit`

usage
should be avoided because it might result in surprising behavior:

```
>>> dBW = u.def_unit('dBW', u.dB(u.W))
>>> 1 * dBW
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for *: 'int' and 'Unit'
```

Instead, it could be defined directly as such:

```
>>> dBW = u.dB(u.W)
>>> 1 * dBW
<Decibel 1. dB(W)>
```

See: astropy/astropy#5945

### mmap Support for `astropy.io.fits`

on GNU Hurd#

On Hurd and possibly other platforms, `flush()`

on memory-mapped files are not
implemented, so writing changes to a mmap’d FITS file may not be reliable and is
thus disabled. Attempting to open a FITS file in writeable mode with mmap will
result in a warning (and mmap will be disabled on the file automatically).

See: astropy/astropy#968

### Color Printing on Windows#

Colored printing of log messages and other colored text does work in Windows, but only when running in the IPython console. Colors are not currently supported in the basic Python command-line interpreter on Windows.

`numpy.int64`

does not decompose input `Quantity`

objects#

Python’s `int()`

goes through `__index__`

while `numpy.int64`

or `numpy.int_`

do not go through `__index__`

. This
means that an upstream fix in NumPy is required in order for
`astropy.units`

to control decomposing the input in these functions:

```
>>> np.int64((15 * u.km) / (15 * u.imperial.foot))
np.int64(1)
>>> np.int_((15 * u.km) / (15 * u.imperial.foot))
np.int64(1)
>>> int((15 * u.km) / (15 * u.imperial.foot))
3280
```

To convert a dimensionless `Quantity`

to an integer, it is
therefore recommended to use `int(...)`

.

## Build/Installation/Test Issues#

### Anaconda Users Should Upgrade with `conda`

, Not `pip`

#

Upgrading `astropy`

in the Anaconda Python distribution using `pip`

can result
in a corrupted install with a mix of files from the old version and the new
version. Anaconda users should update with `conda update astropy`

. There
may be a brief delay between the release of `astropy`

on PyPI and its release
via the `conda`

package manager; users can check the availability of new
versions with `conda search astropy`

.

### Locale Errors in MacOS X and Linux#

On MacOS X, you may see the following error when running `pip`

:

```
...
ValueError: unknown locale: UTF-8
```

This is due to the `LC_CTYPE`

environment variable being incorrectly set to
`UTF-8`

by default, which is not a valid locale setting.

On MacOS X or Linux (or other platforms) you may also encounter the following error:

```
...
stderr = stderr.decode(stdio_encoding)
TypeError: decode() argument 1 must be str, not None
```

This also indicates that your locale is not set correctly.

To fix either of these issues, set this environment variable, as well as the
`LANG`

and `LC_ALL`

environment variables to e.g. `en_US.UTF-8`

using, in
the case of `bash`

:

```
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
```

To avoid any issues in future, you should add this line to your e.g.
`~/.bash_profile`

or `.bashrc`

file.

To test these changes, open a new terminal and type `locale`

, and you should
see something like:

```
$ locale
LANG="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_CTYPE="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
```

If so, you can go ahead and try running `pip`

again (in the new
terminal).

# Licenses#

## Astropy License#

Astropy is licensed under a 3-clause BSD style license:

Copyright (c) 2011-2024, Astropy Developers

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

Neither the name of the Astropy Team nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Other Licenses#

Full licenses for third-party software astropy is derived from or included
with Astropy can be found in the `'licenses/'`

directory of the source
code distribution.

# Known Issues#

While most bugs and issues are managed using the astropy issue tracker, this document lists issues that are too difficult to fix, may require some intervention from the user to work around, or are caused by bugs in other projects or packages.

Issues listed on this page are grouped into two categories: The first is known
issues and shortcomings in actual algorithms and interfaces that currently do
not have fixes or workarounds, and that users should be aware of when writing
code that uses `astropy`

. Some of those issues are still platform-specific,
while others are very general. The second category is of common issues that come
up when configuring, building, or installing `astropy`

. This also includes
cases where the test suite can report false negatives depending on the context/
platform on which it was run.

## Known Deficiencies#

### Quantities Lose Their Units with Some Operations#

Quantities are subclassed from `numpy`

’s `ndarray`

and while we have
ensured that `numpy`

functions will work well with them, they do not always
work in functions from `scipy`

or other packages that use `numpy`

internally, but ignore the subclass. Furthermore, at a few places in `numpy`

itself we cannot control the behaviour. For instance, care must be taken when
setting array slices using Quantities:

```
>>> import astropy.units as u
>>> import numpy as np
>>> a = np.ones(4)
>>> a[2:3] = 2*u.kg
>>> a
array([1., 1., 2., 1.])
```

```
>>> a = np.ones(4)
>>> a[2:3] = 1*u.cm/u.m
>>> a
array([1., 1., 1., 1.])
```

Either set single array entries or use lists of Quantities:

```
>>> a = np.ones(4)
>>> a[2] = 1*u.cm/u.m
>>> a
array([1. , 1. , 0.01, 1. ])
```

```
>>> a = np.ones(4)
>>> a[2:3] = [1*u.cm/u.m]
>>> a
array([1. , 1. , 0.01, 1. ])
```

Both will throw an exception if units do not cancel, e.g.:

```
>>> a = np.ones(4)
>>> a[2] = 1*u.cm
Traceback (most recent call last):
...
TypeError: only dimensionless scalar quantities can be converted to Python scalars
```

### Multiplying a `pandas.Series`

with an `Unit`

does not produce a `Quantity`

#

Quantities may work with certain operations on `Series`

but
this behaviour is not tested.
For example, multiplying a `Series`

instance
with a unit will *not* return a `Quantity`

. It will return a `Series`

object without any unit:

```
>>> import pandas as pd
>>> import astropy.units as u
>>> a = pd.Series([1., 2., 3.])
>>> a * u.m
0 1.0
1 2.0
2 3.0
dtype: float64
```

To avoid this, it is best to initialize the `Quantity`

directly:

```
>>> u.Quantity(a, u.m)
<Quantity [1., 2., 3.] m>
```

Note that the overrides pandas provides are not complete, and as a consequence, using the (in-place) shift operator does work:

```
>>> b = a << u.m
>>> b
<Quantity [1., 2., 3.] m>
>>> a <<= u.m
>>> a
<Quantity [1., 2., 3.] m>
```

But this is fragile as this may stop working in future versions of pandas if they decide to override the dunder methods.

### Using Numpy array creation functions to initialize Quantity#

Trying the following example will ignore the unit:

```
>>> np.full(10, 1 * u.m)
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
```

However, the following works as one would expect

```
>>> np.full(10, 1.0, like=u.Quantity([], u.m))
<Quantity [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.] m>
```

and is equivalent to:

```
>>> np.full(10, 1) << u.m
<Quantity [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.] m>
```

`zeros`

, `ones`

, and `empty`

behave similarly.

`arange`

also supports the `like`

keyword argument

```
>>> np.arange(0 * u.cm, 1 * u.cm, 1 * u.mm, like=u.Quantity([], u.cm))
<Quantity [0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] cm>
```

Also note that the unit of the output array is dictated by that of the `stop`

argument, and that, like for quantities generally, the data has a floating-point
dtype. If `stop`

is a pure number, the unit of the output will default to that
of the `like`

argument.

As with `~numpy.full`

and similar functions, one may alternatively move the
units outside of the call to `arange`

:

```
>>> np.arange(0, 10, 1) << u.mm
<Quantity [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.] mm>
```

Or use `linspace`

:

```
>>> np.linspace(0 * u.cm, 9 * u.mm, 10)
<Quantity [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.] mm>
```

### Quantities Lose Their Units When Broadcasted#

When broadcasting Quantities, it is necessary to pass `subok=True`

to
`broadcast_to`

, or else a bare `ndarray`

will be returned:

```
>>> q = u.Quantity(np.arange(10.), u.m)
>>> b = np.broadcast_to(q, (2, len(q)))
>>> b
array([[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.],
[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]])
>>> b2 = np.broadcast_to(q, (2, len(q)), subok=True)
>>> b2
<Quantity [[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.],
[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]] m>
```

This is analogous to the case of passing a Quantity to `array`

:

```
>>> a = np.array(q)
>>> a
array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
>>> a2 = np.array(q, subok=True)
>>> a2
<Quantity [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.] m>
```

### Chained Quantity comparisons to dimensionless zero can be misleading#

When chaining comparisons using Quantities and dimensionless zero, the result may be misleading:

```
>>> 0 * u.Celsius == 0 * u.m # Correct
False
>>> 0 * u.Celsius == 0 == 0 * u.m # Misleading
np.True_
```

What the second comparison is really doing is this:

```
>>> (0 * u.Celsius == 0) and (0 == 0 * u.m)
np.True_
```

### numpy.prod cannot be applied to Quantity#

Using `numpy.prod`

function on a Quantity would result in error.
This is because correctly implementing it for Quantity is fairly
difficult, since, unlike for most numpy functions, the result unit
depends on the shape of the input (rather than only on the units
of the inputs).

```
>>> np.prod([1, 2, 3] * u.m)
Traceback (most recent call last):
...
astropy.units.errors.UnitsError: Cannot use 'reduce' method on ufunc multiply with a Quantity instance as it would change the unit.
```

### def_unit should not be used for logarithmic unit#

When defining custom unit involving logarithmic unit, `def_unit`

usage
should be avoided because it might result in surprising behavior:

```
>>> dBW = u.def_unit('dBW', u.dB(u.W))
>>> 1 * dBW
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for *: 'int' and 'Unit'
```

Instead, it could be defined directly as such:

```
>>> dBW = u.dB(u.W)
>>> 1 * dBW
<Decibel 1. dB(W)>
```

### mmap Support for `astropy.io.fits`

on GNU Hurd#

On Hurd and possibly other platforms, `flush()`

on memory-mapped files are not
implemented, so writing changes to a mmap’d FITS file may not be reliable and is
thus disabled. Attempting to open a FITS file in writeable mode with mmap will
result in a warning (and mmap will be disabled on the file automatically).

### Color Printing on Windows#

Colored printing of log messages and other colored text does work in Windows, but only when running in the IPython console. Colors are not currently supported in the basic Python command-line interpreter on Windows.

`numpy.int64`

does not decompose input `Quantity`

objects#

Python’s `int()`

goes through `__index__`

while `numpy.int64`

or `numpy.int_`

do not go through `__index__`

. This
means that an upstream fix in NumPy is required in order for
`astropy.units`

to control decomposing the input in these functions:

```
>>> np.int64((15 * u.km) / (15 * u.imperial.foot))
np.int64(1)
>>> np.int_((15 * u.km) / (15 * u.imperial.foot))
np.int64(1)
>>> int((15 * u.km) / (15 * u.imperial.foot))
3280
```

To convert a dimensionless `Quantity`

to an integer, it is
therefore recommended to use `int(...)`

.

## Build/Installation/Test Issues#

### Anaconda Users Should Upgrade with `conda`

, Not `pip`

#

Upgrading `astropy`

in the Anaconda Python distribution using `pip`

can result
in a corrupted install with a mix of files from the old version and the new
version. Anaconda users should update with `conda update astropy`

. There
may be a brief delay between the release of `astropy`

on PyPI and its release
via the `conda`

package manager; users can check the availability of new
versions with `conda search astropy`

.

### Locale Errors in MacOS X and Linux#

On MacOS X, you may see the following error when running `pip`

:

```
...
ValueError: unknown locale: UTF-8
```

This is due to the `LC_CTYPE`

environment variable being incorrectly set to
`UTF-8`

by default, which is not a valid locale setting.

On MacOS X or Linux (or other platforms) you may also encounter the following error:

```
...
stderr = stderr.decode(stdio_encoding)
TypeError: decode() argument 1 must be str, not None
```

This also indicates that your locale is not set correctly.

To fix either of these issues, set this environment variable, as well as the
`LANG`

and `LC_ALL`

environment variables to e.g. `en_US.UTF-8`

using, in
the case of `bash`

:

```
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
```

To avoid any issues in future, you should add this line to your e.g.
`~/.bash_profile`

or `.bashrc`

file.

To test these changes, open a new terminal and type `locale`

, and you should
see something like:

```
$ locale
LANG="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_CTYPE="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
```

If so, you can go ahead and try running `pip`

again (in the new
terminal).

# Licenses#

## Astropy License#

Astropy is licensed under a 3-clause BSD style license:

Copyright (c) 2011-2024, Astropy Developers

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

Neither the name of the Astropy Team nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Other Licenses#

Full licenses for third-party software astropy is derived from or included
with Astropy can be found in the `'licenses/'`

directory of the source
code distribution.

## Source: https://docs.astropy.org/en/latest/index.html

# astropy: A Community Python Library for Astronomy#

**Version**: 8.0.0.dev591+g306868627 - What’s New in Astropy 8.0?

**Useful links**:
Installation |
Issues & Ideas |
Get Help |
Contribute |
About

The `astropy`

package contains key functionality and common tools needed for
performing astronomy and astrophysics with Python. It is at the core of the
Astropy Project, which aims to enable
the community to develop a robust ecosystem of affiliated packages
covering a broad range of needs for astronomical research, data
processing, and data analysis.

Important

If you use Astropy for work presented in a publication or talk please help the project via proper citation or acknowledgement. This also applies to use of software or affiliated packages that depend on the astropy core package.

New to Astropy? Check out the getting started guides. They contain an introduction to astropy’s main concepts and links to additional tutorials.

The user guide provides in-depth information on the key concepts of astropy with useful background information and explanation.

Learn how to use Python for astronomy through tutorials and guides that cover Astropy and other packages in the astronomy Python ecosystem.

The Astropy Project ecosystem includes numerous Coordinated and Affiliated packages. Coordinated packages are maintained by the Project.

Saw a typo in the documentation? Want to improve existing functionalities? The contributing guidelines will show you how to improve astropy.

What’s new in the latest release, changelog, and other project details.
