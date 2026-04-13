## Source: https://docs.astropy.org/en/stable/units/index.html

# Units and Quantities (`astropy.units`

)#

## Introduction#

`astropy.units`

handles defining, converting between, and performing
arithmetic with physical quantities, such as meters, seconds, Hz,
etc. It also handles logarithmic units such as magnitude and decibel.

`astropy.units`

does not know spherical geometry or sexagesimal
(hours, min, sec): if you want to deal with celestial coordinates,
see the `astropy.coordinates`

package.

## Getting Started#

Most users of the `astropy.units`

package will work with Quantity objects: the combination of a value and a unit. The most convenient way to
create a `Quantity`

is to multiply or divide a value by one of the built-in
units. It works with scalars, sequences, and `numpy`

arrays.

### Examples#

To create a `Quantity`

object:

```
>>> from astropy import units as u
>>> 42.0 * u.meter
<Quantity 42. m>
>>> [1., 2., 3.] * u.m
<Quantity [1., 2., 3.] m>
>>> import numpy as np
>>> np.array([1., 2., 3.]) * u.m
<Quantity [1., 2., 3.] m>
```

You can get the unit and value from a `Quantity`

using the unit and
value members:

```
>>> q = 42.0 * u.meter
>>> q.value
np.float64(42.0)
>>> q.unit
Unit("m")
```

From this basic building block, it is possible to start combining quantities with different units:

```
>>> 15.1 * u.meter / (32.0 * u.second)
<Quantity 0.471875 m / s>
>>> 3.0 * u.kilometer / (130.51 * u.meter / u.second)
<Quantity 0.022986744310780783 km s / m>
>>> (3.0 * u.kilometer / (130.51 * u.meter / u.second)).decompose()
<Quantity 22.986744310780782 s>
```

Unit conversion is done using the
`to()`

method, which returns a new
`Quantity`

in the given unit:

```
>>> x = 1.0 * u.parsec
>>> x.to(u.km)
<Quantity 30856775814671.914 km>
```

It is also possible to work directly with units at a lower level, for example, to create custom units:

```
>>> from astropy.units import imperial
>>> cms = u.cm / u.s
>>> # ...and then use some imperial units
>>> mph = imperial.mile / u.hour
>>> # And do some conversions
>>> q = 42.0 * cms
>>> q.to(mph)
<Quantity 0.939513242662849 mi / h>
```

Units that “cancel out” become a special unit called the “dimensionless unit”:

```
>>> u.m / u.m
Unit(dimensionless)
```

To create a basic dimensionless quantity, multiply a value by the unscaled dimensionless unit:

```
>>> q = 1.0 * u.dimensionless_unscaled
>>> q.unit
Unit(dimensionless)
```

`astropy.units`

is able to match compound units against the units it already
knows about:

```
>>> (u.s ** -1).compose()
[Unit("Bq"), Unit("Hz"), Unit("2.7027e-11 Ci")]
```

And it can convert between unit systems, such as SI or CGS:

```
>>> (1.0 * u.Pa).cgs
<Quantity 10. Ba>
```

The units `mag`

, `dex`

, and `dB`

are special, being logarithmic
units, for which a value is the logarithm of a physical
quantity in a given unit. These can be used with a physical unit in
parentheses to create a corresponding logarithmic quantity:

```
>>> -2.5 * u.mag(u.ct / u.s)
<Magnitude -2.5 mag(ct / s)>
>>> from astropy import constants as c
>>> u.Dex((c.G * u.M_sun / u.R_sun**2).cgs)
<Dex 4.438067627303133 dex(cm / s2)>
```

`astropy.units`

also handles equivalencies, such as
that between wavelength and frequency. To use that feature, equivalence objects
are passed to the `to()`

conversion
method. For instance, a conversion from wavelength to frequency does not
normally work:

```
>>> (1000 * u.nm).to(u.Hz)
Traceback (most recent call last):
...
UnitConversionError: 'nm' (length) and 'Hz' (frequency) are not convertible
```

But by passing an equivalency list, in this case
`spectral()`

, it does:

```
>>> (1000 * u.nm).to(u.Hz, equivalencies=u.spectral())
<Quantity 2.99792458e+14 Hz>
```

Quantities and units can be printed nicely to strings using the Format String Syntax. Format
specifiers (like `0.03f`

) in strings will be used to format the quantity
value:

```
>>> q = 15.1 * u.meter / (32.0 * u.second)
>>> q
<Quantity 0.471875 m / s>
>>> f"{q:0.03f}"
'0.472 m / s'
```

The value and unit can also be formatted separately. Format specifiers for units can be used to choose the unit formatter:

```
>>> q = 15.1 * u.meter / (32.0 * u.second)
>>> q
<Quantity 0.471875 m / s>
>>> f"{q.value:0.03f} {q.unit:FITS}"
'0.472 m s-1'
```

## Using `astropy.units`

#

- Quantity
- Creating Quantity Instances
- Converting to Different Units
- Comparing Quantities
- Plotting Quantities
- Arithmetic
- NumPy Functions
- Dimensionless Quantities
- Converting to Plain Python Scalars
- Functions that Accept Quantities
- Representing Vectors with Units
- Creating and Converting Quantities without Copies
- The
`numpy.dtype`

