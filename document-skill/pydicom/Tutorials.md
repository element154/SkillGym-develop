## Source: https://pydicom.github.io/pydicom/stable/tutorials/index.html

Getting started

Documentation

Examples

Additional Information

New to pydicom? Then these tutorials should get you up and running.

## Source: https://pydicom.github.io/pydicom/stable/tutorials/dataset_basics.html

# Dataset basics: read, access, modify, write¶

In this tutorial we’re going to cover the basics of using *pydicom*:

Reading a DICOM dataset from file

Viewing and accessing the contents of the dataset

Modifying the dataset by adding, changing and deleting elements

Writing our modifications back to file

If you haven’t installed *pydicom* yet, follow the instructions in our
installation guide.

## Getting the path to the example dataset¶

In the tutorial we’re going to be using one of the example DICOM datasets included with
*pydicom*: CT_small.dcm.
You can get the file path to the dataset by using the `get_path()`

function to return the path as a `pathlib.Path`

(your path may vary):

```
>>> from pydicom import examples
>>> path = examples.get_path("ct")
>>> path
PosixPath('/path/to/pydicom/data/test_files/CT_small.dcm')
```

## Reading¶

To read the DICOM dataset at a given file path (as a `str`

or `pathlib.Path`

)
we use `dcmread()`

, which returns a
`FileDataset`

instance:

```
>>> from pydicom import dcmread, examples
>>> path = get_path("ct")
>>> ds = dcmread(path)
```

`dcmread()`

can also handle file-likes:

```
>>> with open(path, 'rb') as infile:
... ds = dcmread(infile)
```

And can even be used as a context manager:

```
>>> with dcmread(path) as ds:
... type(ds)
...
<class 'pydicom.dataset.FileDataset'>
```

By default, `dcmread()`

will read any DICOM dataset
stored in accordance with the DICOM File Format.
However, occasionally you may try to read a file that gives you the following
exception:

```
>>> no_meta_path = examples.get_path('no_meta')
>>> ds = dcmread(no_meta_path)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File ".../pydicom/filereader.py", line 887, in dcmread
force=force, specific_tags=specific_tags)
File ".../pydicom/filereader.py", line 678, in read_partial
preamble = read_preamble(fileobj, force)
File ".../pydicom/filereader.py", line 631, in read_preamble
raise InvalidDicomError("File is missing DICOM File Meta Information "
pydicom.errors.InvalidDicomError: File is missing DICOM File Meta Information header or the 'DICM' prefix is missing from the header. Use force=True to force reading.
```

This indicates that either:

The file isn’t a DICOM file, or

The file isn’t in the DICOM File Format but contains DICOM data

If you’re sure that the file contains DICOM data then you can use the force keyword parameter to force reading:

```
>>> ds = dcmread(no_meta_path, force=True)
```

A note of caution about using `force=True`

; because *pydicom* uses a
deferred-read system, **no exceptions** will be raised at the time of reading,
no matter what the contents of the file are:

```
>>> with open('not_dicom.txt', 'w') as not_dicom:
... not_dicom.write('This is not a DICOM file!')
>>> ds = dcmread('not_dicom.txt', force=True)
```

You’ll only run into problems when trying to use the dataset:

```
>>> print(ds)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "../pydicom/dataset.py", line 1703, in __str__
return self._pretty_str()
File "../pydicom/dataset.py", line 1436, in _pretty_str
for data_element in self:
File "../pydicom/dataset.py", line 1079, in __iter__
yield self[tag]
File "../pydicom/dataset.py", line 833, in __getitem__
self[tag] = DataElement_from_raw(data_elem, character_set)
File "../pydicom/dataelem.py", line 581, in DataElement_from_raw
raise KeyError(msg)
KeyError: "Unknown DICOM tag (6854, 7369) can't look up VR"
```

## Viewing and accessing¶

The `CT_small.dcm`

dataset is also included as an example dataset:

```
>>> from pydicom import examples
>>> ds = examples.ct
>>> type(ds)
<class 'pydicom.dataset.FileDataset'>
```

You can view the contents of the entire dataset by using `print()`

:

```
>>> print(ds)
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
...
(0010, 1002) Other Patient IDs Sequence 2 item(s) ----
(0010, 0020) Patient ID LO: 'ABCD1234'
(0010, 0022) Type of Patient ID CS: 'TEXT'
---------
(0010, 0020) Patient ID LO: '1234ABCD'
(0010, 0022) Type of Patient ID CS: 'TEXT'
---------
...
(0043, 104e) [Duration of X-ray on] FL: 10.60060977935791
(7fe0, 0010) Pixel Data OW: Array of 32768 elements
(fffc, fffc) Data Set Trailing Padding OB: Array of 126 elements
```

The print output shows a list of the data elements (or *elements* for short) present in the
dataset, one element per line. The format of each line is:

**(0008, 0005)**: The element’s tag, as (group number, element number) in hexadecimal**Specific Character Set**: the element’s name, if known**CS**: The element’s Value Representation (VR), if known**‘ISO_IR_100’**: the element’s stored value

### Elements¶

There are three categories of elements:

**Standard elements**such as (0008,0016)*SOP Class UID*. These elements are registered in the official DICOM Standard, have an even group number and are unique at each level of the dataset.**Repeating group elements**such as (60xx,3000)*Overlay Data*(not found in this dataset). Repeating group elements are also registered in the official DICOM Standard, however they have a group number defined over a range rather than a fixed value. For example, there may be multiple*Overlay Data*elements at a given level of the dataset as long as each has its own unique group number;`0x6000`

,`0x6002`

,`0x6004`

, or any even value up to`0x601E`

.**Private elements**such as (0043,104E)*[Duration of X-ray on]*. Private elements have an odd group number, aren’t registered in the official DICOM Standard, and are instead created privately, as specified by the (gggg,0010)*Private Creator*element.If the private creator is unknown then the element name will be

*Private tag data*and the VR**UN**.If the private creator is known then the element name will be surrounded by square brackets, e.g.

*[Duration of X-ray on]*and the VR will be as shown.

For all element categories, we can access a particular element in the dataset
through its tag, which returns a `DataElement`

instance:

```
>>> elem = ds[0x0008, 0x0016]
>>> elem
(0008, 0016) SOP Class UID UI: CT Image Storage
>>> elem.keyword
'SOPClassUID'
>>> private_elem = ds[0x0043, 0x104E]
>>> private_elem
(0043, 104e) [Duration of X-ray on] FL: 10.60060977935791
>>> private_elem.keyword
''
```

We can also access standard elements through their *keyword*. The keyword is
usually the same as the element’s name without any spaces, but there are
exceptions - such as (0010,0010) *Patient’s Name* having a keyword of
*PatientName*. A list of keywords for all standard elements can be found
here.

```
>>> elem = ds['SOPClassUID']
>>> elem
(0008, 0016) SOP Class UID UI: CT Image Storage
```

Because of the lack of a unique keyword, this won’t work for private or
repeating group elements. So for those elements stick to the
`Dataset[group number, element number]`

method.

In most cases, the important thing about an element is its value:

```
>>> elem.value
'1.2.840.10008.5.1.4.1.1.2'
```

For standard elements, you can use the Python dot notation with the keyword to get the value:

```
>>> ds.SOPClassUID
'1.2.840.10008.5.1.4.1.1.2'
```

This is the recommended method of accessing the value of standard elements. It’s simpler and more human-friendly then dealing with element tags and later on you’ll see how you can use the keyword to do more than accessing the value.

Elements may also be multi-valued (have a Value Multiplicity (VM) > 1):

```
>>> ds.ImageType
['ORIGINAL', 'PRIMARY', 'AXIAL']
>>> ds['ImageType'].VM
3
```

The items for multi-valued elements can be accessed using the standard Python
`list`

methods:

```
>>> ds.ImageType[1]
'PRIMARY'
```

### Sequences¶

When viewing a dataset, you may see that some of the elements are indented:

```
>>> print(ds)
...
(0010, 1002) Other Patient IDs Sequence 2 item(s) ----
(0010, 0020) Patient ID LO: 'ABCD1234'
(0010, 0022) Type of Patient ID CS: 'TEXT'
---------
(0010, 0020) Patient ID LO: '1234ABCD'
(0010, 0022) Type of Patient ID CS: 'TEXT'
---------
...
```

This indicates that those elements are part of a sequence, in this case
part of the *Other Patient IDs Sequence* element. Sequence elements have a
VR of **SQ** and they usually have the word *Sequence* in their name.
DICOM datasets use the tree data structure, with non-sequence
elements acting as leaves and sequence elements acting as the nodes where
branches start.

The top-level (root) dataset contains 0 or more elements (leaves):

An element may be non-sequence type (VR is not

**SQ**), orAn element may be a sequence type (VR is

**SQ**), contains 0 or more items (branches):Each item in the sequence is another dataset, containing 0 or more elements:

An element may be non-sequence type, or

An element may be a sequence type, and so on…

Sequence elements can be accessed in the same manner as non-sequence ones:

```
>>> seq = ds[0x0010, 0x1002]
>>> seq = ds['OtherPatientIDsSequence']
```

The main difference between sequence and non-sequence elements is that their
value is a list of zero or more `Dataset`

objects,
which can be accessed using the standard Python `list`

methods:

```
>>> len(ds.OtherPatientIDsSequence)
2
>>> type(ds.OtherPatientIDsSequence[0])
<class 'pydicom.dataset.Dataset'>
>>> ds.OtherPatientIDsSequence[0]
(0010, 0020) Patient ID LO: 'ABCD1234'
(0010, 0022) Type of Patient ID CS: 'TEXT'
>>> ds.OtherPatientIDsSequence[1]
(0010, 0020) Patient ID LO: '1234ABCD'
(0010, 0022) Type of Patient ID CS: 'TEXT'
```

### file_meta¶

Earlier we saw that by default `dcmread()`

only reads
files that are in the DICOM File Format. So what’s the difference between a
DICOM dataset written to file and one written in the DICOM File Format?
The answer is a file header containing:

An 128 byte preamble:

>>> ds.preamble b'II*\x00T\x18\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00...

Followed by a 4 byte

`DICM`

prefixFollowed by the required DICOM File Meta Information elements, which in

*pydicom*are stored in a`FileMetaDataset`

instance in the`file_meta`

attribute:>>> ds.file_meta (0002, 0000) File Meta Information Group Length UL: 192 (0002, 0001) File Meta Information Version OB: b'\x00\x01' (0002, 0002) Media Storage SOP Class UID UI: CT Image Storage (0002, 0003) Media Storage SOP Instance UID UI: 1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322 (0002, 0010) Transfer Syntax UID UI: Explicit VR Little Endian (0002, 0012) Implementation Class UID UI: 1.3.6.1.4.1.5962.2 (0002, 0013) Implementation Version Name SH: 'DCTOOL100' (0002, 0016) Source Application Entity Title AE: 'CLUNIE1'

As you can see, all the elements in the `file_meta`

are group `0x0002`

. In
fact, the DICOM File Format header is the only place you should find group
`0x0002`

elements as their presence anywhere else is non-conformant.

Out of all of the elements in the `file_meta`

