## Source: https://pandas.pydata.org/docs/reference/index.html

# API reference#

This page gives an overview of all public pandas objects, functions and
methods. All classes and functions exposed in `pandas.*`

namespace are public.

The following subpackages are public.

`pandas.errors`

: Custom exception and warnings classes that are raised by pandas.`pandas.plotting`

: Plotting public API.`pandas.testing`

: Functions that are useful for writing tests involving pandas objects.`pandas.api.extensions`

: Functions and classes for extending pandas objects.`pandas.api.indexers`

: Functions and classes for rolling window indexers.`pandas.api.interchange`

: DataFrame interchange protocol.`pandas.api.types`

: Datatype classes and functions.`pandas.api.typing`

: Classes that may be necessary for type-hinting. These are classes that are encountered as intermediate results but should not be instantiated directly by users. These classes are not to be confused with classes from the pandas-stubs package which has classes in addition to those that occur in pandas for type-hinting.

In addition, public functions in `pandas.io`

, `pandas.tseries`

, `pandas.util`

submodules
are explicitly mentioned in the documentation. Further APIs in these modules are not guaranteed
to be stable.

Warning

The `pandas.core`

, `pandas.compat`

top-level modules are PRIVATE. Stable functionality in such modules is not guaranteed.

- Input/output
- General functions
- Series
- Constructor
- Attributes
- Conversion
- Indexing, iteration
- Binary operator functions
- Function application, GroupBy & window
- Computations / descriptive stats
- Reindexing / selection / label manipulation
- Missing data handling
- Reshaping, sorting
- Combining / comparing / joining / merging
- Time Series-related
- Accessors
- Plotting
- Serialization / IO / conversion

- DataFrame
- Constructor
- Attributes and underlying data
- Conversion
- Indexing, iteration
- Binary operator functions
- Function application, GroupBy & window
- Computations / descriptive stats
- Reindexing / selection / label manipulation
- Missing data handling
- Reshaping, sorting, transposing
- Combining / comparing / joining / merging
- Time Series-related
- Flags
- Metadata
- Plotting
- Sparse accessor
- Serialization / IO / conversion

- pandas arrays, scalars, and data types
- Index objects
- Date offsets
- DateOffset
- BusinessDay
- BusinessHour
- CustomBusinessDay
- CustomBusinessHour
- MonthEnd
- MonthBegin
- BusinessMonthEnd
- BusinessMonthBegin
- CustomBusinessMonthEnd
- CustomBusinessMonthBegin
- SemiMonthEnd
- SemiMonthBegin
- Week
- WeekOfMonth
- LastWeekOfMonth
- BQuarterEnd
- BQuarterBegin
- QuarterEnd
- QuarterBegin
- BHalfYearEnd
- BHalfYearBegin
- HalfYearEnd
- HalfYearBegin
- BYearEnd
- BYearBegin
- YearEnd
- YearBegin
- FY5253
- FY5253Quarter
- Easter
- Tick
- Day
- Hour
- Minute
- Second
- Milli
- Micro
- Nano

- Frequencies
- Window
- GroupBy
- Resampling
- Style
- Plotting
- pandas.plotting.andrews_curves
- pandas.plotting.autocorrelation_plot
- pandas.plotting.bootstrap_plot
- pandas.plotting.boxplot
- pandas.plotting.deregister_matplotlib_converters
- pandas.plotting.lag_plot
- pandas.plotting.parallel_coordinates
- pandas.plotting.plot_params
- pandas.plotting.radviz
- pandas.plotting.register_matplotlib_converters
- pandas.plotting.scatter_matrix
- pandas.plotting.table

- Options and settings
- Extensions
- pandas.api.extensions.register_extension_dtype
- pandas.api.extensions.register_dataframe_accessor
- pandas.api.extensions.register_series_accessor
- pandas.api.extensions.register_index_accessor
- pandas.api.extensions.ExtensionDtype
- pandas.api.extensions.ExtensionArray
- pandas.arrays.NumpyExtensionArray
- pandas.api.indexers.check_array_indexer