of a Quantity - QTable
- Subclassing Quantity

- Unit-Aware Type Annotations
- Type Annotations Module
- Standard Units
- Combining and Defining Units
- Decomposing and Composing Units
- Magnitudes and Other Logarithmic Units
- Structured Units
- String Representations of Units and Quantities
- Equivalencies
- Physical Types
- Using Prior Versions of Constants
- Low-Level Unit Conversion

## Acknowledgments#

This code was originally based on the pynbody units module written by Andrew Pontzen, who has granted the Astropy Project permission to use the code under a BSD license.

## See Also#

FITS Standard for units in FITS.

The Units in the VO 1.0 Standard for representing units in the VO.

OGIP Units: A standard for storing units in OGIP FITS files.

## Performance Tips#

If you are attaching units to arrays to make `Quantity`

objects, multiplying
arrays by units will result in the array being copied in memory, which will slow
things down. Furthermore, if you are multiplying an array by a composite unit,
the array will be copied for each individual multiplication. Thus, in the
following case, the array is copied four successive times:

```
In [1]: import numpy as np
In [2]: from astropy import units as u
In [3]: rng = np.random.default_rng()
In [4]: array = rng.random(10000000)
In [5]: %timeit array * u.m / u.s / u.kg / u.sr
92.5 ms ± 2.52 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

There are several ways to speed this up. First, when you are using composite units, ensure that the entire unit gets evaluated first, then attached to the array. You can do this by using parentheses as for any other operation:

```
In [6]: %timeit array * (u.m / u.s / u.kg / u.sr)
21.5 ms ± 886 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

In this case, this has sped things up by a factor of 4. If you use a composite unit several times in your code then you can define a variable for it:

```
In [7]: UNIT_MSKGSR = u.m / u.s / u.kg / u.sr
In [8]: %timeit array * UNIT_MSKGSR
22.2 ms ± 551 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

In this case and the case with brackets, the array is still copied once when
creating the `Quantity`

. If you want to avoid any copies altogether, you can
make use of the `<<`

operator to attach the unit to the array:

```
In [9]: %timeit array << u.m / u.s / u.kg / u.sr
47.1 µs ± 5.77 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

Note that these are now **microseconds**, so this is 2000x faster than the
original case with no brackets. Note that brackets are not needed when using
`<<`

since `*`

and `/`

have a higher precedence, so the unit will be
evaluated first. When using `<<`

, be aware that because the data is not being
copied, changing the original array will also change the `Quantity`

object.

Note that for composite units, you will definitely see an impact if you can pre-compute the composite unit:

```
In [10]: %timeit array << UNIT_MSKGSR
6.51 µs ± 112 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

Which is over 10000x faster than the original example. See
Creating and Converting Quantities without Copies for more details about the `<<`

operator.

## Reference/API#

- Reference/API
- astropy.units Package
- astropy.units.si Module
- astropy.units.cgs Module
- astropy.units.astrophys Module
- astropy.units.misc Module
- astropy.units.function.units Module
- astropy.units.photometric Module
- astropy.units.imperial Module
- astropy.units.cds Module
- astropy.units.physical Module
- astropy.units.format Package
- astropy.units.required_by_vounit Module

## Source: https://docs.astropy.org/en/stable/units/quantity.html

# Quantity#

The `Quantity`

object is meant to represent a value that has some unit
associated with the number.

## Creating Quantity Instances#

`Quantity`

objects are normally created through multiplication with
`Unit`

objects.

### Examples#

To create a `Quantity`

to represent 15 m/s:

```
>>> import astropy.units as u
>>> 15 * u.m / u.s
<Quantity 15. m / s>
```

This extends as expected to division by a unit, or using `numpy`

arrays or
Python sequences:

```
>>> 1.25 / u.s
<Quantity 1.25 1 / s>
>>> [1, 2, 3] * u.m
<Quantity [1., 2., 3.] m>
>>> import numpy as np
>>> np.array([1, 2, 3]) * u.m
<Quantity [1., 2., 3.] m>
```

You can also create instances using the `Quantity`

constructor directly, by
specifying a value and unit:

```
>>> u.Quantity(15, u.m / u.s)
<Quantity 15. m / s>
```

The constructor gives a few more options. In particular, it allows you to
merge sequences of `Quantity`

objects (as long as all of their units are
equivalent), and to parse simple strings (which may help, for example, to parse
configuration files, etc.):

```
>>> qlst = [60 * u.s, 1 * u.min]
>>> u.Quantity(qlst, u.minute)
<Quantity [1., 1.] min>
>>> u.Quantity('15 m/s')
<Quantity 15. m / s>
```

The current unit and value can be accessed via the
`unit`

and
`value`

attributes:

```
>>> q = 2.5 * u.m / u.s
>>> q.unit
Unit("m / s")
>>> q.value
np.float64(2.5)
```

Note

`Quantity`

objects are converted to float by default. Furthermore, any
data passed in are copied, which for large arrays may not be optimal.
As discussed further below,
you can instead obtain a view by passing
`copy=False`

to `Quantity`

or by using the `<<`

operator.

## Converting to Different Units#

`Quantity`

objects can be converted to different units using the
`to()`

method.

### Examples#

To convert `Quantity`

objects to different units:

```
>>> q = 2.3 * u.m / u.s
>>> q.to(u.km / u.h)
<Quantity 8.28 km / h>
```

For convenience, the `si`

and
`cgs`

attributes can be used to convert
the `Quantity`

to base SI or CGS units:

```
>>> q = 2.4 * u.m / u.s
>>> q.si
<Quantity 2.4 m / s>
>>> q.cgs
<Quantity 240. cm / s>
```

If you want the value of the quantity in a different unit, you can use
`to_value()`

as a shortcut:

```
>>> q = 2.5 * u.m
>>> q.to_value(u.cm)
np.float64(250.0)
```

Note

You could get the value in `cm`

also by using `q.to(u.cm).value`

.
The difference is that `to_value()`

does
no copying if the unit is already the correct one, instead
returning a view of the data
(just as if you had done `q.value`

). In contrast,
`to()`

always returns a copy (which also
means it is slower for the case where no conversion is necessary).
As discussed further below,
you can avoid the copying by using the `<<`

operator.

## Comparing Quantities#

The equality of `Quantity`

objects is best tested using the
`allclose()`

and `isclose()`

functions,
which are unit-aware analogues of the `numpy`

functions with the same name:

```
>>> u.allclose([1, 2] * u.m, [100, 200] * u.cm)
True
>>> u.isclose([1, 2] * u.m, [100, 20] * u.cm)
array([ True, False])
```

The use of Python comparison operators is also supported:

```
>>> 1*u.m < 50*u.cm
np.False_
```

## Plotting Quantities#

`Quantity`

objects can be conveniently plotted using Matplotlib — see
Plotting quantities for more details.

## Arithmetic#

### Addition and Subtraction#

Addition or subtraction between `Quantity`

objects is supported when their
units are equivalent.

#### Examples#

When the units are equal, the resulting object has the same unit:

```
>>> 11 * u.s + 30 * u.s
<Quantity 41. s>
>>> 30 * u.s - 11 * u.s
<Quantity 19. s>
```

If the units are equivalent, but not equal (e.g., kilometer and meter), the
resulting object **has units of the object on the left**:

```
>>> 1100.1 * u.m + 13.5 * u.km
<Quantity 14600.1 m>
>>> 13.5 * u.km + 1100.1 * u.m
<Quantity 14.6001 km>
>>> 1100.1 * u.m - 13.5 * u.km
<Quantity -12399.9 m>
>>> 13.5 * u.km - 1100.1 * u.m
<Quantity 12.3999 km>
```

Addition and subtraction are not supported between `Quantity`

objects and basic
numeric types, except for dimensionless quantities (see Dimensionless
Quantities) or special values like zero and infinity:

```
>>> 13.5 * u.km + 19.412
Traceback (most recent call last):
...
UnitConversionError: Can only apply 'add' function to dimensionless
quantities when other argument is not a quantity (unless the
latter is all zero/infinity/nan)
```

### Multiplication and Division#

Multiplication and division are supported between `Quantity`

objects with any
units, and with numeric types. For these operations between objects with
equivalent units, the **resulting object has composite units**.

#### Examples#

To perform these operations on `Quantity`

objects:

```
>>> 1.1 * u.m * 140.3 * u.cm
<Quantity 154.33 cm m>
>>> 140.3 * u.cm * 1.1 * u.m
<Quantity 154.33 cm m>
>>> 1. * u.m / (20. * u.cm)
<Quantity 0.05 m / cm>
>>> 20. * u.cm / (1. * u.m)
<Quantity 20. cm / m>
```

For multiplication, you can change how to represent the resulting object by
using the `to()`

method:

```
>>> (1.1 * u.m * 140.3 * u.cm).to(u.m**2)
<Quantity 1.5433 m2>
>>> (1.1 * u.m * 140.3 * u.cm).to(u.cm**2)
<Quantity 15433. cm2>
```

For division, if the units are equivalent, you may want to make the resulting
object dimensionless by reducing the units. To do this, use the
`decompose()`

method:

```
>>> (20. * u.cm / (1. * u.m)).decompose()
<Quantity 0.2>
```

This method is also useful for more complicated arithmetic:

```
>>> 15. * u.kg * 32. * u.cm * 15 * u.m / (11. * u.s * 1914.15 * u.ms)
<Quantity 0.34195097 cm kg m / (ms s)>
>>> (15. * u.kg * 32. * u.cm * 15 * u.m / (11. * u.s * 1914.15 * u.ms)).decompose()
<Quantity 3.41950973 m2 kg / s2>
```

## NumPy Functions#

`Quantity`

objects are actually full `numpy`

arrays (the `Quantity`

class
inherits from and extends `numpy.ndarray`

), and we have tried to ensure
that `numpy`

functions behave properly with quantities:

```
>>> q = np.array([1., 2., 3., 4.]) * u.m / u.s
>>> np.mean(q)
<Quantity 2.5 m / s>
>>> np.std(q)
<Quantity 1.11803399 m / s>
```

This includes functions that only accept specific units such as angles:

```
>>> q = 30. * u.deg
>>> np.sin(q)
<Quantity 0.5>
```

```
>>> from astropy.constants import h, k_B
>>> nu = 3 * u.GHz
>>> T = 30 * u.K
>>> np.exp(-h * nu / (k_B * T))
<Quantity 0.99521225>
```

Note

Support for functions from other packages, such as SciPy, is more incomplete (contributions to improve this are welcomed!).

## Dimensionless Quantities#

Dimensionless quantities have the characteristic that if they are
added to or subtracted from a Python scalar or unitless `ndarray`

,
or if they are passed to a `numpy`

function that takes dimensionless
quantities, the units are simplified so that the quantity is
dimensionless and scale-free. For example:

```
>>> 1. + 1. * u.m / u.km
<Quantity 1.001>
```

Which is different from:

```
>>> 1. + (1. * u.m / u.km).value
np.float64(2.0)
```

In the latter case, the result is `2.0`

because the unit of ```
(1. * u.m /
u.km)
```

is not scale-free by default:

```
>>> q = (1. * u.m / u.km)
>>> q.unit
Unit("m / km")
>>> q.unit.decompose()
Unit(dimensionless with a scale of 0.001)
```

However, when combining with an object that is not a `Quantity`

, the unit is
automatically decomposed to be scale-free, giving the expected result.

This also occurs when passing dimensionless quantities to functions that take dimensionless quantities:

```
>>> nu = 3 * u.GHz
>>> T = 30 * u.K
>>> np.exp(- h * nu / (k_B * T))
<Quantity 0.99521225>
```

The result is independent from the units in which the different quantities were specified:

```
>>> nu = 3.e9 * u.Hz
>>> T = 30 * u.K
>>> np.exp(- h * nu / (k_B * T))
<Quantity 0.99521225>
```

## Converting to Plain Python Scalars#

Converting `Quantity`

objects does not work for non-dimensionless quantities:

```
>>> float(3. * u.m)
Traceback (most recent call last):
...
TypeError: only dimensionless scalar quantities can be converted
to Python scalars
```

Only dimensionless values can be converted to plain Python scalars:

```
>>> float(3. * u.m / (4. * u.m))
0.75
>>> float(3. * u.km / (4. * u.m))
750.0
>>> int(6. * u.km / (2. * u.m))
3000
```

## Functions that Accept Quantities#

If a function accepts a `Quantity`

as an argument then it can be a good idea to
check that the provided `Quantity`

belongs to one of the expected
Physical Types. This can be done with the decorator
`quantity_input()`

.

The decorator does not convert the input `Quantity`

to the desired unit, say
arcseconds to degrees in the example below, it merely checks that such a
conversion is possible, thus verifying that the `Quantity`

argument can be used in calculations.

Keyword arguments to `quantity_input()`

specify which
arguments should be validated and what unit they are expected to be compatible
with.

### Examples#

To verify if a `Quantity`

argument can be used in calculations:

```
>>> @u.quantity_input(myarg=u.deg)
... def myfunction(myarg):
... return myarg.unit
>>> myfunction(100*u.arcsec)
Unit("arcsec")
>>> myfunction(2*u.m)
Traceback (most recent call last):
...
UnitsError: Argument 'myarg' to function 'myfunction' must be in units
convertible to 'deg'.
```

It is also possible to instead specify the physical type of the desired unit:

```
>>> @u.quantity_input(myarg='angle')
... def myfunction(myarg):
... return myarg.unit
>>> myfunction(100*u.arcsec)
Unit("arcsec")
```

Optionally, `None`

keyword arguments are also supported; for such cases, the
input is only checked when a value other than `None`

is passed:

```
>>> @u.quantity_input(a='length', b='angle')
... def myfunction(a, b=None):
... return a, b
>>> myfunction(1.*u.km)
(<Quantity 1. km>, None)
>>> myfunction(1.*u.km, 1*u.deg)
(<Quantity 1. km>, <Quantity 1. deg>)
```

Alternatively, you can use the annotations syntax to provide the units. While the raw unit or string can be used, the preferred method is with the unit-aware Quantity-annotation syntax.

`Quantity[unit or "string", metadata, ...]`

```
>>> @u.quantity_input
... def myfunction(myarg: u.Quantity[u.arcsec]):
... return myarg.unit
>>>
>>> myfunction(100*u.arcsec)
Unit("arcsec")
```

You can also annotate for different types in non-unit expecting arguments:

```
>>> @u.quantity_input
... def myfunction(myarg: u.Quantity[u.arcsec], nice_string: str):
... return myarg.unit, nice_string
>>> myfunction(100*u.arcsec, "a nice string")
(Unit("arcsec"), 'a nice string')
```

The output can be specified to have a desired unit with a function annotation, for example

```
>>> @u.quantity_input
... def myfunction(myarg: u.Quantity[u.arcsec]) -> u.deg:
... return myarg*1000
>>>
>>> myfunction(100*u.arcsec)
<Quantity 27.77777778 deg>
```

This both checks that the return value of your function is consistent with what you expect and makes it much neater to display the results of the function.

Specifying a list of valid equivalent units or Physical Types is supported for functions that should accept inputs with multiple valid units:

```
>>> @u.quantity_input(a=['length', 'speed'])
... def myfunction(a):
... return a.unit
```

```
>>> myfunction(1.*u.km)
Unit("km")
>>> myfunction(1.*u.km/u.s)
Unit("km / s")
```

## Representing Vectors with Units#

`Quantity`

objects can, like `numpy`

arrays, be used to represent vectors or
matrices by assigning specific dimensions to represent the coordinates or
matrix elements, but that implies tracking those dimensions carefully. For
vectors Using and Designing Coordinate Representations can be more convenient as
doing so allows you to use representations other than Cartesian (such as
spherical or cylindrical), as well as simple vector arithmetic.

## Creating and Converting Quantities without Copies#

When creating a `Quantity`

using multiplication with a unit, a copy of the
underlying data is made. This can be avoided by passing on `copy=False`

in
the initializer.

### Examples#

To avoid duplication using `copy=False`

:

```
>>> a = np.arange(5.)
>>> q = u.Quantity(a, u.m, copy=False)
>>> q
<Quantity [0., 1., 2., 3., 4.] m>
>>> np.may_share_memory(a, q)
True
>>> a[0] = -1.
>>> q
<Quantity [-1., 1., 2., 3., 4.] m>
```

This may be particularly useful in functions which do not change their input
while ensuring that if a user passes in a `Quantity`

then it will be converted
to the desired unit.

As a shortcut, you can “shift” to the requested unit using the `<<`

operator:

```
>>> q = a << u.m
>>> np.may_share_memory(a, q)
True
>>> q
<Quantity [-1., 1., 2., 3., 4.] m>
```

The operator works identically to the initialization with `copy=False`

mentioned above:

```
>>> q << u.cm
<Quantity [-100., 100., 200., 300., 400.] cm>
```

It can also be used for in-place conversion:

```
>>> q <<= u.cm
>>> q
<Quantity [-100., 100., 200., 300., 400.] cm>
>>> a
array([-100., 100., 200., 300., 400.])
```

## The `numpy.dtype`

of a Quantity#

`Quantity`

subclasses `numpy.ndarray`

and similarly accepts a `dtype`

argument.

```
>>> q = u.Quantity(1.0, dtype=np.float32)
>>> q.dtype
dtype('float32')
```

Like for `numpy.ndarray`

, `dtype`

does not have to be specified, in which case
the data is inspected to find the best `dtype`

. For `numpy`

this means
integers remain integers, while `Quantity`

instead upcasts integers to floats.

```
>>> v = np.array(1)
>>> np.issubdtype(v.dtype, np.integer)
True
```

```
>>> q = u.Quantity(1)
>>> np.issubdtype(q.dtype, np.integer)
False
```

`Quantity`

promotes integer to floating types because it has a different default
value for `dtype`

than `numpy`

– `numpy.inexact`

versus `None`

. For `Quantity`

to use the same `dtype`

inspection as `numpy`

, use `dtype=None`

.

```
>>> q = u.Quantity(1, dtype=None)
>>> np.issubdtype(q.dtype, np.integer)
True
```

Note that `numpy.inexact`

is a deprecated `dtype`

argument for
`numpy.ndarray`

. `Quantity`

changes `numpy.inexact`

to `numpy.float64`

, but does
not change data that are already floating point or complex.

## QTable#

It is possible to use `Quantity`

objects as columns in `astropy.table`

.
See Quantity and QTable for more details.

## Subclassing Quantity#

To subclass `Quantity`

, you generally proceed as you would when subclassing
`numpy.ndarray`

(i.e., you typically need to override `__new__()`

, rather than
`__init__()`

, and use the `numpy.ndarray.__array_finalize__()`

method to
update attributes). For details, see the NumPy documentation on subclassing. To get a sense
of what is involved, have a look at `Quantity`

itself, where, for example, the
`astropy.units.Quantity.__array_finalize__()`

method is used to pass on the
`unit`

, at `Angle`

, where strings are parsed as
angles in the `astropy.coordinates.Angle.__new__()`

method and at
`Longitude`

, where the
`astropy.coordinates.Longitude.__array_finalize__()`

method is used to pass
on the angle at which longitudes wrap.

Another method that is meant to be overridden by subclasses, specific to
`Quantity`

, is `astropy.units.Quantity.__quantity_subclass__()`

. This is
called to decide which type of subclass to return, based on the unit of the
`Quantity`

that is to be created. It is used, for example, in
`Angle`

to return a `Quantity`

if a calculation
returns a unit other than an angular one. The implementation of this is via
`SpecificTypeQuantity`

, which more generally allows users
to construct `Quantity`

subclasses that have methods that are useful only for a
specific physical type.

## Source: https://docs.astropy.org/en/stable/units/type_hints.html

# Unit-Aware Type Annotations#

Python supports static type analysis using the type syntax of PEP 484. For a detailed guide on type hints, function annotations, and other related syntax see the Real Python Guide. Below we describe how you can be use Quantity type hints and annotations and also include metadata about the associated units.

We assume the following imports:

```
>>> import typing as T
>>> import astropy.units as u
>>> from astropy.units import Quantity
```

## Quantity Type Annotation#

A `Quantity`

can be used as a type annotation,:

```
>>> x: Quantity = 2 * u.km
```

or as a function annotation.:

```
>>> def func(x: Quantity) -> Quantity:
... return x
```

### Preserving Units#

While the above annotations are useful for annotating the value’s type, it
does not inform us of the other most important attribute of a `Quantity`

:
the unit.

Unit information may be included by the syntax
`Quantity[unit or "physical_type", shape, numpy.dtype]`

.:

```
>>> Quantity[u.m]
typing.Annotated[astropy.units.quantity.Quantity, Unit("m")]
>>>
>>> Quantity["length"]
typing.Annotated[astropy.units.quantity.Quantity, PhysicalType('length')]
```

See `typing.Annotated`

for explanation of `Annotated`

These can also be used on functions

```
>>> def func(x: Quantity[u.kpc]) -> Quantity[u.m]:
... return x << u.m
```

## Multiple Annotations#

Multiple Quantity and unit-aware `Quantity`

annotations are supported using
`Union`

or `Optional`

(including `|`

operations).

```
>>> Quantity[u.m] | None
typing.Optional[typing.Annotated[astropy.units.quantity.Quantity, Unit("m")]]
>>>
>>> Quantity[u.m] | Quantity["time"]
typing.Union[typing.Annotated[astropy.units.quantity.Quantity, Unit("m")],
typing.Annotated[astropy.units.quantity.Quantity, PhysicalType('time')]]
```

# Type Annotations Module#

Typing module for supporting type annotations related to `units`

.

- astropy.units.typing.QuantityLike#
Type alias for a quantity-like object.

This is an object that can be converted to a

`Quantity`

object using the`Quantity()`

constructor.Examples

We assume the following imports:

>>> from astropy import units as u

This is a non-exhaustive list of examples of quantity-like objects:

Integers and floats:

>>> u.Quantity(1, u.meter) <Quantity 1.0 m>

>>> u.Quantity(1.0, u.meter) <Quantity 1.0 m>

Lists and tuples:

>>> u.Quantity([1.0, 2.0], u.meter) <Quantity [1., 2.] m>

>>> u.Quantity((1.0, 2.0), u.meter) <Quantity [1., 2.] m>

Numpy arrays:

>>> u.Quantity(np.array([1.0, 2.0]), u.meter)

`Quantity`

objects:>>> u.Quantity(u.Quantity(1.0, u.meter)) <Quantity 1.0 m>

Strings:

>>> u.Quantity('1.0 m') <Quantity 1.0 m>

For more examples see the

`numpy.typing`

definition of`numpy.typing.ArrayLike`

.alias of

`astropy.units.Quantity`

|`Buffer`

|`_SupportsArray`

[`dtype`

[`Any`

]] |`_NestedSequence`

[`_SupportsArray`

[`dtype`

[`Any`

]]] |`complex`

|`bytes`

|`str`

|`_NestedSequence`

[`complex`

|`bytes`

|`str`

]

- astropy.units.typing.UnitLike#
Type alias for input that can be converted to a Unit.

See unit-like. Note that this includes only scalar quantities.

alias of

`astropy.units.UnitBase`

|`str`

|`astropy.units.Quantity`

-
astropy.units.typing.UnitPower
*= int | float | fractions.Fraction*# Alias for types that can be powers of the components of a

`UnitBase`

instance

-
astropy.units.typing.UnitPowerLike
*= int | float | fractions.Fraction | numpy.integer | numpy.floating*# Alias for types that can be used to create powers of the components of a

`UnitBase`

instance

-
astropy.units.typing.UnitScale
*= float | complex*# Alias for types that can be scale factors of a

`CompositeUnit`

-
astropy.units.typing.UnitScaleLike
*= float | complex | int | fractions.Fraction | numpy.number*# Alias for types that can be used to create scale factors of a

`CompositeUnit`

## Source: https://docs.astropy.org/en/stable/units/standard_units.html

# Standard Units#

Standard units are defined in the `astropy.units`

package as object
instances.

All units are defined in terms of basic “irreducible” units. The irreducible units include:

Length (meter)

Time (second)

Mass (kilogram)

Current (ampere)

Temperature (Kelvin)

Angular distance (radian)

Solid angle (steradian)

Luminous intensity (candela)

Stellar magnitude (mag)

Amount of substance (mole)

Photon count (photon)

(There are also some more obscure base units required by the FITS Standard that are no longer recommended for use.)

Units that involve combinations of fundamental units are instances of
`CompositeUnit`

. In most cases, you do not need
to worry about the various kinds of unit classes unless you want to
design a more complex case.

There are many units already predefined in the module. You may use the
`find_equivalent_units()`

method to list
all of the existing predefined units of a given type:

```
>>> from astropy import units as u
>>> u.g.find_equivalent_units()
Primary name | Unit definition | Aliases
[
M_e | 9.10938e-31 kg | ,
M_p | 1.67262e-27 kg | ,
earthMass | 5.97217e+24 kg | M_earth, Mearth ,
g | 0.001 kg | gram ,
jupiterMass | 1.89812e+27 kg | M_jup, Mjup, M_jupiter, Mjupiter ,
kg | irreducible | kilogram ,
solMass | 1.98841e+30 kg | M_sun, Msun ,
t | 1000 kg | tonne ,
u | 1.66054e-27 kg | Da, Dalton ,
]
```

## Prefixes#

Most units can be used with prefixes, with both the standard SI prefixes
and the IEEE 1541-2021 binary prefixes
(for `bit`

and `byte`

) supported:

Available decimal prefixes |
||
|---|---|---|
Symbol |
Prefix |
Value |
Q |
quetta- |
1e30 |
R |
ronna- |
1e27 |
Y |
yotta- |
1e24 |
Z |
zetta- |
1e21 |
E |
exa- |
1e18 |
P |
peta- |
1e15 |
T |
tera- |
1e12 |
G |
giga- |
1e9 |
M |
mega- |
1e6 |
k |
kilo- |
1e3 |
h |
hecto- |
1e2 |
da |
deka-, deca |
1e1 |
d |
deci- |
1e-1 |
c |
centi- |
1e-2 |
m |
milli- |
1e-3 |
u |
micro- |
1e-6 |
n |
nano- |
1e-9 |
p |
pico- |
1e-12 |
f |
femto- |
1e-15 |
a |
atto- |
1e-18 |
z |
zepto- |
1e-21 |
y |
yocto- |
1e-24 |
r |
ronto- |
1e-27 |
q |
quecto- |
1e-30 |

Available binary prefixes |
||
|---|---|---|
Symbol |
Prefix |
Value |
Ki |
kibi- |
2 ** 10 |
Mi |
mebi- |
2 ** 20 |
Gi |
gibi- |
2 ** 30 |
Ti |
tebi- |
2 ** 40 |
Pi |
pebi- |
2 ** 50 |
Ei |
exbi- |
2 ** 60 |
Zi |
zebi- |
2 ** 70 |
Yi |
yobi- |
2 ** 80 |

## The Dimensionless Unit#

In addition to these units, `astropy.units`

includes the concept of
the dimensionless unit, used to indicate quantities that do not have a
physical dimension. This is distinct in concept from a unit that is
equal to `None`

: that indicates that no unit was specified in the data
or by the user.

For convenience, there is a unit that is both dimensionless and
unscaled: the `dimensionless_unscaled`

object:

```
>>> u.dimensionless_unscaled
Unit(dimensionless)
```

Dimensionless quantities are often defined as products or ratios of quantities that are not dimensionless, but whose dimensions cancel out when their powers are multiplied.

### Examples#

To use the `dimensionless_unscaled`

object:

```
>>> u.m / u.m
Unit(dimensionless)
```

For compatibility with the String Representations of Units and Quantities, this is
equivalent to `Unit('')`

and `Unit(1)`

, though using
`u.dimensionless_unscaled`

in Python code is preferred for
readability:

```
>>> u.dimensionless_unscaled == u.Unit('')
True
>>> u.dimensionless_unscaled == u.Unit(1)
True
```

Note that in many cases, a dimensionless unit may also have a scale. For example:

```
>>> (u.km / u.m).decompose()
Unit(dimensionless with a scale of 1000.0)
>>> (u.km / u.m).decompose() == u.dimensionless_unscaled
False
```

As an example of why you might want to create a scaled dimensionless
quantity, say you will be doing many calculations with some big
unit-less number, `big_unitless_num = 20000000 # 20 million`

