## Source: https://pydicom.github.io/pydicom/stable/reference/index.html

# API Reference¶

- Release:
3.0.2

- Date:
Mar 19, 2026

This API reference guide details the functions, modules and objects included in
*pydicom*.

- Character Encoding and Decoding (
`pydicom.charset`

) - Configuration Options (
`pydicom.config`

)`Settings`

- pydicom.config.settings
- pydicom.config.allow_DS_float
- pydicom.config.assume_implicit_vr_switch
- pydicom.config.convert_wrong_length_to_UN
- pydicom.config.data_element_callback
- pydicom.config.data_element_callback_kwargs
- pydicom.config.datetime_conversion
- pydicom.config.debug
- pydicom.config.enforce_valid_values
- pydicom.config.future_behavior
- pydicom.config.pixel_data_handlers
- pydicom.config.reset_data_element_callback
- pydicom.config.show_file_meta
- pydicom.config.DS_decimal
- pydicom.config.DS_numpy
- pydicom.config.use_DS_decimal
- pydicom.config.use_IS_numpy
- pydicom.config.use_DS_numpy
- pydicom.config.APPLY_J2K_CORRECTIONS
- pydicom.config.INVALID_KEY_BEHAVIOR
- pydicom.config.INVALID_KEYWORD_BEHAVIOR
- pydicom.config.IGNORE
- pydicom.config.WARN
- pydicom.config.RAISE

- Getting Included Datasets (
`pydicom.data`

) - Data Dictionary Utilities (
`pydicom.datadict`

) - Representation of Datasets (
`pydicom.dataset`

) - Representation of Data Elements
- Example Datasets (
`pydicom.examples`

) - Bulk Data Encapsulation Utilities (
`pydicom.encaps`

) - Exceptions (
`pydicom.errors`

) - Dataset IO
- DICOM File-sets (
`pydicom.fileset`

) - Bulk Data Handlers
- User Hooks (
`pydicom.hooks`

) - Miscellaneous (
`pydicom.misc`

) - Overlay Data Handling (
`pydicom.overlays`

) - Pixel Data (
`pydicom.pixels`

)- pydicom.pixels.apply_color_lut
- pydicom.pixels.apply_icc_profile
- pydicom.pixels.apply_modality_lut
- pydicom.pixels.apply_presentation_lut
- pydicom.pixels.apply_rescale
- pydicom.pixels.apply_voi_lut
- pydicom.pixels.apply_voi
- pydicom.pixels.apply_windowing
- pydicom.pixels.convert_color_space
- pydicom.pixels.create_icc_transform
- pydicom.pixels.as_pixel_options
- pydicom.pixels.compress
- pydicom.pixels.decompress
- pydicom.pixels.get_decoder
- pydicom.pixels.get_encoder
- pydicom.pixels.iter_pixels
- pydicom.pixels.pack_bits
- pydicom.pixels.pixel_array
- pydicom.pixels.set_pixel_data
- pydicom.pixels.unpack_bits
- Sub-modules

- Concepts and Context Groups (
`pydicom.sr`

) - Waveform Data Handlers (
`pydicom.waveforms`

) - UID Definitions and Utilities (
`pydicom.uid`

)

## Source: https://pydicom.github.io/pydicom/stable/reference/generated/pydicom.dataset.Dataset.html

# pydicom.dataset.Dataset¶

-
*class*pydicom.dataset.Dataset(**args: Dataset | MutableMapping[BaseTag, DataElement | RawDataElement]*,***kwargs: Any*)[source]¶ A DICOM dataset as a mutable mapping of DICOM Data Elements.

Examples

Add an element to the

`Dataset`

(for elements in the DICOM dictionary):>>> ds = Dataset() >>> ds.PatientName = "CITIZEN^Joan" >>> ds.add_new(0x00100020, 'LO', '12345') >>> ds[0x0010, 0x0030] = DataElement(0x00100030, 'DA', '20010101')

Add a sequence element to the

`Dataset`

>>> ds.BeamSequence = [Dataset(), Dataset(), Dataset()] >>> ds.BeamSequence[0].Manufacturer = "Linac, co." >>> ds.BeamSequence[1].Manufacturer = "Linac and Sons, co." >>> ds.BeamSequence[2].Manufacturer = "Linac and Daughters, co."

Add private elements to the

`Dataset`

>>> block = ds.private_block(0x0041, 'My Creator', create=True) >>> block.add_new(0x01, 'LO', '12345')

Updating and retrieving element values:

>>> ds.PatientName = "CITIZEN^Joan" >>> ds.PatientName 'CITIZEN^Joan' >>> ds.PatientName = "CITIZEN^John" >>> ds.PatientName 'CITIZEN^John'

Retrieving an element’s value from a Sequence:

>>> ds.BeamSequence[0].Manufacturer 'Linac, co.' >>> ds.BeamSequence[1].Manufacturer 'Linac and Sons, co.'

Accessing the

`DataElement`

items:>>> elem = ds['PatientName'] >>> elem (0010,0010) Patient's Name PN: 'CITIZEN^John' >>> elem = ds[0x00100010] >>> elem (0010,0010) Patient's Name PN: 'CITIZEN^John' >>> elem = ds.data_element('PatientName') >>> elem (0010,0010) Patient's Name PN: 'CITIZEN^John'

Accessing a private

`DataElement`

item:>>> block = ds.private_block(0x0041, 'My Creator') >>> elem = block[0x01] >>> elem (0041,1001) Private tag data LO: '12345' >>> elem.value '12345'

Alternatively:

>>> ds.get_private_item(0x0041, 0x01, 'My Creator').value '12345'

Deleting an element from the

`Dataset`

>>> del ds.PatientID >>> del ds.BeamSequence[1].Manufacturer >>> del ds.BeamSequence[2]

Deleting a private element from the

`Dataset`

>>> block = ds.private_block(0x0041, 'My Creator') >>> if 0x01 in block: ... del block[0x01]

Determining if an element is present in the

`Dataset`

>>> 'PatientName' in ds True >>> 'PatientID' in ds False >>> (0x0010, 0x0030) in ds True >>> 'Manufacturer' in ds.BeamSequence[0] True

Iterating through the top level of a

`Dataset`

only (excluding Sequences):>>> for elem in ds: ... print(elem) (0010,0010) Patient's Name PN: 'CITIZEN^John'

Iterating through the entire

`Dataset`

(including Sequences):>>> for elem in ds.iterall(): ... print(elem) (0010,0010) Patient's Name PN: 'CITIZEN^John'

Recursively iterate through a

`Dataset`

(including Sequences):>>> def recurse(ds): ... for elem in ds: ... if elem.VR == 'SQ': ... [recurse(item) for item in elem.value] ... else: ... # Do something useful with each DataElement

Converting the

`Dataset`

to and from JSON:>>> ds = Dataset() >>> ds.PatientName = "Some^Name" >>> jsonmodel = ds.to_json() >>> ds2 = Dataset() >>> ds2.from_json(jsonmodel) (0010,0010) Patient's Name PN: 'Some^Name'

- indent_chars¶
For string display, the characters used to indent nested Sequences. Default is

`" "`

.- Type:

-
__init__(
**args: Dataset | MutableMapping[BaseTag, DataElement | RawDataElement]*,***kwargs: Any*) None [source]¶ Create a new

`Dataset`

instance.

Methods

`__init__`

(*args, **kwargs)Create a new

`Dataset`

instance.`add`

(data_element)Add an element to the

`Dataset`

.`add_new`

(tag, VR, value)Create a new element and add it to the

`Dataset`

.`add_new_private`

(private_creator, group, ...)Create a new private element and add it to the

`Dataset`

.`clear`

()Delete all the elements from the

`Dataset`

.`compress`

(transfer_syntax_uid[, arr, ...])Compress uncompressed pixel data and update ds in-place with the resulting encapsulated codestream.

`convert_pixel_data`

([handler_name])Convert pixel data to a

`numpy.ndarray`

internally.`copy`

()Return a shallow copy of the dataset.

`data_element`

(name)Return the element corresponding to the element keyword name.

`decode`

()Apply character set decoding to the elements in the

`Dataset`

.`decompress`

([handler_name, as_rgb, ...])Perform an in-place decompression of a dataset with a compressed

*Transfer Syntax UID*.`dir`

(*filters)Return an alphabetical list of element keywords in the

`Dataset`

.`elements`

()Yield the top-level elements of the

`Dataset`

.Create an empty

`Dataset.file_meta`

if none exists.`formatted_lines`

([element_format, ...])Iterate through the

`Dataset`

yielding formatted`str`

for each element.`from_json`

(json_dataset[, bulk_data_uri_handler])Return a

`Dataset`

from a DICOM JSON Model object.`get`

()Simulate

`dict.get()`

to handle element tags and keywords.`get_item`

()Return the raw data element if possible.

`get_private_item`

(group, element_offset, ...)Return the data element for the given private tag group.

`group_dataset`

(group)Return a

`Dataset`

containing only elements of a certain group.`items`

()Return the

`Dataset`

items to simulate`dict.items()`

.`iterall`

()Iterate through the

`Dataset`

, yielding all the elements.`keys`

()Return the

`Dataset`

keys to simulate`dict.keys()`

.`overlay_array`

(group)Return the

*Overlay Data*in group as a`numpy.ndarray`

.`pixel_array_options`

(*[, index, raw, ...])Set the decoding and processing options used by the

`pixel_array`

property.`pop`

(key, *args)Emulate

`dict.pop()`

with support for tags and keywords.`popitem`

()Emulate

`dict.popitem()`

.`private_block`

(group, private_creator[, create])Return the block for the given tag group and private_creator.

`private_creators`

(group)Return a list of private creator names in the given group.

Remove all private elements from the

`Dataset`

.`save_as`

(filename, /[, ...])Encode the current

`Dataset`

and write it to filename.`set_original_encoding`

(is_implicit_vr, ...[, ...])Set the values for the original dataset encoding.

`set_pixel_data`

(arr, ...[, generate_instance_uid])Use an

`ndarray`

to set the*Pixel Data*and related Image Pixel module elements.`setdefault`

(key[, default])Emulate

`dict.setdefault()`

with support for tags and keywords.`to_json`

([bulk_data_threshold, ...])Return a JSON representation of the

`Dataset`

.`to_json_dict`