, the most important is
(0002,0010) *Transfer Syntax UID*, as the transfer syntax defines the way the
entire dataset (including the pixel data) has been encoded. Chances are
that at some point you’ll need to know it:

```
>>> ds.file_meta.TransferSyntaxUID
'1.2.840.10008.1.2.1'
>>> ds.file_meta.TransferSyntaxUID.name
'Explicit VR Little Endian'
```

## Modifying¶

### Modifying elements¶

We can modify the value of any element by retrieving it and setting the value:

```
>>> elem = ds[0x0010, 0x0010]
>>> elem.value
'CompressedSamples^CT1'
>>> elem.value = 'Citizen^Jan'
>>> elem
(0010, 0010) Patient's Name PN: 'Citizen^Jan'
```

But for standard elements it’s simpler to use the keyword:

```
>>> ds.PatientName = 'Citizen^Snips'
>>> elem
(0010, 0010) Patient's Name PN: 'Citizen^Snips'
```

Multi-valued elements can be set using a `list`

or modified using the
`list`

methods:

```
>>> ds.ImageType = ['ORIGINAL', 'PRIMARY', 'LOCALIZER']
>>> ds.ImageType
['ORIGINAL', 'PRIMARY', 'LOCALIZER']
>>> ds.ImageType[1] = 'DERIVED'
>>> ds.ImageType
['ORIGINAL', 'DERIVED', 'LOCALIZER']
>>> ds.ImageType.insert(1, 'PRIMARY')
>>> ds.ImageType
['ORIGINAL', 'PRIMARY', 'DERIVED', 'LOCALIZER']
```

Similarly, for sequence elements:

```
>>> from pydicom.dataset import Dataset
>>> ds.OtherPatientIDsSequence = [Dataset(), Dataset()]
>>> ds.OtherPatientIDsSequence.append(Dataset())
>>> len(ds.OtherPatientIDsSequence)
3
```

As mentioned before, the items in a sequence are
`Dataset`

instances. If you try to add any other type
to a sequence you’ll get an exception:

```
>>> ds.OtherPatientIDsSequence.append('Hello world?')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File ".../pydicom/multival.py", line 63, in append
self._list.append(self.type_constructor(val))
File ".../pydicom/sequence.py", line 15, in validate_dataset
raise TypeError('Sequence contents must be Dataset instances.')
TypeError: Sequence contents must be Dataset instances.
```

You can set any element value as empty by using `None`

(sequence elements
will automatically be converted to an empty list when you do so):

```
>>> ds.PatientName = None
>>> elem
(0010, 0010) Patient's Name PN: None
>>> ds.OtherPatientIDsSequence = None
>>> len(ds.OtherPatientIDsSequence)
0
```

Elements with a value of `None`

, `b''`

, `''`

or `[]`

will still be
written to file, but will have an empty value and zero length.

### Adding elements¶

#### Any category¶

New elements of any category can be added to the dataset with the
`add_new()`

method, which takes the tag, VR and
value to use for the new element.

Let’s say we wanted to add the (0028,1050) *Window Center* standard element. We
already know the tag is (0028,1050), but how we get the VR and how do we
know the Python `type`

to use for the value?

There are two ways to get an element’s VR:

You can use Part 6 of the DICOM Standard and search for the element

Alternatively, you can use the

`dictionary_VR()`

function to look it up

```
>>> from pydicom.datadict import dictionary_VR
>>> dictionary_VR([0x0028, 0x1050])
'DS'
```

The Python type to use for a given VR is given by this table. For **DS** we can use a `str`

,
`int`

or `float`

, so to add the new element:

```
>>> ds.add_new([0x0028, 0x1050], 'DS', "100.0")
>>> elem = ds[0x0028, 0x1050]
>>> elem
(0028, 1050) Window Center DS: "100.0"
```

#### Standard elements¶

Adding elements with `add_new()`

is a lot of
work, so for standard elements you can just use the keyword
and *pydicom* will do the lookup for you:

```
>>> 'WindowWidth' in ds
False
>>> ds.WindowWidth = 500
>>> ds['WindowWidth']
(0028, 1051) Window Width DS: "500.0"
```

Notice how we can also use the element keyword with the Python
`in`

operator to see if a standard element is in
the dataset? This also works with element tags, so private and repeating group
elements are also covered:

```
>>> [0x0043, 0x104E] in ds
True
```

#### Sequences¶

Because sequence items are also `Dataset`

instances,
you can use the same methods on them as well.

```
>>> seq = ds.OtherPatientIDsSequence
>>> seq += [Dataset(), Dataset(), Dataset()]
>>> seq[0].PatientID = 'Citizen^Jan'
>>> seq[0].TypeOfPatientID = 'TEXT'
>>> seq[1].PatientID = 'CompressedSamples^CT1'
>>> seq[1].TypeOfPatientID = 'TEXT'
>>> seq[0]
(0010, 0020) Patient ID LO: 'Citizen^Jan'
(0010, 0022) Type of Patient ID CS: 'TEXT'
>>> seq[1]
(0010, 0020) Patient ID LO: 'CompressedSamples^CT1'
(0010, 0022) Type of Patient ID CS: 'TEXT'
```

### Deleting elements¶

All elements can be deleted with the `del`

operator in combination with the element tag:

```
>>> del ds[0x0043, 0x104E]
>>> [0x0043, 0x104E] in ds
False
```

For standard elements you can use the keyword instead:

```
>>> del ds.WindowCenter
>>> 'WindowCenter' in ds
False
```

And you can remove items from sequences and multi-valued elements using your
preferred `list`

method:

```
>>> del ds.OtherPatientIDsSequence[2]
>>> len(seq)
2
>>> del ds.ImageType[2]
>>> ds.ImageType
['ORIGINAL', 'PRIMARY', 'LOCALIZER']
```

## Writing¶

After changing the dataset, the final step is to write the modifications back
to file. This can be done by using `save_as()`

to
write the dataset to the supplied path:

```
>>> ds.save_as('out.dcm')
```

You can also write to any Python file-like:

```
>>> with open('out.dcm', 'wb') as outfile:
... ds.save_as(outfile)
...
```

```
>>> from io import BytesIO
>>> out = BytesIO()
>>> ds.save_as(out)
```

By default, `save_as()`

will write the dataset
as-is. This means that even if your dataset is not conformant to the
DICOM File Format it will
still be written exactly as given. To be certain you’re writing the
dataset in the DICOM File Format you can use the enforce_file_format keyword
parameter:

```
>>> ds.save_as('out.dcm', enforce_file_format=True)
```

This will attempt to automatically add in any missing required group
`0x0002`

File Meta Information elements and set a blank 128 byte preamble (if
required). If it’s unable to do so then an exception will be raised:

```
>>> del ds.file_meta
>>> ds.save_as('out.dcm', enforce_file_format=True)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File ".../pydicom/dataset.py", line 2452, in save_as
pydicom.dcmwrite(
File ".../pydicom/filewriter.py", line 1311, in dcmwrite
validate_file_meta(file_meta, enforce_standard=True)
File ".../pydicom/dataset.py", line 3204, in validate_file_meta
raise AttributeError(
AttributeError: Required File Meta Information elements are either missing
or have an empty value: (0002,0010) Transfer Syntax UID
```

The exception message contains the required element(s) that need to be added,
usually this will only be the *Transfer Syntax UID*. It’s an important element,
so get in the habit of making sure it’s there and correct.

Because we deleted the `file_meta`

dataset
we need to add it back:

```
>>> ds.file_meta = FileMetaDataset()
```

And now we can add our *Transfer Syntax UID* element and save to file:

```
>>> ds.file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'
>>> ds.save_as('out.dcm', enforce_file_format=True)
```

And we’re done.

## Next steps¶

Congratulations, you’re now familiar with the basics of using *pydicom* to
read, access, modify and write DICOM datasets. Next up you may be interested
in looking at our User Guide or some of our
examples.

## Source: https://pydicom.github.io/pydicom/stable/tutorials/waveforms.html

# Waveforms¶

This tutorial is about understanding waveforms in DICOM datasets and covers:

An introduction to DICOM waveforms

Decoding and displaying

*Waveform Data*Encoding

*Waveform Data*

It’s assumed that you’re already familiar with the dataset basics.

**Prerequisites**

```
```

```
```

**References**

## Waveforms in DICOM¶

There are a number of DICOM Information Object Definitions (IODs) that contain waveforms, such as 12-Lead ECG, Respiratory Waveform and Real-Time Audio Waveform. Every waveform IOD uses the Waveform Module to represent one or more multi-channel time-based digitized waveforms, sampled at constant time intervals.

The waveforms within a dataset are contained in the items of the (5400,0100)
*Waveform Sequence* element:

```
>>> from pydicom import examples
>>> ds = examples.waveform
>>> ds.SOPClassUID.name
'12-lead ECG Waveform Storage'
>>> waveforms = ds.WaveformSequence
>>> len(waveforms)
2
```

Each item in the sequence is a *multiplex group*, which is a group of related
waveforms that are synchronised at common sampling frequency.

```
>>> multiplex = waveforms[0]
>>> multiplex.MultiplexGroupLabel
'RHYTHM'
>>> multiplex.SamplingFrequency # in Hz
"1000.0"
>>> multiplex.NumberOfWaveformChannels
12
>>> multiplex.NumberOfWaveformSamples
10000
```

So the first multiplex group has 12 channels, each with 10,000 samples. Since
the sampling frequency is 1 kHz, this represents 10 seconds of data. The
defining information for each channel is available in the (5400,0200)
*Channel Definition Sequence*:

```
>>> for ii, channel in enumerate(multiplex.ChannelDefinitionSequence):
... source = channel.ChannelSourceSequence[0].CodeMeaning
... units = 'unitless'
... if 'ChannelSensitivity' in channel: # Type 1C, may be absent
... units = channel.ChannelSensitivityUnitsSequence[0].CodeMeaning
... print(f"Channel {ii + 1}: {source} ({units})")
...
Channel 1: Lead I (Einthoven) (microvolt)
Channel 2: Lead II (microvolt)
Channel 3: Lead III (microvolt)
Channel 4: Lead aVR (microvolt)
Channel 5: Lead aVL (microvolt)
Channel 6: Lead aVF (microvolt)
Channel 7: Lead V1 (microvolt)
Channel 8: Lead V2 (microvolt)
Channel 9: Lead V3 (microvolt)
Channel 10: Lead V4 (microvolt)
Channel 11: Lead V5 (microvolt)
Channel 12: Lead V6 (microvolt)
```

## Decoding *Waveform Data*¶

The combined sample data for each multiplex is stored in the corresponding
(5400,1010) *Waveform Data* element:

```
>>> multiplex.WaveformBitsAllocated
16
>>> multiplex.WaveformSampleInterpretation
'SS'
>>> len(multiplex.WaveformData)
240000
```

If *Waveform Bits Allocated* is `16`

and *Waveform Sample Interpretation* is
`'SS'`

then the data for this multiplex consists of signed 16-bit
samples. Waveform data is encoded
with the channels interleaved, so for our case the data is ordered as:

```
(Ch 1, Sample 1), (Ch 2, Sample 1), ..., (Ch 12, Sample 1),
(Ch 1, Sample 2), (Ch 2, Sample 2), ..., (Ch 12, Sample 2),
...,
(Ch 1, Sample 10,000), (Ch 2, Sample 10,000), ..., (Ch 12, Sample 10,000)
```

To decode the raw multiplex waveform data to a numpy `ndarray`

you can use the `multiplex_array()`

function. The following decodes and returns the raw data from the multiplex at
*index* `0`

within the *Waveform Sequence*:

```
>>> from pydicom.waveforms import multiplex_array
>>> raw = multiplex_array(ds, 0, as_raw=True)
>>> raw[0, 0]
80
```

If (003A,0210) *Channel Sensitivity* is present within the multiplex’s *Channel
Definition Sequence* then the raw sample data needs to be corrected before it’s
in the quantity it represents. This correction is given by sample x *Channel
Sensitivity* x *Channel Sensitivity Correction Factor* + *Channel Baseline*
and will be applied when as_raw is `False`

or when using the
`Dataset.waveform_array()`

function:

```
>>> arr = ds.waveform_array(0)
>>> arr[0, 0]
>>> 100.0
>>> import matplotlib.pyplot as plt
>>> fig, (ax1, ax2) = plt.subplots(2)
>>> ax1.plot(raw[:, 0])
>>> ax1.set_ylabel("unitless")
>>> ax2.plot(arr[:, 0])
>>> ax2.set_ylabel("μV")
>>> plt.show()
```

When processing large amounts of waveform data it might be more efficient to
use the `generate_multiplex()`

function
instead. It yields an `ndarray`

for each multiplex group
within the *Waveform Sequence*:

```
>>> from pydicom.waveforms import generate_multiplex
>>> for arr in generate_multiplex(ds, as_raw=False):
... print(arr.shape)
...
(10000, 12)
(1200, 12)
```

## Encoding *Waveform Data*¶

Having seen how to decode and view a waveform then next step is creating our own multiplex group. The new group will contain two channels representing cosine and sine curves. We’ve chosen to represent our waveforms using signed 16-bit integers, but you can use signed or unsigned 8, 16, 32 or 64-bit integers depending on the requirements of the IOD.

First we create two `ndarrays`

with our waveform data:

```
>>> import numpy as np
>>> x = np.arange(0, 4 * np.pi, 0.1)
>>> ch1 = (np.cos(x) * (2**15 - 1)).astype('int16')
>>> ch2 = (np.sin(x) * (2**15 - 1)).astype('int16')
```

```
>>> from pydicom.dataset import Dataset
>>> new = Dataset()
>>> new.WaveformOriginality = "ORIGINAL"
>>> new.NumberOfWaveformChannels = 2
>>> new.NumberOfWaveformSamples = len(x)
>>> new.SamplingFrequency = 1000.0
```

To find out which elements we need to add to our new multiplex, we check the Waveform Module in Part 3 of the DICOM Standard. Type 1 elements must be present and not empty, Type 1C are conditionally required, Type 2 elements must be present but may be empty, and Type 3 elements are optional.

Set our channel definitions, one for each channel (note that we have opted not
to include a *Channel Sensitivity*, so our data will be unit-less). If you were
to do this for real you would obviously use an official coding scheme.

```
>>> new.ChannelDefinitionSequence = [Dataset(), Dataset()]
>>> chdef_seq = new.ChannelDefinitionSequence
>>> for chdef, curve_type in zip(chdef_seq, ["cosine", "sine"]):
... chdef.ChannelSampleSkew = "0"
... chdef.WaveformBitsStored = 16
... chdef.ChannelSourceSequence = [Dataset()]
... source = chdef.ChannelSourceSequence[0]
... source.CodeValue = "1.0"
... source.CodingSchemeDesignator = "PYDICOM"
... source.CodingSchemeVersion = "1.0"
... source.CodeMeaning = curve_type
```

Interleave the waveform samples, convert to bytes and set the *Waveform Data*.
Since the dataset’s transfer syntax is little endian, if you’re working on
a big endian system you’ll need to perform the necessary conversion. You can
determine the endianness of your system with ```
import sys;
print(sys.byteorder)
```

.

We also set our corresponding *Waveform Bits Allocated* and *Waveform Sample
Interpretation* element values to match our data representation type:

```
>>> arr = np.stack((ch1, ch2), axis=1)
>>> arr.shape
(126, 2)
>>> new.WaveformData = arr.tobytes()
>>> new.WaveformBitsAllocated = 16
>>> new.WaveformSampleInterpretation = 'SS'
```

And finally add the new multiplex group to our example dataset and save:

```
>>> ds.WaveformSequence.append(new)
>>> ds.save_as("my_waveform.dcm")
```

We should now be able to plot our new waveforms:

```
>>> from pydicom import dcmread
>>> ds = dcmread("my_waveform.dcm")
>>> arr = ds.waveform_array(2)
>>> fig, (ax1, ax2) = plt.subplots(2)
>>> ax1.plot(arr[:, 0])
>>> ax2.plot(arr[:, 1])
>>> plt.show()
```

## Source: https://pydicom.github.io/pydicom/stable/tutorials/filesets.html

# DICOM File-sets and DICOMDIR¶

This tutorial is about DICOM File-sets and covers:

An introduction to DICOM File-sets and the DICOMDIR file

Loading a File-set using the

`FileSet`

class and accessing its managed SOP instancesCreating a new File-set and modifying existing ones

It’s assumed that you’re already familiar with the dataset basics.

**References**

## The DICOM File-set¶

A File-set is a collection of DICOM files that share a common naming space. Most people have probably interacted with a File-set without being aware of it; one place they’re frequently used is on the CDs/DVDs containing DICOM data that are given to a patient after a medical procedure (such as an MR or ultrasound).

The specification for File-sets is given in Part 10 of the DICOM Standard.

### The DICOMDIR file¶

Note

Despite its name, a DICOMDIR file is not a file system directory and
can be read using `dcmread()`

like any other DICOM
dataset.

Every File-set must contain a single file with the filename `DICOMDIR`

, the
location of which is dependent on the type of media used to store the File-set.
For the most commonly used media (DVD, CD, USB, PC file system, etc), the
DICOMDIR file will be in the root directory of the File-set. For other
media types, Part 12 of the DICOM Standard
specifies where the DICOMDIR must be located.

Warning

It’s **strongly recommended** that you avoid making changes to a DICOMDIR
dataset directly unless you know what you’re doing. Even minor changes may
require recalculating the offsets for each directory record. Use the
`FileSet`

methods (see below) instead.

The DICOMDIR file is used to summarize the contents of the File-set and is a
*Media Storage Directory* instance that follows the
Basic Directory IOD.

```
>>> from pydicom import examples
>>> ds = examples.dicomdir
>>> ds.file_meta.MediaStorageSOPClassUID.name
'Media Storage Directory Storage'
```

The most important element in a DICOMDIR is the (0004,1220) *Directory
Record Sequence*; each item in the sequence is a *directory record*,
and one or more records are used to briefly describe an available SOP
Instance and its location within the File-set’s directory structure. Each
record has a *record type* given by the (0004,1430) *Directory Record Type*
element, and different records are related to each other using the hierarchy
given in Table F.4-1.

```
>>> print(ds.DirectoryRecordSequence[0])
(0004, 1400) Offset of the Next Directory Record UL: 3126
(0004, 1410) Record In-use Flag US: 65535
(0004, 1420) Offset of Referenced Lower-Level Di UL: 510
(0004, 1430) Directory Record Type CS: 'PATIENT'
(0008, 0005) Specific Character Set CS: 'ISO_IR 100'
(0010, 0010) Patient's Name PN: 'Doe^Archibald'
(0010, 0020) Patient ID LO: '77654033'
```

Here we have a `'PATIENT'`

record, which from Table F.5-1 we see must also contain *Patient’s Name*
and *Patient ID* elements. The full list of available record types and their
requirements is in Annex F.5 of Part 3 of the DICOM Standard.

## FileSet¶

While it’s possible to access everything within a File-set using the DICOMDIR
dataset, making changes to an existing File-set quickly becomes complicated
due to the need to add and remove directory records, recalculate the
byte offsets for existing records and manage the corresponding file
system changes. A more user-friendly way to interact with one is via the
`FileSet`

class.

### Loading existing File-sets¶

To load an existing File-set just pass a DICOMDIR
`Dataset`

or the path to the DICOMDIR file to
`FileSet`

:

```
>>> from pydicom import dcmread
>>> from pydicom.fileset import FileSet
>>> path = examples.get_path("dicomdir") # The path to the examples.dicomdir dataset
>>> ds = dcmread(path)
>>> fs = FileSet(ds) # or FileSet(path)
```

An overview of the File-set’s contents is shown when printing:

```
>>> print(fs)
DICOM File-set
Root directory: /home/user/env/lib/python3.7/site-packages/pydicom/data/test_files/dicomdirtests
File-set ID: PYDICOM_TEST
File-set UID: 1.2.276.0.7230010.3.1.4.0.31906.1359940846.78187
Descriptor file ID: (no value available)
Descriptor file character set: (no value available)
Changes staged for write(): DICOMDIR update, directory structure update
Managed instances:
PATIENT: PatientID='77654033', PatientName='Doe^Archibald'
STUDY: StudyDate=20010101, StudyTime=000000, StudyDescription='XR C Spine Comp Min 4 Views'
SERIES: Modality=CR, SeriesNumber=1
IMAGE: 1 SOP Instance
SERIES: Modality=CR, SeriesNumber=2
IMAGE: 1 SOP Instance
SERIES: Modality=CR, SeriesNumber=3
IMAGE: 1 SOP Instance
STUDY: StudyDate=19950903, StudyTime=173032, StudyDescription='CT, HEAD/BRAIN WO CONTRAST'
SERIES: Modality=CT, SeriesNumber=2
IMAGE: 4 SOP Instances
PATIENT: PatientID='98890234', PatientName='Doe^Peter'
STUDY: StudyDate=20010101, StudyTime=000000
SERIES: Modality=CT, SeriesNumber=4
IMAGE: 2 SOP Instances
SERIES: Modality=CT, SeriesNumber=5
IMAGE: 5 SOP Instances
STUDY: StudyDate=20030505, StudyTime=050743, StudyDescription='Carotids'
SERIES: Modality=MR, SeriesNumber=1
IMAGE: 1 SOP Instance
SERIES: Modality=MR, SeriesNumber=2
IMAGE: 1 SOP Instance
STUDY: StudyDate=20030505, StudyTime=025109, StudyDescription='Brain'
SERIES: Modality=MR, SeriesNumber=1
IMAGE: 1 SOP Instance
SERIES: Modality=MR, SeriesNumber=2
IMAGE: 3 SOP Instances
STUDY: StudyDate=20030505, StudyTime=045357, StudyDescription='Brain-MRA'
SERIES: Modality=MR, SeriesNumber=1
IMAGE: 1 SOP Instance
SERIES: Modality=MR, SeriesNumber=2
IMAGE: 3 SOP Instances
SERIES: Modality=MR, SeriesNumber=700
IMAGE: 7 SOP Instances
```