,
but you want all of your answers to be in multiples of a million. This
can be done by dividing `big_unitless_num`

by `1e6`

, but this
requires you to remember that this scaling factor has been applied,
which may be difficult to do after many calculations. Instead, create
a scaled dimensionless quantity by multiplying a value by `Unit(scale)`

to keep track of the scaling factor. For example:

```
>>> scale = 1e6
>>> big_unitless_num = 20 * u.Unit(scale) # 20 million
>>> some_measurement = 5.0 * u.cm
>>> some_measurement * big_unitless_num
<Quantity 100. 1e+06 cm>
```

To determine if a unit is dimensionless (but regardless of the scale),
use the `physical_type`

property:

```
>>> (u.km / u.m).physical_type
PhysicalType('dimensionless')
>>> # This also has a scale, so it is not the same as u.dimensionless_unscaled
>>> (u.km / u.m) == u.dimensionless_unscaled
False
>>> # However, (u.m / u.m) has a scale of 1.0, so it is the same
>>> (u.m / u.m) == u.dimensionless_unscaled
True
```

## Enabling Other Units#

By default, only the “default” units are searched by
`find_equivalent_units()`

and similar methods
that do searching. This includes SI, CGS, and
astrophysical units. However, you may wish to enable the Imperial or other user-defined units.