- Testing
- Missing values
- pandas typing aliases

## Source: https://pandas.pydata.org/docs/reference/io.html

# Input/output#

## Pickling#

|
Load pickled pandas object (or any object) from file and return unpickled object. |
|
Pickle (serialize) object to file. |

## Flat file#

|
Read general delimited file into DataFrame. |
|
Read a comma-separated values (csv) file into DataFrame. |
|
Write object to a comma-separated values (csv) file. |
|
Read a table of fixed-width formatted lines into DataFrame. |

## Clipboard#

|
Read text from clipboard and pass to |
|
Copy object to the system clipboard. |

## Excel#

|
Read an Excel file into a |
|
Write object to an Excel sheet. |
|
Class for parsing tabular Excel sheets into DataFrame objects. |
Gets the Excel workbook. |
|
Names of the sheets in the document. |
|
|
Parse specified sheet(s) into a DataFrame. |

|
Write Styler to an Excel sheet. |

|
Class for writing DataFrame objects into excel sheets. |

## JSON#

|
Convert a JSON string to pandas object. |
|
Normalize semi-structured JSON data into a flat table. |
|
Convert the object to a JSON string. |

|
Create a Table schema from |

## HTML#

|
Read HTML tables into a |
|
Render a DataFrame as an HTML table. |

|
Write Styler to a file, buffer or string in HTML-CSS format. |

## XML#

|
Read XML document into a |
|
Render a DataFrame to an XML document. |

## Latex#

|
Render object to a LaTeX tabular, longtable, or nested table. |

|
Write Styler to a file, buffer or string in LaTeX format. |

## HDFStore: PyTables (HDF5)#

|
Read from the store, close it if we opened it. |
|
Store object in HDFStore. |
|
Append to Table in file. |
|
Retrieve pandas object stored in file. |
|
Retrieve pandas object stored in file, optionally based on where criteria. |
Print detailed information on the store. |
|
|
Return a list of keys corresponding to objects stored in HDFStore. |
Return a list of all the top-level nodes. |
|
|
Walk the pytables group hierarchy for pandas objects. |

## Feather#

|
Load a feather-format object from the file path. |
|
Write a DataFrame to the binary Feather format. |

## Parquet#

|
Load a parquet object from the file path, returning a DataFrame. |
|
Write a DataFrame to the binary parquet format. |

## Iceberg#

|
Read an Apache Iceberg table into a pandas DataFrame. |
|
Write a DataFrame to an Apache Iceberg table. |

Warning

`read_iceberg`

is experimental and may change without warning.

## ORC#

|
Load an ORC object from the file path, returning a DataFrame. |
|
Write a DataFrame to the Optimized Row Columnar (ORC) format. |

## SAS#

|
Read SAS files stored as either XPORT or SAS7BDAT format files. |

## SPSS#

|
Load an SPSS file from the file path, returning a DataFrame. |

## SQL#

|
Read SQL database table into a DataFrame. |
|
Read SQL query into a DataFrame. |
|
Read SQL query or database table into a DataFrame. |
|
Write records stored in a DataFrame to a SQL database. |

## STATA#

|
Read Stata file into DataFrame. |
|
Export DataFrame object to Stata dta format. |

Return data label of Stata file. |
|
Return a nested dict associating each variable name to its value and label. |
|
Return a dict associating each variable name with corresponding label. |
|
Export DataFrame object to Stata dta format. |

## Source: https://pandas.pydata.org/docs/reference/general_functions.html

# General functions#

## Data manipulations#

