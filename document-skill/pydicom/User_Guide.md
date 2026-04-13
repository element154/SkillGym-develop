## Source: https://pydicom.github.io/pydicom/stable/guides/user/index.html

Getting started

Documentation

Examples

Additional Information

codify

Dataset.pixel_array

Dataset.overlay_array()

Dataset.waveform_array()

Dataset.compress()

## Source: https://pydicom.github.io/pydicom/stable/guides/index.html

Getting started

Documentation

Examples

Additional Information

These guides contain higher-level information for those already familiar with pydicom:

## Source: https://pydicom.github.io/pydicom/stable/guides/plugin_table.html

# Plugins for Pixel Data Compression and Decompression¶

## Plugins for Decompression¶

The table below lists the plugins available for decompressing pixel data that’s been compressed using the corresponding
*Transfer Syntax UID*. No plugins are used for uncompressed pixel data.

Transfer Syntax |
Plugins |
|||||
|---|---|---|---|---|---|---|
Name |
UID |
|
|
|
|
|
|
1.2.840.10008.1.2.4.50 |
✓ |
✓ |
✓ |
||
|
1.2.840.10008.1.2.4.51 |
✓ |
✓ |
✓ |
||
|
1.2.840.10008.1.2.4.57 |
✓ |
✓ |
|||
|
1.2.840.10008.1.2.4.70 |
✓ |
✓ |
|||
|
1.2.840.10008.1.2.4.80 |
✓ |
✓ |
✓ |
||
|
1.2.840.10008.1.2.4.81 |
✓ |
✓ |
✓ |
||
|
1.2.840.10008.1.2.4.90 |
✓ |
✓ |
✓ |
||
|
1.2.840.10008.1.2.4.91 |
✓ |
✓ |
✓ |
||
|
1.2.840.10008.1.2.4.201 |
✓ |
||||
|
1.2.840.10008.1.2.4.202 |
✓ |
||||
|
1.2.840.10008.1.2.4.203 |
✓ |
||||
|
1.2.840.10008.1.2.5 |
✓ |
✓ |
✓ |

1with

`pylibjpeg-libjpeg`

2with

`pylibjpeg-openjpeg`

3with

`pylibjpeg-rle`

4with Pillow’s

*Jpeg2KImagePlugin*

### Plugins¶

`pylibjpeg`

¶

Requires pylibjpeg and at least one of:

**Known limitations**

Maximum supported

*Bits Stored*for JPEG 2000 and HTJ2K is 24

`gdcm`

¶

Requires python-gdcm.

**Known limitations**

*JPEG Extended 12-bit*is only available if*Bits Allocated*is 8*JPEG-LS Near Lossless*only if*Bits Stored*is at least 8 for a*Pixel Representation*of 1*JPEG-LS Lossless*and*JPEG-LS Near Lossless*only if*Bits Stored*is not 6 or 7Maximum supported

*Bits Stored*is 16

`pillow`

¶

Requires Pillow, with support for JPEG 2000 via Pillow’s Jpeg2KImagePlugin requiring OpenJPEG.

**Known limitations**

*JPEG Extended 12-bit*is only available if*Bits Allocated*is 8*JPEG 2000 Lossless*and*JPEG 2000*are only available for a*Samples per Pixel*of 3 when*Bits Stored*is <= 8Maximum supported

*Bits Stored*is 16

`pyjpegls`

¶

Requires pyjpegls.

`pydicom`

¶

Requires pydicom.

**Known limitations**

Slower than the other plugins by 3-4x

## Plugins for Compression¶

Transfer Syntax |
Plugins |
Encoding guide |
|
|---|---|---|---|
Name |
UID |
||
|
1.2.840.10008.1.2.4.80 |
|
|
|
1.2.840.10008.1.2.4.81 |
||
|
1.2.840.10008.1.2.4.90 |
|
|
|
1.2.840.10008.1.2.4.91 |
||
|
1.2.840.10008.1.2.5 |
|
|
|

### Plugins¶

`pyjpegls`

¶

Requires pyjpegls.

`pylibjpeg`

¶

Requires pylibjpeg as well as
pylibjpeg-openjpeg for JPEG 2000
compression and pylibjpeg-rle for
*RLE Lossless*.

**Known limitations**

The maximum supported

*Bits Stored*for JPEG 2000 is 24, however the results for 20-24 are very poor when using lossy compression.

`pydicom`

¶

Requires pydicom.

**Known limitations**

Much slower than the other plugins

## Source: https://pydicom.github.io/pydicom/stable/guides/element_value_types.html

# Element VRs and Python types¶

DICOM elements can contain anything from ASCII strings to unicode text, decimals, floats, signed and unsigned integers of different byte-depth and even encoded data. The format of the value of an element is given by its Value Representation or VR, and a list of VRs is given in the DICOM Standard in Part 5, Table 6.2-1.

So when using *pydicom*, what Python type should be used with a given VR to
ensure that the value gets written correctly?

Elements of any VR:

Can be set as empty by using

`None`

Can have their values set using their

*set using*or*stored as*type from the table below

Non-

**SQ**element values:Can also be set using a

`list`

of their*set using*type - for Value Multiplicity (VM) > 1, the value will be stored as a`MultiValue`

of their*stored as*typeHowever, according to the DICOM Standard, elements with VR

**LT**,**OB**,**OD**,**OF**,**OL**,**OW**,**ST**,**UN**,**UR**and**UT**should never have a VM greater than 1.

**SQ**element values should be set using a`list`

of zero or more`Dataset`

instances.