### Example#

To enable Imperial units, do:

```
>>> from astropy.units import imperial
>>> imperial.enable()
<astropy.units.core._UnitContext object at ...>
>>> u.m.find_equivalent_units()
Primary name | Unit definition | Aliases
[
AU | 1.49598e+11 m | au, astronomical_unit ,
Angstrom | 1e-10 m | AA, angstrom, Å ,
cm | 0.01 m | centimeter ,
earthRad | 6.3781e+06 m | R_earth, Rearth ,
ft | 0.3048 m | foot ,
fur | 201.168 m | furlong ,
inch | 0.0254 m | ,
jupiterRad | 7.1492e+07 m | R_jup, Rjup, R_jupiter, Rjupiter ,
lsec | 2.99792e+08 m | lightsecond ,
lyr | 9.46073e+15 m | lightyear ,
m | irreducible | meter ,
mi | 1609.34 m | mile ,
micron | 1e-06 m | ,
mil | 2.54e-05 m | thou ,
nmi | 1852 m | nauticalmile, NM ,
pc | 3.08568e+16 m | parsec ,
solRad | 6.957e+08 m | R_sun, Rsun ,
yd | 0.9144 m | yard ,
]
```

This may also be used with the Python “with” statement, to temporarily enable additional units:

```
>>> with imperial.enable():
... print(u.m.find_equivalent_units())
Primary name | Unit definition | Aliases
...
```