([bulk_data_threshold, ...])Return a dictionary representation of the

`Dataset`

conforming to the DICOM JSON Model as described in the DICOM Standard, Part 18, Annex F.`top`

()Return a

`str`

representation of the top level elements.Return a

`list`

of valid names for auto-completion code.`update`

(d)Extend

`dict.update()`

to handle DICOM tags and keywords.`update_raw_element`

(tag, *[, vr, value])Modify the VR or value for the raw element with tag.

`values`

()Return the

`Dataset`

values to simulate`dict.values()`

.`walk`

(callback[, recursive])Iterate through the

`Dataset's`

elements and run callback on each.`waveform_array`

(index)Return an

`ndarray`

for the multiplex group at index in the (5400,0100)*Waveform Sequence*.Attributes

Get/set the VR method used when encoding the dataset.

Get/set the endianness used when encoding the dataset.

Return

`True`

if the encoding to be used for writing is set and is the same as that used to originally encode the`Dataset`

.Return the original character set encoding for a dataset decoded from a file or buffer.

Return the original encoding used for a dataset decoded from a file or buffer.

Return the pixel data as a

`numpy.ndarray`

.Return the original character set encoding for a decoded dataset.

Get the VR method used by the original encoding of the dataset.

Get the endianness used by the original encoding of the dataset.

-
add(
*data_element: DataElement*) None [source]¶ Add an element to the

`Dataset`

.Equivalent to

`ds[data_element.tag] = data_element`

- Parameters:
**data_element**(*dataelem.DataElement*) – The`DataElement`

to add.

-
add_new(
*tag: int | str | tuple[int, int] | BaseTag*,*VR: str*,*value: Any*) None [source]¶ Create a new element and add it to the

`Dataset`

.- Parameters:
**tag**– The DICOM (group, element) tag in any form accepted by`Tag()`

such as`[0x0010, 0x0010]`

,`(0x10, 0x10)`

,`0x00100010`

, etc.**VR**(*str*) – The 2 character DICOM value representation (see DICOM Standard, Part 5, Section 6.2).**value**–The value of the data element. One of the following:

-
add_new_private(
*private_creator: str*,*group: int*,*element_offset: int*,*value: Any*,*vr: str | None = None*) None [source]¶ Create a new private element and add it to the

`Dataset`

.- Parameters:
**private_creator**(*str*) – The private creator string related to the new tag.**group**(*int*) – The group ID (0x0009 - 0xFFFF) for the private tag. Must be an odd number.**element_offset**(*int*) – The tag offset, e.g. the lower byte of the tag element of the private tag (0x00 - 0xFF). The higher byte is defined by the location of the private creator tag.**value**(*Any*) –The value of the data element. One of the following:

**vr**(*str**|**None*) – The two-letter DICOM value representation, or`None`

. If set to`None`

, it is taken from the private tag dictionary.

- Raises:
**ValueError**– If group doesn’t belong to a private tag or private_creator is empty.**KeyError**– If vr is`None`

and the tag is not found in the private tag dictionary.

-
compress(
*transfer_syntax_uid: str*,*arr: ndarray | None = None*,*encoding_plugin: str = ''*,*encapsulate_ext: bool = False*,***,*generate_instance_uid: bool = True*,*jls_error: int | None = None*,*j2k_cr: list[float] | None = None*,*j2k_psnr: list[float] | None = None*,***kwargs: Any*) None [source]¶ Compress uncompressed pixel data and update ds in-place with the resulting encapsulated codestream.

Added in version 2.2.

The dataset ds must already have the following Image Pixel module elements present with correct values that correspond to the resulting compressed pixel data:

(0028,0002)

*Samples per Pixel*(0028,0004)

*Photometric Interpretation*(0028,0008)

*Number of Frames*(if more than 1 frame will be present)(0028,0010)

*Rows*(0028,0011)

*Columns*(0028,0100)

*Bits Allocated*(0028,0101)

*Bits Stored*(0028,0103)

*Pixel Representation*

If

*Samples per Pixel*is greater than 1 then the following element is also required:(0028,0006)

*Planar Configuration*

This method will add the file meta dataset if none is present and add or modify the following elements:

(0002,0010)

*Transfer Syntax UID*(7FE0,0010)

*Pixel Data*

If the compressed pixel data is too large for encapsulation using a basic offset table then an extended offset table will also be used, in which case the following elements will also be added:

(7FE0,0001)

*Extended Offset Table*(7FE0,0002)

*Extended Offset Table Lengths*

If generate_instance_uid is

`True`

(default) then a new (0008,0018)*SOP Instance UID*value will be generated.**Supported Transfer Syntax UIDs**UID

Plugins

Encoding Guide

Name

Value

*JPEG-LS Lossless*1.2.840.10008.1.2.4.80

pyjpegls

*JPEG-LS Near Lossless*1.2.840.10008.1.2.4.81

*JPEG 2000 Lossless*1.2.840.10008.1.2.4.90

pylibjpeg

*JPEG 2000*1.2.840.10008.1.2.4.91

*RLE Lossless*1.2.840.10008.1.2.5

pydicom, pylibjpeg, gdcm

Changed in version 3.0: Added the jls_error, j2k_cr, j2k_psnr and generate_instance_uid keyword parameters.

Examples

Compress the existing uncompressed

*Pixel Data*in place:>>> from pydicom import examples >>> from pydicom.uid import RLELossless >>> ds = examples.ct >>> ds.compress(RLELossless) >>> ds.save_as("ct_rle_lossless.dcm")

- Parameters:
**transfer_syntax_uid**(*pydicom.uid.UID*) – The UID of the transfer syntax to use when compressing the pixel data.**arr**(*numpy.ndarray**,**optional*) – Compress the uncompressed pixel data in arr and use it to set the*Pixel Data*. If arr is not used then the existing*Pixel Data*in the dataset will be compressed instead. The`shape`

,`dtype`

and contents of the array should match the dataset.**encoding_plugin**(*str**,**optional*) – Use the encoding_plugin to compress the pixel data. See the user guide for a list of plugins available for each UID and their dependencies. If not specified then all available plugins will be tried (default).**encapsulate_ext**(*bool**,**optional*) – If`True`

then force the addition of an extended offset table. If`False`

(default) then an extended offset table will be added if needed for large amounts of compressed*Pixel Data*, otherwise just the basic offset table will be used.**generate_instance_uid**(*bool**,**optional*) – If`True`

(default) then generate a new (0008,0018)*SOP Instance UID*value for the dataset using`generate_uid()`

, otherwise keep the original value.**jls_error**(*int**,**optional*) –**JPEG-LS Near Lossless only**. The allowed absolute compression error in the pixel values.**j2k_cr**(*list**[**float**]**,**optional*) –**JPEG 2000 only**. A list of the compression ratios to use for each quality layer. There must be at least one quality layer and the minimum allowable compression ratio is`1`

. When using multiple quality layers they should be ordered in decreasing value from left to right. For example, to use 2 quality layers with 20x and 5x compression ratios then j2k_cr should be`[20, 5]`

. Cannot be used with j2k_psnr.**j2k_psnr**(*list**[**float**]**,**optional*) –**JPEG 2000 only**. A list of the peak signal-to-noise ratios (in dB) to use for each quality layer. There must be at least one quality layer and when using multiple quality layers they should be ordered in increasing value from left to right. For example, to use 2 quality layers with PSNR of 80 and 300 then j2k_psnr should be`[80, 300]`

. Cannot be used with j2k_cr.****kwargs**– Optional keyword parameters for the encoding plugin may also be present. See the encoding plugins options for more information.

-
convert_pixel_data(
*handler_name: str = ''*) None [source]¶ Convert pixel data to a

`numpy.ndarray`

internally.Deprecated since version 3.0: This method will be removed in v4.0, use

`pixel_array_options()`

instead.- Parameters:
**handler_name**(*str**,**optional*) –The name of the pixel handler or decoding plugin to use to decode the dataset’s pixel data. Support values are:

If using the

`pixel_data_handlers`

backend:`'gdcm'`

,`'pillow'`

,`'jpeg_ls'`

,`'rle'`

,`'numpy'`

and`'pylibjpeg'`

.If using the

`pixels`

backend see the documentation for the decoder corresponding to the dataset’s*Transfer Syntax UID*.

If not used (the default) then all available handlers or plugins will be tried and the data from first successful one will be used.

- Returns:
Converted pixel data is stored internally in the dataset, it can be accessed with the

`pixel_array`

property.- Return type:
None

- Raises:
**ValueError**– If handler_name is not a valid handler name.**NotImplementedError**– If the given handler or any handler, if none given, is unable to decompress pixel data with the current transfer syntax**RuntimeError**– If the given handler, or the handler that has been selected if none given, is not available.

Notes

If the pixel data is in a compressed image format, the data is decompressed and any related data elements are changed accordingly.

-
data_element(
*name: str*) DataElement | None [source]¶ Return the element corresponding to the element keyword name.

- Parameters:
**name**(*str*) – A DICOM element keyword.- Returns:
For the given DICOM element keyword, return the corresponding

`DataElement`

if present,`None`

otherwise.- Return type:
dataelem.DataElement or None

- decode() None [source]¶
Apply character set decoding to the elements in the

`Dataset`

.See DICOM Standard, Part 5, Section 6.1.1.

-
decompress(
*handler_name: str = ''*,***,*as_rgb: bool = True*,*generate_instance_uid: bool = True*,*decoding_plugin: str = ''*,***kwargs: Any*) None [source]¶ Perform an in-place decompression of a dataset with a compressed

*Transfer Syntax UID*.Warning

This function requires NumPy and may require the installation of additional packages to perform the actual pixel data decoding. See the pixel data decompression documentation for more information.

The dataset’s

*Transfer Syntax UID*will be set to*Explicit VR Little Endian*.The

*Pixel Data*will be decompressed in its entirety and the*Pixel Data*element’s value updated with the decompressed data, padded to an even length.The

*Pixel Data*element’s VR will be set to**OB**if*Bits Allocated*<= 8, otherwise it will be set to**OW**.The

`DataElement.is_undefined_length`

attribute for the*Pixel Data*element will be set to`False`

.Any image pixel module elements may be modified as required to match the uncompressed

*Pixel Data*.If generate_instance_uid is

`True`

(default) then a new (0008,0018)*SOP Instance UID*value will be generated.