The `FileSet`

class treats a File-set as a flat
collection of SOP Instances, abstracting away the need to dig down into the
hierarchy like you would with a DICOMDIR dataset. For example,
iterating over the `FileSet`

yields a
`FileInstance`

object for each of the managed
instances.

```
>>> for instance in fs:
... print(instance.PatientName)
... break
...
Doe^Archibald
```

A list of unique element values within the File-set can be found using the
`find_values()`

method, which by default
searches the corresponding DICOMDIR records:

```
>>> fs.find_values("PatientID")
['77654033', '98890234']
```

The search can be expanded to the File-set’s managed instances by supplying the load parameter, at the cost of a longer search time due to having to read and decode the corresponding files:

```
>>> fs.find_values("PhotometricInterpretation")
[]
>>> fs.find_values("PhotometricInterpretation", load=True)
['MONOCHROME1', 'MONOCHROME2']
```

More importantly, the File-set can be searched to find instances matching
a query using the `find()`

method, which returns
a list of `FileInstance`

. The corresponding file
can then be read and decoded using `FileInstance.load()`

, returning it as a
`FileDataset`

:

```
>>> for instance in fs.find(PatientID='77654033'):
... ds = instance.load()
... print(ds.PhotometricInterpretation)
...
MONOCHROME1
MONOCHROME1
MONOCHROME1
MONOCHROME2
MONOCHROME2
MONOCHROME2
MONOCHROME2
```

`find()`

also supports the use of the load
parameter:

```
>>> len(fs.find(PatientID='77654033', PhotometricInterpretation='MONOCHROME1'))
0
>>> len(fs.find(PatientID='77654033', PhotometricInterpretation='MONOCHROME1', load=True))
3
```

### Creating a new File-set¶

You can create a new File-set by creating a new
`FileSet`

instance:

```
>>> fs = FileSet()
```

This will create a completely conformant File-set, however it won’t contain any SOP instances. Since empty File-sets aren’t very useful, our next step will be to add some SOP instances to it.

### Modifying a File-set¶

`FileSet`

and staging¶

Before we go any further we need to discuss how the
`FileSet`

class manages changes to the File-set.
Modifications to the File-set are first *staged*, which means that although
the `FileSet`

instance behaves as though you’ve applied
them, nothing will actually change on the file system itself until
you explicitly call `FileSet.write()`

.
This includes changes such as:

Adding SOP instances using the

`FileSet.add()`

or`FileSet.add_custom()`

methodsRemoving SOP instances with

`FileSet.remove()`

Changing one of the following properties:

`ID`

,`UID`

,`descriptor_file_id`

and`descriptor_character_set`

When the

`FileSet`

class determines it needs to move SOP instances from an existing File-set’s directory structure to the structure used by*pydicom*

You can tell if changes are staged with the
`is_staged`

property:

```
>>> fs.is_staged
True
```

You may also have noticed this line in the `print(fs)`

output shown above:

```
Changes staged for write(): DICOMDIR update, directory structure update
```

This appears when the `FileSet`

is staged and will
contain at least one of the following:

`DICOMDIR update`

or`DICOMDIR creation`

: the DICOMDIR file will be updated or created`directory structure update`

: one or more of the SOP instances in the existing File-set will be moved over to use the*pydicom*File-set directory structure`N additions`

:*N*SOP instances will be added to the File-set`M removals`

:*M*SOP instances will be removed from the File-set

#### Adding SOP instances¶

The simplest way to add new SOP instances to the File-set is with the
`add()`

method, which takes the path to the
instance or the instance itself as a `Dataset`

and
returns the addition as a `FileInstance`

.

To reduce memory usage, instances staged for addition are written to a
temporary directory and only copied to the File-set itself when
`write()`

is called. However, they can still be
accessed and loaded:

```
>>> instance = fs.add(examples.ct)
>>> instance.is_staged
True
>>> instance.for_addition
True
>>> instance.path
'/tmp/tmp0aalrzir/86e6b75b-b764-46af-bec3-51698a8366f2'
>>> type(instance.load())
<class 'pydicom.dataset.FileDataset'>
```

Alternatively, if you want more control over the directory records that will
be added to the DICOMDIR file, or if you need to use PRIVATE records, you can
use the `add_custom()`

method.

The `add()`

method uses *pydicom’s* default
directory record creation functions to create the necessary records based on
the SOP instance’s attributes, such as *SOP Class UID* and *Modality*.
Occasionally, they may fail when an element required by these functions
is empty or missing:

```
>>> rt_dose = examples.rt_dose
>>> fs.add(rt_dose)
Traceback (most recent call last):
File ".../pydicom/fileset.py", line 1858, in _recordify
record = DIRECTORY_RECORDERS[record_type](ds)
File ".../pydicom/fileset.py", line 2338, in _define_rt_dose
_check_dataset(ds, ["InstanceNumber", "DoseSummationType"])
File ".../pydicom/fileset.py", line 2281, in _check_dataset
raise ValueError(
ValueError: The instance's (0020, 0013) 'Instance Number' element cannot be empty
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File ".../pydicom/fileset.py", line 1039, in add
record = next(record_gen)
File ".../pydicom/fileset.py", line 1860, in _recordify
raise ValueError(
ValueError: Unable to use the default 'RT DOSE' record creator as the instance is missing a required element or value. Either update the instance, define your own record creation function or use 'FileSet.add_custom()' instead
```

When this occurs, there are three options:

Update the instance to include the required element and/or value

Override the default record creation functions with your own by modifying

`DIRECTORY_RECORDERS`

Use the

`add_custom()`

method

According to the exception message above, the *Instance Number* element is empty.
Let’s update the instance and try adding it again:

```
>>> rt_dose.InstanceNumber = "1"
>>> fs.add(rt_dose)
```

#### Removing instances¶

SOP instances can be removed from the File-set with the
`remove()`

method, which takes the
`FileInstance`

or `list`

of
`FileInstance`

to be removed:

```
>>> len(fs)
2
>>> instances = fs.find(PatientID="1CT1")
>>> len(instances)
1
>>> fs.remove(instances)
>>> len(fs)
1
```

### Applying the changes¶

Let’s add a couple of SOP instances back to the File-set:

```
>>> fs.add(examples.ct)
>>> fs.add(examples.mr)
```

To apply the changes we’ve made to the File-set we use
`write()`

. For new File-sets, we have to supply the
path where the File-set root directory will be located:

```
>>> from pathlib import Path
>>> from tempfile import TemporaryDirectory
>>> t = TemporaryDirectory()
>>> t.name
'/tmp/tmpsqz8rhgb'
>>> fs.write(t.name)
>>> fs.is_staged
False
>>> root = Path(t.name)
>>> for path in sorted([p for p in root.glob('**/*') if p.is_file()]):
... print(path)
...
/tmp/tmpsqz8rhgb/DICOMDIR
/tmp/tmpsqz8rhgb/PT000000/ST000000/SE000000/RD000000
/tmp/tmpsqz8rhgb/PT000001/ST000000/SE000000/IM000000
/tmp/tmpsqz8rhgb/PT000002/ST000000/SE000000/IM000000
```

The root directory for existing File-sets cannot be changed, so for those
you only need to call `write()`

without any
arguments:

```
>>> instances = fs.find(PatientID="1CT1")
>>> fs.remove(instances)
>>> fs.write()
>>> for path in sorted([p for p in root.glob('**/*') if p.is_file()]):
... print(path)
...
/tmp/tmpsqz8rhgb/DICOMDIR
/tmp/tmpsqz8rhgb/PT000000/ST000000/SE000000/RD000000
/tmp/tmpsqz8rhgb/PT000001/ST000000/SE000000/IM000000
```

For existing File-sets that don’t use the same directory structure semantics
as `FileSet`

, calling
`write()`

will move SOP instances over to the
new structure. However, if the only modification you’ve made is to remove SOP
instances or change `ID`

,
`UID`

,
`descriptor_file_id`

, or
`descriptor_character_set`

, then you can pass
the *use_existing* keyword parameter to keep the existing directory structure
and update the DICOMDIR file.

First, we need to copy the existing example File-set to a temporary directory so we don’t accidentally modify it:

```
>>> from shutil import copytree, copyfile
>>> t = TemporaryDirectory()
>>> dst = Path(t.name)
>>> src = examples.get_path("dicomdir").parent
>>> copyfile(src / "DICOMDIR", dst / "DICOMDIR")
>>> copytree(src / "77654033", dst / "77654033")
>>> copytree(src / "98892001", dst / "98892001")
>>> copytree(src / "98892003", dst / "98892003")
```

Now we load the File-set from the temporary directory, remove instances and
write out the changes with *use_existing* to keep the current directory
structure:

```
>>> fs = FileSet(dst / "DICOMDIR")
>>> instances = fs.find(PatientID="98890234")
>>> fs.remove(instances)
>>> fs.write(use_existing=True) # Keep the current directory structure
>>> for path in sorted([p for p in dst.glob('**/*') if p.is_file()]):
... print(path)
...
/tmp/tmpu068kdwp/DICOMDIR
/tmp/tmpu068kdwp/77654033/CR1/6154
/tmp/tmpu068kdwp/77654033/CR2/6247
/tmp/tmpu068kdwp/77654033/CR3/6278
/tmp/tmpu068kdwp/77654033/CT2/17106
/tmp/tmpu068kdwp/77654033/CT2/17136
/tmp/tmpu068kdwp/77654033/CT2/17166
/tmp/tmpu068kdwp/77654033/CT2/17196
```

If you’d just called `write()`

without
*use_existing*, then it would’ve moved the SOP instances to the new
directory structure:

```
>>> fs.write()
>>> for path in sorted([p for p in dst.glob('**/*') if p.is_file()]):
... print(path)
...
/tmp/tmpu068kdwp/DICOMDIR
/tmp/tmpu068kdwp/PT000000/ST000000/SE000000/IM000000
/tmp/tmpu068kdwp/PT000000/ST000000/SE000001/IM000000
/tmp/tmpu068kdwp/PT000000/ST000000/SE000002/IM000000
/tmp/tmpu068kdwp/PT000000/ST000001/SE000000/IM000000
/tmp/tmpu068kdwp/PT000000/ST000001/SE000000/IM000001
/tmp/tmpu068kdwp/PT000000/ST000001/SE000000/IM000002
/tmp/tmpu068kdwp/PT000000/ST000001/SE000000/IM000003
```

## Conclusion¶

In this tutorial you’ve learned about DICOM File-sets and the DICOMDIR file.
You should now be able to use the `FileSet`

class
to create new File-sets, and to load, search and modify existing ones.

## Source: https://pydicom.github.io/pydicom/stable/tutorials/pixel_data/introduction.html

*Pixel Data* - Part 1: Introduction and accessing¶

This is part 1 of the tutorial on using *pydicom* with DICOM *Pixel Data*. It covers:

An introduction to DICOM pixel data

Converting pixel data to a NumPy

`ndarray`

Customizing the conversion process

It’s assumed that you’re already familiar with the dataset basics.

**Prerequisites**

Installing using pip:

```
```

Installing on conda:

```
```

## Introduction¶