To enable only specific units, use `add_enabled_units()`

:

```
>>> with u.add_enabled_units([imperial.knot]):
... print(u.m.find_equivalent_units())
Primary name | Unit definition | Aliases
...
```

## Source: https://docs.astropy.org/en/stable/units/combining_and_defining.html

# Combining and Defining Units#

## Basic example#

Units and quantities can be combined together using the regular Python numeric operators:

```
>>> from astropy import units as u
>>> fluxunit = u.erg / (u.cm ** 2 * u.s)
>>> fluxunit
Unit("erg / (s cm2)")
>>> 52.0 * fluxunit
<Quantity 52. erg / (s cm2)>
>>> 52.0 * fluxunit / u.s
<Quantity 52. erg / (cm2 s2)>
```

## Fractional powers#

Units support fractional powers, which retain their precision through
complex operations. To do this, it is recommended to use
`fractions.Fraction`

objects:

```
>>> from fractions import Fraction
>>> Franklin = u.g ** Fraction(1, 2) * u.cm ** Fraction(3, 2) * u.s ** -1
```

Note

Floating-point powers that are effectively the same as fractions
with a denominator less than 10 are implicitly converted to
`Fraction`

objects under the hood. Therefore, the
following are equivalent:

```
>>> x = u.m ** Fraction(1, 3)
>>> x.powers
[Fraction(1, 3)]
>>> x = u.m ** (1. / 3.)
>>> x.powers
[Fraction(1, 3)]
```