VR |
Name |
Set using |
Stored as (T) |
Type hint for element value |
|---|---|---|---|---|
AE |
Application Entity |
None | T | MutableSequence[T] |
||
AS |
Age String |
|||
AT |
Attribute Tag |
Tag |
||
CS |
Code String |
|||
DA |
Date |
|||
DS |
Decimal String |
|||
DT |
Date Time |
|||
FL |
Floating Point Single |
|||
FD |
Floating Point Double |
|||
IS |
Integer String |
|||
LO |
Long String |
|||
LT |
Long Text |
None | T |
||
OB |
Other Byte |
|
None | T |
|
OD |
Other Double |
|||
OF |
Other Float |
|||
OL |
Other Long |
|||
OV |
Other 64-bit Very Long |
|||
OW |
Other Word |
|||
PN |
Person Name |
None | T | MutableSequence[T] |
||
SH |
Short String |
|||
SL |
Signed Long |
|||
SQ |
Sequence of Items |
MutableSequence[
|
||
SS |
Signed Short |
None | T | MutableSequence[T] |
||
ST |
Short Text |
None | T |
||
SV |
Signed 64-bit Very Long |
None | T | MutableSequence[T] |
||
TM |
Time |
|||
UC |
Unlimited Characters |
|||
UI |
Unique Identifier (UID) |
|||
UL |
Unsigned Long |
|||
UN |
Unknown |
None | T |
||
UR |
URI/URL |
|||
US |
Unsigned Short |
None | T | MutableSequence[T] |
||
UT |
Unlimited Text |
None | T |
||
UV |
Unsigned 64-bit Very Long |
None | T | MutableSequence[T] |

1Any type accepted by

`Tag()`

can be used4See notes for bufferable O* VRs below

## Bufferable O* VRs¶

The value for elements with O* VRs (**OB**, **OD**, **OF**, **OL**, **OV** and
**OW**) can be set using an object that inherits from `io.BufferedIOBase`

such
as the `io.BufferedReader`

instances returned by the `open()`

built-in when
in read mode. This allows you to avoid having to read a large amount of data into
memory when creating datasets:

```
from pydicom import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian
with open("a_large_amount_of_data", "rb") as f:
ds = Dataset()
ds.file_meta = FileMetaDataset()
ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
ds.PixelData = f
ds.save_as("large_dataset.dcm")
```

To use a buffered *Pixel Data* value with a dataset that has a compressed transfer
syntax such as *JPEG 2000 Lossles*, the `encapsulate_buffer()`

and
`encapsulate_extended_buffer()`

functions can be used to encapsulate
the buffered frames:

```
from pydicom import Dataset, FileMetaDataset
from pydicom.encaps import encapsulate_buffer
from pydicom.uid import JPEG2000Lossless
with open("a_large_jpeg2000_file.j2k", "rb") as f:
ds = Dataset()
ds.file_meta = FileMetaDataset()
ds.file_meta.TransferSyntaxUID = JPEG2000Lossless
ds.PixelData = encapsulate_buffer([f])
ds.save_as("large_compressed_dataset.dcm")
```

However, be aware that Datasets containing buffered objects that don’t normally work
with `pickle`

or `deepcopy()`

such as
`BufferedReader`

are not able to be pickled or deepcopied.

## Source: https://pydicom.github.io/pydicom/stable/guides/user/image_data_handlers.html

# Handling of compressed pixel data¶

How to get compressed pixel data

## Prerequisites¶

To be able to decompress compressed DICOM pixel data, you need to install one or more packages that are able to handle the format the data is encoded in.

The following packages can be used with *pydicom* and NumPy to
decompress compressed *Pixel Data*:

pylibjpeg with the

`pylibjpeg-libjpeg`

,`pylibjpeg-openjpeg`

and`pylibjpeg-rle`

plugins. Supports the most commonly used transfer syntaxes.jpeg_ls supports JPEG-LS transfer syntaxes.

GDCM supports the most commonly used transfer syntaxes.

Pillow, ideally with the

`jpeg`

and`jpeg2000`

plugins. However we don’t recommend using Pillow as it performs a number of undesirable operations on the decoded images which are not always reversible.

Caution

We rely on the data handling capacity of the mentioned packages and cannot guarantee the correctness of the generated uncompressed pixel data. Be sure to verify the correctness of the output using other means before you use them.

## Supported Transfer Syntaxes¶

To get the transfer syntax of a dataset you can do:

```
>>> from pydicom import dcmread
>>> ds = dcmread('path/to/dicom/file')
>>> ds.file_meta.TransferSyntaxUID
'1.2.840.10008.1.2.1'
>>> ds.BitsAllocated
16
```

As far as we have been able to verify, the following transfer syntaxes are handled by the given packages:

Transfer Syntax |
NumPy |
NumPy + JPEG-LS |
NumPy + GDCM |
NumPy + Pillow |
NumPy + pylibjpeg |
|
|---|---|---|---|---|---|---|
Name |
UID |
|||||
Explicit VR Little Endian |
1.2.840.10008.1.2.1 |
✓ |
✓ |
✓ |
✓ |
✓ |
Implicit VR Little Endian |
1.2.840.10008.1.2 |
✓ |
✓ |
✓ |
✓ |
✓ |
Explicit VR Big Endian |
1.2.840.10008.1.2.2 |
✓ |
✓ |
✓ |
✓ |
✓ |
Deflated Explicit VR Little Endian |
1.2.840.10008.1.2.1.99 |
✓ |
✓ |
✓ |
✓ |
✓ |
RLE Lossless |
1.2.840.10008.1.2.5 |
✓ |
✓ |
✓ |
✓ |
✓ |
JPEG Baseline (Process 1) |
1.2.840.10008.1.2.4.50 |
✓ |
✓ |
✓ |
||
JPEG Extended (Process 2 and 4) |
1.2.840.10008.1.2.4.51 |
✓ |
✓ |
✓ |
||
JPEG Lossless (Process 14) |
1.2.840.10008.1.2.4.57 |
✓ |
✓ |
|||
JPEG Lossless (Process 14, SV1) |
1.2.840.10008.1.2.4.70 |
✓ |
✓ |
|||
JPEG LS Lossless |
1.2.840.10008.1.2.4.80 |
✓ |
✓ |
✓ |
||
JPEG LS Lossy |
1.2.840.10008.1.2.4.81 |
✓ |
✓ |
✓ |
||
JPEG 2000 Lossless |
1.2.840.10008.1.2.4.90 |
✓ |
✓ |
✓ |
||
JPEG 2000 |
1.2.840.10008.1.2.4.91 |
✓ |
✓ |
✓ |
||
High-Throughput JPEG 2000 Lossless |
1.2.840.10008.1.2.4.201 |
✓ |
||||
High-Throughput JPEG 2000 (RPCL) Lossless |
1.2.840.10008.1.2.4.202 |
✓ |
||||
High-Throughput JPEG 2000 |
1.2.840.10008.1.2.4.203 |
✓ |

1

*only with JpegImagePlugin*

2

*only with Jpeg2KImagePlugin*

3

*only if (0028,0100) Bits Allocated = 8*

4

*with the pylibjpeg-rle plugin, 4-5x faster than default*

5

*with the pylibjpeg-libjpeg plugin*

6

*with the pylibjpeg-openjpeg plugin*

## Usage¶

To get uncompressed pixel data as a NumPy `ndarray`

you have a number of options, depending on your requirements:

To access the pixel data without modifying the dataset you can use the

`Dataset.pixel_array`

property, or the`pixel_array()`

and`iter_pixels()`

functions with a`Dataset`

instance.To access the pixel data while minimizing memory usage you can use the

`pixel_array()`

or`iter_pixels()`

functions with the path to the dataset.To decompress a dataset in-place you can use

`Dataset.decompress()`

or the`decompress()`

function.

## Source: https://pydicom.github.io/pydicom/stable/guides/user/base_element.html

# Core elements in pydicom¶

pydicom object model, description of classes, examples

## Dataset¶

The main class in *pydicom* is `Dataset`

which emulates the behavior
of a Python `dict`

whose keys are DICOM tags (`BaseTag`

instances),
and values are the corresponding `DataElement`

instances.

Warning

The iterator of a `Dataset`

yields
`DataElement`

instances, e.g. the values of the
dictionary instead of the keys normally yielded by iterating a `dict`

.

A `Dataset`

can be created directly, but you’ll
usually get one by reading an existing DICOM dataset from file using
`dcmread()`

:

```
>>> from pydicom import dcmread, examples
>>> # Returns the path to pydicom's examples.rt_plan dataset
>>> path = examples.get_path("rt_plan")
>>> print(path)
PosixPath('/path/to/pydicom/data/test_files/rtplan.dcm')
>>> # Read the DICOM dataset at `path`
>>> ds = dcmread(path)
```

You can display the contents of the entire dataset using `str(ds)`

or with:

```
>>> ds
Dataset.file_meta -------------------------------
(0002,0000) File Meta Information Group Length UL: 156
(0002,0001) File Meta Information Version OB: b'\x00\x01'
(0002,0002) Media Storage SOP Class UID UI: RT Plan Storage
(0002,0003) Media Storage SOP Instance UID UI: 1.2.999.999.99.9.9999.9999.20030903150023
(0002,0010) Transfer Syntax UID UI: Implicit VR Little Endian
(0002,0012) Implementation Class UID UI: 1.2.888.888.88.8.8.8
-------------------------------------------------
(0008,0012) Instance Creation Date DA: '20030903'
(0008,0013) Instance Creation Time TM: '150031'
(0008,0016) SOP Class UID UI: RT Plan Storage
(0008,0018) SOP Instance UID UI: 1.2.777.777.77.7.7777.7777.20030903150023
(0008,0020) Study Date DA: '20030716'
(0008,0030) Study Time TM: '153557'
(0008,0050) Accession Number SH: ''
(0008,0060) Modality CS: 'RTPLAN'
...
```

You can access specific elements by their DICOM keyword or tag:

```
>>> ds.PatientName # element keyword
'Last^First^mid^pre'
>>> ds[0x10, 0x10].value # element tag
'Last^First^mid^pre'
```

When using the element tag directly a `DataElement`

instance is returned, so `DataElement.value`

must be used to get the value.

Warning

In *pydicom*, private data elements are displayed with square brackets
around the name (if the name is known to *pydicom*). These are shown for
convenience only; the descriptive name in brackets cannot be used to
retrieve data elements. See details in Private Data Elements.

You can also set an element’s value by using the element’s keyword or tag number:

```
>>> ds.PatientID = "12345"
>>> ds.SeriesNumber = 5
>>> ds[0x10, 0x10].value = 'Test'
```

The use of element keywords is possible because *pydicom* intercepts requests
for member variables, and checks if they are in the DICOM dictionary. It translates
the keyword to a (group, element) tag and returns the corresponding value for
that tag if it exists in the dataset.

See Anonymize DICOM data for a usage example of data elements removal and assignation.

Note

To understand using `Sequence`

in *pydicom*, please refer
to this object model:

`Dataset`

(emulates a Python`dict`

)Contains

`DataElement`

instances, the value of each element can be one of:

The value of sequence elements is a `Sequence`

instance, which wraps a Python `list`

. Items in the sequence are
referenced by number, beginning at index `0`

as per Python convention:

```
>>> ds.BeamSequence[0].BeamName
'Field 1'
>>> # Or, set an intermediate variable to a dataset in the list
>>> beam1 = ds.BeamSequence[0] # First dataset in the sequence
>>> beam1.BeamName
'Field 1'
```

Using DICOM keywords is the recommended way to access data elements, but you can also use the tag numbers directly, such as:

```
>>> # Same thing with tag numbers - much harder to read:
>>> # Really should only be used if DICOM keyword not in pydicom dictionary
>>> ds[0x300a, 0xb0][0][0x300a, 0xc2].value
'Field 1'
```

If you don’t remember or know the exact element tag or keyword,
`Dataset`

provides a handy
`Dataset.dir()`

method, useful during interactive
sessions at the Python prompt:

```
>>> ds.dir("pat")
['PatientBirthDate', 'PatientID', 'PatientName', 'PatientSetupSequence', 'PatientSex']
```

`Dataset.dir()`

will return any non-private element
keywords in the dataset that have the specified string anywhere in the
keyword (case insensitive).

Note

Calling `Dataset.dir()`

without passing it an
argument will return a `list`

of all non-private element keywords in
the dataset.

You can also see all the names that *pydicom* knows about by viewing the
_dicom_dict.py file. It
should not normally be necessary, but you can add your own entries to the
DICOM dictionary at run time using `add_dict_entry()`

or
`add_dict_entries()`

. Similarly, you can add private data
elements to the private dictionary using
`add_private_dict_entry()`

or
`add_private_dict_entries()`

.

Under the hood, `Dataset`

stores a
`DataElement`

object for each item, but when
accessed by keyword (e.g. `ds.PatientName`

) only the value of that
`DataElement`

is returned. If you need the object itself,
you can use the access the item using either the keyword (for official DICOM
elements) or tag number:

```
>>> # reload the data
>>> ds = pydicom.dcmread(path)
>>> elem = ds['PatientName']
>>> elem.VR, elem.value
('PN', 'Last^First^mid^pre')
>>> # an alternative is to use:
>>> elem = ds[0x0010,0x0010]
>>> elem.VR, elem.value
('PN', 'Last^First^mid^pre')
```

To see whether the `Dataset`

contains a particular element, use
the `in`

operator with the element’s keyword or tag:

```
>>> "PatientName" in ds # or (0x0010, 0x0010) in ds
True
```

To remove an element from the `Dataset`

, use the `del`

operator:

```
>>> del ds.SoftwareVersions # or del ds[0x0018, 0x1020]
```

To work with (7FE0,0010) *Pixel Data*, the raw `bytes`

are available
through the PixelData keyword:

```
>>> # example CT dataset with actual pixel data
>>> ds = examples.ct
>>> pixel_bytes = ds.PixelData
```

However its much more convenient to use
`Dataset.pixel_array`

to return a
`numpy.ndarray`

(requires the NumPy library):

```
>>> arr = ds.pixel_array
>>> arr
array([[175, 180, 166, ..., 203, 207, 216],
[186, 183, 157, ..., 181, 190, 239],
[184, 180, 171, ..., 152, 164, 235],
...,
[906, 910, 923, ..., 922, 929, 927],
[914, 954, 938, ..., 942, 925, 905],
[959, 955, 916, ..., 911, 904, 909]], dtype=int16)
```

For more details, see Working with Pixel Data.

## DataElement¶

The `DataElement`

class is not usually used directly in user
code, but is used extensively by `Dataset`

.
`DataElement`

is a simple object which stores the following
things:

`VR`

– the element’s Value Representation – a two letter`str`

that describes to the format of the stored value.

`VM`

– the element’s Value Multiplicity as an`int`

. This is automatically determined from the contents of the`value`

.

`value`

– the element’s actual value. A regular value like a number or string (or`list`

of them if the VM > 1), or a`Sequence`

.

## Tag¶

`Tag()`

is not generally used directly in user code, as
`BaseTags`

are automatically created when you assign or read
elements using their keywords as illustrated in sections above.

The `BaseTag`

class is derived from `int`

,
so in effect it’s just a number with some extra behavior:

`Tag()`

is used to create instances of`BaseTag`

and enforces the expected 4-byte (group, element) structure.A

`BaseTag`

instance can be created from an`int`

or a`tuple`

containing the (group, element), or from the DICOM keyword:>>> from pydicom.tag import Tag >>> t1 = Tag(0x00100010) # all of these are equivalent >>> t2 = Tag(0x10, 0x10) >>> t3 = Tag((0x10, 0x10)) >>> t4 = Tag("PatientName") >>> t1 (0010,0010) >>> type(t1) <class `pydicom.tag.BaseTag`> >>> t1==t2, t1==t3, t1==t4 (True, True, True)

`BaseTag.group`

and`BaseTag.elem`

to return the group and element portions of the tag.The

`BaseTag.is_private`

property checks whether the tag represents a private tag (i.e. if group number is odd).

## Sequence¶

`Sequence`

is derived from Python’s `list`

.
The only added functionality is to make string representations prettier.
Otherwise all the usual methods of `list`

like item selection, append,
etc. are available.

For examples of accessing data nested in sequences, see Working with sequences.

## Source: https://pydicom.github.io/pydicom/stable/guides/user/writing_files.html

# Writing DICOM Files¶

How to write DICOM files using pydicom.

## Introduction¶

Probably the most common use of *pydicom* is to read an existing DICOM file,
alter some items, and write it back out again. The Dataset basics tutorial shows how to do this.

If you need to create a DICOM file from scratch then you can either:

Use the

`codify`

script to create Python code from an existing dataset.Create a new

`Dataset`

instance and populate it.

Warning

To be truly DICOM compliant, certain data elements will be required in the file meta information and in the main dataset. Also, you should create your own UIDs, implementation name, and so on.

## Using `codify`

¶

*pydicom* has a command-line utility called `codify`

that
takes an existing DICOM file, and produces Python code that can be run to
produce a copy of the original file.

In other words: *pydicom* has a tool that can automatically generate
well-designed Python code for you - code that creates DICOM files. The only
requirement is that you have an existing DICOM file that looks approximately
like the one you need. You can then use the code as a model to work from. The
tool is especially useful with sequences, which can be tricky to code
correctly.

Warning

The code produced by `codify`

will contain all the information in the original
file, which may include private health information or other sensitive
information. If the code is run, the resulting DICOM file will also contain
that information. You may want to consider using de-identified DICOM files
with `codify`

, or handling the output files according to your requirements for
sensitive information.

One issue to be aware of is that `codify`

will not create code for large items
like pixel data. Instead it creates a line like:

```
ds.PixelData = # XXX Array of 524288 bytes excluded
```

In that case, the code will produce a syntax error when run, and you will have to edit the code to supply a valid value.

Note

The `--exclude-size parameter`

can set the maximum size of the data
element value that is coded. Data elements bigger than that will have the
syntax error line as shown above.

One potential disadvantage of `codify`

, depending on your use case, is that it
does not create loops. If you have, say, 30 items in a Sequence, `codify`

will
produce code that makes them one at a time. Code you wrote by hand would
likely create them in a loop, because most of the code needed is quite
repetitive. If you want to switch to a loop, you could use the first item’s
code as a starting point, and modify as needed, deleting the code for the
other individual items.

For details on calling the `codify`

command, see the pydicom codify command section.

`codify`

could also be called from code, rather than from a command line; you
can look at the codify.py source and the `code_file`

function for a
starting point for that.

## Writing a file from scratch¶

The `codify`

tool, described in the previous section, is a good starting point
for *pydicom* code, but if you can’t (or don’t want to) use that tool, then you
can certainly write code from scratch to make a complete DICOM file using
*pydicom*.

It’s not particularly difficult, but to produce a valid DICOM file requires specific items to be created. A basic example of that is available in the example file Write DICOM data.

Just don’t forget the warnings in the Introduction section above, and be sure to create all the required DICOM data elements.

## Source: https://pydicom.github.io/pydicom/stable/guides/user/working_with_pixel_data.html

# Working with Pixel Data¶

How to work with pixel data in pydicom.

## Introduction¶

Many DICOM SOP classes contain bulk pixel data, which is usually used to
represent one or more image frames (although other types of data are possible). In these SOP classes the pixel
data is (almost) always contained in the (7FE0,0010) *Pixel Data* element.
The only exception to this is Parametric Map Storage which may instead contain data in the (7FE0,0008)
*Float Pixel Data* or (7FE0,0009) *Double Float Pixel Data* elements.

Note

In the following the term *pixel data* will be used to refer to
the bulk data from *Pixel Data*, *Float Pixel Data* and *Double Float
Pixel Data* elements. While the examples use `PixelData`

,
`FloatPixelData`

or `DoubleFloatPixelData`

could also be used
interchangeably provided the dataset contains the corresponding element.

By default *pydicom* reads in pixel data as the raw bytes found in the file:

```
>>> from pydicom import dcmread, examples
>>> path = examples.get_path("mr") # The path to the examples.mr dataset
>>> ds = dcmread(path)
>>> ds.PixelData
b'\x89\x03\xfb\x03\xcb\x04\xeb\x04\xf9\x02\x94\x01\x7f...
```

`PixelData`

is often not immediately useful as data may be
stored in a variety of different ways:

The pixel values may be signed or unsigned integers, or floats

There may be multiple image frames

There may be multiple planes per frame (i.e. RGB) and the order of the pixels may be different

The image data may be encoded using one of the available compression standards (

`1.2.840.10008.1.2.4.50`

JPEG Baseline,`1.2.840.10008.1.2.5`

RLE Lossless, etc). Encoded image data will also be encapsulated and each encapsulated image frame may be broken up into one or more fragments.

Because of the complexity in interpreting the pixel data, *pydicom* provides
an easy way to get it in a convenient form:
`Dataset.pixel_array`

.

`Dataset.pixel_array`

¶

Warning

`Dataset.pixel_array`

requires NumPy.

`Dataset.pixel_array`

returns a
`numpy.ndarray`

containing the pixel data:

```
>>> arr = ds.pixel_array
>>> arr
array([[ 905, 1019, 1227, ..., 302, 304, 328],
[ 628, 770, 907, ..., 298, 331, 355],
[ 498, 566, 706, ..., 280, 285, 320],
...,
[ 334, 400, 431, ..., 1094, 1068, 1083],
[ 339, 377, 413, ..., 1318, 1346, 1336],
[ 378, 374, 422, ..., 1369, 1129, 862]], dtype=int16)
>>> arr.shape
(64, 64)
```

If the pixel data is compressed then
`pixel_array`

will return the uncompressed data,
provided the dependencies of the required pixel data decoder have been met. See
handling compressed image data for more
information.

NumPy can be used to modify the data, but if the changes are to be saved,
they must be written back to the dataset’s `PixelData`

element.

Warning

Converting data from an `ndarray`

back to `bytes`

may not be
as straightforward as in the following example, particularly for
multi-planar images or where compression is required.

```
# example: zero anything < 300
arr = ds.pixel_array
arr[arr < 300] = 0
ds.PixelData = arr.tobytes()
ds.save_as("temp.dcm")
```

Some changes may require other DICOM tags to be modified. For example, if the
image size is reduced (e.g. a 512x512 image is shrunk to 256x256) then
`Rows`

and `Columns`

should be set
appropriately. You must explicitly set these yourself; *pydicom* does not do so
automatically.

See Downsize MRI image using pydicom for an example.

`pixel_array`

can also be used to pass image
data to graphics libraries for viewing. See Viewing Images for details.

## Color space¶

When using `pixel_array`

with *Pixel Data* that has an (0028,0002) *Samples per Pixel* value
of `3`

then the returned pixel data will be in the color space as given by
(0028,0004) *Photometric Interpretation* (e.g. `RGB`

, `YBR_FULL`

,
`YBR_FULL_422`

, etc).

*pydicom* offers a limited ability to convert between 8-bits/channel YBR and
RGB color spaces through the
`convert_color_space()`

function. When changing the color space you should also change the value
of *Photometric Interpretation* to match.

Note

See the DICOM Standard, Part 3, Section C.7.6.3.1 for more information about color spaces.

## Palette Color¶

Some DICOM datasets store their output image pixel values in a lookup table
(LUT), where the values in *Pixel Data* are the index to a corresponding
LUT entry. When a dataset’s (0028,0004) *Photometric Interpretation* value is
`PALETTE COLOR`

then the
`apply_color_lut()`

function can be used
to apply a palette color LUT to the pixel data to produce an RGB image.

```
from pydicom import examples
from pydicom.pixels import apply_color_lut
# Fetch an example PALETTE COLOR dataset
ds = examples.palette_color
arr = ds.pixel_array
rgb = apply_color_lut(arr, ds)
```

It’s also possible to apply one of the DICOM well-known color palettes provided the bit-depth of the pixel data is 8-bit.

```
from pydicom import examples
from pydicom.pixels import apply_color_lut
ds = examples.palette_color
arr = ds.pixel_array
# You could also use the corresponding well-known SOP Instance UID
rgb = apply_color_lut(arr, palette='PET')
```

## Modality LUT or Rescale Operation¶

The DICOM Modality LUT module
converts raw pixel data values to a specific (possibly unitless) physical
quantity, such as Hounsfield units for CT. The
`apply_modality_lut()`

function can be
used with an input array of raw values and a dataset containing a Modality LUT
module to return the converted values. When a dataset requires multiple
grayscale transformations, the Modality LUT transformation is always applied
first.

```
from pydicom import examples
from pydicom.pixels import apply_modality_lut
ds = examples.ct
arr = ds.pixel_array
hu = apply_modality_lut(arr, ds)
```

## VOI LUT or Windowing Operation¶

The DICOM VOI LUT module applies a
VOI or windowing operation to input values. The
`apply_voi_lut()`

function
can be used with an input array and a dataset containing a VOI LUT module to
return values with applied VOI LUT or windowing. When a dataset contains
multiple VOI or windowing views then a particular view can be returned by
using the index keyword parameter.

When a dataset requires multiple grayscale transformations, then it’s assumed that the modality LUT or rescale operation has already been applied.

```
from pydicom import examples
from pydicom.pixels import apply_voi_lut
ds = examples.overlay
arr = ds.pixel_array
out = apply_voi_lut(arr, ds, index=0)
```

## Source: https://pydicom.github.io/pydicom/stable/guides/user/working_with_overlays.html

# Working with Overlay Data¶

How to work with overlay data in pydicom.

## Introduction¶

Overlays in DICOM are present in what’s called
a Repeating Group, where the group number of the
element tags are defined over a range rather than a specific value. For
example, the tag’s group number for (60xx,3000) *Overlay Data* may be (in hex)
`6000`

, `6002`

, or any even value up to `601E`

. This allows a dataset to
include multiple overlays, where the related elements for each overlay use the
same group number. Because of this, the only way to access a particular
element from an overlay is to use the `Dataset[group, elem]`

method:

```
>>> from pydicom import examples
>>> ds = examples.overlay
>>> elem = ds[0x6000, 0x3000] # returns a DataElement
>>> print(elem)
(6000, 3000) Overlay Data OW: Array of 29282 elements
```

*pydicom* tends to be “lazy” in interpreting DICOM data. For example, by default
it doesn’t do anything with overlay data except read in the raw bytes:

```
>>> elem.value
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00...
```

`Dataset.overlay_array()`

¶

Warning

`Dataset.overlay_array()`

requires NumPy.

The *Overlay Data* element contains the raw bytes exactly as found in the file
as bit-packed data. To unpack and get an overlay in a more useful form you
can use the `overlay_array()`

method to return a
`numpy.ndarray`

. To use it you only need to pass the group number of the
overlay elements you’re interested in:

```
>>> arr = ds.overlay_array(0x6000)
>>> arr
array([[ 0, 0, 0, ..., 0, 0, 0],
[ 0, 0, 0, ..., 0, 0, 0],
[ 0, 0, 0, ..., 0, 0, 0],
...,
[ 0, 0, 0, ..., 0, 0, 0],
[ 0, 0, 0, ..., 0, 0, 0],
[ 0, 0, 0, ..., 0, 0, 0],], dtype=uint8)
>>> arr.shape
(484, 484)
```

One thing to remember when dealing with *Overlay Data* is that the top left
of the overlay doesn’t necessarily have to line up with the top left of the
related *Pixel Data*. The actual offset between them can be determined from
(60xx,0050) *Overlay Origin*, where a value of `[1, 1]`

indicates that
the top left pixels are aligned and a value of `[0, 0]`

indicates that the
overlay pixels start 1 row above and 1 row to the left of the image pixels.

NumPy can be used to modify the pixels, but if the changes are to be saved,
they must be bit-packed (using something like `pack_bits()`

)
and written back to the correct element:

```
# Add a line
arr[10, :] = 1
# Pack the data
from pydicom.pixels import pack_bits
packed_bytes = pack_bits(arr)
# Update the element value
ds[0x6000, 0x3000].value = packed_bytes
ds.save_as("temp.dcm")
```

Some changes may require other DICOM elements to be modified. For example, if
the overlay data is reduced (e.g. a 512x512 image is resized to 256x256) then
the corresponding (60xx,0010) *Overlay Rows* and (60xx,0011) *Overlay Columns*
should be set appropriately. You must explicitly set these yourself as *pydicom*
does not do so automatically.

## Source: https://pydicom.github.io/pydicom/stable/guides/user/working_with_waveforms.html

# Working with Waveform Data¶

How to work with waveform data in pydicom.

## Introduction¶

Some DICOM SOP classes such as Basic Voice Audio Waveform and 12-Lead ECG
contain a (5400,0100) *Waveform Sequence* element,
where each item in the sequence is a related group of waveforms (a multiplex).
The requirements of the sequence is given by the Waveform
module in Part 3, Annex C.10.9 of the DICOM
Standard.

Each multiplex consists of one or more channels synchronised at a
common sampling frequency (in Hz), which is given by the (003A,001A) *Sampling
Frequency*. The waveform data for each multiplex is encoded in the
corresponding (5400,1010) *Waveform Data* element.

```
>>> from pydicom import examples
>>> ds = examples.waveform
>>> ds.WaveformSequence
<Sequence, length 2>
>>> multiplex = ds.WaveformSequence[0]
>>> multiplex.NumberOfWaveformChannels
12
>>> multiplex.SamplingFrequency
"1000.0"
>>> multiplex['WaveformData']
(5400, 1010) Waveform Data OW: Array of 240000 elements
```

`Dataset.waveform_array()`

¶

Warning

`Dataset.waveform_array()`

requires NumPy.

The *Waveform Data* element contains the raw bytes exactly as found in the
file. To get the waveforms in a more useful form you can use the
`Dataset.waveform_array()`

method
to return a `numpy.ndarray`

with shape (samples, channels) for the multiplex
group at index in the *Waveform Sequence*.

```
>>> multiplex_1 = ds.waveform_array(0)
>>> multiplex_1
array([[ 100. , 112.5 , 12.5 , ..., -25. , -68.75, -50. ],
[ 81.25, 106.25, 25. , ..., -25. , -75. , -50. ],
[ 62.5 , 100. , 37.5 , ..., -25. , -81.25, -50. ],
...,
[ 25. , 131.25, 106.25, ..., -137.5 , -150. , -100. ],
[ 21.25, 137.5 , 116.25, ..., -137.5 , -150. , -106.25],
[ 25. , 137.5 , 112.5 , ..., -137.5 , -150. , -112.5 ]])
>>> multiplex_1.shape
(10000, 12)
>>> multiplex_2 = ds.waveform_array(1)
>>> multiplex_2.shape
(1200, 12)
```

If the *Channel Sensitivity Correction Factor* is available for a given channel
then it will be applied to the raw channel data. If you need the raw data
without any corrections then you can use the
`multiplex_array()`

function with the *as_raw* keyword parameter instead:

```
>>> from pydicom.waveforms import multiplex_array
>>> arr = multiplex_array(ds, 0, as_raw=True)
>>> arr
array([[ 80, 90, 10, ..., -20, -55, -40],
[ 65, 85, 20, ..., -20, -60, -40],
[ 50, 80, 30, ..., -20, -65, -40],
...,
[ 20, 105, 85, ..., -110, -120, -80],
[ 17, 110, 93, ..., -110, -120, -85],
[ 20, 110, 90, ..., -110, -120, -90]], dtype=int16)
```

## Source: https://pydicom.github.io/pydicom/stable/guides/user/image_data_compression.html

# Compressing *Pixel Data*¶

How to compress Pixel Data

## Compressing using pydicom¶

### Supported Transfer Syntaxes¶

*Pixel Data* can be compressed natively using *pydicom* for the following
transfer syntaxes:

Transfer Syntax |
Plugin names |
Dependencies |
|
|---|---|---|---|
Name |
UID |
||
JPEG-LS Lossless |
1.2.840.10008.1.2.4.80 |
pyjpegls |
|
JPEG-LS Near Lossless |
1.2.840.10008.1.2.4.81 |
||
JPEG 2000 Lossless |
1.2.840.10008.1.2.4.90 |
pylibjpeg |
|
JPEG 2000 |
1.2.840.10008.1.2.4.91 |
||
RLE Lossless |
1.2.840.10008.1.2.5 |
pydicom |
|
pylibjpeg |
|||
gdcm |

1

*~20x slower than the other plugins*

Each of the supported transfer syntaxes has a corresponding encoding guide to help you with the specific requirements of the encoding method.

Transfer Syntax |
Encoding guide |
|---|---|
JPEG-LS Lossless |
|
JPEG-LS Near Lossless |
|
JPEG 2000 Lossless |
|
JPEG 2000 |
|
RLE Lossless |

### Compressing with `Dataset.compress()`

¶

The `Dataset.compress()`

method or
`compress()`

function can be used to compress an uncompressed
dataset in-place:

```
from pydicom import examples
from pydicom.uid import RLELossless
ds = examples.ct
ds.compress(RLELossless)
ds.save_as("ct_rle_lossless.dcm")
```

A specific encoding plugin can be used by passing the plugin name via the encoding_plugin argument:

```
# Will set `ds.is_little_endian` and `ds.is_implicit_VR` automatically
ds.compress(RLELossless, encoding_plugin='pylibjpeg')
ds.save_as("ct_rle_lossless.dcm")
```

Implicitly changing the compression on an already compressed dataset is not
currently supported, however it can still be done by decompressing
prior to calling `compress()`

. In the example
below, a matching image data handler for the
original transfer syntax - *JPEG 2000 Lossless* - is required.

```
# Requires a JPEG 2000 compatible image data handler
ds = examples.jpeg2k
ds.decompress()
ds.compress(RLELossless)
ds.save_as("US1_RLE.dcm")
```

## Compressing using third-party packages¶

If you need to perform pixel data compression using an encoding method not
supported by *pydicom* - such as ISO/IEC 10918-1 JPEG - then you’ll need to find a third-party
package or application to do so. Once you’ve done that you have to follow the
requirements for compressed *Pixel Data* in the DICOM Standard:

Each frame of pixel data must be encoded separately

All the encoded frames must then be

`encapsulated`

using a basic offset table. When the amount of encoded data is too large for the basic offset table then the use of the`extended offset table`

is recommended.A dataset with encapsulated pixel data must use explicit VR little endian encoding

See the relevant sections of the DICOM Standard for more information.

```
from typing import List, Tuple
from pydicom import examples
from pydicom.encaps import encapsulate, encapsulate_extended
from pydicom.uid import JPEGBaseline8Bit
# Fetch an example dataset
ds = examples.ct
# Use third-party package to compress
# Let's assume it compresses to JPEG Baseline (lossy)
frames: List[bytes] = third_party_compression_func(...)
# Set the *Transfer Syntax UID* appropriately
ds.file_meta.TransferSyntaxUID = JPEGBaseline8Bit
# Basic encapsulation
ds.PixelData = encapsulate(frames)
# Set the element's VR and use an undefined length
ds["PixelData"].is_undefined_length = True
ds["PixelData"].VR = "OB" if ds.BitsAllocated <= 8 else "OW"
# Save!
ds.save_as("ct_compressed_basic.dcm")
# Extended encapsulation
result: Tuple[bytes, bytes, bytes] = encapsulate_extended(frames)
ds.PixelData = result[0]
ds.ExtendedOffsetTable = result[1]
ds.ExtendedOffsetTableLength = result[2]
ds.save_as("ct_compressed_ext.dcm")
```

## Source: https://pydicom.github.io/pydicom/stable/guides/user/viewing_images.html

# Viewing Images¶

How to use other packages with pydicom to view DICOM images

## Introduction¶

*pydicom* is mainly concerned with getting at the DICOM data elements in files,
but it is often desirable to view pixel data as an image.
There are several options:

Use any of the many DICOM viewer programs available

use pydicom with matplotlib

use pydicom with Python’s stdlib Tkinter module.

use pydicom with Pillow

use pydicom with wxPython

## Using pydicom with matplotlib¶

matplotlib can be used with the `numpy.ndarray`

from
`Dataset.pixel_array`

to display it:

```
>>> import matplotlib.pyplot as plt
>>> from pydicom import examples
>>> ds = examples.ct
>>> plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
<matplotlib.image.AxesImage object at ...>
```

## Source: https://pydicom.github.io/pydicom/stable/guides/user/private_data_elements.html

# Private Data Elements¶

Accessing or creating private data elements

## Introduction¶

The DICOM standard allows DICOM file creators to use private data elements to store information that is not defined by the DICOM standard itself.

Private data elements are stored in a `Dataset`

just
like other data elements. When reading files with *pydicom*, they will automatically be read
and available for display. *pydicom* knows descriptive names for some
‘well-known’ private data elements, but for others it may not be able to
show anything except the tag and the value.

When writing your own private data elements, the DICOM standard requires the
use of ‘private creator blocks’. *pydicom* has some convenience
functions to make creating private blocks and data elements easier.

The sections below outlines accessing and creating private blocks and data
elements using *pydicom*.

## Displaying Private Data Elements in *pydicom*¶

Here is an example of some private tags displayed for *pydicom’s* example CT
dataset:

```
>>> from pydicom import examples
>>> ds = examples.ct
>>> ds
Dataset.file_meta -------------------------------
(0002, 0000) File Meta Information Group Length UL: 192
(0002, 0001) File Meta Information Version OB: b'\x00\x01'
(0002, 0002) Media Storage SOP Class UID UI: CT Image Storage
(0002, 0003) Media Storage SOP Instance UID UI: 1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322
(0002, 0010) Transfer Syntax UID UI: Explicit VR Little Endian
(0002, 0012) Implementation Class UID UI: 1.3.6.1.4.1.5962.2
(0002, 0013) Implementation Version Name SH: 'DCTOOL100'
(0002, 0016) Source Application Entity Title AE: 'CLUNIE1'
-------------------------------------------------
(0008, 0005) Specific Character Set CS: 'ISO_IR 100'
(0008, 0008) Image Type CS: ['ORIGINAL', 'PRIMARY', 'AXIAL']
...
(0009, 0010) Private Creator LO: 'GEMS_IDEN_01'
(0009, 1001) [Full fidelity] LO: 'GE_GENESIS_FF'
(0009, 1002) [Suite id] SH: 'CT01'
...
```

The last two lines in the example above show *pydicom’s* display of two private
data elements. The line preceding those shows the private creator data element
that reserves a section of tag element numbers for that creator’s use.

Since the descriptions for private data elements are not part of the DICOM
standard, and are thus not necessarily unique, *pydicom* does not allow you to
access data elements using those names. This is indicated by enclosing the
text in square brackets, to make it clear it is different from DICOM
standard descriptors.

You can still access the private data elements using the tag, remembering that
data elements access by tag number return a full `DataElement`

instance, and the value attribute is needed to get the value:

```
>>> ds[0x00091001].value
'GE_GENESIS_FF'
```

You can also create a `PrivateBlock`

instance and access elements
through it:

```
>>> block = ds.private_block(0x0009, 'GEMS_IDEN_01')
>>> block[0x01]
(0009, 1001) [Full fidelity] LO: 'GE_GENESIS_FF'
>>> block[0x01].value
'GE_GENESIS_FF'
```

Using the private block like this is even more useful when creating your own private data elements, as shown in the next section.

## Setting Private Data Elements with *pydicom*¶

The DICOM standard requires a private creator data element to identify and
reserve a section of private tags. That name should be unique, and usually
has the company name as the first part to accomplish that. *pydicom* provides
convenience functions to manage this:

```
>>> block = ds.private_block(0x000b, "My company 001", create=True)
>>> block.add_new(0x01, "SH", "my value")
>>> ds
...
(000b, 0010) Private Creator LO: 'My company 001'
(000b, 1001) Private tag data SH: 'my value'
...
```

Standard Python operations like `in`

and `del`

can also be used when working
with block object:

```
>>> 0x01 in block
True
>>> 0x02 in block
False
>>> del block[0x01]
>>> 0x01 in block
False
```

Since v3.0, there’s also a convenience method to add a private tag without creating a private block first:

```
>>> block = ds.add_new_private("My company 001", 0x000B, 0x01, "my value", VR.SH)
>>> ds
...
(000b, 0010) Private Creator LO: 'My company 001'
(000b, 1001) Private tag data SH: 'my value'
...
```

Note that for known private tags you don’t need to provide the VR in this function.

## Removing All Private Data Elements¶

One part of anonymizing a DICOM file is to ensure that private data elements
have been removed, as there is no guarantee as to what kind of information
might be contained in them. *pydicom* provides a convenience function
`Dataset.remove_private_tags()`

to recursively remove private elements:

```
>>> ds.remove_private_tags()
```

This can also be helpful during interactive sessions when exploring DICOM files, to remove a large number of lines from the display of a dataset – lines which may not provide useful information.

## Adding new entries to the DICOM dictionary¶

*pydicom* contains a dictionary with all known DICOM tags from the latest DICOM standard
at release time. It also contains a dictionary with a number of known private tags
collected from various sources.
Sometimes you may encounter tags unknown to *pydicom* - either tags defined in a newer version
of the standard, or, the more common case, private tags that are not contained
in the private tags dictionary.

In this case, you can add these tags to the DICOM dictionary before reading or writing datasets
containing these tags. After that, *pydicom* will correctly handle the type of these tags, and
can display their description if needed.

For standard tags, you can use `add_dict_entry()`

or
`add_dict_entries()`

(to add multiple tags at once):

```
>>> add_dict_entry(tag=0x888800001, VR="SH", keyword="SomeNewTag", description="Some New Tag")
```

For private tags, the analogous functions are
`add_private_dict_entry()`

and `add_private_dict_entries()`

:

```
>>> add_private_dict_entry(private_creator="ACME 1.1", tag=0x004100001, VR="DA", description="Release Date")
```

Note that private tags do not have a keyword, as they are not registered in the standard DICOM data dictionary. As a private tag is defined by the tuple of private creator, group ID and tag offset, you always have to provide the private creator to define a new private tag.

An example of how to use `add_private_dict_entries()`

can
be found in this code snippet.

## Source: https://pydicom.github.io/pydicom/stable/guides/user/best_practices.html

# Best Practices¶

Future-proof your code, and help ensure valid DICOM

## Introduction¶

There are some features of *pydicom* that allow you to help check your code
for more strict DICOM practices, and to future-proof against major
*pydicom* version changes.

It is recommended that you turn on two features if you can:
enforcement of valid DICOM, and a flag to enable “future” *pydicom* changes.

## Enforcing Valid DICOM¶

*pydicom* has configuration options to help enforce valid DICOM:
`reading_validation_mode`

and
`writing_validation_mode`

.
The first setting is about validation of values read from existing DICOM data,
the second about validation of newly created and written values.

Both can have the values `IGNORE`

,
`WARN`

and `RAISE`

.

As the name suggests, some non-standard DICOM datasets may result in a warning
(this is the default for `reading_validation_mode`

) or in a raised exception
(the default for `writing_validation_mode`

). If `IGNORE`

is set, the validation
is not performed in most cases. This setting may be used in some special
cases where you want to avoid the validation.

The setting for `writing_validation_mode`

may be changed for some cases,
where writing invalid DICOM is needed to support some legacy software, but
this is generally not recommended.

The default setting for `reading_validation_mode`

allows you to deal with files
that do not strictly adhere to the DICOM Standard. Setting it to
`RAISE`

can help to ensure that only valid DICOM data is accepted.

These flags do not guarantee strict DICOM results, as not all of the possible validations from the DICOM Standard are checked. Included are checks for correct value length, contained character set and for predefined formats where applicable (such as for date/time related values).

To change a flag in your code:

```
from pydicom import config
config.settings.reading_validation_mode = config.RAISE
```

Note that you *must not* use
`from pydicom.config.settings import reading_validation_mode`

.
That makes the `reading_validation_mode`

variable local only to that module,
so *pydicom* would not see your change to its value.

## Future-proofing your code¶

*pydicom*, like all software, must balance its evolution with not breaking
existing code using the library. Sometimes, major changes are necessary
to make significant improvements to the library.

To help you protect your code against future changes, *pydicom* allows you
to flag that it should behave as it will for any known upcoming
major changes.

Running your code with this turned on will help identify any parts of
your code that are not compatible with the known changes in the next major
version of *pydicom*.

The simplest way to set this behavior is to set an environment variable
`PYDICOM_FUTURE`

to `True`

. For example to temporarily turn it on in the
current terminal session:

```
SET PYDICOM_FUTURE=True (Windows)
export PYDICOM_FUTURE=True (many linux environments)
```

If you wish to turn off the behavior, you can either remove the environment variable, or set it to “False”. See your operating system documentation for more details on setting or removing environment variables.

The other way to enable the future behavior is to turn it on at run-time
using the `future_behavior()`

function:

```
from pydicom import config
config.future_behavior()
```

If you needed to turn the future behavior off again at run-time, call
`future_behavior()`

with False:

```
config.future_behavior(False)
```

## Limiting the *pydicom* major version in your package¶

Another way to avoid breaking changes in future *pydicom* versions is to
limit the version of *pydicom* that your code uses.

If you follow standard Python packaging recommendations, you can add a line
to your `requirements.txt`

or `pyproject.toml`

file to limit the *pydicom*
version to the current major version. E.g. a line like:

```
pydicom >=2.0,<3.0
```

in the `requirements.txt`

file will ensure that those installing your package
will get the same major version (in the example, version 2) of *pydicom*
that you have developed the code for. This works best if your package is
installed in a virtual environment.

## Source: https://pydicom.github.io/pydicom/stable/guides/decoding/index.html

pydicom
Getting started
How to install pydicom
Documentation
pydicom User Guide
Tutorials
Guides
pydicom User Guide
Element VRs and Python types
Plugins for Pixel Data Compression and Decompression
Pixel Data Decoding
Pixel Data Decoder Options
Pixel Data Decoder Plugins
Pixel Data Encoding
Command-line Interface Guide
Glossary
Writing documentation
API Reference
Examples
General examples
Image processing
Input-output
Metadata processing
Additional Information
Contributing to pydicom
Frequently asked questions
Release notes
pydicom
Guides
Pixel Data Decoding
Pixel Data Decoding
¶
Decoding plugin information:
Pixel Data Decoder Options
Pixel Data Decoder Plugins

## Source: https://pydicom.github.io/pydicom/stable/guides/encoding/index.html

Getting started

Documentation

Examples

Additional Information

Transfer Syntax UID specific encoding information:

Encoding plugin information:

## Source: https://pydicom.github.io/pydicom/stable/guides/cli/cli_guide.html

pydicom command-line interface

# Command-line Interface Guide¶

Added in version 2.2.

## Introduction¶

Starting in v2.2, *pydicom* offers a useful command-line interface (CLI) for
exploring DICOM files, and access to the codify option for creating pydicom
Python code. Additional subcommands may be added over time.

Example at the command line in a terminal window:

```
$ pydicom show pydicom::rtplan.dcm
Dataset.file_meta -------------------------------
(0002, 0000) File Meta Information Group Length UL: 156
(0002, 0001) File Meta Information Version OB: b'\x00\x01'
(0002, 0002) Media Storage SOP Class UID UI: RT Plan Storage
(0002, 0003) Media Storage SOP Instance UID UI: 1.2.999.999.99.9.9999.9999.20030903150023
(0002, 0010) Transfer Syntax UID UI: Implicit VR Little Endian
(0002, 0012) Implementation Class UID UI: 1.2.888.888.88.8.8.8
-------------------------------------------------
(0008, 0012) Instance Creation Date DA: '20030903'
(0008, 0013) Instance Creation Time TM: '150031'
(0008, 0016) SOP Class UID UI: RT Plan Storage
(0008, 0018) SOP Instance UID UI: 1.2.777.777.77.7.7777.7777.20030903150023
(0008, 0020) Study Date DA: '20030716'
...
```

Note that prefixing the file specification with `pydicom::`

will read the file
from the *pydicom* test data files rather than from the normal file system.
The following examples will use that so that you can replicate these
examples exactly. In normal use, you would leave the `pydicom::`

prefix
off when working with your files.

You can also show just parts of the DICOM file by specifying a data element
using the usual *pydicom* keyword notation:

```
$ pydicom show pydicom::rtplan.dcm::FractionGroupSequence[0]
(300a, 0071) Fraction Group Number IS: "1"
(300a, 0078) Number of Fractions Planned IS: "30"
(300a, 0080) Number of Beams IS: "1"
(300a, 00a0) Number of Brachy Application Setups IS: "0"
(300c, 0004) Referenced Beam Sequence 1 item(s) ----
(300a, 0082) Beam Dose Specification Point DS: [239.531250000000, 239.531250000000, -751.87000000000]
(300a, 0084) Beam Dose DS: "1.0275401"
(300a, 0086) Beam Meterset DS: "116.0036697"
(300c, 0006) Referenced Beam Number IS: "1"
---------
```

You can see the available subcommands by simply typing `pydicom`

with no
arguments, or with `pydicom help`

:

```
$ pydicom help
Use pydicom help [subcommand] to show help for a subcommand
Available subcommands: codify, show
```

And, as noted in the block above, you get help for a particular subcommand
by typing `pydicom help [subcommand]`

. For example:

```
$ pydicom help show
usage: pydicom show [-h] [-x] [-t] [-q] filespec
Display all or part of a DICOM file
positional arguments:
filespec File specification, in format [pydicom::]filename[::element]. If `pydicom::`
prefix is used, then show the pydicom test file with that name. If `element`
is given, use only that data element within the file. Examples:
path/to/your_file.dcm, your_file.dcm::StudyDate,
pydicom::rtplan.dcm::BeamSequence[0], yourplan.dcm::BeamSequence[0].BeamNumber
optional arguments:
-h, --help show this help message and exit
-x, --exclude-private
Don't show private data elements
-t, --top Only show top level
-q, --quiet Only show basic information
```

### Installing the pydicom CLI¶

The `pydicom`

command should automatically be available after you
path or environment variables.

If you are helping develop *pydicom* code, and are using git clones,

or `python setup.py develop`

from
the pydicom repository root. This has to be repeated for any changes to
setup.py (e.g. to add a new subcommand).

If you are developing subcommands within your own package, you will need to reinstall your package similar to the above as you add entry points.

### Combining with other CLIs¶

CLIs are useful for general exploration while programming, but also can be combined with other command-line filters for additional functionality. The following is an example of piping the output of the pydicom ‘show’ subcommand into ‘grep’, filtering for lines with either “Dose” or “Sequence” in them:

```
$ pydicom show pydicom::rtplan.dcm | grep "Dose\|Sequence"
(300a, 0010) Dose Reference Sequence 2 item(s) ----
(300a, 0012) Dose Reference Number IS: "1"
(300a, 0014) Dose Reference Structure Type CS: 'COORDINATES'
(300a, 0016) Dose Reference Description LO: 'iso'
(300a, 0018) Dose Reference Point Coordinates DS: [239.531250000000, 239.531250000000, -741.87000000000]
(300a, 0020) Dose Reference Type CS: 'ORGAN_AT_RISK'
(300a, 0023) Delivery Maximum Dose DS: "75.0"
(300a, 002c) Organ at Risk Maximum Dose DS: "75.0"
(300a, 0012) Dose Reference Number IS: "2"
(300a, 0014) Dose Reference Structure Type CS: 'COORDINATES'
(300a, 0016) Dose Reference Description LO: 'PTV'
(300a, 0018) Dose Reference Point Coordinates DS: [239.531250000000, 239.531250000000, -751.87000000000]
(300a, 0020) Dose Reference Type CS: 'TARGET'
(300a, 0026) Target Prescription Dose DS: "30.826203"
(300a, 0070) Fraction Group Sequence 1 item(s) ----
(300c, 0004) Referenced Beam Sequence 1 item(s) ----
(300a, 0082) Beam Dose Specification Point DS: [239.531250000000, 239.531250000000, -751.87000000000]
(300a, 0084) Beam Dose DS: "1.0275401"
(300a, 00b0) Beam Sequence 1 item(s) ----
(300a, 00b6) Beam Limiting Device Sequence 2 item(s) ----
(300a, 0111) Control Point Sequence 2 item(s) ----
(300a, 0115) Dose Rate Set DS: "650.0"
(300a, 011a) Beam Limiting Device Position Sequence 2 item(s) ----
(300c, 0050) Referenced Dose Reference Sequence 2 item(s) ----
(300a, 010c) Cumulative Dose Reference Coefficie DS: "0.0"
(300c, 0051) Referenced Dose Reference Number IS: "1"
(300a, 010c) Cumulative Dose Reference Coefficie DS: "0.0"
(300c, 0051) Referenced Dose Reference Number IS: "2"
(300c, 0050) Referenced Dose Reference Sequence 2 item(s) ----
(300a, 010c) Cumulative Dose Reference Coefficie DS: "0.9990268"
(300c, 0051) Referenced Dose Reference Number IS: "1"
(300a, 010c) Cumulative Dose Reference Coefficie DS: "1.0"
(300c, 0051) Referenced Dose Reference Number IS: "2"
(300a, 0180) Patient Setup Sequence 1 item(s) ----
(300c, 0002) Referenced RT Plan Sequence 1 item(s) ----
(300c, 0060) Referenced Structure Set Sequence 1 item(s) ----
```

Using the “or Sequence” (``\|Sequence``

) regular expression as above allows you
to see any filtered results in relation to their parent Sequences.

See the pydicom show command section for more examples of the show command, its options, and the ability to show only data elements or sequences within the file.

`pydicom show`

command¶

The pydicom show command displays representation of DICOM files or parts of them from a command-line terminal.

Some examples were already given in the Introduction, but here we will show some additional options.

To see the available options, in a command-line terminal, type `pydicom help show`

or `pydicom show -h`

.

```
$ pydicom help show
usage: pydicom show [-h] [-x] [-t] [-q] filespec
Display all or part of a DICOM file
positional arguments:
filespec File specification, in format [pydicom::]filename[::element]. If `pydicom::`
prefix is present, then use the pydicom test file with that name. If `element`
is given, use only that data element within the file. Examples:
path/to/your_file.dcm, your_file.dcm::StudyDate,
pydicom::rtplan.dcm::BeamSequence[0], yourplan.dcm::BeamSequence[0].BeamNumber
optional arguments:
-h, --help show this help message and exit
-x, --exclude-private
Don't show private data elements
-t, --top Only show top level
-q, --quiet Only show basic information
```

The basic command with no options shows all data elements and nested sequences:

```
$ pydicom show pydicom::CT_small.dcm
Dataset.file_meta -------------------------------
(0002, 0000) File Meta Information Group Length UL: 192
(0002, 0001) File Meta Information Version OB: b'\x00\x01'
(0002, 0002) Media Storage SOP Class UID UI: CT Image Storage
(0002, 0003) Media Storage SOP Instance UID UI: 1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322
(0002, 0010) Transfer Syntax UID UI: Explicit VR Little Endian
(0002, 0012) Implementation Class UID UI: 1.3.6.1.4.1.5962.2
(0002, 0013) Implementation Version Name SH: 'DCTOOL100'
(0002, 0016) Source Application Entity Title AE: 'CLUNIE1'
-------------------------------------------------
(0008, 0005) Specific Character Set CS: 'ISO_IR 100'
(0008, 0008) Image Type CS: ['ORIGINAL', 'PRIMARY', 'AXIAL']
(0008, 0012) Instance Creation Date DA: '20040119'
(0008, 0013) Instance Creation Time TM: '072731'
(0008, 0014) Instance Creator UID UI: 1.3.6.1.4.1.5962.3
(0008, 0016) SOP Class UID UI: CT Image Storage
(0008, 0018) SOP Instance UID UI: 1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322
(0008, 0020) Study Date DA: '20040119'
.
.
.
(0043, 104b) [DAS xm pattern] SL: 0
(0043, 104c) [TGGC trigger mode] SS: 0
(0043, 104d) [Start scan to X-ray on delay] FL: 0.0
(0043, 104e) [Duration of X-ray on] FL: 10.60060977935791
(7fe0, 0010) Pixel Data OW: Array of 32768 elements
(fffc, fffc) Data Set Trailing Padding OB: Array of 126 elements
```

Note that prefixing the file specification with `pydicom::`

will read the file
from the *pydicom* test data files rather than from the file system.

You can also show just parts of the DICOM file by specifying a data element using the usual pydicom keyword notation:

```
$ pydicom show pydicom::CT_small.dcm::PatientName
CompressedSamples^CT1
$ pydicom show pydicom::rtplan.dcm::FractionGroupSequence
[(300a, 0071) Fraction Group Number IS: "1"
(300a, 0078) Number of Fractions Planned IS: "30"
(300a, 0080) Number of Beams IS: "1"
(300a, 00a0) Number of Brachy Application Setups IS: "0"
(300c, 0004) Referenced Beam Sequence 1 item(s) ----
(300a, 0082) Beam Dose Specification Point DS: [239.531250000000, 239.531250000000, -751.87000000000]
(300a, 0084) Beam Dose DS: "1.0275401"
(300a, 0086) Beam Meterset DS: "116.0036697"
(300c, 0006) Referenced Beam Number IS: "1"
---------]
```

The `-q`

quiet argument shows a minimal version of some of the information in the
file, using just the DICOM keyword and value (not showing the tag numbers
and VR). The example below shows the quiet mode with an image slice:

```
pydicom show -q pydicom::ct_small.dcm
SOPClassUID: CT Image Storage
PatientName: CompressedSamples^CT1
PatientID: 1CT1
StudyID: 1CT1
StudyDate: 20040119
StudyTime: 072730
StudyDescription: e+1
BitsStored: 16
Modality: CT
Rows: 128
Columns: 128
SliceLocation: -77.2040634155
```

And the following example shows an RT Plan in quiet mode:

```
pydicom show -q pydicom::rtplan.dcm
SOPClassUID: RT Plan Storage
PatientName: Last^First^mid^pre
PatientID: id00001
StudyID: study1
StudyDate: 20030716
StudyTime: 153557
StudyDescription: N/A
Plan Label: Plan1 Plan Name: Plan1
Fraction Group 1 30 fraction(s) planned
Brachy Application Setups: 0
Beam 1 Dose 1.02754010000000 Meterset 116.003669700000
Beam 1 'Field 1' TREATMENT STATIC PHOTON energy 6.00000000000000 gantry 0.0, coll 0.0, couch 0.0 (0 wedges, 0 comps, 0 boli, 0 blocks)
```

Quiet modes always show the SOP Class UID, patient and study information as
shown in the above two examples. After those elements, custom values for
different SOP classes are shown. Currently “Image Storage” and “RT Plan Storage”
classes have custom extra information. Please submit an issue on the *pydicom*
issues list or a pull request to help us expand the list of custom
‘quiet’ mode SOP Classes.

`pydicom codify`

command¶

The `pydicom codify`

command takes a DICOM file and produces Python code to
recreate that file, or, optionally a subset within that file.

See Using codify for full details of writing a complete file. Here we will review the command-line options in more detail than in that section, and show how to export a dataset within a DICOM file that has sequences.

Warning

The code produced by `codify`

will contain all the information in the original
file, which may include private health information or other sensitive
information.

### A simple example¶

A simple example of using the `codify`

command would be:

```
$ pydicom codify pydicom::rtplan.dcm
# Coded version of DICOM file 'C:\git\pydicom\pydicom\data\test_files\rtplan.dcm'
# Produced by pydicom codify utility script
import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.sequence import Sequence
# Main data elements
ds = Dataset()
ds.InstanceCreationDate = '20030903'
ds.InstanceCreationTime = '150031'
ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.481.5'
ds.SOPInstanceUID = '1.2.777.777.77.7.7777.7777.20030903150023'
ds.StudyDate = '20030716'
ds.StudyTime = '153557'
.
.
.
```

Note that prefixing the file specification with `pydicom::`

will read the file
from the *pydicom* test data files rather than from the file system.

### Command options¶

In the above example, the output was directed to screen, because no output file
was specified. To see the available command options, use the `help`

command:

```
pydicom help codify
usage: pydicom codify [-h] [-e EXCLUDE_SIZE] [-p] [-s SAVE_AS] filespec [outfile]
Read a DICOM file and produce the *pydicom* (Python) code which can create that file
positional arguments:
filespec File specification, in format [pydicom::]filename[::element]. If `pydicom::`
prefix is used, then use the pydicom test file with that name. If `element`
is given, use only that data element within the file. Examples:
path/to/your_file.dcm, your_file.dcm::StudyDate,
pydicom::rtplan.dcm::BeamSequence[0],
yourplan.dcm::BeamSequence[0].BeamNumber
outfile Filename to write python code to. If not specified, code is written to
stdout
optional arguments:
-h, --help show this help message and exit
-e EXCLUDE_SIZE, --exclude-size EXCLUDE_SIZE
Exclude binary data larger than specified (bytes). Default is 100 bytes
-p, --include-private
Include private data elements (default is to exclude them)
-s SAVE_AS, --save-as SAVE_AS
Specify the filename for ds.save_as(save_filename); otherwise the input name
+ '_from_codify' will be used
Binary data (e.g. pixels) larger than --exclude-size (default 100 bytes) is not included. A dummy
line with a syntax error is produced. Private data elements are not included by default.
```

For example:

```
pydicom codify -s savename.dcm dicomfile.dcm pythoncode.py
```

would read the DICOM file “dicomfile.dcm” and write the Python code
to file “pythoncode.py”. In that code, near the end of the file
would be a `ds.save_as("savename.dcm", ...)`

line.

Note

By default, any private data elements within the file are not translated
to code. If you want to include them, use the `-p`

parameter.

### Codifying a part of a DICOM file¶

Note that the `filespec`

argument to the `codify`

command, as for
the show command, allows you to specify a data element within the file,
rather than the whole file:

```
pydicom codify pydicom::rtplan.dcm::FractionGroupSequence[0]
# Coded version of non-file dataset
...
# Main data elements
ds = Dataset()
ds.FractionGroupNumber = "1"
ds.NumberOfFractionsPlanned = "30"
ds.NumberOfBeams = "1"
ds.NumberOfBrachyApplicationSetups = "0"
# Referenced Beam Sequence
refd_beam_sequence = Sequence()
ds.ReferencedBeamSequence = refd_beam_sequence
# Referenced Beam Sequence: Referenced Beam 1
refd_beam1 = Dataset()
refd_beam1.BeamDoseSpecificationPoint = [239.531250000000, 239.531250000000, -751.87000000000]
...
```

Currently, only a data element which is a `Dataset`

(an item within a `Sequence`

) is accepted.
The resulting code would not on its own produce a correct DICOM file,
but could be useful as a model when creating
more complete code. For example, issuing code for one item in a
`Sequence`

could be the starting point towards a loop
producing a number of sequence items.

## Extending the CLI¶

Developers can create their own ‘subcommands’ for the `pydicom`

command,
by adding entry points to their package’s setup.py file, specifying a callback
function to register the subcommand and its arguments.

If you wanted to create two subcommands, ‘command1’ and ‘command2’, your setup.py file should include something like:

```
from setuptools import setup
if __name__ == '__main__':
setup(
name="yourpackage",
# various setup options...,
entry_points = {
"pydicom_subcommands": [
"command1 = yourpackage.command1module.add_subparser",
"command2 = yourpackage.command2module.add_subparser"
]
}
)
```

The `"pydicom_subcommands"`

is a literal string; this must not be
changed or *pydicom* will not find your subcommand.

The `add_subparser`

function name could be changed if you wish, but usually
would be used by convention, and is assumed in the following examples.

In the module you have specified, create the `add_subparser`

function,
which takes a single argument `subparsers`

, and a `do_command`

function,
which will take the call when you subcommand is actually used at the command
line:

```
from pydicom.cli.main import filespec_help, filespec_parser
def add_subparser(subparsers):
# Register the sub-parser
subparser = subparsers.add_parser(
"subcommandname",
description="Summary of your subcommand"
)
subparser.add_argument(
"filespec",
help=filespec_help,
type=filespec_parser
)
subparser.add_argument(
...
)
subparser.set_defaults(func=do_command)
```

And define your command function:

```
def do_command(args):
for ds, element_val in args.filespec:
if args.yourarg:
# Do something...
# work with the dataset ds or element as needed...
```

The `pydicom`

command uses Python’s
argparse library to
process commands.

The above code snippets show adding the `filespec`

argument, and processing
the resulting dataset-element_value pairs in the `do_command()`

function. This is
recommended if you wish to use the filespec as was seen in the pydicom show command
and pydicom codify command sections. If not, you can just create a normal
arg with the type set to `argparse.FileType`

to open files yourself.

The above has been shown in relation to a different package than *pydicom*;
however, if you think your command has general use, please consider contributing
it to *pydicom*: in that case, change the entry points in the *pydicom*
`setup.py`

script, and add a module under `pydicom.cli`

and create a
pull request.

## Source: https://pydicom.github.io/pydicom/stable/guides/glossary.html

# Glossary¶

## File Meta Information¶

**(0002,0010) Transfer Syntax UID**The

*Transfer Syntax UID*is a unique identifier that provides information on how a DICOM dataset has been encoded. All transfer syntaxes have two attributes that describe how the dataset’s encoded elements should be interpreted:Whether the dataset uses little-endian or big-endian byte ordering (retired),

Whether the dataset uses implicit or explicit VR encoding

In addition, transfer syntaxes can be grouped by how the dataset’s

*Pixel Data*has been encoded:**Encapsulated transfer syntaxes**: so-called because any*Pixel Data*present in the dataset is`encapsulated`

. All encapsulated transfer syntaxes have pixel data that’s been compressed using the compression technique specified by the transfer syntax. For example, a dataset with the*JPEG Baseline (Process 1)*transfer syntax will have pixel data that’s compressed using ISO/IEC 10918-1 JPEG compression.**Native (unencapsulated) transfer syntaxes**: these have no encapsulation, and hence no compression of the*Pixel Data*.

All encapsulated transfer syntaxes use explicit VR, little endian encoding, while native transfer syntaxes use the encoding matching their description: a dataset with the

*Implicit VR Little Endian*transfer syntax uses implicit VR, little endian encoding, for example.The DICOM Standard provides a list of public transfer syntaxes, however privately defined transfer syntaxes are also allowed.

References: DICOM Standard, Part 5, Section 10 and Annex A

## Image Pixel Module¶

**(0028,0002) Samples per Pixel**The number of samples per pixel, otherwise known as the number of image channels, components or planes. An RGB image has 3 samples per pixel (red, green and blue), a grayscale image has 1 sample per pixel (intensity). The

*Samples per Pixel*for all DICOM*Pixel Data*is either 1 or 3, however 4 was previously allowed.Allowed values:

`1`

or`3`

, but may be constrained by the IOD.Reference: DICOM Standard, Part 3, Section C.7.6.3.1.1

**(0028,0004) Photometric Interpretation**The intended interpretation of the

*Pixel Data*in its*current form*in the dataset. For example:If you have a dataset with RGB

*Pixel Data*then the*Photometric Interpretation*should be`'RGB'`

.If you take your RGB data and convert it to YCbCr then the

*Photometric Interpretation*should be`'YBR_FULL'`

(or a related interpretation depending on the conversion method).If you then compress that data using

*RLE Lossless*encoding then the*Photometric Interpretation*remains`'YBR_FULL'`

.On the other hand, if you take your original RGB data and apply

*JPEG 2000 Lossless*encoding then the*Photometric Interpretation*will either be`'RGB'`

or`'YBR_RCT'`

depending on whether or not the encoder performs a multi-component transformation when encoding.

When compressing pixel data using one of the JPEG encodings it’s important to know if the encoder is performing any color space transformation prior to compression, as this needs to be taken into account when setting the

*Photometric Interpretation*. This is especially important when an encoder performs a transformation and the decoder doesn’t, since having a correct*Photometric Interpretation*makes it possible to determine which inverse transformation to use to return the pixel data to its original color space.For more detailed information on each of the defined photometric interpretations refer to Annex C.7.6.3.1 of Part 3 of the DICOM Standard.

Allowed values:

`'MONOCHROME1'`

,`'MONOCHROME2'`

,`'PALETTE COLOR'`

,`'RGB'`

,`'YBR_FULL'`

,`'YBR_FULL_422'`

,`'YBR_PARTIAL_420'`

,`'YBR_ICT'`

,`'YBR_RCT'`

, however restrictions apply based on the*Transfer Syntax UID*, and further constraints may be required by the IOD.

**(0028,0006) Planar Configuration**Required when

*Samples per Pixel*is greater than one, this indicates the order of the samples used by the pixel data, as either:`0`

, where sample values for the first pixel is followed by the sample value for the second pixel: R1, G1, B1, R2, G2, B2, …, Rn, Gn, Bn.`1`

, where sample values for each color plane are contiguous: R1, R2, …, Rn, G1, G2, …, Gn, B1, B2, …, Bn.

Allowed values:

`0`

or`1`

Reference: DICOM Standard, Part 3, Section C.7.6.3.1.3

**(0028,0008) Number of Frames**The number of frames in a multi-frame image. May not be present if the pixel data only has a single frame.

Allowed values: must be at least

`1`

(if present)

**(0028,0010) Rows**The number of rows in the image.

Allowed values:

`1`

to`65535`

**(0028,0011) Columns**The number of columns in the image.

Allowed values:

`1`

to`65535`

**(0028,0100) Bits Allocated**The number of bits used to actually

*contain*each sample of each pixel. All DICOM*Pixel Data*is either 1 (for bit-packed*Pixel Data*) or more typically a multiple of 8 such as 8, 16 or 32, with 64 currently being the maximum used. Using the example of a*Bits Stored*of 12, this means that the actual number of bits used to contain the values must be at least 16.For more detailed information refer to Chapter 8 and Annex D in Part 5 of the DICOM Standard.

Allowed values:

`1`

or a multiple of`8`

, however many IODs place further restrictions on what the value may be.

**(0028,0101) Bits Stored**The number of bits actually

*used*by each sample of each pixel. For example, with a*Bits Stored*value of`12`

, an unsigned grayscale image will have pixel values in the range 0 to 4095 and an unsigned RGB image will have values in the range (R: 0 to 4095, G: 0 to 4095, B: 0 to 4095). Must be equal to or less than*Bits Allocated*.For more detailed information refer to Chapter 8 and Annex D in Part 5 of the DICOM Standard.

Allowed values:

`1`

to*Bits Allocated*(inclusive)

**(0028,0102) High Bit**The most significant bit of the pixel sample data and is equal to

*Bits Stored*- 1, however other values have been allowed in past versions of the DICOM Standard.Allowed values:

*Bits Stored*- 1

**(0028,0103) Pixel Representation**Describes the type of pixel values, either signed (using 2’s complement) or unsigned integers. A value of

`0`

indicates the*Pixel Data*contains unsigned integers while a value of`1`

indicates it contains signed integers.Allowed values:

`0`

or`1`

, but may be constrained by the IOD.

## Source: https://pydicom.github.io/pydicom/stable/guides/writing_documentation.html

# Writing documentation¶

## Types of documentation¶

**Tutorials**: take a reader unfamiliar with*pydicom*through a series of steps to achieve something useful**How-to/examples**: more advanced versions of tutorials, for readers that already have some understanding of how*pydicom*works**Guides**: aim to explain a subject at a fairly high level**Reference**: contain technical reference information for the*pydicom*API for a reader that has some familiarity with*pydicom*but needs to learn or be reminded about a specific part of it

## General style guidelines¶

**pydicom**- italicized lowercase:*pydicom***DICOM**,**DICOM Standard**- uppercase DICOM, and S on Standard**Python**- capitalize Python**itemize**, etc - use the American English spelling**(7FE0,0010) Pixel Data**- use uppercase hex, no space between the comma and element number, and italicize the element name, e.g. (7FE0,0010)*Pixel Data*. When referring to an element name by itself then use italics:*Bits Allocated***ds**,**elem**,**seq**,**arr**- when writing examples try to use`ds`

as the variable name for`Dataset`

,`elem`

for`DataElement`

,`seq`

for sequences and`arr`

for numpy arrays.**them**,**they**,**their**- use gender neutral pronouns when referring to a hypothetical personUse the double back-tick markup ``0xB4`` when referring to:

A Python built-in value such as

`True`

,`False`

,`None`

When referring to a value passed by a parameter: If fragments_per_frame is not

`1`

then…When writing a hex value

`0xB4`

When referring to a class, function, variable, etc and you haven’t used semantic markup:

`Dataset`

when not using`Dataset`

Use a single back-tick `italics` for parameter names: If fragments_per_frame is not…

For the API reference documentation, follow the NumPy docstring guide

## Guidelines for reStructuredText¶

In section titles, capitalize only initial words and proper nouns

Documentation should be wrapped at 80 characters unless there’s a good reason not to

Because Sphinx will automatically link to the corresponding API documentation, the more semantic markup you can add, the better. So this:

:attr:`Dataset.pixel_array<pydicom.dataset.Dataset.pixel_array>` returns a :class:`numpy.ndarray`

which produces: “

`Dataset.pixel_array`

returns a`numpy.ndarray`

”, is better than this:``Dataset.pixel_array`` returns a numpy ``ndarray``

which produces: “

`Dataset.pixel_array`

returns a numpy`ndarray`

”Targets can be prefixed with

**~**so that the last bit of the path gets used as the link title. So`:class:`~pydicom.dataset.Dataset``

will show as a`Dataset`

.Python and NumPy objects can also be referenced:

`:class:`float``

,`:class:`numpy.dtype``

Use

`:dcm:`

to link to the CHTML version of the DICOM Standard. For example,`:dcm:`this section<part05/sect_6.2.html>``

will link to this section of the Standard. The link target should be the part of the URL after`http://dicom.nema.org/medical/dicom/current/output/chtml/`

Use these heading styles:

=== One === Two === Three ----- Four ~~~~ Five ^^^^

Use

`.. note::`

and`.. warning::`

and similar boxes sparinglyNew features should be documented with

`.. versionadded:: X.Y`

at the top of the first section and changes to existing features with`..versionchanged:: X.Y`

at the bottom of the first section:.. versionchanged:: 1.4 The ``handler`` keyword argument was added