|
Unpivot a DataFrame from wide to long format, optionally leaving identifiers set. |
|
Return reshaped DataFrame organized by given index / column values. |
|
Create a spreadsheet-style pivot table as a DataFrame. |
|
Compute a simple cross tabulation of two (or more) factors. |
|
Bin values into discrete intervals. |
|
Quantile-based discretization function. |
|
Merge DataFrame or named Series objects with a database-style join. |
|
Perform a merge for ordered data with optional filling/interpolation. |
|
Perform a merge by key distance. |
|
Concatenate pandas objects along a particular axis. |
|
Convert categorical variable into dummy/indicator variables. |
|
Create a categorical |
|
Encode the object as an enumerated type or categorical variable. |
|
Return unique values based on a hash table. |
|
Reshape wide-format data to long. |
|
Unpivot a DataFrame from wide to long format. |

## Top-level missing data#

## Top-level dealing with numeric data#

|
Convert argument to a numeric type. |

## Top-level dealing with datetimelike data#

|
Convert argument to datetime. |
|
Convert argument to timedelta. |
|
Return a fixed frequency DatetimeIndex. |
|
Return a fixed frequency DatetimeIndex with business day as the default. |
|
Return a fixed frequency PeriodIndex. |
|
Return a fixed frequency TimedeltaIndex with day as the default. |
|
Infer the most likely frequency given the input index. |

## Top-level dealing with Interval data#

|
Return a fixed frequency IntervalIndex. |

## Top-level evaluation#

## Datetime formats#

|
Guess the datetime format of a given datetime string. |

## Hashing#

|
Given a 1d array, return an array of deterministic integers. |
|
Return a data hash of the Index/Series/DataFrame. |

## Importing from other DataFrame libraries#

|
Build a |

## Source: https://pandas.pydata.org/docs/reference/series.html

# Series#

## Constructor#

|
One-dimensional ndarray with axis labels (including time series). |

## Attributes#

**Axes**

The index (axis labels) of the Series. |
|
The ExtensionArray of the data backing this Series or Index. |
|
Return Series as ndarray or ndarray-like depending on the dtype. |
|
Return the dtype object of the underlying data. |
|
|
Print a concise summary of a Series. |
Return a tuple of the shape of the underlying data. |
|
Return the number of bytes in the underlying data. |
|
Number of dimensions of the underlying data, by definition 1. |
|
Return the number of elements in the underlying data. |
|
Return the transpose, which is by definition self. |
|
|
Return the memory usage of the Series. |
Return True if there are any NaNs. |
|
Indicator whether Index is empty. |
|
Return the dtype object of the underlying data. |
|
Return the name of the Series. |
|
Get the properties associated with this pandas object. |
|
|
Return a new object with updated flags. |

## Conversion#

|
Cast a pandas object to a specified dtype |
|
Convert columns from numpy dtypes to the best dtypes that support |
|
Attempt to infer better dtypes for object columns. |
|
Make a copy of this object's indices and data. |
|
A NumPy ndarray representing the values in this Series or Index. |
|
Convert Series from DatetimeIndex to PeriodIndex. |
|
Cast to DatetimeIndex of Timestamps, at |
Return a list of the values. |
|
|
Return the values as a NumPy array. |

## Indexing, iteration#

|
Get item from object for given key (ex: DataFrame column). |
Access a single value for a row/column label pair. |
|
Access a single value for a row/column pair by integer position. |
|
Access a group of rows and columns by label(s) or a boolean array. |
|
Purely integer-location based indexing for selection by position. |
|
Return an iterator of the values. |
|
Lazily iterate over (index, value) tuples. |
|
Return alias for index. |
|
|
Return item and drops from series. |
Return the first element of the underlying data as a Python scalar. |
|
|
Return cross-section from the Series/DataFrame. |

For more information on `.at`

, `.iat`

, `.loc`

, and
`.iloc`

, see the indexing documentation.

## Binary operator functions#