## Defining units#

Users are free to define new units, either fundamental or compound,
using the `def_unit()`

function:

```
>>> bakers_fortnight = u.def_unit('bakers_fortnight', 13 * u.day)
```

The addition of a string gives the new unit a name that will show up when the unit is printed:

```
>>> 10. * bakers_fortnight
<Quantity 10. bakers_fortnight>
```

Creating a new fundamental unit is also possible:

```
>>> titter = u.def_unit('titter')
>>> chuckle = u.def_unit('chuckle', 5 * titter)
>>> laugh = u.def_unit('laugh', 4 * chuckle)
>>> guffaw = u.def_unit('guffaw', 3 * laugh)
>>> rofl = u.def_unit('rofl', 4 * guffaw)
>>> death_by_laughing = u.def_unit('death_by_laughing', 10 * rofl)
>>> (1. * rofl).to(titter)
<Quantity 240. titter>
```

Users can see the definition of a unit and its decomposition via:

```
>>> rofl.represents
Unit("4 guffaw")
>>> rofl.decompose()
Unit("240 titter")
```

By default, custom units are not searched by methods such as
`find_equivalent_units()`

. However, they
can be enabled by calling `add_enabled_units()`

:

```
>>> kmph = u.def_unit('kmph', u.km / u.h)
>>> (u.m / u.s).find_equivalent_units()
There are no equivalent units
>>> u.add_enabled_units([kmph])
<astropy.units.core._UnitContext object at ...>
>>> (u.m / u.s).find_equivalent_units()
Primary name | Unit definition | Aliases
[
kmph | 0.277778 m / s | ,
]
```

If new units are defined with prefixes enabled, the prefixed units must be
explicitly enabled as well, e.g., by using the `namespace`

argument:

```
>>> new_units = dict()
>>> foo = u.def_unit(['Fo', 'foo'], prefixes=True, namespace=new_units)
>>> u.add_enabled_units(new_units)
<astropy.units.core._UnitContext object at ...>
```

Now, the prefixed units can be parsed etc:

```
>>> print(u.Unit("megafoo").find_equivalent_units())
Primary name | Unit definition | Aliases
[
Fo | irreducible | foo ,
]
>>> print(u.Unit("megafoo").to(u.Unit("kFo")))
1000.0
```