Many DICOM SOP classes contain bulk pixel data, which typically represents medical
imagery or 2D slices of a 3D volume. This data is most commonly found in
the *Pixel Data* element, however it may be in *Float Pixel Data* or *Double Float
Pixel Data* instead, depending on the SOP class. The table below lists these
possible pixel data containing elements, although it’s important to note that
only one may be present in any given dataset.

Tag |
Description |
Keyword |
VR |
|---|---|---|---|
(7FE0,0008) |
|
FloatPixelData |
|
(7FE0,0009) |
|
DoubleFloatPixelData |
|
(7FE0,0010) |
|
PixelData |
|

All three elements use **O*** VRs (such as **OB** and
**OD**), which in *pydicom* are stored as
(and should be set using) `bytes`

:

```
>>> from pydicom import examples
>>> ds = examples.jpeg2k
>>> ds.group_dataset(0x7FE0)
(7FE0,0010) Pixel Data OB: Array of 152326 elements
>>> ds.PixelData[:50]
b'\xfe\xff\x00\xe0\x00\x00\x00\x00\xfe\xff\x00\xe0\x00\x00\x01\x00\xffO\xffQ...
```

If the dataset’s been written using the DICOM File Format
it should have a *Transfer Syntax UID* element which describes how the pixel data
is encoded and whether it’s undergone compression:

```
>>> tsyntax = ds.file_meta.TransferSyntaxUID
>>> tsyntax.name
'JPEG 2000 Image Compression (Lossless Only)'
>>> tsyntax.is_compressed
True
```

In the example above the *Transfer Syntax UID* indicates that the pixel data has
been compressed using the JPEG 2000 compression method.
Other things to keep in mind with compressed transfer syntaxes are:

Only datasets that use the

*Pixel Data*element may be compressedEach frame of pixel data is compressed separately

The compressed frames are then

`encapsulated`

and the encapsulated data used to set the*Pixel Data*value

To access the encapsulated frames you can use `get_frame()`

or the `generate_frames()`

iterator:

```
>>> from pydicom.encaps import get_frame
>>> frame = get_frame(ds.PixelData, 0, number_of_frames=1)
>>> print(len(frame))
152294
```

The next example uses an uncompressed *Transfer Syntax UID*:

```
>>> ds = examples.ct
>>> tsyntax = ds.file_meta.TransferSyntaxUID
>>> tsyntax.name
'Explicit VR Little Endian'
>>> tsyntax.is_compressed
False
```

The pixel data in this dataset uses little-endian byte ordering and is uncompressed. Uncompressed
transfer syntaxes never use encapsulation and may use any one of the
three pixel data elements, although *Pixel Data* is the most common.

A dataset with pixel data should always contain group `0x0028`

Image Pixel module elements, which are needed to properly interpret
the encoded pixel data byte stream:

```
>>> ds.group_dataset(0x0028)
(0028,0002) Samples per Pixel US: 1
(0028,0004) Photometric Interpretation CS: 'MONOCHROME2'
(0028,0010) Rows US: 128
(0028,0011) Columns US: 128
(0028,0030) Pixel Spacing DS: [0.661468, 0.661468]
(0028,0100) Bits Allocated US: 16
(0028,0101) Bits Stored US: 16
(0028,0102) High Bit US: 15
(0028,0103) Pixel Representation US: 1
...
```

An explanation of what these elements represent can be found in the glossary, but briefly, the above indicates that this dataset contains a single grayscale image with dimensions 128 x 128 and that each pixel should be interpreted as a 2-byte signed integer.

## Converting to an `ndarray`

¶

Properly interpreting all the possible variations of a dataset’s pixel data requires
a lot of specific domain knowledge, not just of DICOM but also the various
JPEG compression schemes. For this reason *pydicom* offers a number of methods
for converting the pixel data to a NumPy `ndarray`

, the most high-level
of which are the `pixel_array()`

and `iter_pixels()`

functions:

```
import matplotlib.pyplot as plt
from pydicom import examples
from pydicom.pixels import pixel_array
# Get an example dataset as a FileDataset instance
ds = examples.ct
# Convert the pixel data to an ndarray
arr = pixel_array(ds)
assert arr.shape == (128, 128)
assert str(arr.dtype) == "int16"
# Display the pixel data using matplotlib
plt.imshow(arr, cmap="gray")
plt.show()
```

This will convert the entire pixel data to an `ndarray`

before using
matplotlib to display it. If the dataset has multiple
frames but you’re only interested in a particular one, then you can use the index parameter
to return it:

```
from pydicom import examples
from pydicom.pixels import pixel_array
# Get an example multi-frame dataset
ds = examples.rt_dose
assert ds.NumberOfFrames == '15'
# Return all frames
arr = pixel_array(ds)
assert arr.shape == (15, 10, 10)
# Return only the first frame
arr = pixel_array(ds, index=0)
assert arr.shape == (10, 10)
```

`iter_pixels()`

can be used to iterate through either all
the available frames or those specified by the indices parameter:

```
from pydicom import examples
from pydicom.pixels import iter_pixels
# Iterate through all frames
for arr in iter_pixels(examples.rt_dose):
assert arr.shape == (10, 10)
# Iterate through the first 3 even frames
for arr in iter_pixels(examples.rt_dose, indices=[1, 3, 5]):
assert arr.shape == (10, 10)
```

### Controlling decoding¶

The default decoding options for `pixel_array()`

and
`iter_pixels()`

have been chosen to return the pixel data in
its most commonly used form; for multi-sample data this means RGB is returned
by default. Datasets with pixel data in YCbCr
color space are converted using `convert_color_space()`

prior
to the array being returned. If you’d like to skip this conversion and return the
data as found in the dataset you can pass `raw=True`

:

```
import matplotlib.pyplot as plt
from pydicom import examples
from pydicom.pixels import pixel_array
ds = examples.ybr_color
assert ds.PhotometricInterpretation == "YBR_FULL_422"
ybr = pixel_array(ds, index=0, raw=True)
rgb = pixel_array(ds, index=0)
fig, (im1, im2) = plt.subplots(1, 2)
im1.imshow(ybr)
im1.set_title("Original (in YCbCr)")
im2.imshow(rgb)
im2.set_title("Converted (in RGB)")
plt.show()
```

Further customization of the returned `ndarray`

is possible by
passing one or more decoding options to
`pixel_array()`

and `iter_pixels()`

.

### Compressed transfer syntaxes¶

When converting datasets with a compressed transfer syntax, one or more additional packages are needed to perform the actual decompression (via their corresponding decoding plugins). By default, all available plugins will be tried and the first successful one will have its results returned:

```
from pydicom import examples
from pydicom.pixels import pixel_array
ds = examples.jpeg2k
# Returns the results from the first successful decoding plugin
arr = pixel_array(ds)
```

If no plugins are available for the given transfer syntax due to missing dependencies you’ll get an exception:

```
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File ".../pydicom/pixels/utils.py", line 1386, in pixel_array
return decoder.as_array(
^^^^^^^^^^^^^^^^^
File ".../pydicom/pixels/decoders/base.py", line 971, in as_array
self._validate_plugins(decoding_plugin),
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File ".../pydicom/pixels/common.py", line 249, in _validate_plugins
raise RuntimeError(
RuntimeError: Unable to decompress 'JPEG 2000 Image Compression (Lossless Only)' pixel data because all plugins are missing dependencies:
gdcm - requires gdcm>=3.0.10
pylibjpeg - requires pylibjpeg>=2.0 and pylibjpeg-openjpeg>=2.0
pillow - requires numpy and pillow>=10.0
```

While the resulting `ndarray`

for lossless compression methods should
be identical no matter which plugin is used, there may be slight differences for lossy
compression methods. To ensure consistency you can use the decoding_plugin argument
to use the specified decompression plugin:

```
from pydicom import examples
from pydicom.pixels import pixel_array
ds = examples.jpeg2k
# Return the results from the 'pylibjpeg' decoding plugin
arr = pixel_array(ds, decoding_plugin="pylibjpeg")
```

And of course if the specified plugin isn’t available you’ll get an exception:

```
>>> from pydicom import examples
>>> from pydicom.pixels import pixel_array
>>> pixel_array(examples.jpeg2k, decoding_plugin="pillow")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File ".../pydicom/pixels/utils.py", line 1386, in pixel_array
return decoder.as_array(
^^^^^^^^^^^^^^^^^
File ".../pydicom/pixels/decoders/base.py", line 971, in as_array
self._validate_plugins(decoding_plugin),
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File ".../pydicom/pixels/common.py", line 230, in _validate_plugins
raise RuntimeError(
RuntimeError: Unable to decompress 'JPEG 2000 Image Compression (Lossless Only)' pixel data because the specified plugin is missing dependencies:
pillow - requires numpy and pillow>=10.0
```

### Minimizing memory usage¶

Sometimes a dataset’s pixel data may be very large due to it having a large number
of frames and you’d like to avoid having the entire thing read into memory.
By passing the path to the dataset (as `str`

or `pathlib.Path`

) to
`pixel_array()`

only the Image Pixel module elements and the minimum amount of required
pixel data will be loaded:

```
from pydicom import examples
from pydicom.pixels import pixel_array
# Get the path to the 'examples.rt_dose' dataset
path = examples.get_path("rt_dose")
# Return the first frame of the pixel data
arr = pixel_array(path, index=0)
```

The same is true for `iter_pixels()`

:

```
import matplotlib.pyplot as plt
import numpy as np
from pydicom import examples
from pydicom.pixels import iter_pixels
# Get the path to the 'examples.ybr_color' dataset
path = examples.get_path("ybr_color")
# Create an empty ndarray and use it to initialize the display
im = plt.imshow(np.zeros((ds.Rows, ds.Columns), dtype="u1"))
# Iterate through the frames and update the display
for frame in iter_pixels(path):
im.set_data(frame)
plt.pause(0.033)
```

If you’re supplying a path to `pixel_array()`

or `iter_pixels()`

and you need access to the Image Pixel elements to perform image processing operations on
the array (such as `rescale`

or
`windowing`

) you can access them by passing
an empty `Dataset`

instance via the ds_out argument,
or alternatively by using `dcmread()`

with
`stop_before_pixels=True`

:

```
from pydicom import Dataset, examples
from pydicom.pixels import pixel_array, apply_rescale
# Get the path to the 'examples.ct' dataset
path = examples.get_path("ct")
ds = Dataset()
arr = pixel_array(path, ds_out=ds)
assert ds.RescaleIntercept == "-1024.0"
assert ds.RescaleSlope == "1.0"
# Convert raw CT values to Hounsfield units
hu = apply_rescale(arr, ds)
```

## Converting to an `ndarray`

with metadata¶

While `pixel_array()`

and `iter_pixels()`

should cover most use cases, you may want more information about the returned
`ndarray`

, such as what color space it’s in. The `Decoder.as_array()`

and `Decoder.iter_array()`

methods provide mid-level access
to *pydicom’s* pixel data decoding functionality while still handling most of the complexity
of conversion to an array. More importantly, they return or yield a tuple of
(`ndarray`

, `dict`

), where the `dict`