Changed in version 3.0: Added the as_rgb and generate_instance_uid keyword parameters.

Deprecated since version 3.0: The handler_name parameter will be removed in v4.0, use decoding_plugin instead.

- Parameters:
**handler_name**(*str**,**optional*) – Deprecated and will be removed in v4.0, use decoding_plugin instead.**as_rgb**(*bool**,**optional*) –`pixels`

**backend only.**If`True`

(default) then convert pixel data with a YCbCr photometric interpretation such as`"YBR_FULL_422"`

to RGB.**generate_instance_uid**(*bool**,**optional*) – If`True`

(default) then generate a new (0008,0018)*SOP Instance UID*value for the dataset using`generate_uid()`

, otherwise keep the original value.**decoding_plugin**(*str**,**optional*) –The name of the decoding plugin to use when decoding compressed pixel data. If no decoding_plugin is specified (default) then all available plugins will be tried and the result from the first successful one yielded.

If using the

`pixels`

backend (default) then see the API documentation for the available plugins for each*Transfer Syntax UID*.If using the deprecated

`pixel_data_handlers`

backend supported plugins are:`'gdcm'`

,`'pillow'`

,`'jpeg_ls'`

,`'rle'`

,`'numpy'`

and`'pylibjpeg'`

.

**kwargs**(*dict**[**str**,**Any**]**,**optional*) –`pixels`

**backend only.**Optional keyword parameters for the decoding plugin may also be present. See the decoding plugins options for more information.

-
dir(
**filters: str*) list[str] [source]¶ Return an alphabetical list of element keywords in the

`Dataset`

.Intended mainly for use in interactive Python sessions. Only lists the element keywords in the current level of the

`Dataset`

(i.e. the contents of any sequence elements are ignored).

- elements() Iterator[DataElement | RawDataElement] [source]¶
Yield the top-level elements of the

`Dataset`

.Examples

>>> ds = Dataset() >>> for elem in ds.elements(): ... print(elem)

The elements are returned in the same way as in

`Dataset.__getitem__()`

.- Yields:
*dataelem.DataElement or dataelem.RawDataElement*– The unconverted elements sorted by increasing tag order.

-
formatted_lines(
*element_format: str = '%(tag)s %(name)-35.35s %(VR)s: %(repval)s'*,*sequence_element_format: str = '%(tag)s %(name)-35.35s %(VR)s: %(repval)s'*,*indent_format: str | None = None*) Iterator[str] [source]¶ Iterate through the

`Dataset`

yielding formatted`str`

for each element.- Parameters:
**element_format**(*str*) – The string format to use for non-sequence elements. Formatting uses the attributes of`DataElement`

. Default is`"%(tag)s %(name)-35.35s %(VR)s: %(repval)s"`

.**sequence_element_format**(*str*) – The string format to use for sequence elements. Formatting uses the attributes of`DataElement`

. Default is`"%(tag)s %(name)-35.35s %(VR)s: %(repval)s"`

**indent_format**(*str**or**None*) – Placeholder for future functionality.

- Yields:
*str*– A string representation of an element.

-
*classmethod*from_json(*json_dataset: dict[str, Any] | str | bytes | bytearray*,*bulk_data_uri_handler: Callable[[str, str, str], None | str | int | float | bytes] | Callable[[str], None | str | int | float | bytes] | None = None*) Dataset [source]¶ Return a

`Dataset`

from a DICOM JSON Model object.See the DICOM Standard, Part 18, Annex F.

- Parameters:
**json_dataset**(*dict**,**str**,**bytes**or**bytearray*) –`dict`

,`str`

,`bytes`

or`bytearray`

representing a DICOM Data Set formatted based on the DICOM JSON Model.**bulk_data_uri_handler**(*callable**,**optional*) – Callable function that accepts either the tag, vr and “BulkDataURI” value or just the “BulkDataURI” value of the JSON representation of a data element and returns the actual value of that data element (retrieved via DICOMweb WADO-RS). If no bulk_data_uri_handler is specified (default) then the corresponding element will have an “empty” value such as`""`

,`b""`

or`None`

depending on the vr (i.e. the Value Multiplicity will be 0).

- Return type:

-
get(
*key: str*,*default: Any | None = None*) Any [source]¶ -
get(
*key: int | tuple[int, int] | BaseTag*,*default: Any | None = None*) DataElement Simulate

`dict.get()`

to handle element tags and keywords.- Parameters:
- Returns:
*value*– If key is the keyword for an element in the`Dataset`

then return the element’s value.*dataelem.DataElement*– If key is a tag for a element in the`Dataset`

then return the`DataElement`

instance.*value*– If key is a class attribute then return its value.

-
get_item(
*key: slice*,***,*keep_deferred: bool = False*) Dataset [source]¶ -
get_item(
*key: int | str | tuple[int, int] | BaseTag*,***,*keep_deferred: bool = False*) DataElement Return the raw data element if possible.

It will be raw if the user has never accessed the value, or set their own value. Note if the data element is a deferred-read element, then it is read and converted before being returned.

- Parameters:
**key**– The DICOM (group, element) tag in any form accepted by`Tag()`

such as`[0x0010, 0x0010]`

,`(0x10, 0x10)`

,`0x00100010`

, etc. May also be a`slice`

made up of DICOM tags.**keep_deferred**(*bool**,**optional*) – If`True`

then when returning`RawDataElement`

do not perform the deferred read of the element’s value (accessing the value will return`None`

instead). Default`False`

.

- Returns:
The corresponding element.

- Return type:

-
get_private_item(
*group: int*,*element_offset: int*,*private_creator: str*) DataElement [source]¶ Return the data element for the given private tag group.

This is analogous to

`Dataset.__getitem__()`

, but only for private tags. This allows to find the private tag for the correct private creator without the need to add the tag to the private dictionary first.- Parameters:
- Returns:
The corresponding element.

- Return type:
- Raises:
**ValueError**– If group is not part of a private tag or private_creator is empty.**KeyError**– If the private creator tag is not found in the given group. If the private tag is not found.

-
group_dataset(
*group: int*) Dataset [source]¶ Return a

`Dataset`

containing only elements of a certain group.

-
*property*is_implicit_VR*: bool | None*¶ Get/set the VR method used when encoding the dataset.

Deprecated since version 3.0:

`is_implicit_VR`

will be removed in v4.0, set the*Transfer Syntax UID*or use the implicit_vr argument with`save_as()`

or`dcmwrite()`

instead.- Returns:
If the dataset has been created from scratch then returns

`None`

, otherwise returns the VR encoding method used by the decoded dataset.- Return type:
bool | None

-
*property*is_little_endian*: bool | None*¶ Get/set the endianness used when encoding the dataset.

Deprecated since version 3.0:

`is_little_endian`

will be removed in v4.0, set the*Transfer Syntax UID*or use the little_endian argument with`save_as()`

or`dcmwrite()`

instead.- Returns:
If the dataset has been created from scratch then returns

`None`

, otherwise returns the endianness of the encoding used by the decoded dataset.- Return type:
bool | None

-
*property*is_original_encoding*: bool*¶ Return

`True`

if the encoding to be used for writing is set and is the same as that used to originally encode the`Dataset`

.This includes properties related to endianness, VR handling and the (0008,0005)

*Specific Character Set*.

- items() Set[tuple[BaseTag, DataElement | RawDataElement]] [source]¶
Return the

`Dataset`

items to simulate`dict.items()`

.- Returns:
The top-level (

`BaseTag`

,`DataElement`

) items for the`Dataset`

.- Return type:
dict_items

- iterall() Iterator[DataElement] [source]¶
Iterate through the

`Dataset`

, yielding all the elements.Unlike

`iter(Dataset)`

, this*does*recurse into sequences, and so yields all elements as if dataset were “flattened”.- Yields:
*dataelem.DataElement*

-
*property*original_character_set*: str | MutableSequence[str]*¶ Return the original character set encoding for a dataset decoded from a file or buffer.

-
*property*original_encoding*: tuple[bool, bool] | tuple[None, None]*¶ Return the original encoding used for a dataset decoded from a file or buffer.

-
overlay_array(
*group: int*) ndarray [source]¶ Return the

*Overlay Data*in group as a`numpy.ndarray`

.- Parameters:
**group**(*int*) – The group number of the overlay data.- Returns:
The (group,3000)

*Overlay Data*converted to a`numpy.ndarray`

.- Return type:

-
*property*pixel_array*: ndarray*¶ Return the pixel data as a

`numpy.ndarray`

.Warning

This property requires NumPy and may require the installation of additional packages to perform the actual pixel data decoding. See the pixel data decompression documentation for more information.

Changed in version 3.0: The backend used for pixel data decoding has changed from the

`pixel_data_handlers`

module to the`pixels`

module. The behavior of the new backend is not backwards compatible with the old one, in particular the default color space should now be RGB when previously YCbCr data was returned.To revert to the deprecated

`pixel_data_handlers`

backend pass`use_v2_backend=True`

to the`pixel_array_options()`

method:>>> from pydicom import examples >>> ds = examples.ct >>> ds.pixel_array_options(use_v2_backend=True) >>> arr = ds.pixel_array

The

`pixel_data_handlers`

module and the use_v2_backend keyword argument will be removed in v4.0.- Returns:
The contents of the (7FE0,0008)

*Float Pixel Data*, (7FE0,0009)*Double Float Pixel Data*or (7FE0,0010)*Pixel Data*elements converted to a`numpy.ndarray`

. The array will be shaped as:(rows, columns) for single frame, single sample data

(rows, columns, samples) for single frame, multi-sample data

(frames, rows, columns) for multi-frame, single sample data

(frames, rows, columns, samples) for multi-frame, multi-sample data

When using the

`pydicom.pixels`

backend the decoding options used with the returned array can be customized via the`pixel_array_options()`

method.- Return type:

See also

`pydicom.pixels.pixel_array`

A function for returning the pixel data from the path to a dataset, a readable file-like containing a dataset or a

`Dataset`

instance. Can be used to minimize the memory required to return the pixel data when used with a path or file-like.`pydicom.pixels.iter_pixels`

Similar to

`pydicom.pixels.pixel_array()`

but returns a generator that iterates through the image frames.

-
pixel_array_options(
***,*index: int | None = None*,*raw: bool = False*,*decoding_plugin: str = ''*,*use_v2_backend: bool = False*,***kwargs: Any*) None [source]¶ Set the decoding and processing options used by the