|
Return Addition of series and other, element-wise (binary operator add). |
|
Return Subtraction of series and other, element-wise (binary operator sub). |
|
Return Multiplication of series and other, element-wise (binary operator mul). |
|
Return Floating division of series and other, element-wise (binary operator truediv). |
|
Return Floating division of series and other, element-wise (binary operator truediv). |
|
Return Integer division of series and other, element-wise (binary operator floordiv). |
|
Return Modulo of series and other, element-wise (binary operator mod). |
|
Return Exponential power of series and other, element-wise (binary operator pow). |
|
Return Addition of series and other, element-wise (binary operator radd). |
|
Return Subtraction of series and other, element-wise (binary operator rsub). |
|
Return Multiplication of series and other, element-wise (binary operator rmul). |
|
Return Floating division of series and other, element-wise (binary operator rtruediv). |
|
Return Floating division of series and other, element-wise (binary operator rtruediv). |
|
Return Integer division of series and other, element-wise (binary operator rfloordiv). |
|
Return Modulo of series and other, element-wise (binary operator rmod). |
|
Return Exponential power of series and other, element-wise (binary operator rpow). |
|
Combine the Series with a Series or scalar according to func. |
|
Update null elements with value in the same location in 'other'. |
|
Round each value in a Series to the given number of decimals. |
|
Return Greater than of series and other, element-wise (binary operator lt). |
|
Return Greater than of series and other, element-wise (binary operator gt). |
|
Return Less than or equal to of series and other, element-wise (binary operator le). |
|
Return Greater than or equal to of series and other, element-wise (binary operator ge). |
|
Return Not equal to of series and other, element-wise (binary operator ne). |
|
Return Equal to of series and other, element-wise (binary operator eq). |
|
Return the product of the values over the requested axis. |
|
Compute the dot product between the Series and the columns of other. |

## Function application, GroupBy & window#

|
Invoke function on values of Series. |
|
Aggregate using one or more operations over the specified axis. |
|
Aggregate using one or more operations over the specified axis. |
|
Call |
|
Map values of Series according to an input mapping or function. |
|
Group Series using a mapper or by a Series of columns. |
|
Provide rolling window calculations. |
|
Provide expanding window calculations. |
|
Provide exponentially weighted (EW) calculations. |
|
Apply chainable functions that expect Series or DataFrames. |

## Computations / descriptive stats#

Return a Series/DataFrame with absolute numeric value of each element. |
|
|
Return whether all elements are True, potentially over an axis. |
|
Return whether any element is True, potentially over an axis. |
|
Compute the lag-N autocorrelation. |
|
Return boolean Series equivalent to left <= series <= right. |
|
Trim values at input threshold(s). |
|
Compute correlation with other Series, excluding missing values. |
Return number of non-NA/null observations in the Series. |
|
|
Compute covariance with Series, excluding missing values. |
|
Return cumulative maximum over a Series. |
|
Return cumulative minimum over a Series. |
|
Return cumulative product over a Series. |
|
Return cumulative sum over a Series. |
|
Generate descriptive statistics. |
|
First discrete difference of Series elements. |
|
Encode the object as an enumerated type or categorical variable. |
|
Return unbiased kurtosis over requested axis. |
|
Return the maximum of the values over the requested axis. |
|
Return the mean of the values over the requested axis. |
|
Return the median of the values over the requested axis. |
|
Return the minimum of the values over the requested axis. |
|
Return the mode(s) of the Series. |
|
Return the largest n elements. |
|
Return the smallest n elements. |
|
Fractional change between the current and a prior element. |
|
Return the product of the values over the requested axis. |
|
Return value at the given quantile. |
|
Compute numerical data ranks (1 through n) along axis. |
|
Return unbiased standard error of the mean over requested axis. |
|
Return unbiased skew over requested axis. |
|
Return sample standard deviation. |
|
Return the sum of the values over the requested axis. |
|
Return unbiased variance over requested axis. |
|
Return unbiased kurtosis over requested axis. |
Return unique values of Series object. |
|
|
Return number of unique elements in the object. |
Return True if values in the object are unique. |
|
Return True if values in the object are monotonically increasing. |
|
Return True if values in the object are monotonically decreasing. |
|
|
Return a Series containing counts of unique values. |

## Reindexing / selection / label manipulation#

