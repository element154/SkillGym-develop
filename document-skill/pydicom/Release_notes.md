## Source: https://pydicom.github.io/pydicom/stable/release_notes/index.html

# Release notes¶

## 3.0.2¶

### Fixes¶

Fixed a security issue: a crafted DICOMDIR could set

`ReferencedFileID`

to a path outside the File-set root. This addresses CVE-2026-32711.

## Version 3.0.1¶

### Fixes¶

Changed logging of missing plugin imports to use

`logging.DEBUG`

(#2128).Include all

`examples`

module datasets with the package (#2128, #2131)Fixed an invalid VR value in the private data dictionary (#2132).

Fixed checking for

*Bits Stored*when converting*Float Pixel Data*and*Double Float Pixel Data*using the`pixels`

backend (#2135).Fixed decoding of pixel data for images with

*Bits Allocated*of 1 when frame boundaries are not aligned with byte boundaries (#2134).

## Version 3.0.0¶

The major breaking changes with the version 3.0 release are:

The value for

`JPEGLossless`

has changed to`1.2.840.10008.1.2.4.57`

.The encoding used when saving datasets defaults to the set

Transfer Syntax UID.

`Dataset.pixel_array`

will convert YCbCrPixel Datato RGB by default when possible.

`read_file`

and`write_file`

have been removed.

### Changes¶

Removed support for Python <= 3.9.

All tag formats changed to upper case, no space e.g. “(7FE0,0010)” rather than “(7fe0, 0010)”.

Values with VR

**AE**with an incorrect value length are now handled gracefully (extra bytes are ignored with a warning).A value of 0 for

*Number of Frames*is now handled as 1 frame, with a user warning issued on reading the pixel data (#1844).The value for

`JPEGLossless`

has changed from 1.2.840.10008.1.2.4.70 to 1.2.840.10008.1.2.4.57 to match its UID keyword. Use`JPEGLosslessSV1`

instead for 1.2.840.10008.1.2.4.70.The theoretical maximum number of instances supported by

`FileSet`

has been reduced to 1838265625 to ensure support for 32-bit systems (#1743).The characters used by

`generate_filename()`

when alphanumeric is`True`

has been reduced to [0-9][A-I,K-Z].`get_testdata_file()`

and`get_testdata_files()`

now raise`ValueError`

if called with an absolute path or pattern.`generate_uid()`

has been changed to use a random suffix generated using`randbelow()`

when entropy_srcs isn’t used, and the maximum allowed length of the prefix has been changed to 54 characters (#1773).`DataElement.VM`

always returns`1`

for**SQ**elements (#1481).DICOM dictionary updated to 2024c.

Concepts dictionaries updated to 2024c.

`validate_file_meta()`

now checks to ensure required Type 1 elements aren’t empty.implicit_vr and little_endian optional arguments added to

`Dataset.save_as()`

. In addition, this method will now raise an exception if the user tries to convert between little and big endian datasets. If this is something you need, use`dcmwrite()`

instead.Added the overwrite argument to

`Dataset.save_as()`

and`dcmwrite()`

to allow raising a`FileExistsError`

if trying to write to a file that already exists (#2104).implicit_vr, little_endian and force_encoding optional arguments added to

`dcmwrite()`

.The priority used to decide which encoding to use with

`Dataset.save_as()`

and`dcmwrite()`

has been changed to:The set

*Transfer Syntax UID*,The implicit_vr and little_endian arguments,

Datasets containing

*Command Set*(0000,eeee) elements can no longer be written using`Dataset.save_as()`

or`dcmwrite()`

, use`write_dataset()`

instead.A dataset’s

`file_meta`

elements are no longer modified when writing.`DicomIO`

now requires a readable or writeable buffer during initialisation and`DicomBytesIO`

directly inherits from it.The

`pydicom.encoders`

module has been moved to`pydicom.pixels.encoders`

, the original import path will be removed in v4.0.Using GDCM v3.0.23 or lower to decode JPEG-LS datasets with a

*Bits Stored*of 6 or 7 produces incorrect results, so attempting to do so now raises an exception.`pyjpegls`

or`pylibjpeg`

with`pylibjpeg-libjpeg`

can be used instead (#2008).Using Pillow with JPEG 2000 encoded > 8-bit multi-sample data (such as RGB) now raises an exception as Pillow cannot decode such data correctly (#2006).

An exception will now be raised if an

`ndarray`

is used to set*Pixel Data*(#50).Logging of errors when converting elements using

`Dataset.to_json_dict()`

have been made more verbose and now use`logging.WARNING`

(#1909).Added

`FileDataset.buffer`

and changed`FileDataset.filename`

to only be the filename the dataset was read from (if any) (#1937).

#### Removals¶

The

`compat`

module has been removed.The

`dicomdir`

module and`DicomDir`

class have been removed and reading a DICOMDIR dataset now returns a normal`FileDataset`

instance. For handling DICOM File-sets and DICOMDIR datasets use the`FileSet`

class instead.The

`read_file`

and`write_file`

functions have been removed, use`dcmread()`

and`dcmwrite()`

instead.The following UID constants have been removed:

`JPEGBaseline`

(use`JPEGBaseline8Bit`

instead)`JPEGExtended`

(use`JPEGExtended12Bit`

instead)`JPEGLSLossy`

(use`JPEGLSNearLossless`

instead)`JPEG2000MultiComponentLossless`

(use`JPEG2000MCLossless`

instead)`JPEG2000MultiComponent`

(use`JPEG2000MC`

instead)

The following UID lists have been removed:

`JPEGLossyCompressedPixelTransferSyntaxes`

: use`JPEGTransferSyntaxes`

`JPEGLSSupportedCompressedPixelTransferSyntaxes`

: use`JPEGLSTransferSyntaxes`

`JPEG2000CompressedPixelTransferSyntaxes`

: use`JPEG2000TransferSyntaxes`

`RLECompressedLosslessSyntaxes`

: use`RLETransferSyntaxes`

`UncompressedPixelTransferSyntaxes`

: use`UncompressedTransferSyntaxes`

`PILSupportedCompressedPixelTransferSyntaxes`

The

`PersonNameUnicode`

class has been removed, use`PersonName`

instead.The

`DataElement.description`

attribute has been removed, use`DataElement.name`

instead.The

`pixel_data_handlers.rle_handler.rle_encode_frame`

function has been removed, use`Dataset.compress()`

or`RLELosslessEncoder`

instead.The

`_storage_sopclass_uids`

module has been removed, import UIDs from the`uid`

module instead.The following properties have been removed:

`Dataset.parent`

and`Dataset.parent_seq`

`Sequence.parent`

and`Sequence.parent_dataset`

`DataElement.parent`

The

`overlay_data_handlers`

module has been removed, use the`overlays`

module instead.`config.overlay_data_handlers`

has been removed.`Dataset.fix_meta_info()`

has been removed as encoding state now follows the transfer syntax instead of the other way around.

### Enhancements¶

Added details of missing required tag information when adding a dataset to a File-set (#1752).

The following UID constants have been added:

Added convenience method

`add_new_private()`

to add a private tag.Added the examples module to make it easier and less confusing for users to work with the example datasets used by the documentation.

Added the ability to set the corresponding dataset encoding for private transfer syntaxes to

`UID`

via the`set_private_encoding()`

method.Added the ability to register private transfer syntaxes with

`register_transfer_syntax()`

so they can be used when reading datasets with`dcmread()`

.Warning messages are also sent to the pydicom logger (#1529).

Added the following to the

`encaps`

module:`parse_basic_offsets()`

for parsing the Basic Offset Table.`parse_fragments()`

for determining the number of encapsulated fragments and their byte offsets.`generate_fragments()`

for yielding encapsulated fragments.`generate_fragmented_frames()`

for yielding encapsulated frame fragments.`generate_frames()`

for yielding whole encapsulated frames.`get_frame()`

for returning the specific encapsulated frame at index without necessarily having to read the preceding frames into memory.

These new functions support reading encapsulated data from both

`bytes`

or any Python object with`read()`

,`seek()`

and`tell()`

methods such as`io.BytesIO`

,`BinaryIO`

or`mmap.mmap`

. They also support using the Extended Offset Table for determining frame boundaries.Added the keep_deferred keyword argument to

`Dataset.get_item()`

to allow accessing the file offset and element length without having to read the element value. (#1873).Added the

`pixels`

module and a new more flexible backend for decoding pixel data via`Decoder`

factory class instances. The new decoding backend adds support for the following:Returning a view over the original pixel data buffer (#746).

Returning RGB pixel data by default for JPEG (#1781, #1133 and many others).

Returning excess frames for JPEG when there is no Basic or Extended Offset Table and the

*Number of Frames*is incorrect (#1666).Returning excess frames for native encoding when the

*Number of Frames*is incorrect (#2035)Returning the decoded pixel data as either a NumPy

`ndarray`

or buffer-like object.Iterating through either all or specific frames.

Added support for decoding HTJ2K transfer syntaxes (#1848).

Added two functions for returning pixel data as a NumPy

`ndarray`

from a path to a dataset while minimizing memory-usage:`pixel_array()`

and`iter_pixels()`

.Added two functions for compressing and decompressing datasets using the new decoding backend:

`compress()`

and`decompress()`

.Added support for the following transfer syntaxes to

`Dataset.compress()`

(#1997):*JPEG-LS Lossless*with`JPEGLSLosslessEncoder`

*JPEG-LS Near Lossless*with`JPEGLSNearLosslessEncoder`

*JPEG 2000 Lossless*with`JPEG2000LosslessEncoder`

*JPEG 2000*with`JPEG2000Encoder`

See the JPEG-LS and JPEG 2000 encoding guides for more information.

Added

`Dataset.pixel_array_options()`

for controlling pixel data decoding when using`Dataset.pixel_array`

with the new`pixels`

backend.Improve support for reading and resolving inline binary data with VR=UN from Json (#2062).

`get_j2k_parameters()`

now takes into account the JP2 header (if present, although it’s non-conformant for it to be) (#2073).Added support for NumPy v2.0 (#2075).

Added

`pydicom.__concepts_version__`

attribute with the DICOM Standard version used to create the concepts dictionaries in`pydicom.sr`

(#1021).Refactored the interface for the concepts in

`pydicom.sr`

to simplify the access types (#1454).Added the

`Dataset.set_pixel_data()`

method and`set_pixel_data()`

function for automatically setting a dataset’s*Pixel Data*and related Image Pixel module elements using an`ndarray`

(#50).Added typing support for

`Dataset`

element access using the types-pydicom package. (#1485).Added

`apply_presentation_lut()`

for applying a Presentation LUT to an`ndarray`

(#1265).Added

`apply_icc_profile()`

and`create_icc_transform()`

for applying ICC profiles to an`ndarray`

(#1244).Added

`Dataset.update_raw_element()`

to make it easier to modify a`RawDataElement`

’s VR or value prior to conversion to a`DataElement`

(#1739).Added support for using

`io.BufferedIOBase`

subclasses to set the value for elements with O* VRs such as**OB**and**OW**(#1913).Added

`encapsulate_buffer()`

and`encapsulate_extended_buffer()`

for encapsulating buffered compressed*Pixel Data*via`EncapsulatedBuffer`

instances.Added elements with

**OB**,**OD**,**OF**,**OL**,**OW**,**OV**VRs to the type validation checking when setting`DataElement`

values (#1414).Added

`convert_raw_data_element()`

for converting raw element data to`DataElement`

instances.Added the

`hooks`

module which contains an interface for adding callback functions via the`Hooks`

singleton, as well as default and alternative convenience callbacks for`convert_raw_data_element()`

(#1556).

### Fixes¶

Fixed the GDCM and pylibjpeg handlers changing the

*Pixel Representation*value to 0 when the J2K stream disagrees with the dataset and`APPLY_J2K_CORRECTIONS`

is`True`

(#1689).Fixed pydicom codify error when relative path did not exist.

Fixed the VR enum sometimes returning invalid values for Python 3.11+ (#1874).

Fixed pixel data handler for Pillow 10.1 raising an AttributeError (#1907).

Fixed a possible security issue with

`FileInstance`

instances being able to escape the temporary directory when being added to a`FileSet`

(#1922).Fixed an

`AttributeError`

when running`deepcopy()`

after`Dataset.update`

(#1816).Fixed

`encapsulate_extended()`

not returning the correct values for odd-length frames (#1968).Fixed using the incorrect encoding when writing datasets converted between explicit and implicit VR when only the

*Transfer Syntax UID*was changed (#1943).Fixed the

`jpeg_ls`

,`pillow`

and`rle`

pixel data handlers not working correctly when a frame is spread across multiple fragments (#1774).Added mitigation for a rare case where clearing the pixel data value prior to updating it may sometimes result in

`pixel_array`

returning the previous array instead of creating a new one (#1983).Fixed a

`KeyError`

when comparing codes with one of the codes having`scheme_designator`

set to`SRT`

but not being included in the`SRT`

to`SCT`

code mapping (#1994).Fixed JPEG-LS datasets with a

*Pixel Representation*of 1 returning incorrect image data when*Bits Stored*is less than*Bits Allocated*(#2009).Fixed decoding failures for JPEG-LS datasets with

*Bits Allocated*of 16 and*Bits Stored*<= 8 (#2010).Fixed the

*Pixel Data*VR not being set correctly with`Dataset.compress()`

(#2013).Fixed

`Dataset.decompress()`

not updating the*Pixel Data*element value until after saving (#2024).Fixed a rare issue with converting pixel data to an

`ndarray`

when*Bits Stored*is less than*Bits Allocated*and the unused bits haven’t been set to an appropriate value for correct interpretation of the data.Fixed a

`RecursionError`

when using`copy.deepcopy()`

with a dataset containing a private block (#2025).Fixed non-unique keywords for the concept codes in

`pydicom.sr`

(#1388).Fixed keywords using Python identifiers in

`pydicom.sr`

(#1273).Fixed being unable to write

*LUT Descriptor*when the VR is**SS**and the first value is greater than 32767 (#2081).Fixed

*Deflated Explicit VR Little Endian*datasets not working correctly with`codify`

(#1937).

### Deprecations¶

`Dataset.is_little_endian`

and`Dataset.is_implicit_VR`

will be removed in v4.0.`Dataset.read_little_endian`

and`Dataset.read_implicit_vr`

will be removed in v4.0, use`Dataset.original_encoding`

instead.`Dataset.read_encoding`

will be removed in v4.0, use`Dataset.original_character_set`

instead.The write_like_original optional argument to

`Dataset.save_as`

and`dcmwrite()`

will be removed in v4.0, use enforce_file_format instead.The following

`encaps`

module functions will be removed in v4.0:`get_frame_offsets()`

, use`parse_basic_offsets()`

instead.`generate_pixel_data_fragment()`

, use`generate_fragments()`

instead.`generate_pixel_data_frame()`

, use`generate_fragmented_frames()`

instead.`generate_pixel_data()`

, use`generate_frames()`

instead.`decode_data_sequence()`

, use`generate_fragments()`

instead.`defragment_data()`

, use`generate_frames()`

instead.`read_item()`

, use`generate_fragments()`

instead.

The

`pydicom.pixel_data_handlers`

module will be removed in v4.0. All pixel data processing will use the`pydicom.pixels`

module instead starting with v3.0.The following functions from

`pydicom.pixel_data_handlers.util`

have been moved to`pydicom.pixels.processing`

:The following functions from

`pydicom.pixel_data_handlers.util`

have been moved to`pydicom.pixels.utils`

:`pydicom.pixel_data_handlers.util.dtype_corrected_for_endianness()`

will be removed in v4.0.

`Dataset.convert_pixel_data()`

will be removed in v4.0, use`Dataset.pixel_array_options()`

instead.`DataElement_from_raw()`

will be removed in v4.0, please use`convert_raw_data_element()`

instead.`config.data_element_callback`

and`config.data_element_callback_kwargs`

will be removed in v4.0, please use the hooks for`convert_raw_data_element()`

instead.The

`pydicom.utils.fixers`

submodule will be removed in v4.0, please use the alternative callbacks for`convert_raw_data_element()`

in the`hooks`

module instead.

### Pydicom Internals¶

Repository folder structure refactored.

Renamed top level

`source`

folder to`util`

.New CI tools - dependabot, and pre-commit using black and ruff.

## Version 2.4.0¶

### Changes¶

Removed support for Python 3.6 (EOL since December 2021)

### Enhancements¶

Added attribute

`alphabetic`

(#1634)Added value validation for numerical VRs, add type validation for all validated VRs (#1414)

CLI commands now accept

*pydicom*charset test files and CLI help shows Python Version (#1674)Added support for Python 3.11 (#1658)

Added

`ISfloat`

to allow non-strict reading of existing files with float IS values (#1661)Improved speed of creating and accessing highly nested structures (#1728, #1734)

Switched to a pyproject.toml build process (#1792)

Updated DICOM and UID dicts to DICOM 2023b (#1803)

### Fixes¶

Fixed length validation of DS values with maximum length without a leading zero (#1632)

Increased download speed with progress bar for test data (#1611)

Fixed crash due to invalid private creator (#1638)

Fixed extremely long BytesLengthException error messages (#1683)

In codify, ensure unique variable names for DICOM keywords repeated in sequences, and handle unicode characters correctly (#1670)

Fixed handling of some invalid values in

`to_json_dict()`

if suppress_invalid_tags is set to True (#1693)Fixed reading of data with 8 bits allocated, encoded in Big Endian transfer syntax using VR

`OW`

(#1680)Fixed crash if reading regular dataset that has the SOP Class of a DICOMDIR (#1702)

Fixed wrong waveform data calculation when as_raw=False and baseline!=0 (#1667)

Fixed reading LUTData to expected size (#1747)

Fixed handling of AT VRs when codifying data elements (#1738)

### Pydicom Internals¶

In test suites, renamed ‘setup’ and ‘teardown’ methods, deprecated starting in pytest 7.2

Use own fork of CharPyLS to handle builds with Python 3.11 (#1788)

## Version 2.3.0¶

### Changes¶

`DataElement.description`

is deprecated and will be removed in v3.0, use`DataElement.name`

insteadUpdated the private dictionary

`enforce_valid_values`

is deprecated in favor of`reading_validation_mode`

Added download parameter to

`get_testdata_file()`

to allow skipping downloading the file if missed locally (#1617)

### Enhancements¶

Values are now validated for valid length, allowed character set and format on reading and writing. Depending on the value of

`reading_validation_mode`

and`writing_validation_mode`

a warning is logged, an exception is raised, or the validation is skipped.UIDs for all Storage SOP Classes have been added to the

`uid`

module (#1498)Use rle_handler as last resort handler for decoding RLE encoded data as it is the slowest handler (#1487)

Added, enhanced, or removed a number of Mitra private dictionary entries (#1588)

Added support for unpacking bit-packed data without using NumPy to

`unpack_bits`(:pr:`1594()`

)Added

`expand_ybr422()`

for expanding uncompressed`YBR_FULL_422`

data to`YBR_FULL`

(#1593)Replacement of

`UN`

VR with`SQ`

VR for undefined length data elements (introduced in 2.2.2), can now be configured via`infer_sq_for_un_vr`

Updated dictionaries to DICOM 2022a

### Fixes¶

Fixed odd-length

**OB**values not being padded during write (#1511)Fixed Hologic private dictionary entry (0019xx43)

Fixed Mitra global patient ID private dictionary entry (#1588)

Fixed

`compress()`

not setting the correct encoding for the rest of the dataset (#1565)Fixed AttributeError on deep copy of

`FileDataset`

(#1571)Fixed an exception during pixel decoding if using GDCM < 2.8.8 on Windows (#1581)

Fixed crashes on Windows and MacOS when using the GDCM plugin to compress into

*RLE Lossless*(#1581)Fixed

`dir(Dataset())`

not returning class attributes (#1599)Fixed bad DICOMDIR offsets when using

`FileSet.write()`

with a*Directory Record Sequence*using undefined length items (#1596)Assigning a list of length one as tag value is now correctly handled as assigning the single value (#1606)

Fixed an exception with multiple deferred reads with file-like objects (#1609)

## Version 2.2.0¶

### Changes¶

Data elements with a VR of

**AT**must now be set with values acceptable to`Tag()`

, and are always stored as a`BaseTag`

. Previously, any Python type could be set.`BaseTag.__eq__()`

returns`False`

rather than raising an exception when the operand cannot be converted to`BaseTag`

(#1327)`DA.__str__()`

,`DT.__str__()`

and`TM.__str__()`

return valid DICOM strings instead of the formatted date and time representations (#1262)If comparing

`FileDataset`

instances, the file metadata is now ignored. This makes it possible to compare a`FileDataset`

object with a`Dataset`

object.`rle_encode_frame()`

is deprecated and will be removed in v3.0, use`compress()`

or`RLELosslessEncoder`

instead.`read_file()`

is deprecated and will be removed in v3.0, use`dcmread()`

instead.`write_file()`

is deprecated and will be removed in v3.0, use`dcmwrite()`

instead.Data dictionaries updated to version 2021b of the DICOM Standard

### Enhancements¶

Added a command-line interface for pydicom. Current subcommands are:

`show`

: display all or part of a DICOM file`codify`

to produce Python code for writing files or sequence items from scratch.

Please see the Command-line Interface Guide for examples and details of all the options for each command.

A field containing an invalid number of bytes will result in a warning instead of an exception when

`convert_wrong_length_to_UN`

is set to`True`

.Private tags known via the private dictionary will now get the configured VR if read from a dataset instead of

**UN**(#1051).While reading explicit VR, a switch to implicit VR will be silently attempted if the VR bytes are not valid VR characters, and config option

`assume_implicit_vr_switch`

is`True`

(default)New functionality to help with correct formatting of decimal strings (

**DS**)Added

`is_valid_ds()`

to check whether a string is valid as a DICOM decimal string and`format_number_as_ds()`

to format a given`float`

or`Decimal`

as a DS while retaining the highest possible level of precisionIf

`enforce_valid_values`

is set to`True`

, all**DS**objects created will be checked for the validity of their string representations.Added optional

`auto_format`

parameter to the init methods of`DSfloat`

and`DSdecimal`

and the`DS()`

factory function to allow explicitly requesting automatic formatting of the string representations of these objects when they are constructed.

Added methods to construct

`PersonName`

objects from individual components of names (`family_name`

,`given_name`

, etc.). See`from_named_components()`

and`from_named_components_veterinary()`

.Added support for downloading the large test files with the requests package in addition to

`urllib.request`

(#1340)Ensured

`convert_color_space()`

uses 32-bit floats for calculation, added per_frame flag to allow frame-by-frame processing and improved the speed by ~20-60% (#1348)Optimisations for RLE encoding using

*pydicom*(~40% faster).Added support for faster decoding (~4-5x) and encoding (~20x) of

*RLE Lossless**Pixel Data*via the pylibjpeg-rle plugin (#1361, #1372).Added

`Dataset.compress()`

function for compressing uncompressed pixel data using a given encoding format as specified by a UID. Only*RLE Lossless*is currently supported (#1372)Added

`encoders`

module and the following encoders:`RLELosslessEncoder`

with ‘pydicom’, ‘pylibjpeg’ and ‘gdcm’ plugins

Added read parameter to

`get_testdata_file()`

to allow reading and returning the corresponding dataset (#1372)Handle decoded RLE segments with padding (#1438)

Add option to JSON functions to suppress exception and continue (#1332)

### Fixes¶

Fixed pickling a

`Dataset`

instance with sequences after the sequence had been read (#1278)Fixed JSON export of numeric values

Fixed handling of sequences of unknown length that switch to implicit encoding, and sequences with VR

**UN**(#1312)Do not load external data sources until needed - fixes problems with standard workflow if setuptools are not installed (#1341)

Fixed empty

**PN**elements read from file being`str`

rather than`PersonName`

(#1338)Fixed handling of JPEG (10918-1) images compressed using RGB colourspace rather than YBR with the Pillow pixel data handler (#878)

Allow to deepcopy a ~pydicom.dataset.FileDataset object (#1147)

Fixed elements with a VR of

**OL**,**OD**and**OV**not being set correctly when an encoded backslash was part of the element value (#1412)Fixed expansion of linear segments with floating point steps in segmented LUTs (#1415)

Fixed handling of code extensions with person name component delimiter (#1449)

Fixed bug decoding RBG jpg with APP14 marker due to change in Pillow (#1444)

Fixed decoding for FloatPixelData and DoubleFloatPixelData via pydicom.pixel_data_handlers.numpy_handler (#1457)

## Version 2.1.1¶

### Fixes¶

## Version 2.1.0¶

### Enhancements¶

Large testing data is no longer distributed within the pydicom package with the aim to reduce the package download size. These test files will download on-the-fly whenever either the tests are run, or should the file(s) be requested via the data manager functions. For example:

To download all files and get their paths on disk you can run

`pydicom.data.get_testdata_files()`

.To download an individual file and get its path on disk you can use

`pydicom.data.get_testdata_file()`

, e.g. for`RG1_UNCI.dcm`

use`pydicom.data.get_testdata_file("RG1_UNCI.dcm")`

Added a new pixel data handler based on pylibjpeg which supports all (non-retired) JPEG transfer syntaxes (#1127)

Added

`apply_rescale()`

aliasAdded

`apply_voi()`

and`apply_windowing()`

Added

*prefer_lut*keyword parameter to`apply_voi_lut()`

and handle empty VOI LUT module elements (#1234, #1237)Added ability to register external data sources for use with the functions in

`pydicom.data`

(#1156)`__contains__`

,`__next__`

and`__iter__`

implementations added to`PersonName`

(#1103)Added convenience constants for the MPEG transfer syntaxes to

`pydicom.uid`

(#1155)Added support for decoding

*Waveform Data*:Added

`pydicom.waveforms`

module and`generate_multiplex()`

and`multiplex_array()`

functions.Added

`Dataset.waveform_array()`

which returns an`ndarray`

for the multiplex group at index within a*Waveform Sequence*element.

When JPEG 2000 image data is unsigned and the

*Pixel Representation*is 1 the image data is converted to signed (#1149)Added

`keyword`

property for the new UID keywords in version 2020d of the DICOM StandardAdded testing of the variable names used when setting

`Dataset`

attributes and`INVALID_KEYWORD_BEHAVIOR`

config option to allow customizing the behavior when a camel case variable name is used that isn’t a known element keyword (#1014)Added

`INVALID_KEY_BEHAVIOR`

config option to allow customizing the behavior when an invalid key is used with the`Dataset`

`in`

operator (#1200)Implemented full support (loading, accessing, modifying, writing) of DICOM File-sets and their DICOMDIR files via the

`FileSet`

class (#9, #243, #1093)Added

`AllTransferSyntaxes`

Added option to turn on

*pydicom*future breaking behavior to allow user code to check itself against the next major version release. Set environment variable “PYDICOM_FUTURE” to “True” or call`future_behavior()`

Added another signature to the bulk_data_uri_handler in from_json to allow for the communication of not just the URI but also the tag and VR to the handler. Previous handlers will work as expected, new signature handlers will get the additional information.

`pack_bits()`

can now be used with 2D or 3D input arrays and will pad the packed data to even length by default.Elements with the

`IS`

VR accept float strings that are convertible to integers without loss, e.g. “1.0” (#1240)Added

`encapsulate_extended()`

function for use when an Extended Offset Table is required (#1178)

### Changes¶

Dropped support for Python 3.5 (only Python 3.6+ supported)

Reading and adding unknown non-private tags now does not raise an exception per default, only when

`enforce_valid_values`

is set (#1161)Data dictionaries updated to version 2020d of the DICOM Standard

Updated a handful of the SOP Class variable names in

`_storage_sopclass_uids`

to use the new UID keywords. Variables with`Multiframe`

in them become`MultiFrame`

, those with`and`

in them become`And`

, and`DICOSQuadrupoleResonanceQRStorage`

becomes`DICOSQuadrupoleResonanceStorage`

.The following UID constants are deprecated and will be removed in v2.2:

`JPEGBaseline`

: use`JPEGBaseline8Bit`

`JPEGExtended`

: use`JPEGExtended12Bit`

`JPEGLossless`

: use`JPEGLosslessSV1`

`JPEGLSLossy`

: use`JPEGLSNearLossless`

`JPEG2000MultiComponentLossless`

: use`JPEG2000MCLossless`

`JPEG2000MultiComponent`

: use`JPEG2000MC`

In v3.0 the value for

`JPEGLossless`

will change from 1.2.840.10008.1.2.4.70 to 1.2.840.10008.1.2.4.57 to match its UID keywordThe following lists of UIDs are deprecated and will be removed in v2.2:

`JPEGLossyCompressedPixelTransferSyntaxes`

: use`JPEGTransferSyntaxes`

`JPEGLSSupportedCompressedPixelTransferSyntaxes`

: use`JPEGLSTransferSyntaxes`

`JPEG2000CompressedPixelTransferSyntaxes`

: use`JPEG2000TransferSyntaxes`

`RLECompressedLosslessSyntaxes`

: use`RLETransferSyntaxes`

`UncompressedPixelTransferSyntaxes`

: use`UncompressedTransferSyntaxes`

`PILSupportedCompressedPixelTransferSyntaxes`

`DicomDir`

and the`dicomdir`

module are deprecated and will be removed in v3.0. Use`FileSet`

instead (#1211)`pydicom.overlay_data_handlers`

is deprecated, use`pydicom.overlays`

insteadRemoved transfer syntax limitations when converting overlays to an

`ndarray`

(#1181)The

`overlay_data_handlers`

config option is deprecated, the default handler will always be used.

### Fixes¶

`Dataset.copy()`

now works as expected (#1146)Optimistically parse undefined length non-SQ data as if it’s encapsulated pixel data to avoid erroring out on embedded sequence delimiter (#1140)

Fixed

`get_testdata_file()`

and`get_testdata_files()`

raising an exception if no network connection is available (#1156)Fixed GDCM < v2.8.8 not returning the pixel array for datasets not read from a file-like (#1153)

Raise

`TypeError`

if`dcmread()`

or`dcmwrite()`

is called with wrong argumentGracefully handle empty Specific Character Set (#1190)

Fixed empty ambiguous VR elements raising an exception (#1193)

Allow

`apply_voi_lut()`

to apply VOI lookup to an input float arrayFixed

`Dataset.setdefault()`

not adding working correctly when the default value is`None`

and not adding private elements when`enforce_valid_values`

is`True`

(#1215)

## Version 2.0.0¶

### Changelog¶

Dropped support for Python 2 (only Python 3.5+ supported)

Changes to Dataset.file_meta

file_meta now shown by default in dataset str or repr output;

`pydicom.config.show_file_meta`

can be set`False`

to restore previous behaviornew

`FileMetaDataset`

class that accepts only group 2 data elementsDeprecation warning given unless Dataset.file_meta set with a

`FileMetaDataset`

object (in*pydicom*3, it will be required)

Old PersonName class removed; PersonName3 renamed to PersonName. Classes PersonNameUnicode and PersonName3 are aliased to PersonName but are deprecated and will be removed in version 2.1

`dataelem.isMultiValue`

(previously deprecated) has been removed. Use`dataelem.DataElement.VM`

instead.

### Enhancements¶

Allow PathLike objects for filename argument in dcmread, dcmwrite and Dataset.save_as (#1047)

Deflate post-file meta information data when writing a dataset with the Deflated Explicit VR Little Endian transfer syntax UID (#1086)

Added config.replace_un_with_known_vr to be able to switch off automatic VR conversion for known tags with VR “UN” (see #1067)

Added config.use_DS_numpy and config.use_IS_numpy to have multi-valued data elements with VR of

**DS**or**IS**return a numpy array (#623) (much faster for bigger arrays). Both default to False to preserve previous behavior

### Fixes¶

Fixed reading of datasets with an empty Specific Character Set tag (regression, #1038)

Fixed failure to parse dataset with an empty

*LUT Descriptor*or*Red/Green/Blue Palette Color LUT Descriptor*element. (#1049)Made Dataset.save_as a wrapper for dcmwrite (#1042) rather than having different checks in each

Removed

`1.2.840.10008.1.2.4.70`

- JPEG Lossless (Process 14, SV1) from the Pillow pixel data handler as Pillow doesn’t support JPEG Lossless. (#1053)Fixed error when writing elements with a VR of

**OF**(#1075)Fixed improper conversion when reading elements with a VR of

**OF**(#1075)Fixed

`apply_voi_lut()`

and`apply_modality_lut()`

not handling (0028,3006)*LUT Data*with a VR of**OW**(#1073)Fixed access to private creator tag in raw datasets (#1078)

Fixed description of newly added known private tag (#1082)

Fixed update of private blocks after deleting private creator (#1097)

Fixed bug in updating pydicom.config.use_DS_Decimal flag in

`DS_decimal()`

## Version 1.4.1¶

### Fixes¶

Fixed writing of empty sequences (regression, #1030)

### Changes¶

In Dataset.to_json and Dataset.to_json_dict, the default of the bulk_data_threshold argument has changed to 1024, and is now ignored if no bulk data handler is set (see #1029)

## Version 1.4.0¶

### Fixes¶

Fixed handling of VRs AT and PN in json encoding (#915)

Fixed handling of binary values in json encoding (#887)

Prevent exception if assigning None to UI element (#894)

Fixed print output for numeric multi-value elements (#892)

Fixed testing PN values for truthiness (#891)

Fixed handling of data too large to written in explicit transfer syntax

Fixed assigning of empty values to data elements (#896)

Fixed error in unpickling dataset (#947)

Fixed error in pickling modified datasets (#951)

Fixed improper conversion of the first value of the

*LUT Descriptor*elements (0028,1101-1103) and (0028,3002) (#942)Fixed handling of ISO IR 159 encoding (#917)

Fixed propagation of bulk data handler in Dataset.from_json (#971)

Correctly handle DICOMDIR files with records in reverse-hierarchical order (#822)

*Pixel Data*encoded using JPEG2000 and decoded using the Pillow handler no longer returns RGB data when the (0028,0004)*Photometric Interpretation*is YBR_FULL or YBR_FULL_422. (#263, #273, #826)Avoid possible high memory usage while reading sequences (#994)

Fixed

`generate_pixel_data()`

not returning all available frames when the Basic Offset Table was empty. This may still occur when multiple fragments per frame are present for non-JPEG transfer syntaxes or where no JPEG EOI/EOC marker is present (#685)Fixed possible incorrect switch to explicit VR in sequence items (#999)

Fixed JPEG 2000 (UIDs 1.2.840.10008.1.2.4.90 and 1.2.840.10008.1.2.4.91) pixel data with bit depth range 9-16 not producing the correct values with the Pillow handler (#693)

Fixed parsing a DICOMDIR file with no records raising an exception (#1004)

### Enhancements¶

Added support for converting (60xx,3000)

*Overlay Data*to a numpy ndarray using`Dataset.overlay_array()`

(#912)Added support for deferred reading in file-like objects (#932)

Tolerate values with multiple and/or incorrect padding bytes (#940)

Added support for uncompressed pixel data with (0028,0004)

*Photometric Interpretation*of YBR_FULL_422 to the numpy pixel data handler.Added

`apply_color_lut()`

function for applying color palette LUTs (#205)Added

`apply_modality_lut()`

function for applying modality LUTs.Added

`get_palette_files()`

for retrieving well-known palette color datasets.Raise on end of file errors if config.enforce_valid_values is set (#277)

Added user warning, or exception in strict mode, if a DICOMDIR has an unexpected transfer syntax (#848)

Handle missing offset tags in DICOMDIR (#981)

Added optional handler argument to

`decompress()`

. This lets you specify a particular handler, rather than following pydicom’s default order (#537)Added

`apply_voi_lut()`

function for applying VOI LUTs or windowing operations.Added support for (7fe0,0008)

*Float Pixel Data*and (7fe0,0009)*Double Float Pixel Data*to`pixel_array`

(#452)JPEG 2000 (1.2.840.10008.1.2.4.91) transfer syntax is supported for data with bit depth > 8 with the Pillow pixel data handler

`PixelData.is_undefined_length`

is now set automatically based on whether the Dataset’s Transfer Syntax is compressed (#1006)Updated DICOM dictionary to 2019e edition (#1013)

Added support for new VRs OV, SV, UV (#1016)

Code dictionaries and

`Code`

class for structured reporting added (alpha release only). See the Structured Reporting tutorial for more information

### Changes¶

`get_frame_offsets()`

now returns whether the Basic Offset Table is empty and a list of the offsets.

## Version 1.3.0¶

### Documentation¶

New User Guide page for Python 2 support timeline

New User Guide page for working with private data elements

example loading set of CT slices and plotting axial, sagittal and coronal (#789)

### Changes¶

Removed deprecated uid variables, config.image_handlers and DeferredDataElement (#760)

`dataelem.isMultiValue`

is deprecated and will be removed in v1.4. Use`dataelem.DataElement.VM`

instead.`dataelem.isStringOrStringList`

and`dataelem.isString`

functions are removed`datadict.add_dict_entry`

and`datadict.add_dict_entries`

now raise if trying to add a private tag`dataset.Dataset.maxBytesToDisplay`

also limits display length for non-binary VRs (by number of items) (#666)

### Enhancements¶

Added

`datadict.add_private_dict_entry`

and`datadict.add_private_dict_entries`

to add custom private tags (#799)Added possibility to write into zip file using gzip, by avoiding seek (#753)

Added RLE encoding (#730)

Added handling of incorrect transfer syntax (explicit vs implicit) (#820)

Added creation of Tag instances by DICOM keyword, e.g Tag(“PatientName”)

Added possibility to get and add private tags without adding them to the private dictionary

Added possibility to use a

`Dataset`

in a`NumPy`

arrayAllow missing padding byte in Pixel Data, issue a warning in this case (#864)

Add in-memory image decoding with GDCM

Check really used implicit/explicit VR before reading a data set (#819, #820)

Added alpha conversion of Datasets to/from JSON format (Python 3 only)

### Fixes¶

Correctly handle Dataset.pop and Dataset.setdefault for tuple and keyword arguments (#852)

Correctly handle encoding errors when any of the encodings are invalid (not just the first) (#850)

Do not raise while resolving an ambiguous VR dependent on PixelRepresentation if both PixelRepresentation and PixelData are not present (#838)

Raise exception with specific message if value is too large to be written in explicit transfer syntax (#757)

Make hash for PersonName3 behave as expected, make PersonName objects immutable (#785)

Fixed generate_uid() returning non-conformant UIDs when prefix=None (#788)

Avoid exception if reading from empty file (#810)

An invalid encoding is now replaced by the default encoding, if

`config.enforce_valid_values`

is not set (#815)Correctly handle elements with ambiguous VR in sequence items (#804)

Fix bug where new DicomDir objects always have is_implicit_VR

Fix dataset equality for mixed raw vs converted data elements (#835)

Remove excess padding in Pixel Data

Fix wrong date format in anonymize example

Fix unknown VR exception message when VR isn’t ASCII (#791)

Fix jis-x-0201 characters encoding (#856)

## Version 1.2.0¶

### Changes¶

PIL removed as a fallback if Pillow is not available in the pillow pixel data handler (#722)

`uid.JPEGBaseLineLossy8bit`

deprecated and will be removed in v1.3. Use`uid.JPEGBaseline`

instead. (#726)`uid.JPEGBaseLineLossy12bit`

deprecated and will be removed in v1.3. Use`uid.JPEGExtended`

instead. (#726)`uid.JPEG2000Lossy`

deprecated and will be removed in v1.3. Use`uid.JPEG2000`

instead. (#726)Equality and inequality operator overrides removed from

`UID`

.`config.image_handlers`

deprecated and will be removed in v1.3. - use`config.pixel_data_handlers`

instead. There is also a change in behavior in that`image_handlers`

previously used to only contain the pixel data handlers that had their dependencies met. Now`pixel_data_handlers`

contains all handlers no matter whether or not their dependencies are met. To check if a handler is available for use (it has its dependency met) use the handler’s`is_available`

method.`DeferredDataElement`

class deprecated and will be removed in v1.3 (#291)The use of NumPyPy with PyPy is no longer supported, use NumPy instead.

### Enhancements¶

Updated DICOM dictionary for 2018c edition (#677)

Added possibility to set byte strings as value for VRs that use only the default character set (#624)

Functions for encapsulating frames added to

`encaps`

module (#696)Added

`Dataset.fix_meta_info()`

(#584)Added new function for bit packing

`pack_bits`

for use with BitsAllocated = 1 (#715)Added/corrected encoding and decoding of text and person name VRs using character sets with code extensions, added handling of encoding/decoding errors (#716)

Handle common spelling errors in Specific Character Set values (#695,737)

Added

`uid.JPEGLosslessP14`

for UID 1.2.840.10008.1.2.4.57Added

`uid.JPEG2000MultiComponentLossless`

for UID 1.2.840.10008.1.2.4.92Added

`uid.JPEG2000MultiComponent`

for UID 1.2.840.10008.1.2.4.93Added full support for Planar Configuration (#713)

Added support for single frame pixel data where BitsAllocated > 8 and SamplesPerPixel > 1 (#713)

Small improvement in RLE decoding speed (~10%)

Added support for non-conformant RLE segment ordering (#729)

### Fixes¶

Removed unused

`original_string`

attribute from the`DataElement`

class (#660)Improve performance for Python 3 when dealing with compressed multi-frame Pixel Data with pillow and jpeg-ls (#682)

Fixed handling of private tags in repeater range (#689)

Fixed Pillow pixel data handler for non-JPEG2k transfer syntax (#663)

Fixed handling of elements with ambiguous VR (#700, 728)

Adapted pixel handlers where endianness is explicitly adapted (#704)

Improve performance of bit unpacking (#715)

First character set no longer removed (#707)

Fixed RLE decoded data having the wrong byte order (#729)

Fixed RLE decoded data having the wrong planar configuration (#729)

Fixed numpy arrays returned by the pixel data handlers sometimes being read-only. Read-only arrays are still available for uncompressed transfer syntaxes via a keyword argument for the numpy pixel data handler and should help reduce memory consumption if required. (#717)

Fixed deprecation warning in Python 3.7 (#740)

## Version 1.1.0¶

### Enhancements¶

`UID.__str__`

no longer returns the UID name (when known). The UID name is still available using the`UID.name`

property.`Dataset`

equality now only compares the dataset’s`DataElements`

(#464)the

`codify`

script now supports VRs OD and OL, and works in Python 3 (#498); documentation has been added for`codify`

the performance for reading and writing datasets has been improved to be better than in pydicom 0.9.9 (#605, #512)

added support for bit-packed pixel data (#292)

updated DICOM dictionary for 2018b edition

added full API documentation to pydicom documentation (#649)

### Fixes¶

`UID`

should behave as expected for a python`str`

subclass (#256)group length elements in groups above 0x0006 removed on writing (#32)

fixed

`write_PN`

raising a`TypeError`

when called with a non-iterable encoding parameter (#489)fixed padding for some odd-sized image data (#599)

removed unneeded warning for incorrect date string length (#597)

fixed

`Dataset`

not slicing correctly when an (0xFFFF,0xFFFF) element is present (#92)use correct VR for unknown private tags and private creators (#620)

fixed crash on reading RGB data with implicit VR (#620)

parent encoding was not used in sequences without own encoding (#625)

fixed error handling for values too large to fit in VR IS (#640)

### Other¶

A deprecation warning has been added for UID.__eq__ and UID.__ne__ when comparing

`UID == [UID name]`

and`UID != [UID name]`

. Starting in v1.2,`UID`

equality and inequality comparisons will return`False`

when performing the equivalent of`UID == [UID name]`

and`UID != [UID name]`

, respectively. E.g. UID(‘1.2.840.10008.1.1’) == ‘Verification SOP Class’ will return False. Use`UID.name == [UID name]`

instead.

## Version 1.0.0¶

This is a major release, with major changes, including backwards-incompatible changes.

### Major changes¶

full Python 3 compatibility - one code base for both Python 2 and Python 3

package name and import name now match – use

`import pydicom`

rather than`import dicom`

.added handlers for converting (7fe0,0010)

*Pixel Data*to a numpy.ndarrayoptional GDCM support for reading files with compressed pixel data (#18)

optional Pillow and jpeg_ls support for reading some compressed pixel data files

support for decompressing a compressed dataset in-place

DICOM dictionary updated to 2017c

cleaned up DICOM dictionary code, old non-DICOM-keyword code removed

### Other enhancements¶

added

`util/fixer.py`

callbacks available to fix non DICOM-compliant values before exceptions thrownadded context management methods to

`Dataset`

added

`misc.is_dicom()`

function to check for DICOM file formatadded date/time converters (#143)

added option to attempt other VRs if translate fails (#197)

added heuristics to read files that have no preamble or file meta information

support for multi-valued DA, DT, TM data elements (#212)

`DataElement`

: added`keyword`

and`is_retired`

properties`datadict`

: added`dictionary_is_retired()`

`datadict`

: added ability to add custom DICOM dictionary items via`add_dict_entry()`

and`add_dict_entries()`

added some support for pickle

added support for VRs

`OD`

,`OL`

and`UC`

added support for Thai, Japanese and Chinese encodings (#346, #353)

added support for slicing to Dataset

add/update TransferSyntaxUID when writing standard

renamed

`UID`

package to`uid`

(conforms to Python standard)added property

`uid.is_private`

added definitions for storage SOP Class UIDs (#172)

added possibility to read only specific tags (#95)

added missing meta elements when writing DICOM file

added

`encaps`

generator functions to access compressed frames`read_file`

changed to`dcmread`

,`write_file`

to`dcmwrite`

for greater clarity. Previous names still available for backwards compatibility.

### Infrastructure¶

added TravisCI and AppVeyor builds for automatic tests under Linux and Windows

added automatic code coverage builds and PEP-8 checks

added automatic documentation builds on GitHub Pages for development and release builds

added PyPy support

removed support for Python 2.6, added support for Python 3.6

### Fixes¶

correctly handle PlanarConfiguration==0 (#151)

updated uid generation to ensure uniqueness (#125)

handle missing patient data in

`show_dicomdir`

assume default transfer syntax if none in file meta (#258)

fixed reading/writing of empty tags and tags with bad VR

fixed reading AE elements with leading or trailing spaces

fixed handling of ambiguous VR elements

fixed handling for several error conditions

fixed Latin5 (Turkish) character set handling

a lot of other small fixes…

## Version 0.9.9¶

In addition to bug fixes, pydicom 0.9.9 contains updates for all DICOM dictionaries. New features include DICOMDIR handling, and a utility module which produces python/pydicom source code to recreate a DICOM file.

### Enhancements¶

All DICOM dictionaries updated (standard dictionary, UID dictionary, and private dictionaries)

Dicom commands also added to dictionary

Ability to work with DICOMDIR:

`read_dicomdir()`

function and`DicomDir`

class. Example file`show_dicomdir.py`

file added to examples subdirectory.`codify.py`

: Produce python/pydicom source code from a DICOM file.a number of Python 3 compatibility enhancements

setup.py uses ez_setup only if setuptools not already installed

exceptions carry tag info with them, to aid in debugging

### Contrib file changes¶

pydicom_series: force parameter added (Nil Goyette)

dcm_qt_tree: switch to OrderedDict to preserve ordering of tags (Padraig Looney)

### Other Contributors¶

Other than Jonathan and myself, other contributors were: Rickard Holmberg, Julien Lamy, Yaroslav Halchenko, Mark White, Matthew Brett, Dimitri Papadopoulos, videan42 …(sorry if I’ve missed anyone).

## Version 0.9.8¶

pydicom 0.9.8 is mainly a consolidation step before moving to official Python 3 compatibility in pydicom 1.0. It also reverts the change to using Decimal for VR of DS (in pydicom 0.9.7), due to performance issues. DS as Decimal is still available, but is off by default.

### Major changes¶

Requires Python 2.6 or later, in preparation for Python 3 compatibility

experimental Python 3 compatibility (unofficial at this point) – uncomment the two indicated lines in setup.py to use it. Please provide feedback to the issues list.

DS values reverted to using float as default (issue 114) due to slow performance using Python Decimal. Speed tests show approx factor of 10 improvement compared with pydicom 0.9.7 (several revisions up to r78ba350a3eb8)

streamlined much code internally taking advantage of modern Python constructs: decorators, generators, etc

### Bug fixes¶

Fix for duplicate logger from Gunnar Schaefer. Fixes issue 107 (revision 774b7a55db33)

Fix rewind behavior in find_bytes (issue 60, revision 6b949a5b925b)

Fix error in nested private sequences (issue 113, revision 84af4b240add)

### Enhancements¶

UID generator added (Félix C. Morency) (revisions 0197b5846bb5 and 3678b1be6aca, tests in f1ae573d9de5, 0411bab7c985)

new PersonName3 class for Python 3: (revision 9b92b336e7d4)

### Contrib file changes¶

Fix for pydicom_series for DS decimal (revision e830f30b6781)

new dcm_qt_tree.py module - tree display of DICOM files using PySide and Qt. Contributed by Padraig Looney.

Special acknowledgement to Jonathan Suever who contributed most of the Python 3 work and many bug fixes.

## Version 0.9.7¶

pydicom 0.9.7 resolves some remaining bugs before moving to Python 3 compatibility. ** It is the last version which will run with Python < 2.6 ** (it will run with Python 2.4 to Python 2.7)

### Major changes¶

Added DICOM 2011 keywords. Old “named tags” still work, but will be deprecated in future versions. Most names are identical, but some have changed. For example:

SamplesperPixel becomes SamplesPerPixel (capital ‘P’ on ‘Per’)

Beams becomes BeamSequence (and similar for all sequences)

Decimal and integer strings handled much better (revisions 4ed698a7bfbe and c313d2befb08).

New classes for VR of types DS and IS (DS is derived from Python Decimal)

New MultiValue class, enforcing all values of same type

New config.py file with user-definable parameters:

allow_DS_float (default False) for controlling whether float values can be used to construct DS or IS strings.

enforce_valid_values (default True) for ensuring IS, DS meet DICOM standard limits To change these, use ‘import dicom.config, then dicom.config.<parameter>={True|False}’ before setting values of data elements

Users are encouraged to switch to the official DICOM keywords, as these are now part of the standard, and promote consistency across programming languages and libraries.

### Bug fixes¶

New way to read file meta information, not using the group length, instead reading until end of group 2 data elements. If group length dose not match, log a warning (revision b6b3658f3b14).

Fix bug in copying raw private data elements (issue 98)

Force logging level to warning on ‘import dicom’ (issue 102)

Deferred read fixed to work with gzipped files (issue 103)

Setting individual items in a DS or IS list now saves to file correctly

Japanese and Korean encoding fixes (issue 110)

### Other Enhancements¶

New Sequence class which verifies items are Datasets (issue 52)

Assignment to SQ data element checks value is a Sequence or can be converted to one (issue 111)

dir(ds) now includes methods and properties as well as DICOM named tags. Work only on Python >= 2.6 as previous versions do not call __dir__ method (issue 95)

Added much more debugging info and simplified reading of data elements (revision b6b3658f3b14)

updated example files to DICOM 2011 keywords; fixed bugs

Many of the bug fixes/enhancements were submitted by users. Many thanks to those who contributed.

## Version 0.9.6¶

pydicom 0.9.6 updates the dictionary to the DICOM 2011 standard, and has a number of bug fixes

### Major changes¶

updated the dictionary to the DICOM 2011 standard’s dictionary.

### Bug fixes¶

Fixed bug in Dataset.file_metadata() and deprecated in favor of FileDataset (issue 93)

Fixed UID comparisons against non-string values (issue 96)

catch exceptions on reading undefined length private data elements (issue 91, issue 97)

Fixed bug in raising exception for unknown tag

### Other¶

added example file write_new.py to show how to create DICOM files from scratch

updated other example files

more PEP-8 style changes

## Version 0.9.5¶

pydicom 0.9.5 is primarily a bug-fix release but includes some contrib files also.

### Major fixes in this release¶

fix for incorrect pixel integer types which could lead to numeric errors (issue 79)

By default an InvalidDicomError will be raised when trying to read a non-DICOM file (unless read_file keyword arg {{{force}}} is True) (revision fc790f01f5)

fix recursion error on private data elements (issue 81, issue 84)

### Other fixes in this release¶

Fix for unicode decode failing with VM > 1 (issue 78)

fix for fail of DicomIter on files with Explicit VR Transfer Syntax UID (issue 82)

Fix for Python 2.5 and ‘with’ statement (revision 1c32791bf0)

Handle ‘OB/OW’ VR as well as ‘OW/OB’ (revision e3ee934bbc)

Fix dataset.get(tag) so returns same as dataset[tag] (issue 88)

### New ‘Contrib’ files¶

dicom_dao.py by Mike Wallace – CouchDB storage of DICOM info and binary data

pydicom_series.py by Almar Klein – Reads files and separates into distinct series.

### Other¶

switch to Distribute for packaging

preliminary work on Python 3 compatibility

preliminary work on using sphinx for documentation

preliminary work on better writing of files from scratch

## Version 0.9.4¶

Note

there is a

*backwards incompatible*change made to storage of file_meta info. See item below.pydicom 0.9.4 requires Python 2.4 or higher (pydicom 0.9.3 can run under Python 2.3)

### Major changes/additions in this version¶

file reading code reorganized substantially

significant speed increase for reading DICOM files – approx 3 times faster than 0.9.3

partial file reading available – in particular, new optional argument to read_file(), stop_before_pixels, will stop before getting to the pixel data, not reading those into memory. Saves a little time for small images, but could be quite helpful for very large images when the pixel data is not needed.

read_file() now returns a !FileDataset object, instead of a plain Dataset. Most user code will not see much difference (except see next bullet on file meta information) but now the information stored in the object has been made explicit – e.g. the endian-ness and whether the file syntax was explicit VR or implicit VR.

file meta info has been separated from the main dataset. Logically, this makes more sense, as the file meta is not really part of the dataset, but is specific to the method of storage. This is a backwards-incompatible change, but is easily fixed by changing any references to file-meta data elements from {{{dataset.<name>}}} to {{{dataset.file_meta.<name>}}}. The file_meta is a dataset like any other, all the usual methods for viewing, changing data elements work on it also.

private dictionaries file now generated from the GDCM library’s private dictionary – code to convert formats contributed by Daniel Nanz.

license has returned to an MIT-based license (with the compatible GDCM also noted for the private dictionary component).

contributed files with example code for viewing using wxPython or Tkinter (and PIL) – in dicom.contrib folder. Thanks to Dave Witten, Daniel Nanz and Adit Panchal for these contributions.

updates to pydicom’s DICOM data dictionary contributed by Adit Panchal: CP805/916; Supp 43 and 117 (and UID dict), Supp 119 and 122

### Other changes and bug fixes¶

Tag is now a factory function; the class is called !BaseTag. This was part of the file reading speed-up process – a new class !TupleTag was also created, for faster file reading

passing a file object to read_file() now works correctly, and also the file closing works as it should (caller needs to close any files passed in) (issue 73)

Fix for issue 72 : dataset.get() fails when passed type other than string or Tag. Patch contributed by !NikitaTheSpider

Fix for issue 58 : error opening file with unicode. Fix contributed by Pierre Raybaut

Fix for issue 42 : catch !AttributeError in property and give proper error message

Fix for issue 55 : UI type changed with string operations

Tag fixes and enhancements : can create tags with hex string (group, elem). Allow lists as well as tuples (issue 47). Fix arg2=0 bug (issue 64).

## Version 0.9.3¶

### Major changes¶

changed to MIT-style license

option to defer reading of large data element values using read_file()’s new defer_size argument (r102, r103)

dictionary of private tags added – descriptive text shown when available (issue36, r97, r110)

more conversion to PEP-8 style. Should now use read_file(), save_as(), pixel_array rather than !ReadFile(), !SaveAs(), !PixelArray. Old names kept for now as aliases.

### Other Enhancements¶

added DicomFileLike class to simplify and generalize access. Any object that has read, write, seek, tell, and close can now be used. (r105)

added dataset.iterall() function to iterate through all items (including inside sequences) (r105)

added dataset.formatted_lines() generator to allow custom formatting (r91, r113)

made reading tolerant of truncated files – gives a warning, but returns dataset read to that point (r95)

### Bug Fixes¶

fixed issue38, name collision for ‘Other Patient Ids’ as both data element and sequence name in DICOM standard (r95, r96)

fixed issue40, blank VRs in some DICOM dictionary entries caused NotImplementError on reading (r100)

fixed issue41, reading VRs of ‘US or SS’ and similar split on backslash character (r104)

fixed bug where TransferSyntaxUID not present when reading file without DICOM header (r109)

fixed print recursion bug when printing a UID (r111)

### Other¶

many of the example files updated

updated anonymize example file to also deal with ‘OtherPatientIDs’ and ‘PatientsBirthDate’ (r98)

## Version 0.9.2¶

### Major changes¶

Renamed Attribute class and related modules to !DataElement. Old code will continue to work until pydicom 1.0, but with a !DeprecationWarning (issue22, r72, r73)

Added support for character sets through Specific Character Set (0008,0005), using Python unicode. Thus foreign languages can display names in Greek, Japanese, Chinese etc characters in environments which support unicode (demonstrated in dicomtree.py example using Tkinter GUI) (r64, r65)

### Other Enhancements¶

Added support for auto-completion of dataset elements in ipython; also all environments using Python 2.6 (r69, r70)

Added __iter__() to Dataset so returns data elements in DICOM order with “for data_elem in dataset:” (r68)

Added dicomtree.py example program showing a DICOM file in a GUI window (Tkinter/Tix).

Added !PersonName class to parse components of names more easily (r55)

Added UID class to handle UID values. Name rather than UID number shown, UID_dictionary used (r51).

Code tested under Python 2.6

Added !DataElement.name property; synonym for !DataElement.description() function

### Bug Fixes¶

Fixed issue27, sequence with a single empty item read incorrectly

Fixed bug that read_OW did not handle !UndefinedLength (r50)

Fixed bugs in example files anonymize.py, !DicomInfo.py, and dicomtree.py (r51)

Fixed issue33, VR=UN being split on backslash (r70)

Fixed issue18, util directory not installed (r45)

### Other¶

Added example file myprint.py – shows how to custom format DICOM file information (r67)

Reorganized test files and added various new tests

added preliminary work on encapsulated data (r50)

added some simple files to view or work with pixel data (r46)

Dataset.!PixelDataArray() NumPy array changed to property Dataset.!PixelArray

changed to setuptools for packaging rather than distutils