`pixel_array`

property.Added in version 3.0.

Deprecated since version 3.0: The use_v2_backend keyword parameter will be removed in v4.0.

**Processing**The following processing operations on the raw pixel data will always be performed:

Natively encoded bit-packed pixel data for a bits allocated of

`1`

will be unpacked.Natively encoded pixel data with a photometric interpretation of

`"YBR_FULL_422"`

will have it’s sub-sampling removed.The output array will be reshaped to the specified dimensions.

JPEG-LS or JPEG 2000 encoded data whose signedness doesn’t match the expected pixel representation will be converted to match.

With the

`pydicom.pixels`

backend, if`raw = False`

(the default) then the following processing operation will also be performed:Pixel data with a photometric interpretation of

`"YBR_FULL"`

or`"YBR_FULL_422"`

will be converted to RGB.

Examples

Convert the

*Pixel Data*to an array that’s a view on the original buffer:>>> from pydicom import examples >>> ds = examples.ct >>> ds.pixel_array_options(view_only=True) >>> arr = ds.pixel_array

Use the deprecated

`pixel_data_handlers`

backend to convert the*Pixel Data*to an array:>>> from pydicom import examples >>> ds = examples.ct >>> ds.pixel_array_options(use_v2_backend=True) >>> arr = ds.pixel_array

- Parameters:
**index**(*int**|**None**,**optional*) – If`None`

(default) then return an array containing all the frames in the pixel data, otherwise return one containing only the frame from the specified index, which starts at 0 for the first frame. Only available with the`pixels`

backend.**raw**(*bool**,**optional*) – If`True`

then return the decoded pixel data after only minimal processing (see the processing section above). If`False`

(default) then additional processing may be applied to convert the pixel data to it’s most commonly used form (such as converting from YCbCr to RGB). Only available with the`pixels`

backend.**decoding_plugin**(*str**,**optional*) –The name of the decoding plugin to use when decoding compressed pixel data. If no decoding_plugin is specified (default) then all available plugins will be tried and the result from the first successful one returned. For information on the available plugins for each

*Transfer Syntax UID*:If using the

`pixels`

backend see the documentation for the decoder corresponding to the dataset’s*Transfer Syntax UID*.If using the

`pixel_data_handlers`

backend supported values are`'gdcm'`

,`'pillow'`

,`'jpeg_ls'`

,`'rle'`

,`'numpy'`

and`'pylibjpeg'`

.

**use_v2_backend**(*bool**,**optional*) – If`False`

(default) then use the`pydicom.pixels`

backend to decode the pixel data, otherwise use the deprecated`pydicom.pixel_data_handlers`

backend.****kwargs**– Optional keyword parameters for controlling decoding with the`pixels`

backend, please see the decoding options documentation for more information.

-
pop(
*key: BaseTag | TagType*,**args: Any*) DataElement | RawDataElement [source]¶ Emulate

`dict.pop()`

with support for tags and keywords.Removes the element for key if it exists and returns it, otherwise returns a default value if given or raises

`KeyError`

.- Parameters:
***args**(*zero**or**one argument*) – Defines the behavior if no tag exists for key: if given, it defines the return value, if not given,`KeyError`

is raised

- Returns:
The element for key if it exists, or the default value if given.

- Return type:
- Raises:
**KeyError**– If the key is not a valid tag or keyword. If the tag does not exist and no default is given.

- popitem() tuple[BaseTag, DataElement | RawDataElement] [source]¶
Emulate

`dict.popitem()`

.- Return type:
tuple of (BaseTag, DataElement)

-
private_block(
*group: int*,*private_creator: str*,*create: bool = False*) PrivateBlock [source]¶ Return the block for the given tag group and private_creator.

If create is

`True`

and the private_creator does not exist, the private creator tag is added.Notes

We ignore the unrealistic case that no free block is available.

- Parameters:
**group**(*int*) – The group of the private tag to be found as a 32-bit`int`

. Must be an odd number (e.g. a private group).**private_creator**(*str*) – The private creator string associated with the tag.**create**(*bool**,**optional*) – If`True`

and private_creator does not exist, a new private creator tag is added at the next free block. If`False`

(the default) and private_creator does not exist,`KeyError`

is raised instead.

- Returns:
The existing or newly created private block.

- Return type:
- Raises:
**ValueError**– If group doesn’t belong to a private tag or private_creator is empty.**KeyError**– If the private creator tag is not found in the given group and the create parameter is`False`

.

-
private_creators(
*group: int*) list[str] [source]¶ Return a list of private creator names in the given group.

Examples

This can be used to check if a given private creator exists in the group of the dataset:

>>> ds = Dataset() >>> if 'My Creator' in ds.private_creators(0x0041): ... block = ds.private_block(0x0041, 'My Creator')

- Parameters:
**group**(*int*) – The private group as a 32-bit`int`

. Must be an odd number.- Returns:
All private creator names for private blocks in the group.

- Return type:
- Raises:
**ValueError**– If group is not a private group.

-
*property*read_encoding*: str | MutableSequence[str]*¶ Return the original character set encoding for a decoded dataset.

Deprecated since version 3.0:

`read_encoding`

will be removed in v4.0, use`original_character_set`

instead.

-
*property*read_implicit_vr*: bool | None*¶ Get the VR method used by the original encoding of the dataset.

Deprecated since version 3.0:

`read_implicit_vr`

will be removed in v4.0, , use`original_encoding`

instead.- Returns:
Returns

`None`

if the dataset has been created from scratch, otherwise returns`True`

if the dataset was decoded from file or buffer and used implicit VR,`False`

if it used explicit VR.- Return type:
bool | None

-
*property*read_little_endian*: bool | None*¶ Get the endianness used by the original encoding of the dataset.

Deprecated since version 3.0:

`read_little_endian`

will be removed in v4.0, use`original_encoding`

instead.- Returns:
Returns

`None`

if the dataset has been created from scratch, otherwise returns`True`

if the dataset was decoded from file or buffer and used little endian encoding,`False`

for big endian.- Return type:
bool | None