|
Align two objects on their axes with the specified join method. |
|
Replace values where the conditions are True. |
|
Return Series with specified index labels removed. |
|
Return Series/DataFrame with requested index / column level(s) removed. |
|
Return Series with duplicate values removed. |
|
Indicate duplicate Series values. |
|
Test whether two objects contain the same elements. |
|
Return the first n rows. |
|
Return the row label of the maximum value. |
|
Return the row label of the minimum value. |
|
Whether elements in Series are contained in values. |
|
Conform Series to new index with optional filling logic. |
|
Return an object with matching indices as other object. |
|
Alter Series index labels or name. |
|
Set the name of the axis for the index. |
|
Generate a new DataFrame or Series with the index reset. |
|
Return a random sample of items from an axis of object. |
|
(DEPRECATED) Assign desired index to given axis. |
|
Return the elements in the given |
|
Return the last n rows. |
|
Truncate a Series or DataFrame before and after some index value. |
|
Replace values where the condition is False. |
|
Replace values where the condition is True. |
|
Prefix labels with string prefix. |
|
Suffix labels with string suffix. |
|
Subset the DataFrame or Series according to the specified index labels. |

## Missing data handling#

|
Fill NA/NaN values by using the next valid observation to fill the gap. |
|
Return a new Series with missing values removed. |
|
Fill NA/NaN values by propagating the last valid observation to next valid. |
|
Fill NA/NaN values with value. |
|
Fill NaN values using an interpolation method. |
Detect missing values. |
|
Series.isnull is an alias for Series.isna. |
|
Detect existing (non-missing) values. |
|
Series.notnull is an alias for Series.notna. |
|
|
Replace values given in to_replace with value. |

## Reshaping, sorting#

|
Return the integer indices that would sort the Series values. |
|
Return int position of the smallest value in the Series. |
|
Return int position of the largest value in the Series. |
|
Rearrange index levels using input order. |
|
Sort by the values. |
|
Sort Series by index labels. |
|
Swap levels i and j in a |
|
Unstack, also known as pivot, Series with MultiIndex to produce DataFrame. |
|
Transform each element of a list-like to a row. |
|
Find indices where elements should be inserted to maintain order. |
|
Repeat elements of a Series. |
|
Squeeze 1 dimensional axis objects into scalars. |

## Combining / comparing / joining / merging#

|
Compare to another Series and show the differences. |
|
Modify Series in place using values from passed Series. |

## Accessors#

pandas provides dtype-specific methods under various accessors.
These are separate namespaces within `Series`

that only apply
to specific data types.

### Datetimelike properties#

`Series.dt`

can be used to access the values of the series as
datetimelike and return several properties.
These can be accessed like `Series.dt.<property>`

.

#### Datetime properties#

Returns numpy array of python |
|
Returns numpy array of |
|
Returns numpy array of |
|
The year of the datetime. |
|
The month as January=1, December=12. |
|
The day of the datetime. |
|
The hours of the datetime. |
|
The minutes of the datetime. |
|
The seconds of the datetime. |
|
The microseconds of the datetime. |
|
The nanoseconds of the datetime. |
|
The day of the week with Monday=0, Sunday=6. |
|
The day of the week with Monday=0, Sunday=6. |
|
The day of the week with Monday=0, Sunday=6. |
|
The ordinal day of the year. |
|
The ordinal day of the year. |
|
The number of days in the month. |
|
The quarter of the date. |
|
Indicates whether the date is the first day of the month. |
|
Indicates whether the date is the last day of the month. |
|
Indicator for whether the date is the first day of a quarter. |
|
Indicator for whether the date is the last day of a quarter. |
|
Indicate whether the date is the first day of a year. |
|
Indicate whether the date is the last day of the year. |
|
Boolean indicator if the date belongs to a leap year. |
|
The number of days in the month. |
|
The number of days in the month. |
|
Return the timezone. |
|
Tries to return a string representing a frequency generated by infer_freq. |
|
The precision unit of the datetime data. |

