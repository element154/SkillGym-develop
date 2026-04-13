## Source: https://docs.astropy.org/en/stable/glossary.html

# Astropy Glossary#

- (
`n`

,)# A parenthesized number followed by a comma denotes a tuple with one element. The trailing comma distinguishes a one-element tuple from a parenthesized

`n`

. This is from NumPy; see https://numpy.org/doc/stable/glossary.html#term-n.- -like#
`<Class>-like`

is an instance of the`Class`

or a valid initializer argument for`Class`

as`Class(value)`

. E.g.`Quantity`

-like includes`"2 * u.km"`

because`astropy.units.Quantity("2 * u.km")`

works.- [‘physical type’]#
The physical type of a quantity can be annotated in square brackets following a

`Quantity`

(or similar quantity-like).For example,

`distance : quantity-like ['length']`

- angle-like#
quantity-like and a valid initializer for

`Angle`

. The`unit`

must be an angular. A string input is interpreted as an angle as described in the`Angle`

documentation.- buffer-like#
Object that implements Python’s buffer protocol.

- coordinate-like#
`BaseCoordinateFrame`

subclass instance, or a`SkyCoord`

(or subclass) instance, or a valid initializer as described in COORD.- file-like (readable)#
file-like object object that supports reading with a method

`read`

.For a formal definition see

`ReadableFileLike`

.- file-like (writeable)#
file-like object object that supports writing with a method

`write`

.For a formal definition see

`WriteableFileLike`

.- frame-like#
`BaseCoordinateFrame`

subclass or subclass instance or a valid Frame name (string).- length-like#
quantity-like and a valid initializer for

`Distance`

. The`unit`

must be a convertible to a unit of length.- number#
- quantity-like#
`Quantity`

(or subclass) instance, a number or array-like object, or a string which is a valid initializer for`Quantity`

.For a formal definition see

`QuantityLike`

.- table-like#
`Table`

(or subclass) instance or valid initializer for`Table`

as described in Constructing a Table. Common types include`dict[list]`

,`list[dict]`

,`list[list]`

, and`ndarray`

(structured array).- time-like#
`Time`

(or subclass) instance or a valid initializer for`Time`

, e.g.`str`

, array-like[str],`datetime`

, or`datetime64`

.- trait type#
In short, a trait type is a class with the following properties:

It is a class that can be used as a mixin to add functionality to another class.

It should never be instantiated directly.

It should not be used as a base class for other classes, but only as a mixin.

It can define methods, properties, and attributes – any of which can be abstract.

It can be generic, i.e. it can have type parameters.

It can subclass other traits, but should have a linear MRO.

These are the same set of properties as orthogonal mixin classes, with the added emphasis that they can serve as compiled types, if so enabled by a compilation system such as mypyc.

- unit-like#
`UnitBase`

subclass instance or a valid initializer for`Unit`

, e.g.,`str`

or scalar`Quantity`

.

## Optional Packages’ Glossary#

- color#
Any valid Matplotlib color.