-
save_as(
*filename: str | PathLike | BinaryIO | WriteableBuffer*,*/*,*_Dataset__write_like_original: bool | None = None*,***,*implicit_vr: bool | None = None*,*little_endian: bool | None = None*,*enforce_file_format: bool = False*,*overwrite: bool = True*,***kwargs: Any*) None [source]¶ Encode the current

`Dataset`

and write it to filename.See the documentation for

`dcmwrite()`

for more detailed information.Warning

Encoding a dataset with

`little_endian=False`

(i.e. as big endian) is not recommended. Big endian encoding was retired from the DICOM Standard in 2006.Warning

This function cannot be used to convert a decoded dataset to an encoding that uses a different endianness, such as from big to little endian.

`dcmwrite()`

must be used instead, however the process is not automatic. See the documentation of`dcmwrite()`

for details.Changed in version 3.0: Added implicit_vr, little_endian, enforce_file_format and overwrite keyword arguments

Deprecated since version 3.0: write_like_original will be removed in v4.0, please use enforce_file_format instead

- Parameters:
**filename**(*str**|**PathLike**|**BinaryIO*) – The path, file-like or writeable buffer to write the encoded dataset to. If using a buffer it must have`write()`

,`seek()`

and`tell()`

methods.**write_like_original**(*bool**,**optional*) – If`True`

(default) then write the dataset as-is, otherwise ensure that the dataset is written in the DICOM File Format or raise an exception is that isn’t possible. This parameter is deprecated, please use enforce_file_format instead.**implicit_vr**(*bool**,**optional*) – Required if the dataset has no valid public*Transfer Syntax UID*set in the file meta and`is_implicit_VR`

or`original_encoding`

are`None`

. If`True`

then encode using implicit VR, otherwise use explicit VR.**little_endian**(*bool**,**optional*) – Required if the dataset has no valid public*Transfer Syntax UID*set in the file meta and`is_little_endian`

or`original_encoding`

are`None`

. If`True`

(default) then use little endian byte order when encoding, otherwise use big endian (not recommended).**enforce_file_format**(*bool**,**optional*) –If

`True`

then ensure the dataset is written in the DICOM File Format or raise an exception if that isn’t possible. If`False`

(default) then write the dataset as-is, preserving the following - which may result in a non-conformant file:`Dataset.preamble`

: if the dataset has no preamble then none will be written`Dataset.file_meta`

: if the dataset is missing any required*File Meta Information Group*elements then they will not be added or written

**overwrite**(*bool**,**optional*) – If`False`

and filename is a`str`

or PathLike, then raise a`FileExistsError`

if a file already exists with the given filename (default`True`

).

See also

`pydicom.filewriter.dcmwrite`

Encode a

`Dataset`

and write it to a file or buffer.

-
set_original_encoding(
*is_implicit_vr: bool | None*,*is_little_endian: bool | None*,*character_encoding: str | MutableSequence[str] | None = None*) None [source]¶ Set the values for the original dataset encoding.

Can be used for a

`Dataset`

with raw data elements to enable optimized writing (e.g. without decoding the data elements).Changed in version 3.0: character_encoding is now optional

- Parameters:
**is_implicit_vr**(*bool**|**None*) – The the original VR encoding of the dataset,`True`

for implicit VR,`False`

for explicit VR or`None`

to reset.**is_little_endian**(*bool**|**None*) – Set the original endianness of the dataset,`True`

for little endian,`False`

for big or`None`

to reset.**character_encoding**(*str**|**MutableSequence**[**str**]**,**optional*) – Set the original character set encoding of the dataset. If`None`

then no changes will be made to the original character set encoding.

-
set_pixel_data(
*arr: ndarray*,*photometric_interpretation: str*,*bits_stored: int*,***,*generate_instance_uid: bool = True*) None [source]¶ Use an

`ndarray`

to set the*Pixel Data*and related Image Pixel module elements.Added in version 3.0.

The following Image Pixel module elements values will be added, updated or removed as necessary:

(0028,0002)

*Samples per Pixel*using a value corresponding to photometric_interpretation.(0028,0104)

*Photometric Interpretation*from photometric_interpretation.(0028,0006)

*Planar Configuration*will be added and set to`0`

if*Samples per Pixel*is > 1, otherwise it will be removed.(0028,0008)

*Number of Frames*from the array`shape`

, however it will be removed if arr only contains a single frame.(0028,0010)

*Rows*and (0028,0011)*Columns*from the array`shape`

.(0028,0100)

*Bits Allocated*from the array`dtype`

.(0028,0101)

*Bits Stored*and (0028,0102)*High Bit*from bits_stored.(0028,0103)

*Pixel Representation*from the array`dtype`

.

In addition:

The

*Transfer Syntax UID*will be set to*Explicit VR Little Endian*if it doesn’t already exist or uses a compressed (encapsulated) transfer syntax.If generate_instance_uid is

`True`

(default) then the*SOP Instance UID*will be added or updated.

- Parameters:
**arr**(*numpy.ndarray*) –An array with

`dtype`

uint8, uint16, int8 or int16. The array must be shaped as one of the following:(rows, columns) for a single frame of grayscale data.

(frames, rows, columns) for multi-frame grayscale data.

(rows, columns, samples) for a single frame of multi-sample data such as RGB.

(frames, rows, columns, samples) for multi-frame, multi-sample data.

**photometric_interpretation**(*str*) – The value to use for (0028,0004)*Photometric Interpretation*. Valid values are`"MONOCHROME1"`

,`"MONOCHROME2"`

,`"PALETTE COLOR"`

,`"RGB"`

,`"YBR_FULL"`

,`"YBR_FULL_422"`

.**bits_stored**(*int*) – The value to use for (0028,0101)*Bits Stored*. Must be no greater than the number of bits used by the`itemsize`

of arr.**generate_instance_uid**(*bool**,**optional*) – If`True`

(default) then add or update the (0008,0018)*SOP Instance UID*element with a value generated using`generate_uid()`

.

- Raises:
**NotImplementedError**– If the dataset has a big-endian*Transfer Syntax UID*.

-
setdefault(
*key: int | str | tuple[int, int] | BaseTag*,*default: Any | None = None*) DataElement [source]¶ Emulate

`dict.setdefault()`

with support for tags and keywords.Examples

>>> ds = Dataset() >>> elem = ds.setdefault((0x0010, 0x0010), "Test") >>> elem (0010,0010) Patient's Name PN: 'Test' >>> elem.value 'Test' >>> elem = ds.setdefault('PatientSex', ... DataElement(0x00100040, 'CS', 'F')) >>> elem.value 'F'

- Parameters:
**default**(*pydicom.dataelem.DataElement**or**object**,**optional*) – The`DataElement`

to use with key, or the value of the`DataElement`

to use with key (default`None`

).

- Returns:
The

`DataElement`

for key.- Return type:
- Raises:
**ValueError**– If key is not convertible to a valid tag or a known element keyword.**KeyError**– If`reading_validation_mode`

is`RAISE`

and key is an unknown non-private tag.

-
to_json(
*bulk_data_threshold: int = 1024*,*bulk_data_element_handler: Callable[[DataElement], str] | None = None*,*dump_handler: Callable[[dict[str, Any]], str] | None = None*,*suppress_invalid_tags: bool = False*) str [source]¶ Return a JSON representation of the

`Dataset`

.See the DICOM Standard, Part 18, Annex F.

- Parameters:
**bulk_data_threshold**(*int**,**optional*) – Threshold for the length of a base64-encoded binary data element above which the element should be considered bulk data and the value provided as a URI rather than included inline (default:`1024`

). Ignored if no bulk data handler is given.**bulk_data_element_handler**(*callable**,**optional*) – Callable function that accepts a bulk data element and returns a JSON representation of the data element (dictionary including the “vr” key and either the “InlineBinary” or the “BulkDataURI” key).**dump_handler**(*callable**,**optional*) –Callable function that accepts a

`dict`

and returns the serialized (dumped) JSON string (by default uses`json.dumps()`

).**suppress_invalid_tags**(*bool**,**optional*) – Flag to specify if errors while serializing tags should be logged and the tag dropped or if the error should be bubbled up.

- Returns:
`Dataset`

serialized into a string based on the DICOM JSON Model.- Return type:

Examples

>>> def my_json_dumps(data): ... return json.dumps(data, indent=4, sort_keys=True) >>> ds.to_json(dump_handler=my_json_dumps)

-
to_json_dict(
*bulk_data_threshold: int = 1024*,*bulk_data_element_handler: Callable[[DataElement], str] | None = None*,*suppress_invalid_tags: bool = False*) dict[str, Any] [source]¶ Return a dictionary representation of the

`Dataset`

conforming to the DICOM JSON Model as described in the DICOM Standard, Part 18, Annex F.- Parameters:
**bulk_data_threshold**(*int**,**optional*) – Threshold for the length of a base64-encoded binary data element above which the element should be considered bulk data and the value provided as a URI rather than included inline (default:`1024`

). Ignored if no bulk data handler is given.**bulk_data_element_handler**(*callable**,**optional*) – Callable function that accepts a bulk data element and returns a JSON representation of the data element (dictionary including the “vr” key and either the “InlineBinary” or the “BulkDataURI” key).**suppress_invalid_tags**(*bool**,**optional*) – Flag to specify if errors while serializing tags should be logged and the tag dropped or if the error should be bubbled up.

- Returns:
`Dataset`

representation based on the DICOM JSON Model.- Return type:

- trait_names() list[str] [source]¶
Return a

`list`

of valid names for auto-completion code.Used in IPython, so that data element names can be found and offered for autocompletion on the IPython command line.

-
update(
*d: Dataset | MutableMapping[BaseTag, DataElement | RawDataElement]*) None [source]¶ Extend

`dict.update()`

to handle DICOM tags and keywords.

-
update_raw_element(
*tag: int | str | tuple[int, int] | BaseTag*,***,*vr: str | None = None*,*value: bytes | None = None*) None [source]¶ Modify the VR or value for the raw element with tag.

When a

`Dataset`

is created most of it’s elements are in their`RawDataElement`

form, and only upon trying to access the element is it converted to a`DataElement`

. When this conversion fails due to non-conformance issues, this method can be used to modify the raw element data prior to conversion in order to fix any issues.Example

Change the VR for the element with tag (0029,1026) before conversion to

`DataElement`

.>>> from pydicom import examples >>> ds = examples.ct >>> ds.update_raw_element(0x00291026, vr="US") >>> elem = ds[0x00291026] # conversion to DataElement occurs here >>> type(elem) <class 'pydicom.dataelem.DataElement'> >>> elem.VR "US"

- Parameters:
**tag**(*int**|**str**|**tuple**[**int**,**int**]**|**BaseTag*) – The tag for a`RawDataElement`

in the dataset.**vr**(*str**,**optional*) – Required if value is not used, the value to use for the modified element’s VR, if not used then the existing VR will be kept.**value**(*bytes**,**optional*) – Required if vr is not used, the value to use for the modified element’s raw encoded value, if not used then the existing value will be kept.

- values() ValuesView[DataElement | RawDataElement] [source]¶
Return the

`Dataset`

values to simulate`dict.values()`

.- Returns:
The

`DataElements`

that make up the values of the`Dataset`

.- Return type:
dict_keys

-
walk(
*callback: Callable[[Dataset, DataElement], None]*,*recursive: bool = True*) None [source]¶ Iterate through the

`Dataset's`

elements and run callback on each.Visit all elements in the

`Dataset`

, possibly recursing into sequences and their items. The callback function is called for each`DataElement`

(including elements with a VR of ‘SQ’). Can be used to perform an operation on certain types of elements.For example,

`remove_private_tags()`

finds all elements with private tags and deletes them.The elements will be returned in order of increasing tag number within their current

`Dataset`

.- Parameters:
**callback**–A callable function that takes two arguments:

a

`Dataset`

a

`DataElement`

belonging to that`Dataset`

**recursive**(*bool**,**optional*) – Flag to indicate whether to recurse into sequences (default`True`

).

-
waveform_array(
*index: int*) ndarray [source]¶ Return an

`ndarray`

for the multiplex group at index in the (5400,0100)*Waveform Sequence*.Added in version 2.1.

- Parameters:
**index**(*int*) – The index of the multiplex group to return the array for.- Returns:
The

*Waveform Data*for the multiplex group as an`ndarray`

with shape (samples, channels). If (003A,0210)*Channel Sensitivity*is present then the values will be in the units specified by the (003A,0211)*Channel Sensitivity Units Sequence*.- Return type:

See also

## Source: https://pydicom.github.io/pydicom/stable/reference/charset.html

# Character Encoding and Decoding (`pydicom.charset`

)¶

Character encoding and decoding functions.

|
Convert DICOM encodings into corresponding Python encodings. |
|
Apply the DICOM character encoding to a data element |
|
Decode an encoded byte value into a unicode string using encodings. |
|
Encode a unicode string value into |

## Source: https://pydicom.github.io/pydicom/stable/reference/config.html

# Configuration Options (`pydicom.config`

)¶

*pydicom* configuration options

-
*class*pydicom.config.Settings[source]¶ Collection of several configuration values. Accessed via the singleton

`settings`

.Added in version 2.3.

-
*property*buffered_read_size*: int*¶ Get or set the chunk size when reading from buffered

`DataElement`

values.- Parameters:
**size**(*int*) – The chunk size to use, must be greater than 0 (default 8192).

-
*property*infer_sq_for_un_vr*: bool*¶ If

`True`

, and the VR of a known data element is encoded as**UN**in an explicit encoding for an undefined length data element, the VR is changed to SQ per PS 3.5, section 6.2.2. Can be set to`False`

where the content of the tag shown as**UN**is not DICOM conformant and would lead to a failure if accessing it.

-
*property*reading_validation_mode*: int*¶ Defines behavior of validation while reading values, compared with the DICOM standard, e.g. that DS strings are not longer than 16 characters and contain only allowed characters.

-
*property*writing_validation_mode*: int*¶ Defines behavior for value validation while writing a value. See

`Settings.reading_validation_mode`

.

-

The global configuration object of type |
|
Set to |
|
If invalid VR encountered, assume file switched to implicit VR |
|
Convert a field VR to "UN" and return bytes if bytes length is invalid. |
|
Set to a callable function to be called from |
|
Set the keyword arguments passed to |
|
Set to |
|
|
Turn on/off debugging of DICOM file reading and writing. |
Deprecated. |
|
|
Imitate the behavior for the next major version of |
Handlers for converting (7FE0,0010) |
|
Reset the |
|
If |
|
|
Set DS class to be derived from |
|
Set whether multi-valued elements with VR of |
Set using |
|
Set to False to avoid IS values being returned as numpy ndarray objects. |
|
Set using the function |
|
Use the information within JPEG 2000 data to correct the returned pixel data |
|
Control the behavior when invalid keys are used with |
|
Control the behavior when setting a |
|
If one of the validation modes is set to this value, no value validation will be performed. |
|
If one of the validation modes is set to this value, a warning is issued if a value validation error occurs. |
|
If one of the validation modes is set to this value, an exception is raised if a value validation error occurs. |

## Source: https://pydicom.github.io/pydicom/stable/reference/data.html

# Getting Included Datasets (`pydicom.data`

)¶

Getting datasets included with *pydicom*

|
Return a list of absolute paths to charsets with filenames matching pattern. |
|
Return a list of absolute paths to palettes with filenames matching pattern. |
|
Return an absolute path to the first matching dataset with filename name that is found in a local or external pydicom datastore. |
|
Return a list of absolute paths to datasets with filenames matching pattern. |

## Source: https://pydicom.github.io/pydicom/stable/reference/datadict.html

# Data Dictionary Utilities (`pydicom.datadict`

)¶

Data dictionary functions

## DICOM Data Dictionary¶

|
Update the DICOM dictionary with new non-private entries. |
|
Update the DICOM dictionary with a new non-private entry. |
Return the description of the element corresponding to tag. |
|
|
Return |
Return |
|
|
Return the keyword of the element corresponding to tag. |
|
Return the VM of the element corresponding to tag. |
|
Return the VR of the element corresponding to tag. |
|
Return an entry from the DICOM dictionary as a tuple. |
|
Return the keyword of the element corresponding to tag. |
|
Return the repeaters tag mask for tag. |
|
Return |
|
Return |
|
Return the tag of the element corresponding to keyword. |

## Private Data Dictionary¶

|
Update pydicom's private DICOM tag dictionary with new entries. |
|
Update the private DICOM dictionary with a new entry. |
|
Return an entry from the private dictionary corresponding to tag. |
|
Return the description of the private element corresponding to tag. |
|
Return the VM of the private element corresponding to tag. |
|
Return the VR of the private element corresponding to tag. |

## Source: https://pydicom.github.io/pydicom/stable/reference/dataset.html

# Representation of Datasets (`pydicom.dataset`

)¶

Representation of DICOM datasets and related functions.

|
A DICOM dataset as a mutable mapping of DICOM Data Elements. |
|
An extension of |
|
Contains a collection (dictionary) of group 2 DICOM Data Elements. |
|
Helper class for a private block in the |
|
Validate the |

## Source: https://pydicom.github.io/pydicom/stable/reference/elem.html

# Representation of Data Elements¶

- Data Elements (
`pydicom.dataelem`

) - Element Tags (
`pydicom.tag`

) - Element Value Decoding (
`pydicom.values`

)- pydicom.values.convert_AE_string
- pydicom.values.convert_ATvalue
- pydicom.values.convert_DA_string
- pydicom.values.convert_DS_string
- pydicom.values.convert_DT_string
- pydicom.values.convert_IS_string
- pydicom.values.convert_numbers
- pydicom.values.convert_OBvalue
- pydicom.values.convert_OWvalue
- pydicom.values.convert_PN
- pydicom.values.convert_single_string
- pydicom.values.convert_SQ
- pydicom.values.convert_string
- pydicom.values.convert_tag
- pydicom.values.convert_text
- pydicom.values.convert_TM_string
- pydicom.values.convert_UI
- pydicom.values.convert_UN
- pydicom.values.convert_UR_string
- pydicom.values.convert_value
- pydicom.values.multi_string

- Element Multi-value Representation (
`pydicom.multival`

) - Sequence Element Value Representation (
`pydicom.sequence`

) - Specialized Element Value Representation (
`pydicom.valuerep`

)

## Source: https://pydicom.github.io/pydicom/stable/reference/examples.html

# Example Datasets (`pydicom.examples`

)¶

The `examples`

module contains the following DICOM datasets:

Module Attribute |
File |
SOP Class |
|---|---|---|
|
|
CT Image |
|
|
MR Image |
|
|
RT Plan |
|
|
RT Dose |
|
|
RT Structure Set |
|
|
MR Image |
|
|
12 Lead ECG |
|
|
US Image |
|
|
US Image |
|
|
US Multi-frame Image |
|
|
US Image |
|
|
Media Storage |

As well as the utility function:

|
Return the path to the example dataset with the attribute name name as |

## Usage¶

The module attributes are all normal `FileDataset`

instances:

```
>>> from pydicom import examples
>>> type(examples.ct)
<class 'pydicom.dataset.FileDataset'>
>>> examples.ct.PatientName
'CompressedSamples^CT1'
```

Each time the module attribute is accessed a new
`FileDataset`

instance of the dataset will be returned:

```
>>> examples.ct is examples.ct
False
>>> examples.ct == examples.ct
True
```

Because of this, best practice is to assign the returned dataset to a local variable:

```
>>> ds = examples.ct
```

The `get_path()`

function can be used to return the path
to an example dataset as a `pathlib.Path`

instance:

```
>>> examples.get_path("ct")
PosixPath('/home/user/pydicom/src/pydicom/data/test_files/CT_small.dcm')
```

## Source: https://pydicom.github.io/pydicom/stable/reference/encaps.html

# Bulk Data Encapsulation Utilities (`pydicom.encaps`

)¶

Functions for parsing and applying encapsulation to bulk data elements such
as (7FE0,0010) *Pixel Data*.

## Parsing Encapsulated Data¶

|
Read encapsulated data and return a list of bytes. |
|
Read encapsulated data and return the fragments as one continuous bytes. |
|
Yield an encapsulated pixel data frame. |
Yield the encapsulated pixel data fragments. |
|
|
Yield complete frames from buffer as |
Return a list of the fragment offsets from the Basic Offset Table. |
|
|
Read and return a single Item in the fragmented data stream. |
|
Return the encapsulated pixel data's basic offset table frame offsets. |
|
Return the number of fragments and their positions in buffer. |
|
Yield frame fragments from the encapsulated pixel data in buffer. |
|
Yield fragmented pixel data frames from buffer. |
|
Yield complete pixel data frames from buffer. |
|
Return the specified frame at index. |

## Creating Encapsulated Data¶

|
Return encapsulated frames. |
|
Return an |
|
Return encapsulated image data and values for the Extended Offset Table elements. |
|
Return |
|
Yield one or more fragments from frame. |
|
Return an itemized fragment. |
|
Yield items generated from frame. |

Management class for encapsulating buffers:

-
*class*pydicom.encaps.EncapsulatedBuffer(*buffers: list[BufferedIOBase]*,*use_bot: bool = False*)[source]¶ Convenience class for managing the encapsulation of one or more buffers containing compressed

*Pixel Data*.Added in version 3.0.

-
*property*extended_lengths*: bytes*¶ Return an encoded

*Extended Offset Table Lengths*value from lengths- Returns:
The encoded lengths of the frame.

- Return type:

-
*property*extended_offsets*: bytes*¶ Return an encoded

*Extended Offset Table*value from offsets- Returns:
The encoded offsets to the first byte of the item tag of the first fragment for every frame, as measured from the first byte of the first item tag following the empty Basic Offset Table Item.

- Return type:

-
*property*offsets*: list[int]*¶ Return the encapsulated item offsets, starting at 0 for the first item.

-
read(
*size: int | None = 8192*,*/*) bytes [source]¶ Read up to size bytes of data from the encapsulated buffers.