#### Datetime methods#

Calculate year, week, and day according to the ISO 8601 standard. |
|
|
Cast to PeriodArray/PeriodIndex at a particular frequency. |
Return the data as a Series of |
|
|
Localize tz-naive Datetime Array/Index to tz-aware Datetime Array/Index. |
Convert tz-aware Datetime Array/Index from one time zone to another. |
|
Convert times to midnight. |
|
|
Convert to Index using specified date_format. |
|
Perform round operation on the data to the specified freq. |
|
Perform floor operation on the data to the specified freq. |
|
Perform ceil operation on the data to the specified freq. |
|
Return the month names with specified locale. |
|
Return the day names with specified locale. |
|
Convert to a dtype with the given unit resolution. |

#### Period properties#

Fiscal year the Period lies in according to its starting-quarter. |
|
Get the Timestamp for the start of the period. |
|
Get the Timestamp for the end of the period. |

#### Timedelta properties#

Number of days for each element. |
|
Number of seconds (>= 0 and less than 1 day) for each element. |
|
Number of microseconds (>= 0 and less than 1 second) for each element. |
|
Number of nanoseconds (>= 0 and less than 1 microsecond) for each element. |
|
Return a Dataframe of the components of the Timedeltas. |
|
The precision unit of the datetime data. |

#### Timedelta methods#

Return an array of native |
|
Return total duration of each element expressed in seconds. |
|
|
Convert to a dtype with the given unit resolution. |

### String handling#

`Series.str`

can be used to access the values of the series as
strings and apply several methods to it. These can be accessed like
`Series.str.<function/property>`

.

Convert strings in the Series/Index to be capitalized. |
|
Convert strings in the Series/Index to be casefolded. |
|
|
Concatenate strings in the Series/Index with given separator. |
|
Pad left and right side of strings in the Series/Index. |
|
Test if pattern or regex is contained within a string of a Series or Index. |
|
Count occurrences of pattern in each string of the Series/Index. |
|
Decode character string in the Series/Index using indicated encoding. |
|
Encode character string in the Series/Index using indicated encoding. |
|
Test if the end of each string element matches a pattern. |
|
Extract capture groups in the regex pat as columns in a DataFrame. |
|
Extract capture groups in the regex pat as columns in DataFrame. |
|
Return lowest indexes in each strings in the Series/Index. |
|
Find all occurrences of pattern or regular expression in the Series/Index. |
|
Determine if each string entirely matches a regular expression. |
Extract element from each component at specified position or with specified key. |
|
|
Return lowest indexes in each string in Series/Index. |
Check whether all characters in each string are ascii. |
|
|
Join lists contained as elements in the Series/Index with passed delimiter. |
Compute the length of each element in the Series/Index. |
|
|
Pad right side of strings in the Series/Index. |
Convert strings in the Series/Index to lowercase. |
|
|
Remove leading characters. |
|
Determine if each string starts with a match of a regular expression. |
|
Return the Unicode normal form for the strings in the Series/Index. |
|
Pad strings in the Series/Index up to width. |
|
Split the string at the first occurrence of sep. |
|
Remove a prefix from an object series. |
|
Remove a suffix from an object series. |
|
Duplicate each string in the Series or Index. |
|
Replace each occurrence of pattern/regex in the Series/Index. |
|
Return highest indexes in each strings in the Series/Index. |
|
Return highest indexes in each string in Series/Index. |
|
Pad left side of strings in the Series/Index. |
|
Split the string at the last occurrence of sep. |
|
Remove trailing characters. |
|
Slice substrings from each element in the Series or Index. |
|
Replace a positional slice of a string with another value. |
|
Split strings around given separator/delimiter. |
|
Split strings around given separator/delimiter. |
|
Test if the start of each string element matches a pattern. |
|
Remove leading and trailing characters. |
Convert strings in the Series/Index to be swapcased. |
|
Convert strings in the Series/Index to titlecase. |
|
|
Map all characters in the string through the given mapping table. |
Convert strings in the Series/Index to uppercase. |
|
|
Wrap strings in Series/Index at specified line width. |
|
Pad strings in the Series/Index by prepending '0' characters. |
Check whether all characters in each string are alphanumeric. |
|
Check whether all characters in each string are alphabetic. |
|
Check whether all characters in each string are digits. |
|
Check whether all characters in each string are whitespace. |
|
Check whether all characters in each string are lowercase. |
|
Check whether all characters in each string are uppercase. |
|
Check whether all characters in each string are titlecase. |
|
Check whether all characters in each string are numeric. |
|
Check whether all characters in each string are decimal. |
|
|
Return DataFrame of dummy/indicator variables for Series. |