contains metadata
describing the corresponding `ndarray`

.

Warning

The `Decoder`

class should not be used
directly, instead use the class instance returned by `get_decoder()`

.

```
from pydicom import examples
from pydicom.pixels import get_decoder
ds = examples.ybr_color
assert ds.PhotometricInterpretation == "YBR_FULL_422"
# Get the 'Decoder' instance required to decode the dataset's pixel data
decoder = get_decoder(ds.file_meta.TransferSyntaxUID)
# Converts the pixel data to an ndarray in the original color space
arr, meta = decoder.as_array(ds, raw=True, index=0)
assert (meta["rows"], meta["columns"], meta["samples_per_pixel"]) == arr.shape
assert meta["photometric_interpretation"] == "YBR_FULL_422"
# Converts the pixel data to an ndarray in RGB color space
arr, meta = decoder.as_array(ds, index=0)
assert meta["photometric_interpretation"] == "RGB"
```

This is especially useful for non-conformant datasets where the Image Pixel module elements have values that don’t match the
actual pixel data (such as *Number of Frames* or *Photometric Interpretation*).

## Conclusion and next steps¶

In part 1 of this tutorial you’ve been introduced to DICOM’s pixel data and learned how to
use *pydicom* to access it, convert it to an `ndarray`

and how to
control the conversion process. In the next part you’ll learn how to
create your own pixel data from scratch.

## Source: https://pydicom.github.io/pydicom/stable/tutorials/pixel_data/creation.html

*Pixel Data* - Part 2: Creation of pixel data¶

In part 1 of this tutorial you learned how to access the pixel data as either the raw `bytes`

or a NumPy
`ndarray`

. In this part we’ll be creating pixel data from
scratch and adding it to a `Dataset`

. We’ll be creating
uncompressed datasets with the following types of *Pixel Data*:

Grayscale with 8-bit unsigned integers

Multi-frame RGB with 8-bit unsigned integers

Grayscale with 12-bit signed integers

Grayscale with 32-bit floats (for

*Float Pixel Data*)

**Prerequisites**

Installing using pip:

```
```

Installing on conda:

```
```

## Creating *Pixel Data*¶

We’ll be using NumPy to create an array containing the pixel data and converting
it to little-endian ordered `bytes`

using `ndarray.tobytes()`

. This is the function we’ll be using to create the array:

```
import numpy as np
def draw_circle(shape: tuple[int, int], dtype: str, value: int) -> np.ndarray:
"""Return an ndarray containing a circle."""
(rows, columns), radius = shape, min(shape) // 2
x0, y0 = columns // 2, rows // 2
x = np.linspace(0, columns, columns)
y = np.linspace(0, rows, rows)[:, None]
# Create a boolean array where values inside the radius are True
arr = (x - x0)**2 + (y - y0)**2 <= radius**2
# Convert to the required `dtype` and set the maximum `value`
return arr.astype(dtype) * value
```

The datasets we’ll be creating don’t meet the requirements of any DICOM
IOD and so aren’t conformant DICOM SOP instances, but
they’re sufficient to demonstrate how to create and add pixel data to a
`Dataset`

using *pydicom*. To create pixel data for an
actual dataset you should check the requirements of the specific IOD you’re working
with, as many IODs place restrictions on the allowed values for elements such
as *Bits Stored*, *Photometric Interpretation* and others.

### Grayscale with 8-bit unsigned integers¶

The first example uses a single frame of grayscale *Pixel Data* with 8-bit unsigned integers:

For 8-bit pixel values

*Bits Stored*is`8`

*Bits Allocated*must be a multiple of 8 and not less than*Bits Stored*For unsigned integers

*Pixel Representation*must be`0`

For 8-bit unsigned integers all pixel values must be in the closed interval [0, 2

8- 1]For pixel data that uses a single sample per pixel,

*Samples per Pixel*is`1`

The

*Photometric Interpretation*should be appropriate for a single sample per pixelIf

*Bits Allocated*is <= 8 then*Pixel Data*uses a VR of**OB**

The VR for *Pixel Data* may be **OB** or **OW** depending
on the value of *Bits Allocated*. *pydicom* will set this automatically when
writing the `Dataset`

to file as long as *Bits Allocated* has
been set, but for completeness we’ll be setting it manually.

The example has two different sets of *Pixel Data*; one with an even number of bytes
and one with an odd number. The DICOM Standard requires
odd length *Pixel Data* have trailing padding sufficient to make it an even length,
so the latter case demonstrates how to do so.

Because we’ll be using NumPy to create the data we need an array with a `dtype`

appropriate for our chosen pixel data properties. For unsigned 8-bit integers
the obvious choice is `uint8`

as it can contain the values with the minimum
amount of memory usage and can be converted directly to a suitable *Pixel Data*
`bytes`

value with `ndarray.tobytes()`

.
If instead we were to use something like `uint16`

we would double the memory usage
and require either setting `ds.BitsAllocated = 16`

(and roughly doubling the
final size of the dataset) or keeping *Bits Stored* as `8`

and stripping out the
unused bytes with `ds.PixelData == arr.tobytes()[1::2]`

.

```
import matplotlib.pyplot as plt
from pydicom import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian
ds = Dataset()
ds.file_meta = FileMetaDataset()
ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
ds.BitsAllocated = 8 # 8-bit containers
ds.BitsStored = 8 # 8-bits used
ds.HighBit = ds.BitsStored - 1
ds.PixelRepresentation = 0 # unsigned
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
## Even number of bytes
# Create a 480 x 320, 8-bit unsigned array
arr = draw_circle((320, 480), "uint8", 255)
assert arr.size % 2 == 0
# No padding needed
ds.PixelData = arr.tobytes()
ds["PixelData"].VR = "OB"
ds.Rows = arr.shape[0] # 320 pixels
ds.Columns = arr.shape[1] # 480 pixels
plt.imshow(ds.pixel_array)
plt.show()
## Odd number of bytes
# Create a 31 x 63, 8-bit unsigned array
arr = draw_circle((63, 31), "uint8", 255)
assert arr.size % 2 == 1
# Trailing padding required to make the length an even number of bytes
ds.PixelData = b"".join((arr.tobytes(), b"\x00"))
ds["PixelData"].VR = "OB"
ds.Rows = arr.shape[0]
ds.Columns = arr.shape[1]
plt.imshow(ds.pixel_array)
plt.show()
```

**Experimentation**

Modify the example to use the following and see what effects they have on the displayed images:

Set

*Bits Allocated*and*Bits Stored*to`16`

and`ds.Columns = arr.shape[1] // 2`

Set

`ds.Rows = arr.shape[1]`

and`ds.Columns = arr.shape[0]`

### Multi-frame RGB with 8-bit unsigned integers¶

The second example uses multi-frame RGB *Pixel Data* with 8-bit unsigned integers:

*Samples per Pixel*has changed to`3`

, because there are 3 channels; R, G and B.*Photometric Interpretation*has changed to`"RGB"`

to match the image type*Planar Configuration*has been added as it’s required when*Samples per Pixel*> 1*Number of Frames*has been added as it’s required when there are multiple frames

The *Planar Configuration* value is set as `0`

, which means each pixel is encoded
separately then all the encoded pixels are concatenated together. This matches how
`ndarray.tobytes()`

will encode an array that’s ordered as
(rows, columns, samples) or (frames, rows, columns, samples).

```
import matplotlib.pyplot as plt
from pydicom import Dataset, FileMetaDataset
from pydicom.pixels import iter_pixels
from pydicom.uid import ExplicitVRLittleEndian
ds = Dataset()
ds.file_meta = FileMetaDataset()
ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
ds.BitsAllocated = 8 # 8-bit containers
ds.BitsStored = 8 # 8-bits used
ds.HighBit = ds.BitsStored - 1
ds.PixelRepresentation = 0 # unsigned
ds.SamplesPerPixel = 3
ds.PhotometricInterpretation = "RGB"
ds.PlanarConfiguration = 0
ds.NumberOfFrames = 2
# Create 2 frames of 480 x 320 x 3, 8-bit unsigned array
arr = np.empty((2, 320, 480, 3), dtype="uint8")
# Frame 1
arr[0, ..., 0] = draw_circle((320, 480), "uint8", 255)
arr[0, ..., 1] = draw_circle((320, 480), "uint8", 127)
arr[0, ..., 2] = draw_circle((320, 480), "uint8", 0)
# Frame 2
arr[1, ..., 0] = draw_circle((320, 480), "uint8", 0)
arr[1, ..., 1] = draw_circle((320, 480), "uint8", 127)
arr[1, ..., 2] = draw_circle((320, 480), "uint8", 255)
ds.PixelData = b"".join((arr.tobytes(), b"\x00")) if arr.size % 2 else arr.tobytes()
ds["PixelData"].VR = "OB"
ds.Rows = arr.shape[1]
ds.Columns = arr.shape[2]
# Display the frames
im = plt.imshow(np.zeros((ds.Rows, ds.Columns, 3), dtype="uint8"))
for frame in iter_pixels(ds):
im.set_data(frame)
plt.pause(1)
```

**Experimentation**

A

*Planar Configuration*value of`1`

means each color channel is encoded separately and then the results concatenated together. Try setting`ds.PlanarConfiguration = 1`

and seeing what effect it has.By default

*pydicom*will return any extra frames it finds in the*Pixel Data*. Set`ds.NumberOfFrames = 1`

and see what effect it has, then pass`allow_excess_frames=False`

to`iter_pixels()`

and compare the results.

### Grayscale with 12-bit signed integers¶

The final *Pixel Data* example uses a single channel of 12-bit signed integers:

For 12-bit pixel values

*Bits Stored*is`12`

and*Bits Allocated*should be at least`16`

For signed integers

*Pixel Representation*must be`1`

For 12-bit signed integers all pixels must have values in the closed interval [-2

11, 211- 1]If

*Bits Allocated*is > 8 then*Pixel Data*uses a VR of**OW**

We need a `dtype`

sufficient for containing 12-bit integers, so
to minimize memory usage we’ll go with `int16`

and use a *Bits Allocated* value
of `16`

to match.

```
import matplotlib.pyplot as plt
from pydicom import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian
ds = Dataset()
ds.file_meta = FileMetaDataset()
ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
ds.BitsAllocated = 16 # 16-bits allocated
ds.BitsStored = 12 # 12-bits used; interval is [-2048, 2047]
ds.HighBit = ds.BitsStored - 1
ds.PixelRepresentation = 1 # signed
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
# Create a 480 x 320, 16-bit signed array
arr = draw_circle((320, 480), "int16", -2048)
ds.PixelData = arr.tobytes()
ds["PixelData"].VR = "OW"
ds.Rows = arr.shape[0]
ds.Columns = arr.shape[1]
plt.imshow(ds.pixel_array)
plt.show()
```

**Experimentation**

Set *Pixel Representation* to 0 and see what effect it has on the value of the
pixels in the circle.

## Creating *Float Pixel Data* and *Double Float Pixel Data*¶

The creation of *Float Pixel Data* or *Double Float Pixel Data* is very similar to
that of *Pixel Data*, the main differences being:

*Bits Allocated*and*Bits Stored*are always 32 for*Float Pixel Data*and 64 for*Double Float Pixel Data*The

*Pixel Representation*element should not be presentThe VR doesn’t need to be set manually

Element |
VR |
|
|
|
|---|---|---|---|---|
|
|
32 |
32 |
|
|
|
64 |
64 |
|

The example below demonstrates creating *Float Pixel Data*:

```
from pydicom import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian
ds = Dataset()
ds.file_meta = FileMetaDataset()
ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
ds.BitsAllocated = 32
ds.BitsStored = 32
ds.HighBit = ds.BitsStored - 1
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
# Create a 480 x 320, 32-bit float array
arr = draw_circle((320, 480), "float32", 1024.58)
ds.FloatPixelData = arr.tobytes()
ds.Rows = arr.shape[0]
ds.Columns = arr.shape[1]
```

## Conclusion and next steps¶

In part 2 of this tutorial you’ve learned how to create and add a variety of different pixel
data to a `Dataset`

using an `ndarray`

. In the final
part you’ll learn how to compress and decompress datasets containing pixel data.

## Source: https://pydicom.github.io/pydicom/stable/tutorials/pixel_data/compressing.html

*Pixel Data* - Part 3: Compression and decompression¶

In part 1 of this tutorial you learned how to access the pixel data as either the raw `bytes`

or a NumPy
`ndarray`

and in part 2 you learned how to create new pixel data and add it to a `Dataset`

.
In this final part you’ll learn how to compress and decompress datasets containing
*Pixel Data*.

**Prerequisites**

Installing using pip:

```
```

Installing on conda:

```
```

## Compression of *Pixel Data*¶

*pydicom* can perform dataset compression for the the following transfer syntaxes:

*JPEG-LS Lossless*and*JPEG-LS Near-lossless*compression with pyjpegls.*JPEG 2000 Lossless*and*JPEG 2000*compression with pylibjpeg and pylibjpeg-openjpeg.*RLE Lossless*, which doesn’t need any additional packages but can be sped up if pylibjpeg and pylibjpeg-rle are available.

For all other transfer syntaxes it’s entirely up to you to compress the *Pixel
Data* in a manner conformant to the requirements of the DICOM Standard:

Each frame of pixel data must be compressed separately

All compressed frames must then be encapsulated.

The encapsulated byte stream is used to set the

*Pixel Data*valueWhen the amount of compressed frame data is very large then it’s recommended (but not required) that an extended offset table also be included in the dataset

The VR for compressed

*Pixel Data*is always**OB**

### Compressing a dataset (with *RLE Lossless*)¶

Compression of an existing uncompressed dataset can be performed by passing the *Transfer
Syntax UID* of the compression method you’d like to use to `Dataset.compress()`

, or by using the `compress()`

function. We’ll be using *RLE Lossless* to start with, which is based on the
PackBits compression scheme:

```
>>> from pydicom import examples
>>> from pydicom.uid import RLELossless
>>> ds = examples.ct
>>> ds.file_meta.TransferSyntaxUID.is_compressed
False
>>> ds.compress(RLELossless)
```

If you’re creating a new dataset, or if you want to update the *Pixel Data* for an
existing dataset, you can pass an `ndarray`

along with the *Transfer
Syntax UID*:

```
import numpy as np
from pydicom import Dataset
from pydicom.uid import RLELossless
ds = Dataset()
ds.Rows = 320
ds.Columns = 480
ds.BitsAllocated = 8
ds.BitsStored = 8
ds.HighBit = ds.BitsStored - 1
ds.PixelRepresentation = 0
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
arr = np.ones((ds.Rows, ds.Columns), dtype="uint8")
ds.compress(RLELossless, arr)
assert ds.file_meta.TransferSyntaxUID == RLELossless
assert isinstance(ds.PixelData, bytes)
```

In both cases this will compress the `Dataset`

in-place:

The

*Pixel Data*will be set with the encapsulated RLE codestreamThe

*Transfer Syntax UID*will be set to*RLE Lossless*A new

*SOP Instance UID*value will be also be generated, but this can be disabled by passing`generate_instance_uid=False`

.

When using an `ndarray`

the `shape`

,
`dtype`

and contents of arr must match the corresponding
Image Pixel module elements in the dataset,
such as *Rows*, *Columns*, *Samples per Pixel*, etc. If they don’t match you’ll get an exception:

```
>>> from pydicom import examples
>>> from pydicom.uid import RLELossless
>>> ds = examples.ct
>>> arr = np.zeros((ds.Rows, ds.Columns + 1), dtype='<i2')
>>> ds.compress(RLELossless, arr)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File ".../pydicom/src/pydicom/dataset.py", line 1957, in compress
encoded = [f for f in frame_iterator]
^^^^^^^^^^^^^^^^^^^^^^^^^^^
File ".../pydicom/pixels/encoders/base.py", line 678, in iter_encode
runner.validate()
File ".../pydicom/pixels/encoders/base.py", line 304, in validate
self._validate_array()
File ".../pydicom/pixels/encoders/base.py", line 333, in _validate_array
raise ValueError(
ValueError: Mismatch between the expected ndarray shape (128, 128) and the actual shape (128, 129)
```

When there are multiple plugins available for compressing the given transfer syntax a specific encoding plugin can be used by passing the plugin name via the encoding_plugin argument:

```
>>> ds.compress(RLELossless, encoding_plugin='pylibjpeg')
```

The RLE compression method is well supported by DICOM applications and can
compress a wide range of images, however it’s usually less efficient than the JPEG
family of compression schemes. More information on performing compression with
*RLE Lossless* can be found in the RLE encoding guide.

### Compressing with JPEG-LS¶

The JPEG-LS compression scheme is based on ISO/IEC 14495-1/ITU T.87. While it can compress 2- to 16-bit images and uses a lossy quality specification mechanism that’s easy to understand, it’s not well suited for lossy compression of signed integers and is generally not well supported by third-party applications, so keep that in mind if you decide to use it.

**Lossless compression**

Performing lossless compression is straightforward:

```
>>> from pydicom import examples
>>> from pydicom.uid import JPEGLSLossless
>>> ds = examples.ct
>>> ds.compress(JPEGLSLossless)
```

**Lossy compression**

Lossy compression is a bit more complicated, especially when the pixel data uses signed integers. First up though, we’ll use an example with unsigned pixel data.

Warning

*pydicom* makes no recommendations for specifying the image quality for
lossy encoding methods. Any examples of lossy encoding are for
**illustration purposes only**.

```
>>> from pydicom import examples
>>> from pydicom.uid import JPEGLSNearLossless
>>> ds = examples.rgb_color
>>> ds.PixelRepresentation
0
>>> ds.compress(JPEGLSNearLossless, jls_error=3)
```

The jls_error parameter is used to control the loss in image quality, and is
directly related to the JPEG-LS NEAR parameter, which is the absolute allowed error
in (unsigned) pixel data values. A jls_error of `3`

therefore means that all
pixels will be within 3 intensity units of the original.

In our second lossy JPEG-LS example we’ll use a dataset with 16-bit signed integers, which is where the complication starts. The NEAR parameter is defined in terms of unsigned integers, so when used with signed values there can potentially be compression errors of up to the maximum bit-depth of the pixel data. To avoid this, the range of pixel values must be in the closed interval:

```
[-2**(ds.BitsStored - 1) + jls_error, 2**(ds.BitsStored - 1) - 1 - jls_error]
```

For example, with a *Bits Stored* of `8`

and `jls_error=3`

the pixels must be in the
range [-125, 124].

```
>>> from pydicom import examples
>>> from pydicom.uid import JPEGLSNearLossless
>>> ds = examples.ct
>>> ds.PixelRepresentation
1
>>> ds.BitsStored
16
>>> arr = ds.pixel_array
>>> arr.min(), arr.max()
(128, 2191)
>>> ds.compress(JPEGLSNearLossless, jls_error=3)
```

In this example the pixel values are within the allowed range so we don’t need to do anything further. If that weren’t the case you’d have to rescale the values or use a different compression method such as JPEG 2000 (recommended).

More information on performing compression with JPEG-LS can be found in the JPEG-LS encoding guide.

### Compressing with JPEG 2000¶

The JPEG 2000 compression scheme is based on ISO/IEC 15444-1/ITU T.800. The format is fairly well supported by third-party applications and it can compress images with a wide variety of properties, making it a good choice for compressing datasets.

Two transfer syntaxes are available that use JPEG 2000 compression; *JPEG 2000 Lossless*
and *JPEG 2000*. While the DICOM Standard allows *JPEG 2000* to be either lossy or
lossless, when used for compression in *pydicom* it’s always treated as being lossy in
order to simplify its usage.

**Lossless compression**

As with RLE and JPEG-LS, performing lossless compression is straightforward:

```
>>> from pydicom import examples
>>> from pydicom.uid import JPEG2000Lossless
>>> ds = examples.ct
>>> ds.compress(JPEG2000Lossless)
```

For RGB pixel data, JPEG 2000 can perform multiple component transformation
(MCT) during the encoding process, which should improve the compression efficiency.
This can be enabled or disabled by setting an appropriate *Photometric Interpretation*
prior to compression:

`"RGB"`

to disable MCT`"YBR_RCT"`

to enable MCT for*JPEG 2000 Lossless*`"YBR_ICT"`

to enable MCT for*JPEG 2000*

```
>>> from pydicom import examples
>>> from pydicom.uid import JPEG2000Lossless
>>> ds = examples.rgb_color
>>> ds.PhotometricInterpretation
"RGB"
>>> ds.compress(JPEG2000Lossless) # No MCT applied
>>> len(ds.PixelData)
334412
>>> ds = examples.rgb_color
>>> ds.PhotometricInterpretation = "YBR_RCT"
>>> ds.compress(JPEG2000Lossless) # MCT applied
>>> len(ds.PixelData)
152342
```

**Lossy compression**

Lossy compression with *JPEG 2000* is both more and less complicated then JPEG-LS;
you don’t have to worry about the pixel values for signed integers, but specifying
the image quality is less intuitive.

Warning

*pydicom* makes no recommendations for specifying the image quality for
lossy encoding methods. Any examples of lossy encoding are for
**illustration purposes only**.

```
>>> from pydicom import examples
>>> from pydicom.uid import JPEG2000
>>> ds = examples.ct
>>> ds.compress(JPEG2000, j2k_cr=[5, 2]) # 2 quality layers
```

With JPEG 2000 image quality is specified with either the j2k_cr or j2k_psnr parameters:

j2k_cr is a

`list[float]`

of compression ratios to use for each quality layer and is directly related to OpenJPEG’s -r compression ratio option. There must be at least one layer and the minimum allowable compression ratio is`1`

. When using multiple layers they should be ordered in decreasing value from left to right.j2k_psnr is a

`list[float]`

of the peak signal-to-noise ratios (in dB) to use for each quality layer and is directly related to OpenJPEG’s -q quality option. There must be at least one layer and when using multiple layers they should be ordered in increasing value from left to right.

Choosing appropriate quality settings for *JPEG 2000* is far beyond the scope of this
tutorial, but whatever you end up selecting should be thoroughly tested with a
representative sample of expected pixel data.