-

## Source: https://pydicom.github.io/pydicom/stable/reference/errors.html

Getting started

Documentation

pydicom.charset

pydicom.config

pydicom.data

pydicom.datadict

pydicom.dataset

pydicom.examples

pydicom.encaps

pydicom.errors

pydicom.fileset

pydicom.hooks

pydicom.misc

pydicom.overlays

pydicom.pixels

pydicom.sr

pydicom.waveforms

pydicom.uid

Examples

Additional Information

InvalidDicomError(*args)

InvalidDicomError

Exception that is raised when the the file does not appear to be DICOM.

## Source: https://pydicom.github.io/pydicom/stable/reference/fileio.html

# Dataset IO¶

Reading and writing DICOM datasets and support classes and functions.

- Dataset Reading (
`pydicom.filereader`

)- pydicom.filereader.data_element_generator
- pydicom.filereader.data_element_offset_to_value
- pydicom.filereader.dcmread
- pydicom.filereader.read_dataset
- pydicom.filereader.read_deferred_data_element
- pydicom.filereader.read_file_meta_info
- pydicom.filereader.read_partial
- pydicom.filereader.read_preamble
- pydicom.filereader.read_sequence
- pydicom.filereader.read_sequence_item

- Dataset Writing (
`pydicom.filewriter`

)- pydicom.filewriter.correct_ambiguous_vr
- pydicom.filewriter.correct_ambiguous_vr_element
- pydicom.filewriter.dcmwrite
- pydicom.filewriter.multi_string
- pydicom.filewriter.write_ATvalue
- pydicom.filewriter.write_DA
- pydicom.filewriter.write_dataset
- pydicom.filewriter.write_data_element
- pydicom.filewriter.write_DT
- pydicom.filewriter.write_file_meta_info
- pydicom.filewriter.write_numbers
- pydicom.filewriter.write_number_string
- pydicom.filewriter.write_OBvalue
- pydicom.filewriter.write_OWvalue
- pydicom.filewriter.write_PN
- pydicom.filewriter.write_sequence
- pydicom.filewriter.write_sequence_item
- pydicom.filewriter.write_string
- pydicom.filewriter.write_text
- pydicom.filewriter.write_TM
- pydicom.filewriter.write_UI
- pydicom.filewriter.write_UN

- IO Base Classes (
`pydicom.filebase`

) - IO Utilities (
`pydicom.fileutil`

)

## Source: https://pydicom.github.io/pydicom/stable/reference/fileset.html

# DICOM File-sets (`pydicom.fileset`

)¶

Representation of DICOM File-sets.

|
Representation of a DICOMDIR's directory record. |
|
Representation of a File in the File-set. |
|
Representation of a DICOM File-set. |
|
Yield File IDs for a File-set. |
|
Return |
A |