### Categorical accessor#

Categorical-dtype specific methods and attributes are available under
the `Series.cat`

accessor.

The categories of this categorical. |
|
Whether the categories have an ordered relationship. |
|
Return Series of codes as well as the index. |

|
Rename categories. |
|
Reorder categories as specified in new_categories. |
|
Add new categories. |
|
Remove the specified categories. |
Remove categories which are not used. |
|
|
Set the categories to the specified new categories. |
Set the Categorical to be ordered. |
|
Set the Categorical to be unordered. |

### Sparse accessor#

Sparse-dtype specific methods and attributes are provided under the
`Series.sparse`

accessor.

The number of non- |
|
The percent of non- |
|
Elements in data that are fill_value are not stored. |
|
An ndarray containing the non- |

|
Create a Series with sparse values from a scipy.sparse.coo_matrix. |
|
Create a scipy.sparse.coo_matrix from a Series with MultiIndex. |

### List accessor#

Arrow list-dtype specific methods and attributes are provided under the
`Series.list`

accessor.

Flatten list values. |
|
Return the length of each list in the Series. |
|
Index or slice lists in the Series. |

### Struct accessor#

Arrow struct-dtype specific methods and attributes are provided under the
`Series.struct`

accessor.

Return the dtype object of each child field of the struct. |

|
Extract a child field of a struct as a Series. |
Extract all child fields of a struct as a DataFrame. |

### Flags#

Flags refer to attributes of the pandas object. Properties of the dataset (like
the date is was recorded, the URL it was accessed from, etc.) should be stored
in `Series.attrs`

.

|
Flags that apply to pandas objects. |

### Metadata#

`Series.attrs`

is a dictionary for storing global metadata for this Series.

Warning

`Series.attrs`

is considered experimental and may change without warning.

Dictionary of global attributes of this dataset. |

## Plotting#

`Series.plot`

is both a callable method and a namespace attribute for
specific plotting methods of the form `Series.plot.<kind>`

.

|
Series plotting accessor and method |

|
Draw a stacked area plot. |
|
Vertical bar plot. |
|
Make a horizontal bar plot. |
|
Make a box plot of the DataFrame columns. |
|
Generate Kernel Density Estimate plot using Gaussian kernels. |
|
Draw one histogram of the DataFrame's columns. |
|
Generate Kernel Density Estimate plot using Gaussian kernels. |
|
Plot Series or DataFrame as lines. |
|
Generate a pie plot. |

|
Draw histogram of the input series using matplotlib. |

## Serialization / IO / conversion#

|
Construct a Series from an array-like Arrow object. |
|
Pickle (serialize) object to file. |
|
Write object to a comma-separated values (csv) file. |
|
Convert Series to {label -> value} dict or dict-like object. |
|
Write object to an Excel sheet. |
|
Convert Series to DataFrame. |
Return an xarray object from the pandas object. |
|
|
Write the contained data to an HDF5 file using HDFStore. |
|
Write records stored in a DataFrame to a SQL database. |
|
Convert the object to a JSON string. |
|
Render a string representation of the Series. |
|
Copy object to the system clipboard. |
|
Render object to a LaTeX tabular, longtable, or nested table. |
|
Print Series in Markdown-friendly format. |