More information on performing compression with JPEG 2000 can be found in the JPEG 2000 encoding guide.

#### Encapsulating data compressed by third-party packages¶

You can also use *pydicom* with third-party compression packages to encapsulate
the compressed *Pixel Data*, provided they meet the requirements of the
corresponding transfer syntax. The `encapsulate()`

or
`encapsulate_extended()`

functions are used to encapsulate the
compressed data.

```
from pydicom import examples
from pydicom.encaps import encapsulate, encapsulate_extended
from pydicom.uid import JPEGBaseline8Bit
# Fetch an example dataset
ds = examples.ct
# Use third-party package to compress
# Let's assume it compresses to JPEG Baseline
frames: list[bytes] = third_party_compression_func(...)
# Set the *Transfer Syntax UID* appropriately
ds.file_meta.TransferSyntaxUID = JPEGBaseline8Bit
# For *Samples per Pixel* 1 the *Photometric Interpretation* is unchanged
# Basic encapsulation
ds.PixelData = encapsulate(frames)
ds["PixelData"].VR = "OB" # always for encapsulated pixel data
ds.save_as("ct_compressed_basic.dcm")
# Extended encapsulation
result: tuple[bytes, bytes, bytes] = encapsulate_extended(frames)
ds.PixelData = result[0]
ds.ExtendedOffsetTable = result[1]
ds.ExtendedOffsetTableLength = result[2]
ds.save_as("ct_compressed_ext.dcm")
```

## Decompression of *Pixel Data*¶

Datasets with a compressed *Transfer Syntax UID* can be decompressed with
`Dataset.decompress()`

or the
`decompress()`

function.

```
>>> from pydicom import examples
>>> ds = examples.jpeg2k
>>> ds.decompress()
```

This will decompress the `Dataset`

in-place:

The

*Pixel Data*will be set using the uncompressed pixel data.The

*Transfer Syntax UID*will be changed to*Explicit VR Little Endian*.The Image Pixel module elements will be updated as required to match the uncompressed pixel data.

A new

*SOP Instance UID*value will be also be generated, but this can be disabled by passing`generate_instance_uid=False`

.

Dataset decompression uses the same backend as accessing compressed *Pixel Data*,
so the same customization options of the decoding
process apply. For example, to use a specific plugin
you can pass its name via the decoding_plugin argument:

```
>>> from pydicom import examples
>>> ds = examples.jpeg2k
>>> ds.decompress(decoding_plugin="pylibjpeg")
```

If the dataset’s *Pixel Data* is in the YCbCr color space it will also be converted
to RGB by default. This can be disabled by passing `as_rgb=False`

:

```
import numpy as np
from pydicom import examples
from pydicom.pixels import convert_color_space, pixel_array
from pydicom.uid import JPEG2000Lossless
# Original dataset in RGB
ds = examples.rgb_color
assert ds.PhotometricInterpretation == "RGB"
# Convert to YCbCr and compress
ybr = convert_color_space(ds.pixel_array, "RGB", "YBR_FULL")
ds.PhotometricInterpretation = "YBR_FULL"
ds.compress(JPEG2000Lossless, ybr)
assert ds.PhotometricInterpretation == "YBR_FULL"
# RGB reference - needed because converting RGB -> YBR -> RGB is lossy
rgb = convert_color_space(ybr, "YBR_FULL", "RGB")
# Decompress with conversion to RGB
ds.decompress()
assert ds.PhotometricInterpretation == "RGB"
assert np.array_equal(rgb, pixel_array(ds, raw=True))
# Decompress without conversion to RGB
ds.PhotometricInterpretation = "YBR_FULL"
ds.compress(JPEG2000Lossless, ybr)
ds.decompress(as_rgb=False)
assert ds.PhotometricInterpretation == "YBR_FULL"
assert np.array_equal(ybr, pixel_array(ds, raw=True))
```

## Conclusion¶

In part 3 of this tutorial you’ve learned how to use *pydicom* to compress and decompress
datasets and how to encapsulate pixel data that has been compressed by third-party
packages. Having made it to the end of the pixel data tutorial you should now be
comfortable using *pydicom* to perform pixel data related tasks.

## Source: https://pydicom.github.io/pydicom/stable/tutorials/pixel_data/index.html

pydicom
Getting started
How to install pydicom
Documentation
pydicom User Guide
Tutorials
How to install pydicom
Dataset basics: read, access, modify, write
Pixel Data
Pixel Data
- Part 1: Introduction and accessing
Pixel Data
- Part 2: Creation of pixel data
Pixel Data
- Part 3: Compression and decompression
Waveforms
DICOM File-sets and DICOMDIR
Structured Reporting
Introduction to JSON support
Contributing a source code change
Contributing a documentation change
Guides
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
Tutorials
Pixel Data
Pixel Data
¶
Pixel Data
- Part 1: Introduction and accessing
Pixel Data
- Part 2: Creation of pixel data
Pixel Data
- Part 3: Compression and decompression

## Source: https://pydicom.github.io/pydicom/stable/tutorials/sr_basics.html

# Structured Reporting¶

Starting in *pydicom* version 1.4, some support for DICOM Structured Reporting (SR) began to be added,
as alpha code; the API for this is subject to change in future *pydicom* versions. At this point the
code is limited to code dictionaries and one class `Code`

as a foundational step for future work.

Most access is through a `codes`

class instance provided in `pydicom.sr.codedict`

. This can be used
with a `dir()`

method on a particular scheme designator (‘DCM’ here) or CID (see further below):

```
>>> from pydicom.sr.codedict import codes
>>> codes.DCM.dir("Modality")
['IncorrectModalityWorklistEntry', 'MixedModality3DCAMModel', 'Modality', 'ModalityToRead', 'OtherModality']
```

Once a name is known, the `Code`

instance can be created using that name:

```
>>> codes.DCM.ModalityToRead
Code(value='128002', scheme_designator='DCM', meaning='Modality to Read', scheme_version=None)
```

Codes with keywords that start with a number are prefixed with an underscore:

```
>>> codes.SCT._1SigmaLowerValueOfPopulation
Code(value='371919006', scheme_designator='SCT', meaning='1 Sigma Lower Value of population', scheme_version=None)
```

Codes can also be accessed by CID:

```
>>> codes.cid270.Person
Code(value='121006', scheme_designator='DCM', meaning='Person', scheme_version=None)
>>> codes.cid270.dir()
['Device', 'Person']
```

If the CID number is unknown, it is possible to find it through a CID name dictionary:

```
>>> from pydicom.sr.codedict import cid_for_name
>>> [name for name in cid_for_name if 'Observ' in name]
['ObservationSubjectClass', 'ObserverType', 'EchoFindingObservationTypes']
>>> cid_for_name['ObserverType']
270
```

The following Scheme Designators are available in `codes`

:
SCT, DCM, LN, FMA, MDC, UMLS, BARI, NCIt,
NEU, UCUM, RADLEX, NDC, ITIS_TSN, PUBCHEM_CID, MSH

As noted, these steps do not yet directly provide SR capabilities in *pydicom*, but provide some access
to codes and CIDs in a similar way to DICOM keywords for the DICOM dictionary.

## Source: https://pydicom.github.io/pydicom/stable/tutorials/dicom_json.html

# Introduction to JSON support¶

Starting in *pydicom* version 1.3, some support for converting DICOM data to
and from JSON format has been added. This support is considered to be in
beta state, and the API is still subject to change.

Support for the JSON format has been added to the DICOM Standard in Part 18 as the DICOM JSON Model. The standard describes how different DICOM value representations can be encoded in JSON.

## Converting a dataset into JSON format¶

*pydicom* supports the conversion of a DICOM dataset both into a JSON string
and into a deserialized JSON dictionary:

```
>>> import pydicom
>>> ds = pydicom.examples.ct
>>> ds.to_json()
'{"00080005": {"Value": ["ISO_IR 100"], "vr": "CS"}, "00080008": {"Value":...
>>> ds.to_json_dict()
{"00080005": {"Value": ["ISO_IR 100"], "vr": "CS"}, "00080008": {"Value":...
```

Which of these methods you need depends on your use case. The JSON string
format created by `to_json()`

can be used in
low-level APIs to serialize the dataset.
Higher-level Python APIs (like Django) often work directly with Python
dictionaries deserialized from a JSON string instead, so
`to_json_dict()`

can be more convenient here.

## Creating a dataset from JSON¶

Similar, a dataset can be created both from a JSON string and from a JSON dictionary. There is only a single function to handle both cases:

```
>>> from pydicom.dataset import Dataset
>>> Dataset.from_json('{"00080005": {"Value": ["ISO_IR 100"], "vr": "CS"}}')
(0008, 0005) Specific Character Set CS: u'ISO_IR 100'
>>> Dataset.from_json({"00080005": {"Value": ["ISO_IR 100"], "vr": "CS"}})
(0008, 0005) Specific Character Set CS: u'ISO_IR 100'
```

The conversion in both directions is symmetric:

```
>>> import pydicom
>>> ds = pydicom.examples.ct
>>> ds_json = ds.to_json()
>>> ds1 = pydicom.dataset.Dataset.from_json(ds_json)
>>> assert ds == ds1
```

## Working with large binary data¶

Large binary data can be handled in two ways. It can be encoded inline as a base64-encoded string, or it can be accessed via a BulkDataURI provided in the JSON data, that provides the possibility to retrieve the data using the DICOMweb WADO-RS standard.

If you don’t provide additional arguments to the encoding functions, the data is encoded inline. If you want to save or retrieve data using DICOMweb WADO-RS, you have to provide a bulk data handler.

On writing JSON data, the bulk data handler is responsible to store the data
so it can be retrieved via the `BulkDataURI`

saved in the JSON dataset.
Note that only data greater than `bulk_data_threshold`

(by default set to
1024) is handled by the bulk data handler - smaller data is encoded inline.

```
>>> import pydicom
>>> def bulk_data_handler(data_element):
>>> uri = store_data_and_return_uri(data_element)
>>> return uri
>>>
>>> ds = pydicom.examples.ct
>>> ds_json = ds.to_json(bulk_data_element_handler=bulk_data_handler)
```

On reading JSON data, the handler must be able to retrieve the data using
the stored `BulkDataURI`

:

```
>>> def bulk_data_reader(bulk_data_uri):
>>> return data_retrieved_via_uri(bulk_data_uri)
>>>
>>> json_data = {
>>> "00091002": {"vr": "OB", "BulkDataURI": "https://my.wado.org/123"}
>>> }
>>> ds = Dataset.from_json(json_data, bulk_data_uri_handler=bulk_data_reader)
```

or, if you need to also know the tag and the vr, in addition to the stored
`BulkDataURI`

:

```
>>> def bulk_data_reader(tag, vr, bulk_data_uri):
>>> return data_retrieved_for_tag_and_vr_via_uri(tag, vr, bulk_data_uri)
>>>
>>> json_data = {
>>> "00091002": {"vr": "OB", "BulkDataURI": "https://my.wado.org/123"}
>>> }
>>> ds = Dataset.from_json(json_data, bulk_data_uri_handler=bulk_data_reader)
```