## Source: https://pydicom.github.io/pydicom/stable/reference/handlers.html

Getting started

Documentation

pydicom.charset

pydicom.config

pydicom.data

pydicom.datadict

pydicom.dataset

pydicom.examples

pydicom.encaps

pydicom.errors

pydicom.fileset

pydicom.pixel_data_handlers

pydicom.hooks

pydicom.misc

pydicom.overlays

pydicom.pixels

pydicom.sr

pydicom.waveforms

pydicom.uid

Examples

Additional Information

Deprecated since version 3.0: The pydicom.pixel_data_handlers module is deprecated and will be removed in v4.0. Use the pixels module instead.

pixels

Functions for handling bulk data elements such as (7FE0,0010) Pixel Data

## Source: https://pydicom.github.io/pydicom/stable/reference/hooks.html

# User Hooks (`pydicom.hooks`

)¶

Hooks manager class and instance

The global |
|
|
Management class for callback functions. |

Hooks for `convert_raw_data_element()`

|
Determine the VR to use for raw. |
|
Convert the encoded value for raw to an appropriate type. |
|
Convenience function to fix values with an invalid multivalue separator. |
|
Convenience function to retry value conversion using a different VR. |

## Source: https://pydicom.github.io/pydicom/stable/reference/misc.html

# Miscellaneous (`pydicom.misc`

)¶

Miscellaneous functions.

|
Return |
|
Return the number of bytes for defer_size argument in |

`pydicom.misc`

)¶Miscellaneous functions.

|
Return |
|
Return the number of bytes for defer_size argument in |

## Source: https://pydicom.github.io/pydicom/stable/reference/overlays.html

Getting started

Documentation

pydicom.charset

pydicom.config

pydicom.data

pydicom.datadict

pydicom.dataset

pydicom.examples

pydicom.encaps

pydicom.errors

pydicom.fileset

pydicom.hooks

pydicom.misc

pydicom.overlays

pydicom.pixels

pydicom.sr

pydicom.waveforms

pydicom.uid

Examples

Additional Information

numpy_handler

Use the numpy package to convert supported Overlay Data to a numpy.ndarray.

numpy.ndarray

## Source: https://pydicom.github.io/pydicom/stable/reference/pixels.html

# Pixel Data (`pydicom.pixels`

)¶

Image processing functions

|
Apply a color palette lookup table to arr. |
|
Apply an ICC Profile to arr, either from the dataset ds or an existing Pillow color transformation object transform. |
|
Apply a modality lookup table or rescale operation to arr. |
|
Apply a Presentation LUT to arr and return the P-values. |
|
Apply a modality lookup table or rescale operation to arr. |
|
Apply a VOI lookup table or windowing operation to arr. |
|
Apply a VOI lookup table to arr. |
|
Apply a windowing operation to arr. |
|
Convert the image(s) in arr from one color space to another. |
|
Return a Pillow color transformation object from either the dataset ds or an ICC profile icc_profile. |

Utility functions

|
Return a dict containing the image pixel element values from ds. |
|
Compress uncompressed pixel data and update ds in-place with the resulting encapsulated codestream. |
|
Perform an in-place decompression of a dataset with a compressed |
|
Return the pixel data decoder corresponding to uid. |
|
Return the pixel data encoder corresponding to uid. |
|
Yield decoded pixel data frames from src as |
|
Pack a binary |
|
Return decoded pixel data from src as |
|
Use an |
|
Unpack the bit-packed data in src. |

## Source: https://pydicom.github.io/pydicom/stable/reference/sr.html

# Concepts and Context Groups (`pydicom.sr`

)¶

The `sr`

module contains an interface for DICOM’s CIDs.

|
Interface for a collection of concepts, such as SNOMED-CT, or a DICOM CID. |
|
Management class for the available concept collections. |
|
Namedtuple for representation of a coded concept consisting of the actual code |

## Usage¶

Individual `Code`

values can be accessed via either
their scheme (such as SCT) or the DICOM CID:

```
>>> from pydicom.sr import codes
>>> codes.SCT.Transverse
Code(value='62824007', scheme_designator='SCT', meaning='Transverse', scheme_version=None)
>>> codes.CID4.Cornea
Code(value='28726007', scheme_designator='SCT', meaning='Cornea', scheme_version=None)
```

A list of available attribute keywords for each scheme or CID is available via
`dir()`

:

```
>>> dir(codes.CID6)
['Coronal', 'FiveChamber', 'FourChamber', ... ]
```

## Source: https://pydicom.github.io/pydicom/stable/reference/waveforms.html

Getting started

Documentation

pydicom.charset

pydicom.config

pydicom.data

pydicom.datadict

pydicom.dataset

pydicom.examples

pydicom.encaps

pydicom.errors

pydicom.fileset

pydicom.hooks

pydicom.misc

pydicom.overlays

pydicom.pixels

pydicom.sr

pydicom.waveforms

pydicom.uid

Examples

Additional Information

numpy_handler

Use the numpy package to convert supported Waveform Data to a numpy.ndarray.

numpy.ndarray

## Source: https://pydicom.github.io/pydicom/stable/reference/uid.html

# UID Definitions and Utilities (`pydicom.uid`

)¶

## Transfer Syntax UIDs¶

1.2.840.10008.1.2 |
|
1.2.840.10008.1.2.1 |
|
1.2.840.10008.1.2.1.99 |
|
1.2.840.10008.1.2.2 |
|
1.2.840.10008.1.2.4.50 |
|
1.2.840.10008.1.2.4.51 |
|
1.2.840.10008.1.2.4.57 |
|
1.2.840.10008.1.2.4.70 |
|
1.2.840.10008.1.2.4.80 |
|
1.2.840.10008.1.2.4.81 |
|
1.2.840.10008.1.2.4.90 |
|
1.2.840.10008.1.2.4.91 |
|
1.2.840.10008.1.2.4.92 |
|
1.2.840.10008.1.2.4.93 |
|
1.2.840.10008.1.2.4.100 |
|
1.2.840.10008.1.2.4.100.1 |
|
1.2.840.10008.1.2.4.101 |
|
1.2.840.10008.1.2.4.101.1 |
|
1.2.840.10008.1.2.4.102 |
|
1.2.840.10008.1.2.4.102.1 |
|
1.2.840.10008.1.2.4.103 |
|
1.2.840.10008.1.2.4.103.1 |
|
1.2.840.10008.1.2.4.104 |
|
1.2.840.10008.1.2.4.104.1 |
|
1.2.840.10008.1.2.4.105 |
|
1.2.840.10008.1.2.4.105.1 |
|
1.2.840.10008.1.2.4.106 |
|
1.2.840.10008.1.2.4.106.1 |
|
1.2.840.10008.1.2.4.107 |
|
1.2.840.10008.1.2.4.108 |
|
1.2.840.10008.1.2.5 |
|
1.2.840.10008.1.2.4.201 |
|
1.2.840.10008.1.2.4.202 |
|
1.2.840.10008.1.2.4.203 |
|
1.2.840.10008.1.2.4.204 |
|
1.2.840.10008.1.2.4.205 |
|
1.2.840.10008.1.2.7.1 |
|
1.2.840.10008.1.2.7.2 |
|
1.2.840.10008.1.2.7.3 |

## Transfer Syntax Lists¶

All non-retired transfer syntaxes and |
|
JPEG (ISO/IEC 10918-1) transfer syntaxes |
|
JPEG-LS (ISO/IEC 14495-1) transfer syntaxes. |
|
JPEG 2000 (ISO/IEC 15444-1) transfer syntaxes. |
|
MPEG transfer syntaxes. |
|
RLE transfer syntaxes. |
|
Uncompressed (native) transfer syntaxes. |
|
Private transfer syntaxes added using the |

## UID Utilities¶

|
Return a 64 character UID which starts with prefix. |
|
Register a private transfer syntax with the |
pydicom's root UID |
|
pydicom's (0002,0012) |
|
Regex for a valid UID |
|
Regex for a valid UID prefix |
|
|
Human friendly UIDs as a Python |

## Storage SOP Class UIDs¶

1.2.840.10008.5.1.4.1.1.88.71 |
|
1.2.840.10008.5.1.4.1.1.11.8 |
|
1.2.840.10008.5.1.4.1.1.9.1.3 |
|
1.2.840.10008.5.1.4.1.1.9.5.1 |
|
1.2.840.10008.5.1.4.1.1.78.2 |
|
1.2.840.10008.5.1.4.1.1.131 |
|
1.2.840.10008.5.1.4.1.1.88.11 |
|
1.2.840.10008.5.1.4.1.1.9.4.1 |
|
1.2.840.10008.5.1.4.1.1.11.4 |
|
1.2.840.10008.5.1.4.1.1.9.8.1 |
|
1.2.840.10008.5.1.4.1.1.13.1.4 |
|
1.2.840.10008.5.1.4.1.1.13.1.5 |
|
1.2.840.10008.5.1.4.1.1.13.1.3 |
|
1.2.840.10008.5.1.4.1.1.481.19 |
|
1.2.840.10008.5.1.4.1.1.481.13 |
|
1.2.840.10008.5.1.4.1.1.200.1 |
|
1.2.840.10008.5.1.4.1.1.2 |
|
1.2.840.10008.5.1.4.1.1.200.2 |
|
1.2.840.10008.5.1.4.1.1.9.3.1 |
|
1.2.840.10008.5.1.4.1.1.88.65 |
|
1.2.840.10008.5.1.4.1.1.88.69 |
|
1.2.840.10008.5.1.4.39.1 |
|
1.2.840.10008.5.1.4.1.1.11.2 |
|
1.2.840.10008.5.1.4.1.1.11.7 |
|
1.2.840.10008.5.1.4.1.1.88.34 |
|
1.2.840.10008.5.1.4.1.1.88.33 |
|
1.2.840.10008.5.1.4.1.1.1 |
|
1.2.840.10008.5.1.4.1.1.77.1.8 |
|
1.2.840.10008.5.1.4.1.1.77.1.9 |
|
1.2.840.10008.5.1.4.1.1.90.1 |
|
1.2.840.10008.5.1.4.1.1.82.1 |
|
1.2.840.10008.5.1.4.1.1.501.4 |
|
1.2.840.10008.5.1.4.1.1.501.5 |
|
1.2.840.10008.5.1.4.1.1.501.1 |
|
1.2.840.10008.5.1.4.1.1.501.2.1 |
|
1.2.840.10008.5.1.4.1.1.501.2.2 |
|
1.2.840.10008.5.1.4.1.1.501.6 |
|
1.2.840.10008.5.1.4.1.1.501.3 |
|
1.2.840.10008.5.1.4.1.1.66.3 |
|
1.2.840.10008.5.1.4.1.1.77.1.7 |
|
1.2.840.10008.5.1.4.1.1.1.3 |
|
1.2.840.10008.5.1.4.1.1.1.3.1 |
|
1.2.840.10008.5.1.4.1.1.1.2 |
|
1.2.840.10008.5.1.4.1.1.1.2.1 |
|
1.2.840.10008.5.1.4.1.1.1.1 |
|
1.2.840.10008.5.1.4.1.1.1.1.1 |
|
1.2.840.10008.5.1.4.1.1.601.1 |
|
1.2.840.10008.5.1.4.1.1.601.2 |
|
1.2.840.10008.5.1.4.1.1.9.7.2 |
|
1.2.840.10008.5.1.4.1.1.9.7.3 |
|
1.2.840.10008.5.1.4.1.1.104.2 |
|
1.2.840.10008.5.1.4.1.1.104.5 |
|
1.2.840.10008.5.1.4.1.1.104.4 |
|
1.2.840.10008.5.1.4.1.1.104.1 |
|
1.2.840.10008.5.1.4.1.1.104.3 |
|
1.2.840.10008.5.1.4.1.1.2.1 |
|
1.2.840.10008.5.1.4.1.1.481.24 |
|
1.2.840.10008.5.1.4.1.1.4.3 |
|
1.2.840.10008.5.1.4.1.1.4.1 |
|
1.2.840.10008.5.1.4.1.1.130 |
|
1.2.840.10008.5.1.4.1.1.481.23 |
|
1.2.840.10008.5.1.4.1.1.88.22 |
|
1.2.840.10008.5.1.4.1.1.6.2 |
|
1.2.840.10008.5.1.4.1.1.12.1.1 |
|
1.2.840.10008.5.1.4.1.1.12.2.1 |
|
1.2.840.10008.5.1.4.1.1.88.76 |
|
1.2.840.10008.5.1.4.1.1.88.35 |
|
1.2.840.10008.5.1.4.1.1.9.1.4 |
|
1.2.840.10008.5.1.4.1.1.9.4.2 |
|
1.2.840.10008.5.1.4.1.1.9.1.2 |
|
1.2.840.10008.5.1.4.43.1 |
|
1.2.840.10008.5.1.4.1.1.11.6 |
|
1.2.840.10008.5.1.4.1.1.11.1 |
|
1.2.840.10008.5.1.4.38.1 |
|
1.2.840.10008.5.1.4.1.1.9.2.1 |
|
1.2.840.10008.5.1.4.44.1 |
|
1.2.840.10008.5.1.4.45.1 |
|
1.2.840.10008.5.1.4.1.1.88.70 |
|
1.2.840.10008.5.1.4.1.1.78.8 |
|
|
1.2.840.10008.5.1.4.1.1.14.1 |
|
1.2.840.10008.5.1.4.1.1.14.2 |
1.2.840.10008.5.1.4.1.1.201.1 |
|
1.2.840.10008.5.1.4.1.1.78.3 |
|
1.2.840.10008.5.1.4.1.1.88.59 |
|
1.2.840.10008.5.1.4.1.1.2.2 |
|
1.2.840.10008.5.1.4.1.1.4.4 |
|
1.2.840.10008.5.1.4.1.1.128.1 |
|
1.2.840.10008.5.1.4.1.1.78.1 |
|
1.2.840.10008.5.1.4.1.1.4 |
|
1.2.840.10008.5.1.4.1.1.4.2 |
|
1.2.840.10008.5.1.4.1.1.79.1 |
|
1.2.840.10008.5.1.4.1.1.88.50 |
|
1.2.840.10008.1.3.10 |
|
1.2.840.10008.5.1.4.1.1.91.1 |
|
1.2.840.10008.5.1.4.1.1.7.2 |
|
1.2.840.10008.5.1.4.1.1.7.3 |
|
1.2.840.10008.5.1.4.1.1.7.1 |
|
1.2.840.10008.5.1.4.1.1.7.4 |
|
1.2.840.10008.5.1.4.1.1.9.6.2 |
|
1.2.840.10008.5.1.4.1.1.11.11 |
|
1.2.840.10008.5.1.4.1.1.20 |
|
1.2.840.10008.5.1.4.1.1.78.7 |
|
|
1.2.840.10008.5.1.4.1.1.77.1.5.8 |
1.2.840.10008.5.1.4.1.1.77.1.5.7 |
|
1.2.840.10008.5.1.4.1.1.77.1.5.2 |
|
1.2.840.10008.5.1.4.1.1.77.1.5.1 |
|
1.2.840.10008.5.1.4.1.1.81.1 |
|
1.2.840.10008.5.1.4.1.1.77.1.5.4 |
|
1.2.840.10008.5.1.4.1.1.80.1 |
|
1.2.840.10008.5.1.4.1.1.30 |
|
1.2.840.10008.5.1.4.1.1.88.73 |
|
1.2.840.10008.5.1.4.1.1.88.75 |
|
1.2.840.10008.5.1.4.1.1.6.3 |
|
1.2.840.10008.5.1.4.1.1.88.74 |
|
1.2.840.10008.5.1.4.1.1.128 |
|
1.2.840.10008.5.1.4.1.1.88.40 |
|
1.2.840.10008.5.1.4.1.1.200.3 |
|
1.2.840.10008.5.1.4.1.1.11.3 |
|
1.2.840.10008.5.1.4.34.7 |
|
1.2.840.10008.5.1.4.1.1.481.4 |
|
1.2.840.10008.5.1.4.34.10 |
|
1.2.840.10008.5.1.4.1.1.481.6 |
|
1.2.840.10008.5.1.4.1.1.481.2 |
|
1.2.840.10008.5.1.4.1.1.481.1 |
|
1.2.840.10008.5.1.4.1.1.481.9 |
|
1.2.840.10008.5.1.4.1.1.481.8 |
|
1.2.840.10008.5.1.4.1.1.481.25 |
|
1.2.840.10008.5.1.4.1.1.481.10 |
|
1.2.840.10008.5.1.4.1.1.481.5 |
|
1.2.840.10008.5.1.4.1.1.481.16 |
|
1.2.840.10008.5.1.4.1.1.481.17 |
|
1.2.840.10008.5.1.4.1.1.481.21 |
|
1.2.840.10008.5.1.4.1.1.481.12 |
|
1.2.840.10008.5.1.4.1.1.481.11 |
|
1.2.840.10008.5.1.4.1.1.481.3 |
|
1.2.840.10008.5.1.4.1.1.481.22 |
|
1.2.840.10008.5.1.4.1.1.481.7 |
|
1.2.840.10008.5.1.4.1.1.88.68 |
|
1.2.840.10008.5.1.4.1.1.66 |
|
1.2.840.10008.5.1.4.1.1.67 |
|
1.2.840.10008.5.1.4.1.1.9.6.1 |
|
1.2.840.10008.5.1.4.1.1.481.15 |
|
1.2.840.10008.5.1.4.1.1.481.20 |
|
1.2.840.10008.5.1.4.1.1.9.7.1 |
|
1.2.840.10008.5.1.4.1.1.7 |
|
1.2.840.10008.5.1.4.1.1.66.4 |
|
1.2.840.10008.5.1.4.1.1.11.10 |
|
1.2.840.10008.5.1.4.1.1.88.72 |
|
1.2.840.10008.5.1.4.1.1.9.7.4 |
|
1.2.840.10008.5.1.4.1.1.66.2 |
|
1.2.840.10008.5.1.4.1.1.66.1 |
|
1.2.840.10008.5.1.4.1.1.78.6 |
|
1.2.840.10008.5.1.4.1.1.77.1.5.3 |
|
1.2.840.10008.5.1.4.1.1.78.4 |
|
1.2.840.10008.5.1.4.1.1.68.1 |
|
1.2.840.10008.5.1.4.1.1.68.2 |
|
1.2.840.10008.5.1.4.1.1.66.5 |
|
1.2.840.10008.5.1.4.1.1.481.18 |
|
1.2.840.10008.5.1.4.1.1.481.14 |
|
1.2.840.10008.5.1.4.1.1.66.6 |
|
1.2.840.10008.5.1.4.1.1.9.1.1 |
|
1.2.840.10008.5.1.4.1.1.6.1 |
|
1.2.840.10008.5.1.4.1.1.3.1 |
|
1.2.840.10008.5.1.4.1.1.77.1.1 |
|
1.2.840.10008.5.1.4.1.1.77.1.2 |
|
1.2.840.10008.5.1.4.1.1.77.1.4 |
|
1.2.840.10008.5.1.4.1.1.77.1.3 |
|
1.2.840.10008.5.1.4.1.1.77.1.6 |
|
1.2.840.10008.5.1.4.1.1.11.12 |
|
1.2.840.10008.5.1.4.1.1.77.1.1.1 |
|
1.2.840.10008.5.1.4.1.1.77.1.2.1 |
|
1.2.840.10008.5.1.4.1.1.77.1.4.1 |
|
1.2.840.10008.5.1.4.1.1.78.5 |
|
1.2.840.10008.5.1.4.1.1.11.9 |
|
1.2.840.10008.5.1.4.1.1.88.77 |
|
1.2.840.10008.5.1.4.1.1.77.1.5.6 |
|
|
1.2.840.10008.5.1.4.1.1.77.1.5.5 |
1.2.840.10008.5.1.4.1.1.200.7 |
|
1.2.840.10008.5.1.4.1.1.200.8 |
|
1.2.840.10008.5.1.4.1.1.11.5 |
|
1.2.840.10008.5.1.4.1.1.13.1.1 |
|
1.2.840.10008.5.1.4.1.1.13.1.2 |
|
1.2.840.10008.5.1.4.1.1.12.1 |
|
1.2.840.10008.5.1.4.1.1.88.67 |
|
1.2.840.10008.5.1.4.1.1.12.2 |
