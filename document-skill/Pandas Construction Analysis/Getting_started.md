## Source: https://pandas.pydata.org/docs/getting_started/index.html

# Getting started#

## Installation#

pandas can be installed via conda from conda-forge.

pandas can be installed via pip from PyPI.

Installing a specific version? Installing from source? Check the advanced installation page.

## Intro to pandas#

When working with tabular data, such as data stored in spreadsheets or databases, pandas is the right tool for you. pandas will help you
to explore, clean, and process your data. In pandas, a data table is called a `DataFrame`

.

pandas supports the integration with many file formats or data sources out of the box (csv, excel, sql, json, parquet,…). The ability to import data from each of these
data sources is provided by functions with the prefix, `read_*`

. Similarly, the `to_*`

methods are used to store data.

Selecting or filtering specific rows and/or columns? Filtering the data on a particular condition? Methods for slicing, selecting, and extracting the data you need are available in pandas.

pandas provides plotting for your data right out of the box with the power of Matplotlib. Simply pick the plot type (scatter, bar, boxplot,…) corresponding to your data.

There’s no need to loop over all rows of your data table to do calculations. Column data manipulations work elementwise in pandas.
Adding a column to a `DataFrame`

based on existing data in other columns is straightforward.

Basic statistics (mean, median, min, max, counts…) are easily calculable across data frames. These, or even custom aggregations, can be applied on the entire data set, a sliding window of the data, or grouped by categories. The latter is also known as the split-apply-combine approach.

Multiple tables can be concatenated column wise or row wise with pandas’ database-like join and merge operations.

pandas has great support for time series and has an extensive set of tools for working with dates, times, and time-indexed data.

Data sets often contain more than just numerical data. pandas provides a wide range of functions to clean textual data and extract useful information from it.

## Coming from…#

Are you familiar with other software for manipulating tabular data? Learn the pandas-equivalent operations compared to software you already know:

The R programming language provides a
`data.frame`

data structure as well as packages like
tidyverse which use and extend `data.frame`

for convenient data handling functionalities similar to pandas.

Already familiar with `SELECT`

, `GROUP BY`

, `JOIN`

, etc.?
Many SQL manipulations have equivalents in pandas.

The `data set`

included in the STATA
statistical software suite corresponds to the pandas `DataFrame`

.
Many of the operations known from STATA have an equivalent in pandas.

Users of Excel or other spreadsheet programs will find that many of the concepts are transferable to pandas.

SAS, the statistical software suite,
uses the `data set`

structure, which closely corresponds pandas’ `DataFrame`

.
Also SAS vectorized operations such as filtering or string processing operations
have similar functions in pandas.

## Tutorials#

For a quick overview of pandas functionality, see 10 Minutes to pandas.

You can also reference the pandas cheat sheet for a succinct guide for manipulating data with pandas.

The community produces a wide variety of tutorials available online. Some of the material is enlisted in the community contributed Community tutorials.

## Source: https://pandas.pydata.org/docs/getting_started/install.html

# Installation#

The pandas development team officially distributes pandas for installation through the following methods:

Available on conda-forge for installation with the conda package manager.

Available on PyPI for installation with pip.

Available on Github for installation from source.

Note

pandas may be installable from other sources besides the ones listed above,
but they are **not** managed by the pandas development team.

## Python version support#

## Installing pandas#

### Installing with Conda#

For users working with the Conda package manager,
pandas can be installed from the `conda-forge`

channel.

```
```

To install the Conda package manager on your system, the Miniforge distribution is recommended.

Additionally, it is recommended to install and run pandas from a virtual environment.

```
conda create -c conda-forge -n name_of_my_env python pandas
# On Linux or MacOS
source activate name_of_my_env
# On Windows
activate name_of_my_env
```

Tip

For users that are new to Python, the easiest way to install Python, pandas, and the packages that make up the PyData stack such as SciPy, NumPy and Matplotlib is with Anaconda, a cross-platform (Linux, macOS, Windows) Python distribution for data analytics and scientific computing.

However, pandas from Anaconda is **not** officially managed by the pandas development team.

### Installing with pip#

For users working with the pip package manager, pandas can be installed from PyPI.

```
```

pandas can also be installed with sets of optional dependencies to enable certain functionality. For example, to install pandas with the optional dependencies to read Excel files.

```
```

The full list of extras that can be installed can be found in the dependency section.

Additionally, it is recommended to install and run pandas from a virtual environment, for example, using the Python standard library’s venv

### Installing from source#

See the contributing guide for complete instructions on building from the git source tree. Further, see creating a development environment if you wish to create a pandas development environment.

### Installing the development version of pandas#

Installing the development version is the quickest way to:

Try a new feature that will be shipped in the next release (that is, a feature from a pull-request that was recently merged to the main branch).

Check whether a bug you encountered has been fixed since the last release.

The development version is usually uploaded daily to the scientific-python-nightly-wheels index from the PyPI registry of anaconda.org. You can install it by running.

```
```

Note

You might be required to uninstall an existing version of pandas to install the development version.

```
pip uninstall pandas -y
```

## Running the test suite#

If pandas has been installed from source, running `pytest pandas`

will run all of pandas unit tests.

The unit tests can also be run from the pandas module itself with the `test()`

function. The packages required to run the tests

.

Note

Test failures are not necessarily indicative of a broken pandas installation.

## Dependencies#

### Required dependencies#

pandas requires the following dependencies.

Package |
Minimum supported version |
|---|---|
1.26.0 |
|
2.8.2 |
|
tzdata * |
/ |

* `tzdata`

is only required on Windows and Pyodide (Emscripten).

Generally, the minimum supported version is ~2 years old from the release date of a major or minor pandas version.

### Optional dependencies#

pandas has many optional dependencies that are only used for specific methods.
For example, `pandas.read_hdf()`

requires the `pytables`

package, while
`DataFrame.to_markdown()`

requires the `tabulate`

package. If the
optional dependency is not installed, pandas will raise an `ImportError`

when
the method requiring that dependency is called.

With pip, optional pandas dependencies can be installed or managed in a file (e.g. requirements.txt or pyproject.toml)
as optional extras (e.g. `pandas[performance, aws]`

). All optional dependencies can be installed with `pandas[all]`

,
and specific sets of dependencies are listed in the sections below.

Generally, the minimum supported version is ~1 years old from the release date of a major or minor pandas version. Older versions of optional dependencies may still work, but they are not tested or considered supported.

#### Performance dependencies (recommended)#

Note

You are highly encouraged to install these libraries, as they provide speed improvements, especially when working with large data sets.

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
2.10.2 |
performance |
Accelerates certain numerical operations by using multiple cores as well as smart chunking and caching to achieve large speedups |
|
1.4.2 |
performance |
Accelerates certain types of |
|
0.60.0 |
performance |
Alternative execution engine for operations that accept |

#### Visualization#

.

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
3.8.3 |
plot |
Plotting library |
|
3.1.3 |
output-formatting |
Conditional formatting with DataFrame.style |
|
0.9.0 |
output-formatting |
Printing in Markdown-friendly format (see tabulate) |

#### Computation#

.

#### Excel files#

.

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
2.0.1 |
excel |
Reading for xls files |
|
3.2.0 |
excel |
Writing for xlsx files |
|
3.1.5 |
excel |
Reading / writing for Excel 2010 xlsx/xlsm/xltx/xltm files |
|
1.0.10 |
excel |
Reading for xlsb files |
|
0.3.0 |
excel |
Reading for xls/xlsx/xlsm/xlsb/xla/xlam/ods files |
|
1.4.1 |
excel |
Reading / writing for OpenDocument 1.2 files |

#### HTML#

.

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
4.12.3 |
html |
HTML parser for read_html |
|
1.1 |
html |
HTML parser for read_html |
|
4.9.2 |
html |
HTML parser for read_html |

One of the following combinations of libraries is needed to use the
top-level `read_html()`

function:

BeautifulSoup4 and lxml

BeautifulSoup4 and html5lib and lxml

Only lxml, although see HTML Table Parsing for reasons as to why you should probably

**not**take this approach.

Warning

if you install BeautifulSoup4 you must install either lxml or html5lib or both.

`read_html()`

will**not**work with*only*BeautifulSoup4 installed.You are highly encouraged to read HTML Table Parsing gotchas. It explains issues surrounding the installation and usage of the above three libraries.

#### XML#

.

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
5.3.0 |
xml |
XML parser for read_xml and tree builder for to_xml |

#### SQL databases#

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
2.0.36 |
postgresql, mysql, sql-other |
SQL support for databases other than sqlite |
|
2.9.10 |
postgresql |
PostgreSQL engine for sqlalchemy |
|
1.1.1 |
mysql |
MySQL engine for sqlalchemy |
|
1.2.0 |
postgresql |
ADBC Driver for PostgreSQL |
|
1.2.0 |
sql-other |
ADBC Driver for SQLite |

#### Other data sources#

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
3.10.1 |
hdf5 |
HDF5-based reading / writing |
|
hdf5 |
Compression for HDF5 |
||
2024.11.0 |
Parquet reading / writing (pyarrow is default) |
||
13.0.0 |
parquet, feather |
Parquet, ORC, and feather reading / writing |
|
0.8.1 |
iceberg |
Apache Iceberg reading / writing |
|
1.2.8 |
spss |
SPSS files (.sav) reading |
|
1.4.1 |
excel |
Open document format (.odf, .ods, .odt) reading / writing |

Warning

If you want to use

`read_orc()`

, it is highly recommended to install pyarrow using conda.`read_orc()`

may fail if pyarrow was installed from pypi, and`read_orc()`

is not compatible with Windows OS.

#### Access data in the cloud#

#### Clipboard#

.

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
5.15.9 |
clipboard |
Clipboard I/O |
|
2.4.2 |
clipboard |
Clipboard I/O |

Note

Depending on operating system, system-level packages may need to installed.
For clipboard to operate on Linux one of the CLI tools `xclip`

or `xsel`

must be installed on your system.

#### Compression#

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
0.19.0 |
compression |
Zstandard compression |

#### Timezone#

Dependency |
Minimum Version |
pip extra |
Notes |
|---|---|---|---|
2024.2 |
timezone |
Alternative timezone library to |

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

# Getting started tutorials#

- What kind of data does pandas handle?
- How do I read and write tabular data?
- How do I select a subset of a
`DataFrame`

? - How do I create plots in pandas?
- How to create new columns derived from existing columns
- How to calculate summary statistics
- How to reshape the layout of tables
- How to combine data from multiple tables
- How to handle time series data with ease
- How to manipulate textual data

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html

# What kind of data does pandas handle?#

I want to start using pandas

In [1]: import pandas as pd

To load the pandas package and start working with it, import the package. The community agreed alias for pandas is

`pd`

, so loading pandas as`pd`

is assumed standard practice for all of the pandas documentation.

## pandas data table representation#

I want to store passenger data of the Titanic. For a number of passengers, I know the name (characters), age (integers) and sex (male/female) data.

In [2]: df = pd.DataFrame( ...: { ...: "Name": [ ...: "Braund, Mr. Owen Harris", ...: "Allen, Mr. William Henry", ...: "Bonnell, Miss Elizabeth", ...: ], ...: "Age": [22, 35, 58], ...: "Sex": ["male", "male", "female"], ...: } ...: ) ...: In [3]: df Out[3]: Name Age Sex 0 Braund, Mr. Owen Harris 22 male 1 Allen, Mr. William Henry 35 male 2 Bonnell, Miss Elizabeth 58 female

To manually store data in a table, create a

`DataFrame`

. When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values in each list as columns of the`DataFrame`

.

A `DataFrame`

is a 2-dimensional data structure that can store data of
different types (including characters, integers, floating point values,
categorical data and more) in columns. It is similar to a spreadsheet, a
SQL table or the `data.frame`

in R.

The table has 3 columns, each of them with a column label. The column labels are respectively

`Name`

,`Age`

and`Sex`

.The column

`Name`

consists of textual data with each value a string, the column`Age`

are numbers and the column`Sex`

is textual data.The index labels each row. By default, this is a sequence of integers starting at 0.

In spreadsheet software, the table representation of our data would look very similar:

## Each column in a `DataFrame`

is a `Series`

#

I’m just interested in working with the data in the column

`Age`

In [4]: df["Age"] Out[4]: 0 22 1 35 2 58 Name: Age, dtype: int64

When selecting a single column of a pandas

`DataFrame`

, the result is a pandas`Series`

. To select the column, use the column label in between square brackets`[]`

.

Note

If you are familiar with Python dictionaries, the selection of a single column is very similar to the selection of dictionary values based on the key.

You can create a `Series`

from scratch as well:

```
In [5]: ages = pd.Series([22, 35, 58], name="Age")
In [6]: ages
Out[6]:
0 22
1 35
2 58
Name: Age, dtype: int64
```

A pandas `Series`

has no column labels, as it is just a single column
of a `DataFrame`

. A Series does have row labels.

## Do something with a DataFrame or Series#

I want to know the maximum Age of the passengers

We can do this on the

`DataFrame`

by selecting the`Age`

column and applying`max()`

:In [7]: df["Age"].max() Out[7]: 58

Or to the

`Series`

:In [8]: ages.max() Out[8]: 58

As illustrated by the `max()`

method, you can *do* things with a
`DataFrame`

or `Series`

. pandas provides a lot of functionalities,
each of them a *method* you can apply to a `DataFrame`

or `Series`

.
As methods are functions, do not forget to use parentheses `()`

.

I’m interested in some basic statistics of the numerical data of my data table

In [9]: df.describe() Out[9]: Age count 3.000000 mean 38.333333 std 18.230012 min 22.000000 25% 28.500000 50% 35.000000 75% 46.500000 max 58.000000

The

`describe()`

method provides a quick overview of the numerical data in a`DataFrame`

. As the`Name`

and`Sex`

columns are textual data, these are by default not taken into account by the`describe()`

method.

Many pandas operations return a `DataFrame`

or a `Series`

. The
`describe()`

method is an example of a pandas operation returning a
pandas `Series`

or a pandas `DataFrame`

.

Check more options on `describe`

in the user guide section about aggregations with describe

Note

This is just a starting point. Similar to spreadsheet software, pandas represents data as a table with columns and rows. Apart from the representation, the data manipulations and calculations you would do in spreadsheet software are also supported by pandas. Continue reading the next tutorials to get started!

#### REMEMBER

Import the package, aka

`import pandas as pd`

A table of data is stored as a pandas

`DataFrame`

Each column in a

`DataFrame`

is a`Series`

You can do things by applying a method on a

`DataFrame`

or`Series`

A more extended explanation of `DataFrame`

and `Series`

is provided in the introduction to data structures page.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html

```
In [1]: import pandas as pd
```

- Titanic data
This tutorial uses the Titanic data set, stored as CSV. The data consists of the following data columns:

PassengerId: Id of every passenger.

Survived: Indication whether passenger survived.

`0`

for no and`1`

for yes.Pclass: One out of the 3 ticket classes: Class

`1`

, Class`2`

and Class`3`

.Name: Name of passenger.

Sex: Gender of passenger.

Age: Age of passenger in years.

SibSp: Number of siblings or spouses aboard.

Parch: Number of parents or children aboard.

Ticket: Ticket number of passenger.

Fare: Indicating the fare.

Cabin: Cabin number of passenger.

Embarked: Port of embarkation.

# How do I read and write tabular data?#

I want to analyze the Titanic passenger data, available as a CSV file.

In [2]: titanic = pd.read_csv("data/titanic.csv")

pandas provides the

`read_csv()`

function to read data stored as a csv file into a pandas`DataFrame`

. pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), each of them with the prefix`read_*`

.

Make sure to always have a check on the data after reading in the
data. When displaying a `DataFrame`

, the first and last 5 rows will be
shown by default:

```
In [3]: titanic
Out[3]:
PassengerId Survived Pclass ... Fare Cabin Embarked
0 1 0 3 ... 7.2500 NaN S
1 2 1 1 ... 71.2833 C85 C
2 3 1 3 ... 7.9250 NaN S
3 4 1 1 ... 53.1000 C123 S
4 5 0 3 ... 8.0500 NaN S
.. ... ... ... ... ... ... ...
886 887 0 2 ... 13.0000 NaN S
887 888 1 1 ... 30.0000 B42 S
888 889 0 3 ... 23.4500 NaN S
889 890 1 1 ... 30.0000 C148 C
890 891 0 3 ... 7.7500 NaN Q
[891 rows x 12 columns]
```

I want to see the first 8 rows of a pandas DataFrame.

In [4]: titanic.head(8) Out[4]: PassengerId Survived Pclass ... Fare Cabin Embarked 0 1 0 3 ... 7.2500 NaN S 1 2 1 1 ... 71.2833 C85 C 2 3 1 3 ... 7.9250 NaN S 3 4 1 1 ... 53.1000 C123 S 4 5 0 3 ... 8.0500 NaN S 5 6 0 3 ... 8.4583 NaN Q 6 7 0 1 ... 51.8625 E46 S 7 8 0 3 ... 21.0750 NaN S [8 rows x 12 columns]

To see the first N rows of a

`DataFrame`

, use the`head()`

method with the required number of rows (in this case 8) as argument.

Note

Interested in the last N rows instead? pandas also provides a
`tail()`

method. For example, `titanic.tail(10)`

will return the last
10 rows of the DataFrame.

A check on how pandas interpreted each of the column data types can be
done by requesting the pandas `dtypes`

attribute:

```
In [5]: titanic.dtypes
Out[5]:
PassengerId int64
Survived int64
Pclass int64
Name str
Sex str
Age float64
SibSp int64
Parch int64
Ticket str
Fare float64
Cabin str
Embarked str
dtype: object
```

For each of the columns, the used data type is enlisted. The data types
in this `DataFrame`

are integers (`int64`

), floats (`float64`

) and
strings (`object`

).

Note

When asking for the `dtypes`

, no parentheses `()`

are used!
`dtypes`

is an attribute of a `DataFrame`

and `Series`

. Attributes
of a `DataFrame`

or `Series`

do not need `()`

. Attributes
represent a characteristic of a `DataFrame`

/`Series`

, whereas
methods (which require parentheses `()`

) *do* something with the
`DataFrame`

/`Series`

as introduced in the first tutorial.

My colleague requested the Titanic data as a spreadsheet.

Note

If you want to use

`to_excel()`

and`read_excel()`

, you need to install an Excel reader as outlined in the Excel files section of the installation documentation.In [6]: titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

Whereas

`read_*`

functions are used to read data to pandas, the`to_*`

methods are used to store data. The`to_excel()`

method stores the data as an excel file. In the example here, the`sheet_name`

is named*passengers*instead of the default*Sheet1*. By setting`index=False`

the row index labels are not saved in the spreadsheet.

The equivalent read function `read_excel()`

will reload the data to a
`DataFrame`

:

```
In [7]: titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```

```
In [8]: titanic.head()
Out[8]:
PassengerId Survived Pclass ... Fare Cabin Embarked
0 1 0 3 ... 7.2500 NaN S
1 2 1 1 ... 71.2833 C85 C
2 3 1 3 ... 7.9250 NaN S
3 4 1 1 ... 53.1000 C123 S
4 5 0 3 ... 8.0500 NaN S
[5 rows x 12 columns]
```

I’m interested in a technical summary of a

`DataFrame`

In [9]: titanic.info() <class 'pandas.DataFrame'> RangeIndex: 891 entries, 0 to 890 Data columns (total 12 columns): # Column Non-Null Count Dtype --- ------ -------------- ----- 0 PassengerId 891 non-null int64 1 Survived 891 non-null int64 2 Pclass 891 non-null int64 3 Name 891 non-null str 4 Sex 891 non-null str 5 Age 714 non-null float64 6 SibSp 891 non-null int64 7 Parch 891 non-null int64 8 Ticket 891 non-null str 9 Fare 891 non-null float64 10 Cabin 204 non-null str 11 Embarked 889 non-null str dtypes: float64(2), int64(5), str(5) memory usage: 118.7 KB

The method

`info()`

provides technical information about a`DataFrame`

, so let’s explain the output in more detail:It is indeed a

`DataFrame`

.There are 891 entries, i.e. 891 rows.

Each row has a row label (aka the

`index`

) with values ranging from 0 to 890.The table has 12 columns. Most columns have a value for each of the rows (all 891 values are

`non-null`

). Some columns do have missing values and less than 891`non-null`

values.The columns

`Name`

,`Sex`

,`Cabin`

and`Embarked`

consist of textual data (strings, aka`object`

). The other columns are numerical data, some of them are whole numbers (`integer`

) and others are real numbers (`float`

).The kind of data (characters, integers, …) in the different columns are summarized by listing the

`dtypes`

.The approximate amount of RAM used to hold the DataFrame is provided as well.

#### REMEMBER

Getting data in to pandas from many different file formats or data sources is supported by

`read_*`

functions.Exporting data out of pandas is provided by different

`to_*`

methods.The

`head`

/`tail`

/`info`

methods and the`dtypes`

attribute are convenient for a first check.

For a complete overview of the input and output possibilities from and to pandas, see the user guide section about reader and writer functions.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html

```
In [1]: import pandas as pd
```

- Titanic data
This tutorial uses the Titanic data set, stored as CSV. The data consists of the following data columns:

PassengerId: Id of every passenger.

Survived: Indication whether passenger survived.

`0`

for no and`1`

for yes.Pclass: One out of the 3 ticket classes: Class

`1`

, Class`2`

and Class`3`

.Name: Name of passenger.

Sex: Gender of passenger.

Age: Age of passenger in years.

SibSp: Number of siblings or spouses aboard.

Parch: Number of parents or children aboard.

Ticket: Ticket number of passenger.

Fare: Indicating the fare.

Cabin: Cabin number of passenger.

Embarked: Port of embarkation.

In [2]: titanic = pd.read_csv("data/titanic.csv") In [3]: titanic.head() Out[3]: PassengerId Survived Pclass ... Fare Cabin Embarked 0 1 0 3 ... 7.2500 NaN S 1 2 1 1 ... 71.2833 C85 C 2 3 1 3 ... 7.9250 NaN S 3 4 1 1 ... 53.1000 C123 S 4 5 0 3 ... 8.0500 NaN S [5 rows x 12 columns]

# How do I select a subset of a `DataFrame`

?#

## How do I select specific columns from a `DataFrame`

?#

I’m interested in the age of the Titanic passengers.

In [4]: ages = titanic["Age"] In [5]: ages.head() Out[5]: 0 22.0 1 38.0 2 26.0 3 35.0 4 35.0 Name: Age, dtype: float64

To select a single column, use square brackets

`[]`

with the column name of the column of interest.For more explanation, see Brackets in Python and pandas.

Each column in a `DataFrame`

is a `Series`

. As a single column is
selected, the returned object is a pandas `Series`

. We can verify this
by checking the type of the output:

```
In [6]: type(titanic["Age"])
Out[6]: pandas.Series
```

And have a look at the `shape`

of the output:

```
In [7]: titanic["Age"].shape
Out[7]: (891,)
```

`DataFrame.shape`

is an attribute (remember tutorial on reading and writing, do not use parentheses for attributes) of a
pandas `Series`

and `DataFrame`

containing the number of rows and
columns: *(nrows, ncolumns)*. A pandas Series is 1-dimensional and only
the number of rows is returned.

I’m interested in the age and sex of the Titanic passengers.

In [8]: age_sex = titanic[["Age", "Sex"]] In [9]: age_sex.head() Out[9]: Age Sex 0 22.0 male 1 38.0 female 2 26.0 female 3 35.0 female 4 35.0 male

To select multiple columns, use a list of column names within the selection brackets

`[]`

.

Note

The inner square brackets define a
Python list with column names, whereas
the outer square brackets are used to select the data from a pandas
`DataFrame`

as seen in the previous example.

The returned data type is a pandas DataFrame:

```
In [10]: type(titanic[["Age", "Sex"]])
Out[10]: pandas.DataFrame
```

```
In [11]: titanic[["Age", "Sex"]].shape
Out[11]: (891, 2)
```

The selection returned a `DataFrame`

with 891 rows and 2 columns. Remember, a
`DataFrame`

is 2-dimensional with both a row and column dimension.

For basic information on indexing, see the user guide section on indexing and selecting data.

## How do I filter specific rows from a `DataFrame`

?#

I’m interested in the passengers older than 35 years.

In [12]: above_35 = titanic[titanic["Age"] > 35] In [13]: above_35.head() Out[13]: PassengerId Survived Pclass ... Fare Cabin Embarked 1 2 1 1 ... 71.2833 C85 C 6 7 0 1 ... 51.8625 E46 S 11 12 1 1 ... 26.5500 C103 S 13 14 0 3 ... 31.2750 NaN S 15 16 1 2 ... 16.0000 NaN S [5 rows x 12 columns]

To select rows based on a conditional expression, use a condition inside the selection brackets

`[]`

.

The condition inside the selection
brackets `titanic["Age"] > 35`

checks for which rows the `Age`

column has a value larger than 35:

```
In [14]: titanic["Age"] > 35
Out[14]:
0 False
1 True
2 False
3 False
4 False
...
886 False
887 False
888 False
889 False
890 False
Name: Age, Length: 891, dtype: bool
```

The output of the conditional expression (`>`

, but also `==`

,
`!=`

, `<`

, `<=`

,… would work) is actually a pandas `Series`

of
boolean values (either `True`

or `False`

) with the same number of
rows as the original `DataFrame`

. Such a `Series`

of boolean values
can be used to filter the `DataFrame`

by putting it in between the
selection brackets `[]`

. Only rows for which the value is `True`

will be selected.

We know from before that the original Titanic `DataFrame`

consists of
891 rows. Let’s have a look at the number of rows which satisfy the
condition by checking the `shape`

attribute of the resulting
`DataFrame`

`above_35`

:

```
In [15]: above_35.shape
Out[15]: (217, 12)
```

I’m interested in the Titanic passengers from cabin class 2 and 3.

In [16]: class_23 = titanic[titanic["Pclass"].isin([2, 3])] In [17]: class_23.head() Out[17]: PassengerId Survived Pclass ... Fare Cabin Embarked 0 1 0 3 ... 7.2500 NaN S 2 3 1 3 ... 7.9250 NaN S 4 5 0 3 ... 8.0500 NaN S 5 6 0 3 ... 8.4583 NaN Q 7 8 0 3 ... 21.0750 NaN S [5 rows x 12 columns]

Similar to the conditional expression, the

`isin()`

conditional function returns a`True`

for each row the values are in the provided list. To filter the rows based on such a function, use the conditional function inside the selection brackets`[]`

. In this case, the condition inside the selection brackets`titanic["Pclass"].isin([2, 3])`

checks for which rows the`Pclass`

column is either 2 or 3.

The above is equivalent to filtering by rows for which the class is
either 2 or 3 and combining the two statements with an `|`

(or)
operator:

```
In [18]: class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
In [19]: class_23.head()
Out[19]:
PassengerId Survived Pclass ... Fare Cabin Embarked
0 1 0 3 ... 7.2500 NaN S
2 3 1 3 ... 7.9250 NaN S
4 5 0 3 ... 8.0500 NaN S
5 6 0 3 ... 8.4583 NaN Q
7 8 0 3 ... 21.0750 NaN S
[5 rows x 12 columns]
```

Note

When combining multiple conditional statements, each condition
must be surrounded by parentheses `()`

. Moreover, you can not use
`or`

/`and`

but need to use the `or`

operator `|`

and the `and`

operator `&`

.

See the dedicated section in the user guide about boolean indexing or about the isin function.

I want to work with passenger data for which the age is known.

In [20]: age_no_na = titanic[titanic["Age"].notna()] In [21]: age_no_na.head() Out[21]: PassengerId Survived Pclass ... Fare Cabin Embarked 0 1 0 3 ... 7.2500 NaN S 1 2 1 1 ... 71.2833 C85 C 2 3 1 3 ... 7.9250 NaN S 3 4 1 1 ... 53.1000 C123 S 4 5 0 3 ... 8.0500 NaN S [5 rows x 12 columns]

The

`notna()`

conditional function returns a`True`

for each row the values are not a`Null`

value. As such, this can be combined with the selection brackets`[]`

to filter the data table.

You might wonder what actually changed, as the first 5 lines are still the same values. One way to verify is to check if the shape has changed:

```
In [22]: age_no_na.shape
Out[22]: (714, 12)
```

For more dedicated functions on missing values, see the user guide section about handling missing data.

## How do I select specific rows and columns from a `DataFrame`

?#

I’m interested in the names of the passengers older than 35 years.

In [23]: adult_names = titanic.loc[titanic["Age"] > 35, "Name"] In [24]: adult_names.head() Out[24]: 1 Cumings, Mrs. John Bradley (Florence Briggs Th... 6 McCarthy, Mr. Timothy J 11 Bonnell, Miss Elizabeth 13 Andersson, Mr. Anders Johan 15 Hewlett, Mrs. (Mary D Kingcome) Name: Name, dtype: str

In this case, a subset of both rows and columns is made in one go and just using selection brackets

`[]`

is not sufficient anymore. The`loc`

/`iloc`

operators are required in front of the selection brackets`[]`

. When using`loc`

/`iloc`

, the part before the comma is the rows you want, and the part after the comma is the columns you want to select.

When using column names, row labels or a condition expression, use
the `loc`

operator in front of the selection brackets `[]`

. For both
the part before and after the comma, you can use a single label, a list
of labels, a slice of labels, a conditional expression or a colon. Using
a colon specifies you want to select all rows or columns.

I’m interested in rows 10 till 25 and columns 3 to 5.

In [25]: titanic.iloc[9:25, 2:5] Out[25]: Pclass Name Sex 9 2 Nasser, Mrs. Nicholas (Adele Achem) female 10 3 Sandstrom, Miss Marguerite Rut female 11 1 Bonnell, Miss Elizabeth female 12 3 Saundercock, Mr. William Henry male 13 3 Andersson, Mr. Anders Johan male .. ... ... ... 20 2 Fynney, Mr. Joseph J male 21 2 Beesley, Mr. Lawrence male 22 3 McGowan, Miss Anna "Annie" female 23 1 Sloper, Mr. William Thompson male 24 3 Palsson, Miss Torborg Danira female [16 rows x 3 columns]

Again, a subset of both rows and columns is made in one go and just using selection brackets

`[]`

is not sufficient anymore. When specifically interested in certain rows and/or columns based on their position in the table, use the`iloc`

operator in front of the selection brackets`[]`

.

When selecting specific rows and/or columns with `loc`

or `iloc`

,
new values can be assigned to the selected data. For example, to assign
the name `anonymous`

to the first 3 elements of the fourth column:

```
In [26]: titanic.iloc[0:3, 3] = "anonymous"
In [27]: titanic.iloc[:5, 3]
Out[27]:
0 anonymous
1 anonymous
2 anonymous
3 Futrelle, Mrs. Jacques Heath (Lily May Peel)
4 Allen, Mr. William Henry
Name: Name, dtype: str
```

See the user guide section on different choices for indexing to get more insight into the usage of `loc`

and `iloc`

.

#### REMEMBER

When selecting subsets of data, square brackets

`[]`

are used.Inside these square brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.

Use

`loc`

for label-based selection (using row/column names).Use

`iloc`

for position-based selection (using table positions).You can assign new values to a selection based on

`loc`

/`iloc`

.

A full overview of indexing is provided in the user guide pages on indexing and selecting data.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

# How do I create plots in pandas?#

```
In [1]: import pandas as pd
In [2]: import matplotlib.pyplot as plt
```

- Air quality data
For this tutorial, air quality data about \(NO_2\) is used, made available by OpenAQ and using the py-openaq package. The

To raw data`air_quality_no2.csv`

data set provides \(NO_2\) values for the measurement stations*FR04014*,*BETR801*and*London Westminster*in respectively Paris, Antwerp and London.In [3]: air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True) In [4]: air_quality.head() Out[4]: station_antwerp station_paris station_london datetime 2019-05-07 02:00:00 NaN NaN 23.0 2019-05-07 03:00:00 50.5 25.0 19.0 2019-05-07 04:00:00 45.0 27.7 19.0 2019-05-07 05:00:00 NaN 50.4 16.0 2019-05-07 06:00:00 NaN 61.9 NaN

Note

The

`index_col=0`

and`parse_dates=True`

parameters passed to the`read_csv`

function define the first (0th) column as index of the resulting`DataFrame`

and convert the dates in the column to`Timestamp`

objects, respectively.

I want a quick visual check of the data.

In [5]: air_quality.plot() Out[5]: <Axes: xlabel='datetime'> In [6]: plt.show()

With a

`DataFrame`

, pandas creates by default one line plot for each of the columns with numeric data.

I want to plot only the columns of the data table with the data from Paris.

In [7]: air_quality["station_paris"].plot() Out[7]: <Axes: xlabel='datetime'> In [8]: plt.show()

To plot a specific column, use a selection method from the subset data tutorial in combination with the

`plot()`

method. Hence, the`plot()`

method works on both`Series`

and`DataFrame`

.

I want to visually compare the \(NO_2\) values measured in London versus Paris.

In [9]: air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5) Out[9]: <Axes: xlabel='station_london', ylabel='station_paris'> In [10]: plt.show()

Apart from the default `line`

plot when using the `plot`

function, a
number of alternatives are available to plot data. Let’s use some
standard Python to get an overview of the available plot methods:

```
In [11]: [
....: method_name
....: for method_name in dir(air_quality.plot)
....: if not method_name.startswith("_")
....: ]
....:
Out[11]:
['area',
'bar',
'barh',
'box',
'density',
'hexbin',
'hist',
'kde',
'line',
'pie',
'scatter']
```

Note

In many development environments such as IPython and
Jupyter Notebook, use the TAB button to get an overview of the available
methods, for example `air_quality.plot.`

+ TAB.

One of the options is `DataFrame.plot.box()`

, which refers to a
boxplot. The `box`

method is applicable on the air quality example data:

```
In [12]: air_quality.plot.box()
Out[12]: <Axes: >
In [13]: plt.show()
```

For an introduction to plots other than the default line plot, see the user guide section about supported plot styles.

I want each of the columns in a separate subplot.

In [14]: axs = air_quality.plot.area(figsize=(12, 4), subplots=True) In [15]: plt.show()

Separate subplots for each of the data columns are supported by the

`subplots`

argument of the`plot`

functions. The builtin options available in each of the pandas plot functions are worth reviewing.

Some more formatting options are explained in the user guide section on plot formatting.

I want to further customize, extend or save the resulting plot.

In [16]: fig, axs = plt.subplots(figsize=(12, 4)) In [17]: air_quality.plot.area(ax=axs) Out[17]: <Axes: xlabel='datetime'> In [18]: axs.set_ylabel("NO$_2$ concentration") Out[18]: Text(0, 0.5, 'NO$_2$ concentration') In [19]: fig.savefig("no2_concentrations.png") In [20]: plt.show()

Each of the plot objects created by pandas is a Matplotlib object. As Matplotlib provides plenty of options to customize plots, making the link between pandas and Matplotlib explicit enables all the power of Matplotlib to the plot. This strategy is applied in the previous example:

```
fig, axs = plt.subplots(figsize=(12, 4)) # Create an empty Matplotlib Figure and Axes
air_quality.plot.area(ax=axs) # Use pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel("NO$_2$ concentration") # Do any Matplotlib customization you like
fig.savefig("no2_concentrations.png") # Save the Figure/Axes using the existing Matplotlib method.
plt.show() # Display the plot
```

#### REMEMBER

The

`.plot.*`

methods are applicable on both Series and DataFrames.By default, each of the columns is plotted as a different element (line, boxplot, …).

Any plot created by pandas is a Matplotlib object.

A full overview of plotting in pandas is provided in the visualization pages.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html

```
In [1]: import pandas as pd
```

- Air quality data
For this tutorial, air quality data about \(NO_2\) is used, made available by OpenAQ and using the py-openaq package. The

To raw data`air_quality_no2.csv`

data set provides \(NO_2\) values for the measurement stations*FR04014*,*BETR801*and*London Westminster*in respectively Paris, Antwerp and London.In [2]: air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True) In [3]: air_quality.head() Out[3]: station_antwerp station_paris station_london datetime 2019-05-07 02:00:00 NaN NaN 23.0 2019-05-07 03:00:00 50.5 25.0 19.0 2019-05-07 04:00:00 45.0 27.7 19.0 2019-05-07 05:00:00 NaN 50.4 16.0 2019-05-07 06:00:00 NaN 61.9 NaN

# How to create new columns derived from existing columns#

I want to express the \(NO_2\) concentration of the station in London in mg/m\(^3\).

(

*If we assume temperature of 25 degrees Celsius and pressure of 1013 hPa, the conversion factor is 1.882*)In [4]: air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882 In [5]: air_quality.head() Out[5]: station_antwerp ... london_mg_per_cubic datetime ... 2019-05-07 02:00:00 NaN ... 43.286 2019-05-07 03:00:00 50.5 ... 35.758 2019-05-07 04:00:00 45.0 ... 35.758 2019-05-07 05:00:00 NaN ... 30.112 2019-05-07 06:00:00 NaN ... NaN [5 rows x 4 columns]

To create a new column, use the square brackets

`[]`

with the new column name at the left side of the assignment.

Note

The calculation of the values is done **element-wise**. This
means all values in the given column are multiplied by the value 1.882
at once. You do not need to use a loop to iterate each of the rows!

I want to check the ratio of the values in Paris versus Antwerp and save the result in a new column.

In [6]: air_quality["ratio_paris_antwerp"] = ( ...: air_quality["station_paris"] / air_quality["station_antwerp"] ...: ) ...: In [7]: air_quality.head() Out[7]: station_antwerp ... ratio_paris_antwerp datetime ... 2019-05-07 02:00:00 NaN ... NaN 2019-05-07 03:00:00 50.5 ... 0.495050 2019-05-07 04:00:00 45.0 ... 0.615556 2019-05-07 05:00:00 NaN ... NaN 2019-05-07 06:00:00 NaN ... NaN [5 rows x 5 columns]

The calculation is again element-wise, so the

`/`

is applied*for the values in each row*.

Other mathematical operators (`+`

, `-`

, `*`

, `/`

, …) and logical
operators (`<`

, `>`

, `==`

, …) also work element-wise. The latter was already
used in the subset data tutorial to filter
rows of a table using a conditional expression.

If you need more advanced logic, you can use arbitrary Python code via `apply()`

.

I want to rename the data columns to the corresponding station identifiers used by OpenAQ.

In [8]: air_quality_renamed = air_quality.rename( ...: columns={ ...: "station_antwerp": "BETR801", ...: "station_paris": "FR04014", ...: "station_london": "London Westminster", ...: } ...: ) ...:

In [9]: air_quality_renamed.head() Out[9]: BETR801 FR04014 ... london_mg_per_cubic ratio_paris_antwerp datetime ... 2019-05-07 02:00:00 NaN NaN ... 43.286 NaN 2019-05-07 03:00:00 50.5 25.0 ... 35.758 0.495050 2019-05-07 04:00:00 45.0 27.7 ... 35.758 0.615556 2019-05-07 05:00:00 NaN 50.4 ... 30.112 NaN 2019-05-07 06:00:00 NaN 61.9 ... NaN NaN [5 rows x 5 columns]

The

`rename()`

function can be used for both row labels and column labels. Provide a dictionary with the keys the current names and the values the new names to update the corresponding names.

The mapping should not be restricted to fixed names only, but can be a mapping function as well. For example, converting the column names to lowercase letters can be done using a function as well:

```
In [10]: air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
In [11]: air_quality_renamed.head()
Out[11]:
betr801 fr04014 ... london_mg_per_cubic ratio_paris_antwerp
datetime ...
2019-05-07 02:00:00 NaN NaN ... 43.286 NaN
2019-05-07 03:00:00 50.5 25.0 ... 35.758 0.495050
2019-05-07 04:00:00 45.0 27.7 ... 35.758 0.615556
2019-05-07 05:00:00 NaN 50.4 ... 30.112 NaN
2019-05-07 06:00:00 NaN 61.9 ... NaN NaN
[5 rows x 5 columns]
```

Details about column or row label renaming is provided in the user guide section on renaming labels.

#### REMEMBER

Create a new column by assigning the output to the DataFrame with a new column name in between the

`[]`

.Operations are element-wise, no need to loop over rows.

Use

`rename`

with a dictionary or function to rename row labels or column names.

The user guide contains a separate section on column addition and deletion.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

```
In [1]: import pandas as pd
```

- Titanic data
This tutorial uses the Titanic data set, stored as CSV. The data consists of the following data columns:

PassengerId: Id of every passenger.

Survived: Indication whether passenger survived.

`0`

for no and`1`

for yes.Pclass: One out of the 3 ticket classes: Class

`1`

, Class`2`

and Class`3`

.Name: Name of passenger.

Sex: Gender of passenger.

Age: Age of passenger in years.

SibSp: Number of siblings or spouses aboard.

Parch: Number of parents or children aboard.

Ticket: Ticket number of passenger.

Fare: Indicating the fare.

Cabin: Cabin number of passenger.

Embarked: Port of embarkation.

In [2]: titanic = pd.read_csv("data/titanic.csv") In [3]: titanic.head() Out[3]: PassengerId Survived Pclass ... Fare Cabin Embarked 0 1 0 3 ... 7.2500 NaN S 1 2 1 1 ... 71.2833 C85 C 2 3 1 3 ... 7.9250 NaN S 3 4 1 1 ... 53.1000 C123 S 4 5 0 3 ... 8.0500 NaN S [5 rows x 12 columns]

# How to calculate summary statistics#

## Aggregating statistics#

What is the average age of the Titanic passengers?

In [4]: titanic["Age"].mean() Out[4]: np.float64(29.69911764705882)

Different statistics are available and can be applied to columns with numerical data. Operations in general exclude missing data and operate across rows by default.

What is the median age and ticket fare price of the Titanic passengers?

In [5]: titanic[["Age", "Fare"]].median() Out[5]: Age 28.0000 Fare 14.4542 dtype: float64

The statistic applied to multiple columns of a

`DataFrame`

(the selection of two columns returns a`DataFrame`

, see the subset data tutorial) is calculated for each numeric column.

The aggregating statistic can be calculated for multiple columns at the
same time. Remember the `describe`

function from the first tutorial?

```
In [6]: titanic[["Age", "Fare"]].describe()
Out[6]:
Age Fare
count 714.000000 891.000000
mean 29.699118 32.204208
std 14.526497 49.693429
min 0.420000 0.000000
25% 20.125000 7.910400
50% 28.000000 14.454200
75% 38.000000 31.000000
max 80.000000 512.329200
```

Instead of the predefined statistics, specific combinations of
aggregating statistics for given columns can be defined using the
`DataFrame.agg()`

method:

```
In [7]: titanic.agg(
...: {
...: "Age": ["min", "max", "median", "skew"],
...: "Fare": ["min", "max", "median", "mean"],
...: }
...: )
...:
Out[7]:
Age Fare
min 0.420000 0.000000
max 80.000000 512.329200
median 28.000000 14.454200
skew 0.389108 NaN
mean NaN 32.204208
```

Details about descriptive statistics are provided in the user guide section on descriptive statistics.

## Aggregating statistics grouped by category#

What is the average age for male versus female Titanic passengers?

In [8]: titanic[["Sex", "Age"]].groupby("Sex").mean() Out[8]: Age Sex female 27.915709 male 30.726645

As our interest is the average age for each gender, a subselection on these two columns is made first:

`titanic[["Sex", "Age"]]`

. Next, the`groupby()`

method is applied on the`Sex`

column to make a group per category. The average age*for each gender*is calculated and returned.

Calculating a given statistic (e.g. `mean`

age) *for each category in
a column* (e.g. male/female in the `Sex`

column) is a common pattern.
The `groupby`

method is used to support this type of operations. This
fits in the more general `split-apply-combine`

pattern:

**Split**the data into groups**Apply**a function to each group independently**Combine**the results into a data structure

The apply and combine steps are typically done together in pandas.

In the previous example, we explicitly selected the 2 columns first. If
not, the `mean`

method is applied to each column containing numerical
columns by passing `numeric_only=True`

:

```
In [9]: titanic.groupby("Sex").mean(numeric_only=True)
Out[9]:
PassengerId Survived Pclass ... SibSp Parch Fare
Sex ...
female 431.028662 0.742038 2.159236 ... 0.694268 0.649682 44.479818
male 454.147314 0.188908 2.389948 ... 0.429809 0.235702 25.523893
[2 rows x 7 columns]
```

It does not make much sense to get the average value of the `Pclass`

.
If we are only interested in the average age for each gender, the
selection of columns (square brackets `[]`

as usual) is supported
on the grouped data as well:

```
In [10]: titanic.groupby("Sex")["Age"].mean()
Out[10]:
Sex
female 27.915709
male 30.726645
Name: Age, dtype: float64
```

Note

The `Pclass`

column contains numerical data but actually
represents 3 categories (or factors) with respectively the labels ‘1’,
‘2’ and ‘3’. Calculating statistics on these does not make much sense.
Therefore, pandas provides a `Categorical`

data type to handle this
type of data. More information is provided in the user guide
Categorical data section.

What is the mean ticket fare price for each of the sex and cabin class combinations?

In [11]: titanic.groupby(["Sex", "Pclass"])["Fare"].mean() Out[11]: Sex Pclass female 1 106.125798 2 21.970121 3 16.118810 male 1 67.226127 2 19.741782 3 12.661633 Name: Fare, dtype: float64

Grouping can be done by multiple columns at the same time. Provide the column names as a list to the

`groupby()`

method.

A full description on the split-apply-combine approach is provided in the user guide section on groupby operations.

## Count number of records by category#

What is the number of passengers in each of the cabin classes?

In [12]: titanic["Pclass"].value_counts() Out[12]: Pclass 3 491 1 216 2 184 Name: count, dtype: int64

The

`value_counts()`

method counts the number of records for each category in a column.

The function is a shortcut, it is actually a groupby operation in combination with counting the number of records within each group:

```
In [13]: titanic.groupby("Pclass")["Pclass"].count()
Out[13]:
Pclass
1 216
2 184
3 491
Name: Pclass, dtype: int64
```

Note

Both `size`

and `count`

can be used in combination with
`groupby`

. Whereas `size`

includes `NaN`

values and just provides
the number of rows (size of the table), `count`

excludes the missing
values. In the `value_counts`

method, use the `dropna`

argument to
include or exclude the `NaN`

values.

The user guide has a dedicated section on `value_counts`

, see the page on discretization.

#### REMEMBER

Aggregation statistics can be calculated on entire columns or rows.

`groupby`

provides the power of the*split-apply-combine*pattern.`value_counts`

is a convenient shortcut to count the number of entries in each category of a variable.

A full description on the split-apply-combine approach is provided in the user guide pages about groupby operations.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html

```
In [1]: import pandas as pd
```

- Titanic data
PassengerId: Id of every passenger.

Survived: Indication whether passenger survived.

`0`

for no and`1`

for yes.Pclass: One out of the 3 ticket classes: Class

`1`

, Class`2`

and Class`3`

.Name: Name of passenger.

Sex: Gender of passenger.

Age: Age of passenger in years.

SibSp: Number of siblings or spouses aboard.

Parch: Number of parents or children aboard.

Ticket: Ticket number of passenger.

Fare: Indicating the fare.

Cabin: Cabin number of passenger.

Embarked: Port of embarkation.

In [2]: titanic = pd.read_csv("data/titanic.csv") In [3]: titanic.head() Out[3]: PassengerId Survived Pclass ... Fare Cabin Embarked 0 1 0 3 ... 7.2500 NaN S 1 2 1 1 ... 71.2833 C85 C 2 3 1 3 ... 7.9250 NaN S 3 4 1 1 ... 53.1000 C123 S 4 5 0 3 ... 8.0500 NaN S [5 rows x 12 columns]

-
Air quality data
This tutorial uses air quality data about \(NO_2\) and Particulate matter less than 2.5 micrometers, made available by OpenAQ and using the py-openaq package. The

`air_quality_long.csv`

data set provides \(NO_2\) and \(PM_{25}\) values for the measurement stations*FR04014*,*BETR801*and*London Westminster*in respectively Paris, Antwerp and London.The air-quality data set has the following columns:

city: city where the sensor is used, either Paris, Antwerp or London

country: country where the sensor is used, either FR, BE or GB

location: the id of the sensor, either

*FR04014*,*BETR801*or*London Westminster*parameter: the parameter measured by the sensor, either \(NO_2\) or Particulate matter

value: the measured value

unit: the unit of the measured parameter, in this case ‘µg/m³’

and the index of the

`DataFrame`

is`datetime`

, the datetime of the measurement.To raw dataNote

The air-quality data is provided in a so-called

*long format*data representation with each observation on a separate row and each variable a separate column of the data table. The long/narrow format is also known as the tidy data format.In [4]: air_quality = pd.read_csv( ...: "data/air_quality_long.csv", index_col="date.utc", parse_dates=True ...: ) ...: In [5]: air_quality.head() Out[5]: city country location parameter value unit date.utc 2019-06-18 06:00:00+00:00 Antwerpen BE BETR801 pm25 18.0 µg/m³ 2019-06-17 08:00:00+00:00 Antwerpen BE BETR801 pm25 6.5 µg/m³ 2019-06-17 07:00:00+00:00 Antwerpen BE BETR801 pm25 18.5 µg/m³ 2019-06-17 06:00:00+00:00 Antwerpen BE BETR801 pm25 16.0 µg/m³ 2019-06-17 05:00:00+00:00 Antwerpen BE BETR801 pm25 7.5 µg/m³

# How to reshape the layout of tables#

## Sort table rows#

I want to sort the Titanic data according to the age of the passengers.

In [6]: titanic.sort_values(by="Age").head() Out[6]: PassengerId Survived Pclass ... Fare Cabin Embarked 803 804 1 3 ... 8.5167 NaN C 755 756 1 2 ... 14.5000 NaN S 469 470 1 3 ... 19.2583 NaN C 644 645 1 3 ... 19.2583 NaN C 78 79 1 2 ... 29.0000 NaN S [5 rows x 12 columns]

I want to sort the Titanic data according to the cabin class and age in descending order.

In [7]: titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head() Out[7]: PassengerId Survived Pclass ... Fare Cabin Embarked 851 852 0 3 ... 7.7750 NaN S 116 117 0 3 ... 7.7500 NaN Q 280 281 0 3 ... 7.7500 NaN Q 483 484 1 3 ... 9.5875 NaN S 326 327 0 3 ... 6.2375 NaN S [5 rows x 12 columns]

With

`DataFrame.sort_values()`

, the rows in the table are sorted according to the defined column(s). The index will follow the row order.

More details about sorting of tables is provided in the user guide section on sorting data.

## Long to wide table format#

Let’s use a small subset of the air quality data set. We focus on
\(NO_2\) data and only use the first two measurements of each
location (i.e. the head of each group). The subset of data will be
called `no2_subset`

.

```
# filter for no2 data only
In [8]: no2 = air_quality[air_quality["parameter"] == "no2"]
```

```
# use 2 measurements (head) for each location (groupby)
In [9]: no2_subset = no2.sort_index().groupby(["location"]).head(2)
In [10]: no2_subset
Out[10]:
city country ... value unit
date.utc ...
2019-04-09 01:00:00+00:00 Antwerpen BE ... 22.5 µg/m³
2019-04-09 01:00:00+00:00 Paris FR ... 24.4 µg/m³
2019-04-09 02:00:00+00:00 London GB ... 67.0 µg/m³
2019-04-09 02:00:00+00:00 Antwerpen BE ... 53.5 µg/m³
2019-04-09 02:00:00+00:00 Paris FR ... 27.4 µg/m³
2019-04-09 03:00:00+00:00 London GB ... 67.0 µg/m³
[6 rows x 6 columns]
```

I want the values for the three stations as separate columns next to each other.

In [11]: no2_subset.pivot(columns="location", values="value") Out[11]: location BETR801 FR04014 London Westminster date.utc 2019-04-09 01:00:00+00:00 22.5 24.4 NaN 2019-04-09 02:00:00+00:00 53.5 27.4 67.0 2019-04-09 03:00:00+00:00 NaN NaN 67.0

The

`pivot()`

function is purely reshaping of the data: a single value for each index/column combination is required.

As pandas supports plotting of multiple columns (see plotting tutorial) out of the box, the conversion from
*long* to *wide* table format enables the plotting of the different time
series at the same time:

```
In [12]: no2.head()
Out[12]:
city country location parameter value unit
date.utc
2019-06-21 00:00:00+00:00 Paris FR FR04014 no2 20.0 µg/m³
2019-06-20 23:00:00+00:00 Paris FR FR04014 no2 21.8 µg/m³
2019-06-20 22:00:00+00:00 Paris FR FR04014 no2 26.5 µg/m³
2019-06-20 21:00:00+00:00 Paris FR FR04014 no2 24.9 µg/m³
2019-06-20 20:00:00+00:00 Paris FR FR04014 no2 21.4 µg/m³
```

```
In [13]: no2.pivot(columns="location", values="value").plot()
Out[13]: <Axes: xlabel='date.utc'>
```

Note

When the `index`

parameter is not defined, the existing
index (row labels) is used.

For more information about `pivot()`

, see the user guide section on pivoting DataFrame objects.

## Pivot table#

I want the mean concentrations for \(NO_2\) and \(PM_{2.5}\) in each of the stations in table form.

In [14]: air_quality.pivot_table( ....: values="value", index="location", columns="parameter", aggfunc="mean" ....: ) ....: Out[14]: parameter no2 pm25 location BETR801 26.950920 23.169492 FR04014 29.374284 NaN London Westminster 29.740050 13.443568

In the case of

`pivot()`

, the data is only rearranged. When multiple values need to be aggregated (in this specific case, the values on different time steps),`pivot_table()`

can be used, providing an aggregation function (e.g. mean) on how to combine these values.

Pivot table is a well known concept in spreadsheet software. When
interested in the row/column margins (subtotals) for each variable, set
the `margins`

parameter to `True`

:

```
In [15]: air_quality.pivot_table(
....: values="value",
....: index="location",
....: columns="parameter",
....: aggfunc="mean",
....: margins=True,
....: )
....:
Out[15]:
parameter no2 pm25 All
location
BETR801 26.950920 23.169492 24.982353
FR04014 29.374284 NaN 29.374284
London Westminster 29.740050 13.443568 21.491708
All 29.430316 14.386849 24.222743
```

For more information about `pivot_table()`

, see the user guide section on pivot tables.

Note

In case you are wondering, `pivot_table()`

is indeed directly linked
to `groupby()`

. The same result can be derived by grouping on both
`parameter`

and `location`

:

```
air_quality.groupby(["parameter", "location"])[["value"]].mean()
```

## Wide to long format#

Starting again from the wide format table created in the previous
section, we add a new index to the `DataFrame`

with `reset_index()`

.

```
In [16]: no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
In [17]: no2_pivoted.head()
Out[17]:
location date.utc BETR801 FR04014 London Westminster
0 2019-04-09 01:00:00+00:00 22.5 24.4 NaN
1 2019-04-09 02:00:00+00:00 53.5 27.4 67.0
2 2019-04-09 03:00:00+00:00 54.5 34.2 67.0
3 2019-04-09 04:00:00+00:00 34.5 48.5 41.0
4 2019-04-09 05:00:00+00:00 46.5 59.5 41.0
```

I want to collect all air quality \(NO_2\) measurements in a single column (long format).

In [18]: no_2 = no2_pivoted.melt(id_vars="date.utc") In [19]: no_2.head() Out[19]: date.utc location value 0 2019-04-09 01:00:00+00:00 BETR801 22.5 1 2019-04-09 02:00:00+00:00 BETR801 53.5 2 2019-04-09 03:00:00+00:00 BETR801 54.5 3 2019-04-09 04:00:00+00:00 BETR801 34.5 4 2019-04-09 05:00:00+00:00 BETR801 46.5

The

`pandas.melt()`

method on a`DataFrame`

converts the data table from wide format to long format. The column headers become the variable names in a newly created column.

The solution is the short version on how to apply `pandas.melt()`

. The method
will *melt* all columns NOT mentioned in `id_vars`

together into two
columns: A column with the column header names and a column with the
values itself. The latter column gets by default the name `value`

.

The parameters passed to `pandas.melt()`

can be defined in more detail:

```
In [20]: no_2 = no2_pivoted.melt(
....: id_vars="date.utc",
....: value_vars=["BETR801", "FR04014", "London Westminster"],
....: value_name="NO_2",
....: var_name="id_location",
....: )
....:
In [21]: no_2.head()
Out[21]:
date.utc id_location NO_2
0 2019-04-09 01:00:00+00:00 BETR801 22.5
1 2019-04-09 02:00:00+00:00 BETR801 53.5
2 2019-04-09 03:00:00+00:00 BETR801 54.5
3 2019-04-09 04:00:00+00:00 BETR801 34.5
4 2019-04-09 05:00:00+00:00 BETR801 46.5
```

The additional parameters have the following effects:

`value_vars`

defines which columns to*melt*together`value_name`

provides a custom column name for the values column instead of the default column name`value`

`var_name`

provides a custom column name for the column collecting the column header names. Otherwise it takes the index name or a default`variable`

Hence, the arguments `value_name`

and `var_name`

are just
user-defined names for the two generated columns. The columns to melt
are defined by `id_vars`

and `value_vars`

.

Conversion from wide to long format with `pandas.melt()`

is explained in the user guide section on reshaping by melt.

#### REMEMBER

Sorting by one or more columns is supported by

`sort_values`

.The

`pivot`

function is purely restructuring of the data,`pivot_table`

supports aggregations.The reverse of

`pivot`

(long to wide format) is`melt`

(wide to long format).

A full overview is available in the user guide on the pages about reshaping and pivoting.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html

```
In [1]: import pandas as pd
```

-
Air quality Nitrate data
For this tutorial, air quality data about \(NO_2\) is used, made available by OpenAQ and downloaded using the py-openaq package.

The

To raw data`air_quality_no2_long.csv`

data set provides \(NO_2\) values for the measurement stations*FR04014*,*BETR801*and*London Westminster*in respectively Paris, Antwerp and London.In [2]: air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", ...: parse_dates=True) ...: In [3]: air_quality_no2 = air_quality_no2[["date.utc", "location", ...: "parameter", "value"]] ...: In [4]: air_quality_no2.head() Out[4]: date.utc location parameter value 0 2019-06-21 00:00:00+00:00 FR04014 no2 20.0 1 2019-06-20 23:00:00+00:00 FR04014 no2 21.8 2 2019-06-20 22:00:00+00:00 FR04014 no2 26.5 3 2019-06-20 21:00:00+00:00 FR04014 no2 24.9 4 2019-06-20 20:00:00+00:00 FR04014 no2 21.4

-
Air quality Particulate matter data
For this tutorial, air quality data about Particulate matter less than 2.5 micrometers is used, made available by OpenAQ and downloaded using the py-openaq package.

The

To raw data`air_quality_pm25_long.csv`

data set provides \(PM_{25}\) values for the measurement stations*FR04014*,*BETR801*and*London Westminster*in respectively Paris, Antwerp and London.In [5]: air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", ...: parse_dates=True) ...: In [6]: air_quality_pm25 = air_quality_pm25[["date.utc", "location", ...: "parameter", "value"]] ...: In [7]: air_quality_pm25.head() Out[7]: date.utc location parameter value 0 2019-06-18 06:00:00+00:00 BETR801 pm25 18.0 1 2019-06-17 08:00:00+00:00 BETR801 pm25 6.5 2 2019-06-17 07:00:00+00:00 BETR801 pm25 18.5 3 2019-06-17 06:00:00+00:00 BETR801 pm25 16.0 4 2019-06-17 05:00:00+00:00 BETR801 pm25 7.5

# How to combine data from multiple tables#

## Concatenating objects#

I want to combine the measurements of \(NO_2\) and \(PM_{25}\), two tables with a similar structure, in a single table.

In [8]: air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0) In [9]: air_quality.head() Out[9]: date.utc location parameter value 0 2019-06-18 06:00:00+00:00 BETR801 pm25 18.0 1 2019-06-17 08:00:00+00:00 BETR801 pm25 6.5 2 2019-06-17 07:00:00+00:00 BETR801 pm25 18.5 3 2019-06-17 06:00:00+00:00 BETR801 pm25 16.0 4 2019-06-17 05:00:00+00:00 BETR801 pm25 7.5

The

`concat()`

function performs concatenation operations of multiple tables along one of the axes (row-wise or column-wise).

By default concatenation is along axis 0, so the resulting table combines the rows of the input tables. Let’s check the shape of the original and the concatenated tables to verify the operation:

```
In [10]: print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
Shape of the ``air_quality_pm25`` table: (1110, 4)
In [11]: print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
Shape of the ``air_quality_no2`` table: (2068, 4)
In [12]: print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)
Shape of the resulting ``air_quality`` table: (3178, 4)
```

Hence, the resulting table has 3178 = 1110 + 2068 rows.

Note

The **axis** argument will return in a number of pandas
methods that can be applied **along an axis**. A `DataFrame`

has two
corresponding axes: the first running vertically downwards across rows
(axis 0), and the second running horizontally across columns (axis 1).
Most operations like concatenation or summary statistics are by default
across rows (axis 0), but can be applied across columns as well.

Sorting the table on the datetime information also illustrates the
combination of both tables, with the `parameter`

column defining the
origin of the table (either `no2`

from table `air_quality_no2`

or
`pm25`

from table `air_quality_pm25`

):

```
In [13]: air_quality = air_quality.sort_values("date.utc")
In [14]: air_quality.head()
Out[14]:
date.utc location parameter value
100 2019-05-07 01:00:00+00:00 BETR801 pm25 12.5
1109 2019-05-07 01:00:00+00:00 London Westminster pm25 8.0
1003 2019-05-07 01:00:00+00:00 FR04014 no2 25.0
1098 2019-05-07 01:00:00+00:00 BETR801 no2 50.5
2067 2019-05-07 01:00:00+00:00 London Westminster no2 23.0
```

In this specific example, the `parameter`

column provided by the data
ensures that each of the original tables can be identified. This is not
always the case. The `concat`

function provides a convenient solution
with the `keys`

argument, adding an additional (hierarchical) row
index. For example:

```
In [15]: air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])
In [16]: air_quality_.head()
Out[16]:
date.utc location parameter value
PM25 0 2019-06-18 06:00:00+00:00 BETR801 pm25 18.0
1 2019-06-17 08:00:00+00:00 BETR801 pm25 6.5
2 2019-06-17 07:00:00+00:00 BETR801 pm25 18.5
3 2019-06-17 06:00:00+00:00 BETR801 pm25 16.0
4 2019-06-17 05:00:00+00:00 BETR801 pm25 7.5
```

Note

The existence of multiple row/column indices at the same time
has not been mentioned within these tutorials. *Hierarchical indexing*
or *MultiIndex* is an advanced and powerful pandas feature to analyze
higher dimensional data.

Multi-indexing is out of scope for this pandas introduction. For the
moment, remember that the function `reset_index`

can be used to
convert any level of an index to a column, e.g.
`air_quality.reset_index(level=0)`

Feel free to dive into the world of multi-indexing at the user guide section on advanced indexing.

More options on table concatenation (row and column
wise) and how `concat`

can be used to define the logic (union or
intersection) of the indexes on the other axes is provided at the section on
object concatenation.

## Join tables using a common identifier#

Add the station coordinates, provided by the stations metadata table, to the corresponding rows in the measurements table.

Warning

The air quality measurement station coordinates are stored in a data file

`air_quality_stations.csv`

, downloaded using the py-openaq package.In [17]: stations_coord = pd.read_csv("data/air_quality_stations.csv") In [18]: stations_coord.head() Out[18]: location coordinates.latitude coordinates.longitude 0 BELAL01 51.23619 4.38522 1 BELHB23 51.17030 4.34100 2 BELLD01 51.10998 5.00486 3 BELLD02 51.12038 5.02155 4 BELR833 51.32766 4.36226

Note

The stations used in this example (FR04014, BETR801 and London Westminster) are just three entries enlisted in the metadata table. We only want to add the coordinates of these three to the measurements table, each on the corresponding rows of the

`air_quality`

table.In [19]: air_quality.head() Out[19]: date.utc location parameter value 100 2019-05-07 01:00:00+00:00 BETR801 pm25 12.5 1109 2019-05-07 01:00:00+00:00 London Westminster pm25 8.0 1003 2019-05-07 01:00:00+00:00 FR04014 no2 25.0 1098 2019-05-07 01:00:00+00:00 BETR801 no2 50.5 2067 2019-05-07 01:00:00+00:00 London Westminster no2 23.0

In [20]: air_quality = pd.merge(air_quality, stations_coord, how="left", on="location") In [21]: air_quality.head() Out[21]: date.utc ... coordinates.longitude 0 2019-05-07 01:00:00+00:00 ... 4.43182 1 2019-05-07 01:00:00+00:00 ... -0.13193 2 2019-05-07 01:00:00+00:00 ... 2.39390 3 2019-05-07 01:00:00+00:00 ... 2.39390 4 2019-05-07 01:00:00+00:00 ... 4.43182 [5 rows x 6 columns]

Using the

`merge()`

function, for each of the rows in the`air_quality`

table, the corresponding coordinates are added from the`air_quality_stations_coord`

table. Both tables have the column`location`

in common which is used as a key to combine the information. By choosing the`left`

join, only the locations available in the`air_quality`

(left) table, i.e. FR04014, BETR801 and London Westminster, end up in the resulting table. The`merge`

function supports multiple join options similar to database-style operations.

Add the parameters’ full description and name, provided by the parameters metadata table, to the measurements table.

Warning

The air quality parameters metadata are stored in a data file

`air_quality_parameters.csv`

, downloaded using the py-openaq package.In [22]: air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv") In [23]: air_quality_parameters.head() Out[23]: id description name 0 bc Black Carbon BC 1 co Carbon Monoxide CO 2 no2 Nitrogen Dioxide NO2 3 o3 Ozone O3 4 pm10 Particulate matter less than 10 micrometers in... PM10

In [24]: air_quality = pd.merge(air_quality, air_quality_parameters, ....: how='left', left_on='parameter', right_on='id') ....: In [25]: air_quality.head() Out[25]: date.utc ... name 0 2019-05-07 01:00:00+00:00 ... PM2.5 1 2019-05-07 01:00:00+00:00 ... PM2.5 2 2019-05-07 01:00:00+00:00 ... NO2 3 2019-05-07 01:00:00+00:00 ... NO2 4 2019-05-07 01:00:00+00:00 ... NO2 [5 rows x 9 columns]

Compared to the previous example, there is no common column name. However, the

`parameter`

column in the`air_quality`

table and the`id`

column in the`air_quality_parameters`

table both provide the measured variable in a common format. The`left_on`

and`right_on`

arguments are used here (instead of just`on`

) to make the link between the two tables.

pandas also supports inner, outer, and right joins. More information on join/merge of tables is provided in the user guide section on database style merging of tables. Or have a look at the comparison with SQL page.

#### REMEMBER

Multiple tables can be concatenated column-wise or row-wise using the

`concat`

function.For database-like merging/joining of tables, use the

`merge`

function.

See the user guide for a full description of the various facilities to combine data tables.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html

```
In [1]: import pandas as pd
In [2]: import matplotlib.pyplot as plt
```

-
Air quality data
For this tutorial, air quality data about \(NO_2\) and Particulate matter less than 2.5 micrometers is used, made available by OpenAQ and downloaded using the py-openaq package. The

To raw data`air_quality_no2_long.csv"`

data set provides \(NO_2\) values for the measurement stations*FR04014*,*BETR801*and*London Westminster*in respectively Paris, Antwerp and London.In [3]: air_quality = pd.read_csv("data/air_quality_no2_long.csv") In [4]: air_quality = air_quality.rename(columns={"date.utc": "datetime"}) In [5]: air_quality.head() Out[5]: city country datetime location parameter value unit 0 Paris FR 2019-06-21 00:00:00+00:00 FR04014 no2 20.0 µg/m³ 1 Paris FR 2019-06-20 23:00:00+00:00 FR04014 no2 21.8 µg/m³ 2 Paris FR 2019-06-20 22:00:00+00:00 FR04014 no2 26.5 µg/m³ 3 Paris FR 2019-06-20 21:00:00+00:00 FR04014 no2 24.9 µg/m³ 4 Paris FR 2019-06-20 20:00:00+00:00 FR04014 no2 21.4 µg/m³

In [6]: air_quality.city.unique() Out[6]: <ArrowStringArray> ['Paris', 'Antwerpen', 'London'] Length: 3, dtype: str

# How to handle time series data with ease#

## Using pandas datetime properties#

I want to work with the dates in the column

`datetime`

as datetime objects instead of plain textIn [7]: air_quality["datetime"] = pd.to_datetime(air_quality["datetime"]) In [8]: air_quality["datetime"] Out[8]: 0 2019-06-21 00:00:00+00:00 1 2019-06-20 23:00:00+00:00 2 2019-06-20 22:00:00+00:00 3 2019-06-20 21:00:00+00:00 4 2019-06-20 20:00:00+00:00 ... 2063 2019-05-07 06:00:00+00:00 2064 2019-05-07 04:00:00+00:00 2065 2019-05-07 03:00:00+00:00 2066 2019-05-07 02:00:00+00:00 2067 2019-05-07 01:00:00+00:00 Name: datetime, Length: 2068, dtype: datetime64[us, UTC]

Initially, the values in

`datetime`

are character strings and do not provide any datetime operations (e.g. extract the year, day of the week, …). By applying the`to_datetime`

function, pandas interprets the strings and convert these to datetime (i.e.`datetime64[ns, UTC]`

) objects. In pandas we call these datetime objects that are similar to`datetime.datetime`

from the standard library as`pandas.Timestamp`

.

Note

As many data sets do contain datetime information in one of
the columns, pandas input function like `pandas.read_csv()`

and `pandas.read_json()`

can do the transformation to dates when reading the data using the
`parse_dates`

parameter with a list of the columns to read as
Timestamp:

```
pd.read_csv("../data/air_quality_no2_long.csv", parse_dates=["datetime"])
```

Why are these `pandas.Timestamp`

objects useful? Let’s illustrate the added
value with some example cases.

What is the start and end date of the time series data set we are working with?

```
In [9]: air_quality["datetime"].min(), air_quality["datetime"].max()
Out[9]:
(Timestamp('2019-05-07 01:00:00+0000', tz='UTC'),
Timestamp('2019-06-21 00:00:00+0000', tz='UTC'))
```

Using `pandas.Timestamp`

for datetimes enables us to calculate with date
information and make them comparable. Hence, we can use this to get the
length of our time series:

```
In [10]: air_quality["datetime"].max() - air_quality["datetime"].min()
Out[10]: Timedelta('44 days 23:00:00')
```

The result is a `pandas.Timedelta`

object, similar to `datetime.timedelta`

from the standard Python library which defines a time duration.

The various time concepts supported by pandas are explained in the user guide section on time related concepts.

I want to add a new column to the

`DataFrame`

containing only the month of the measurementIn [11]: air_quality["month"] = air_quality["datetime"].dt.month In [12]: air_quality.head() Out[12]: city country datetime ... value unit month 0 Paris FR 2019-06-21 00:00:00+00:00 ... 20.0 µg/m³ 6 1 Paris FR 2019-06-20 23:00:00+00:00 ... 21.8 µg/m³ 6 2 Paris FR 2019-06-20 22:00:00+00:00 ... 26.5 µg/m³ 6 3 Paris FR 2019-06-20 21:00:00+00:00 ... 24.9 µg/m³ 6 4 Paris FR 2019-06-20 20:00:00+00:00 ... 21.4 µg/m³ 6 [5 rows x 8 columns]

By using

`Timestamp`

objects for dates, a lot of time-related properties are provided by pandas. For example the`month`

, but also`year`

,`quarter`

,… All of these properties are accessible by the`dt`

accessor.

An overview of the existing date properties is given in the
time and date components overview table. More details about the `dt`

accessor
to return datetime like properties are explained in a dedicated section on the dt accessor.

What is the average \(NO_2\) concentration for each day of the week for each of the measurement locations?

In [13]: air_quality.groupby( ....: [air_quality["datetime"].dt.weekday, "location"])["value"].mean() ....: Out[13]: datetime location 0 BETR801 27.875000 FR04014 24.856250 London Westminster 23.969697 1 BETR801 22.214286 FR04014 30.999359 ... 5 FR04014 25.266154 London Westminster 24.977612 6 BETR801 21.896552 FR04014 23.274306 London Westminster 24.859155 Name: value, Length: 21, dtype: float64

Remember the split-apply-combine pattern provided by

`groupby`

from the tutorial on statistics calculation? Here, we want to calculate a given statistic (e.g. mean \(NO_2\))**for each weekday**and**for each measurement location**. To group on weekdays, we use the datetime property`weekday`

(with Monday=0 and Sunday=6) of pandas`Timestamp`

, which is also accessible by the`dt`

accessor. The grouping on both locations and weekdays can be done to split the calculation of the mean on each of these combinations.Danger

As we are working with a very short time series in these examples, the analysis does not provide a long-term representative result!

Plot the typical \(NO_2\) pattern during the day of our time series of all stations together. In other words, what is the average value for each hour of the day?

In [14]: fig, axs = plt.subplots(figsize=(12, 4)) In [15]: air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot( ....: kind='bar', rot=0, ax=axs ....: ) ....: Out[15]: <Axes: xlabel='datetime'> In [16]: plt.xlabel("Hour of the day"); # custom x label using Matplotlib In [17]: plt.ylabel("$NO_2 (µg/m^3)$");

Similar to the previous case, we want to calculate a given statistic (e.g. mean \(NO_2\))

**for each hour of the day**and we can use the split-apply-combine approach again. For this case, we use the datetime property`hour`

of pandas`Timestamp`

, which is also accessible by the`dt`

accessor.

## Datetime as index#

In the tutorial on reshaping,
`pivot()`

was introduced to reshape the data table with each of the
measurements locations as a separate column:

```
In [18]: no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
In [19]: no_2.head()
Out[19]:
location BETR801 FR04014 London Westminster
datetime
2019-05-07 01:00:00+00:00 50.5 25.0 23.0
2019-05-07 02:00:00+00:00 45.0 27.7 19.0
2019-05-07 03:00:00+00:00 NaN 50.4 19.0
2019-05-07 04:00:00+00:00 NaN 61.9 16.0
2019-05-07 05:00:00+00:00 NaN 72.4 NaN
```

Note

By pivoting the data, the datetime information became the
index of the table. In general, setting a column as an index can be
achieved by the `set_index`

function.

Working with a datetime index (i.e. `DatetimeIndex`

) provides powerful
functionalities. For example, we do not need the `dt`

accessor to get
the time series properties, but have these properties available on the
index directly:

```
In [20]: no_2.index.year, no_2.index.weekday
Out[20]:
(Index([2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
...
2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019],
dtype='int32', name='datetime', length=1033),
Index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
...
3, 3, 3, 3, 3, 3, 3, 3, 3, 4],
dtype='int32', name='datetime', length=1033))
```

Some other advantages are the convenient subsetting of time period or the adapted time scale on plots. Let’s apply this on our data.

Create a plot of the \(NO_2\) values in the different stations from May 20th till the end of May 21st.

In [21]: no_2["2019-05-20":"2019-05-21"].plot();

By providing a

**string that parses to a datetime**, a specific subset of the data can be selected on a`DatetimeIndex`

.

More information on the `DatetimeIndex`

and the slicing by using strings is provided in the section on time series indexing.

## Resample a time series to another frequency#

Aggregate the current hourly time series values to the monthly maximum value in each of the stations.

In [22]: monthly_max = no_2.resample("MS").max() In [23]: monthly_max Out[23]: location BETR801 FR04014 London Westminster datetime 2019-05-01 00:00:00+00:00 74.5 97.0 97.0 2019-06-01 00:00:00+00:00 52.5 84.7 52.0

A very powerful method on time series data with a datetime index, is the ability to

`resample()`

time series to another frequency (e.g., converting secondly data into 5-minutely data).

The `resample()`

method is similar to a groupby operation:

it provides a time-based grouping, by using a string (e.g.

`M`

,`5H`

, …) that defines the target frequencyit requires an aggregation function such as

`mean`

,`max`

,…

An overview of the aliases used to define time series frequencies is given in the offset aliases overview table.

When defined, the frequency of the time series is provided by the
`freq`

attribute:

```
In [24]: monthly_max.index.freq
Out[24]: <MonthBegin>
```

Make a plot of the daily mean \(NO_2\) value in each of the stations.

In [25]: no_2.resample("D").mean().plot(style="-o", figsize=(10, 5));

More details on the power of time series `resampling`

is provided in the user guide section on resampling.

#### REMEMBER

Valid date strings can be converted to datetime objects using

`to_datetime`

function or as part of read functions.Datetime objects in pandas support calculations, logical operations and convenient date-related properties using the

`dt`

accessor.A

`DatetimeIndex`

contains these date-related properties and supports convenient slicing.`Resample`

is a powerful method to change the frequency of a time series.

A full overview on time series is given on the pages on time series and date functionality.

## Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html

```
In [1]: import pandas as pd
```

- Titanic data
PassengerId: Id of every passenger.

Survived: Indication whether passenger survived.

`0`

for no and`1`

for yes.Pclass: One out of the 3 ticket classes: Class

`1`

, Class`2`

and Class`3`

.Name: Name of passenger.

Sex: Gender of passenger.

Age: Age of passenger in years.

SibSp: Number of siblings or spouses aboard.

Parch: Number of parents or children aboard.

Ticket: Ticket number of passenger.

Fare: Indicating the fare.

Cabin: Cabin number of passenger.

Embarked: Port of embarkation.

# How to manipulate textual data#

Make all name characters lowercase.

In [4]: titanic["Name"].str.lower() Out[4]: 0 braund, mr. owen harris 1 cumings, mrs. john bradley (florence briggs th... 2 heikkinen, miss laina 3 futrelle, mrs. jacques heath (lily may peel) 4 allen, mr. william henry ... 886 montvila, rev. juozas 887 graham, miss margaret edith 888 johnston, miss catherine helen "carrie" 889 behr, mr. karl howell 890 dooley, mr. patrick Name: Name, Length: 891, dtype: str

To make each of the strings in the

`Name`

column lowercase, select the`Name`

column (see the tutorial on selection of data), add the`str`

accessor and apply the`lower`

method. As such, each of the strings is converted element-wise.

Similar to datetime objects in the time series tutorial
having a `dt`

accessor, a number of
specialized string methods are available when using the `str`

accessor. These methods have in general matching names with the
equivalent built-in string methods for single elements, but are applied
element-wise (remember element-wise calculations?)
on each of the values of the columns.

Create a new column

`Surname`

that contains the surname of the passengers by extracting the part before the comma.In [5]: titanic["Name"].str.split(",") Out[5]: 0 [Braund, Mr. Owen Harris] 1 [Cumings, Mrs. John Bradley (Florence Briggs ... 2 [Heikkinen, Miss Laina] 3 [Futrelle, Mrs. Jacques Heath (Lily May Peel)] 4 [Allen, Mr. William Henry] ... 886 [Montvila, Rev. Juozas] 887 [Graham, Miss Margaret Edith] 888 [Johnston, Miss Catherine Helen "Carrie"] 889 [Behr, Mr. Karl Howell] 890 [Dooley, Mr. Patrick] Name: Name, Length: 891, dtype: object

Using the

`Series.str.split()`

method, each of the values is returned as a list of 2 elements. The first element is the part before the comma and the second element is the part after the comma.In [6]: titanic["Surname"] = titanic["Name"].str.split(",").str.get(0) In [7]: titanic["Surname"] Out[7]: 0 Braund 1 Cumings 2 Heikkinen 3 Futrelle 4 Allen ... 886 Montvila 887 Graham 888 Johnston 889 Behr 890 Dooley Name: Surname, Length: 891, dtype: object

As we are only interested in the first part representing the surname (element 0), we can again use the

`str`

accessor and apply`Series.str.get()`

to extract the relevant part. Indeed, these string functions can be concatenated to combine multiple functions at once!

More information on extracting parts of strings is available in the user guide section on splitting and replacing strings.

Extract the passenger data about the countesses on board of the Titanic.

In [8]: titanic["Name"].str.contains("Countess") Out[8]: 0 False 1 False 2 False 3 False 4 False ... 886 False 887 False 888 False 889 False 890 False Name: Name, Length: 891, dtype: bool

In [9]: titanic[titanic["Name"].str.contains("Countess")] Out[9]: PassengerId Survived Pclass ... Cabin Embarked Surname 759 760 1 1 ... B77 S Rothes [1 rows x 13 columns]

(

*Interested in her story? See*Wikipedia*!*)The string method

`Series.str.contains()`

checks for each of the values in the column`Name`

if the string contains the word`Countess`

and returns for each of the values`True`

(`Countess`

is part of the name) or`False`

(`Countess`

is not part of the name). This output can be used to subselect the data using conditional (boolean) indexing introduced in the subsetting of data tutorial. As there was only one countess on the Titanic, we get one row as a result.

Note

More powerful extractions on strings are supported, as the
`Series.str.contains()`

and `Series.str.extract()`

methods accept regular
expressions, but are out of
the scope of this tutorial.

More information on extracting parts of strings is available in the user guide section on string matching and extracting.

Which passenger of the Titanic has the longest name?

In [10]: titanic["Name"].str.len() Out[10]: 0 23 1 51 2 21 3 44 4 24 .. 886 21 887 27 888 39 889 21 890 19 Name: Name, Length: 891, dtype: int64

To get the longest name we first have to get the lengths of each of the names in the

`Name`

column. By using pandas string methods, the`Series.str.len()`

function is applied to each of the names individually (element-wise).In [11]: titanic["Name"].str.len().idxmax() Out[11]: 307

`idxmax()`

method does exactly that. It is not a string method and is applied to integers, so no`str`

is used.In [12]: titanic.loc[titanic["Name"].str.len().idxmax(), "Name"] Out[12]: 'Penasco y Castellana, Mrs. Victor de Satode (Maria Josefa Perez de Soto y Vallejo)'

Based on the index name of the row (

`307`

) and the column (`Name`

), we can do a selection using the`loc`

operator, introduced in the tutorial on subsetting.

In the “Sex” column, replace values of “male” by “M” and values of “female” by “F”.

In [13]: titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"}) In [14]: titanic["Sex_short"] Out[14]: 0 M 1 F 2 F 3 F 4 M .. 886 M 887 F 888 F 889 M 890 M Name: Sex_short, Length: 891, dtype: str

Whereas

`replace()`

is not a string method, it provides a convenient way to use mappings or vocabularies to translate certain values. It requires a`dictionary`

to define the mapping`{from: to}`

.

Warning

There is also a `replace()`

method available to replace a
specific set of characters. However, when having a mapping of multiple
values, this would become:

```
titanic["Sex_short"] = titanic["Sex"].str.replace("female", "F")
titanic["Sex_short"] = titanic["Sex_short"].str.replace("male", "M")
```

This would become cumbersome and easily lead to mistakes. Just think (or try out yourself) what would happen if those two statements are applied in the opposite order…

#### REMEMBER

String methods are available using the

`str`

accessor.String methods work element-wise and can be used for conditional indexing.

The

`replace`

method is a convenient method to convert values according to a given dictionary.

A full overview is provided in the user guide pages on working with text data.

## Source: https://pandas.pydata.org/docs/getting_started/comparison/index.html

Comparison with other tools# Comparison with R / R libraries Quick reference Base R plyr reshape / reshape2 Comparison with SQL Copies vs. in place operations SELECT WHERE GROUP BY JOIN UNION LIMIT pandas equivalents for some SQL analytic and aggregate functions UPDATE DELETE Comparison with spreadsheets Data structures Data input / output Data operations String processing Merging Other considerations Comparison with SAS Data structures Data input / output Data operations String processing Merging Missing data GroupBy Other considerations Comparison with Stata Data structures Data input / output Data operations String processing Merging Missing data GroupBy Other considerations Comparison with SPSS Data structures Copies vs. in place operations Data input / output Data operations String processing Merging GroupBy operations Missing data Other considerations Output management

## Source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html

# Comparison with R / R libraries#

Since pandas aims to provide a lot of the data manipulation and analysis functionality that people use R for, this page was started to provide a more detailed look at the R language and its many third party libraries as they relate to pandas. In comparisons with R and CRAN libraries, we care about the following things:

**Functionality / flexibility**: what can/cannot be done with each tool**Performance**: how fast are operations. Hard numbers/benchmarks are preferable**Ease-of-use**: Is one tool easier/harder to use (you may have to be the judge of this, given side-by-side code comparisons)

This page is also here to offer a bit of a translation guide for users of these R packages.

## Quick reference#

We’ll start off with a quick reference guide pairing some common R operations using dplyr with pandas equivalents.

### Querying, filtering, sampling#

R |
pandas |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

### Sorting#

R |
pandas |
|---|---|
|
|
|
|

### Transforming#

R |
pandas |
|---|---|
|
|
|
|
|
|

### Grouping and summarizing#

R |
pandas |
|---|---|
|
|
|
|
|
|
|
|

## Base R#

### Slicing with R’s `c`

#

R makes it easy to access `data.frame`

columns by name

```
df <- data.frame(a=rnorm(5), b=rnorm(5), c=rnorm(5), d=rnorm(5), e=rnorm(5))
df[, c("a", "c", "e")]
```

or by integer location

```
df <- data.frame(matrix(rnorm(1000), ncol=100))
df[, c(1:10, 25:30, 40, 50:100)]
```

Selecting multiple columns by name in pandas is straightforward

```
In [1]: df = pd.DataFrame(np.random.randn(10, 3), columns=list("abc"))
In [2]: df[["a", "c"]]
Out[2]:
a c
0 0.469112 -1.509059
1 -1.135632 -0.173215
2 0.119209 -0.861849
3 -2.104569 1.071804
4 0.721555 -1.039575
5 0.271860 0.567020
6 0.276232 -0.673690
7 0.113648 0.524988
8 0.404705 -1.715002
9 -1.039268 -1.157892
In [3]: df.loc[:, ["a", "c"]]
Out[3]:
a c
0 0.469112 -1.509059
1 -1.135632 -0.173215
2 0.119209 -0.861849
3 -2.104569 1.071804
4 0.721555 -1.039575
5 0.271860 0.567020
6 0.276232 -0.673690
7 0.113648 0.524988
8 0.404705 -1.715002
9 -1.039268 -1.157892
```

Selecting multiple noncontiguous columns by integer location can be achieved
with a combination of the `iloc`

indexer attribute and `numpy.r_`

.

```
In [4]: named = list("abcdefg")
In [5]: n = 30
In [6]: columns = named + np.arange(len(named), n).tolist()
In [7]: df = pd.DataFrame(np.random.randn(n, n), columns=columns)
In [8]: df.iloc[:, np.r_[:10, 24:30]]
Out[8]:
a b c ... 27 28 29
0 -1.344312 0.844885 1.075770 ... 0.813850 0.132003 -0.827317
1 -0.076467 -1.187678 1.130127 ... 0.149748 -0.732339 0.687738
2 0.176444 0.403310 -0.154951 ... -0.493662 0.600178 0.274230
3 0.132885 -0.023688 2.410179 ... 0.109121 1.126203 -0.977349
4 1.474071 -0.064034 -1.282782 ... -0.858447 0.306996 -0.028665
.. ... ... ... ... ... ... ...
25 1.492125 -0.068190 0.681456 ... 0.428572 0.880609 0.487645
26 0.725238 0.624607 -0.141185 ... 1.008500 1.424017 0.717110
27 1.262419 1.950057 0.301038 ... 1.007824 2.826008 1.458383
28 -1.585746 -0.899734 0.921494 ... 0.577223 -1.088417 0.326687
29 -0.986248 0.169729 -1.158091 ... -2.013086 -1.602549 0.333109
[30 rows x 16 columns]
```

`aggregate`

#

In R you may want to split data into subsets and compute the mean for each.
Using a data.frame called `df`

and splitting it into groups `by1`

and
`by2`

:

```
df <- data.frame(
v1 = c(1,3,5,7,8,3,5,NA,4,5,7,9),
v2 = c(11,33,55,77,88,33,55,NA,44,55,77,99),
by1 = c("red", "blue", 1, 2, NA, "big", 1, 2, "red", 1, NA, 12),
by2 = c("wet", "dry", 99, 95, NA, "damp", 95, 99, "red", 99, NA, NA))
aggregate(x=df[, c("v1", "v2")], by=list(mydf2$by1, mydf2$by2), FUN = mean)
```

The `groupby()`

method is similar to base R `aggregate`

function.

```
In [9]: df = pd.DataFrame(
...: {
...: "v1": [1, 3, 5, 7, 8, 3, 5, np.nan, 4, 5, 7, 9],
...: "v2": [11, 33, 55, 77, 88, 33, 55, np.nan, 44, 55, 77, 99],
...: "by1": ["red", "blue", 1, 2, np.nan, "big", 1, 2, "red", 1, np.nan, 12],
...: "by2": [
...: "wet",
...: "dry",
...: 99,
...: 95,
...: np.nan,
...: "damp",
...: 95,
...: 99,
...: "red",
...: 99,
...: np.nan,
...: np.nan,
...: ],
...: }
...: )
...:
In [10]: g = df.groupby(["by1", "by2"])
In [11]: g[["v1", "v2"]].mean()
Out[11]:
v1 v2
by1 by2
1 95 5.0 55.0
99 5.0 55.0
2 95 7.0 77.0
99 NaN NaN
big damp 3.0 33.0
blue dry 3.0 33.0
red red 4.0 44.0
wet 1.0 11.0
```

For more details and examples see the groupby documentation.

`match`

/ `%in%`

#

A common way to select data in R is using `%in%`

which is defined using the
function `match`

. The operator `%in%`

is used to return a logical vector
indicating if there is a match or not:

```
s <- 0:4
s %in% c(2,4)
```

The `isin()`

method is similar to R `%in%`

operator:

```
In [12]: s = pd.Series(np.arange(5), dtype=np.float32)
In [13]: s.isin([2, 4])
Out[13]:
0 False
1 False
2 True
3 False
4 True
dtype: bool
```

The `match`

function returns a vector of the positions of matches
of its first argument in its second:

```
s <- 0:4
match(s, c(2,4))
```

For more details and examples see the reshaping documentation.

`tapply`

#

`tapply`

is similar to `aggregate`

, but data can be in a ragged array,
since the subclass sizes are possibly irregular. Using a data.frame called
`baseball`

, and retrieving information based on the array `team`

:

```
baseball <-
data.frame(team = gl(5, 5,
labels = paste("Team", LETTERS[1:5])),
player = sample(letters, 25),
batting.average = runif(25, .200, .400))
tapply(baseball$batting.average, baseball.example$team,
max)
```

In pandas we may use `pivot_table()`

method to handle this:

```
In [14]: import random
In [15]: import string
In [16]: baseball = pd.DataFrame(
....: {
....: "team": ["team %d" % (x + 1) for x in range(5)] * 5,
....: "player": random.sample(list(string.ascii_lowercase), 25),
....: "batting avg": np.random.uniform(0.200, 0.400, 25),
....: }
....: )
....:
In [17]: baseball.pivot_table(values="batting avg", columns="team", aggfunc="max")
Out[17]:
team team 1 team 2 team 3 team 4 team 5
batting avg 0.352134 0.295327 0.397191 0.394457 0.396194
```

For more details and examples see the reshaping documentation.

`subset`

#

The `query()`

method is similar to the base R `subset`

function. In R you might want to get the rows of a `data.frame`

where one
column’s values are less than another column’s values:

```
df <- data.frame(a=rnorm(10), b=rnorm(10))
subset(df, a <= b)
df[df$a <= df$b,] # note the comma
```

In pandas, there are a few ways to perform subsetting. You can use
`query()`

or pass an expression as if it were an
index/slice as well as standard boolean indexing:

```
In [18]: df = pd.DataFrame({"a": np.random.randn(10), "b": np.random.randn(10)})
In [19]: df.query("a <= b")
Out[19]:
a b
1 0.174950 0.552887
2 -0.023167 0.148084
3 -0.495291 -0.300218
4 -0.860736 0.197378
5 -1.134146 1.720780
7 -0.290098 0.083515
8 0.238636 0.946550
In [20]: df[df["a"] <= df["b"]]
Out[20]:
a b
1 0.174950 0.552887
2 -0.023167 0.148084
3 -0.495291 -0.300218
4 -0.860736 0.197378
5 -1.134146 1.720780
7 -0.290098 0.083515
8 0.238636 0.946550
In [21]: df.loc[df["a"] <= df["b"]]
Out[21]:
a b
1 0.174950 0.552887
2 -0.023167 0.148084
3 -0.495291 -0.300218
4 -0.860736 0.197378
5 -1.134146 1.720780
7 -0.290098 0.083515
8 0.238636 0.946550
```

For more details and examples see the query documentation.

`with`

#

An expression using a data.frame called `df`

in R with the columns `a`

and
`b`

would be evaluated using `with`

like so:

```
df <- data.frame(a=rnorm(10), b=rnorm(10))
with(df, a + b)
df$a + df$b # same as the previous expression
```

In pandas the equivalent expression, using the
`eval()`

method, would be:

```
In [22]: df = pd.DataFrame({"a": np.random.randn(10), "b": np.random.randn(10)})
In [23]: df.eval("a + b")
Out[23]:
0 -0.091430
1 -2.483890
2 -0.252728
3 -0.626444
4 -0.261740
5 2.149503
6 -0.332214
7 0.799331
8 -2.377245
9 2.104677
dtype: float64
In [24]: df["a"] + df["b"] # same as the previous expression
Out[24]:
0 -0.091430
1 -2.483890
2 -0.252728
3 -0.626444
4 -0.261740
5 2.149503
6 -0.332214
7 0.799331
8 -2.377245
9 2.104677
dtype: float64
```

In certain cases `eval()`

will be much faster than
evaluation in pure Python. For more details and examples see the eval
documentation.

## plyr#

`plyr`

is an R library for the split-apply-combine strategy for data
analysis. The functions revolve around three data structures in R, `a`

for `arrays`

, `l`

for `lists`

, and `d`

for `data.frame`

. The
table below shows how these data structures could be mapped in Python.

R |
Python |
|---|---|
array |
list |
lists |
dictionary or list of objects |
data.frame |
dataframe |

### ddply#

An expression using a data.frame called `df`

in R where you want to
summarize `x`

by `month`

:

```
require(plyr)
df <- data.frame(
x = runif(120, 1, 168),
y = runif(120, 7, 334),
z = runif(120, 1.7, 20.7),
month = rep(c(5,6,7,8),30),
week = sample(1:4, 120, TRUE)
)
ddply(df, .(month, week), summarize,
mean = round(mean(x), 2),
sd = round(sd(x), 2))
```

In pandas the equivalent expression, using the
`groupby()`

method, would be:

```
In [25]: df = pd.DataFrame(
....: {
....: "x": np.random.uniform(1.0, 168.0, 120),
....: "y": np.random.uniform(7.0, 334.0, 120),
....: "z": np.random.uniform(1.7, 20.7, 120),
....: "month": [5, 6, 7, 8] * 30,
....: "week": np.random.randint(1, 4, 120),
....: }
....: )
....:
In [26]: grouped = df.groupby(["month", "week"])
In [27]: grouped["x"].agg(["mean", "std"])
Out[27]:
mean std
month week
5 1 63.653367 40.601965
2 78.126605 53.342400
3 92.091886 57.630110
6 1 81.747070 54.339218
2 70.971205 54.687287
3 100.968344 54.010081
7 1 61.576332 38.844274
2 61.733510 48.209013
3 71.688795 37.595638
8 1 62.741922 34.618153
2 91.774627 49.790202
3 73.936856 60.773900
```

For more details and examples see the groupby documentation.

## reshape / reshape2#

### meltarray#

An expression using a 3 dimensional array called `a`

in R where you want to
melt it into a data.frame:

```
a <- array(c(1:23, NA), c(2,3,4))
data.frame(melt(a))
```

In Python, since `a`

is a list, you can simply use list comprehension.

```
In [28]: a = np.array(list(range(1, 24)) + [np.nan]).reshape(2, 3, 4)
In [29]: pd.DataFrame([tuple(list(x) + [val]) for x, val in np.ndenumerate(a)])
Out[29]:
0 1 2 3
0 0 0 0 1.0
1 0 0 1 2.0
2 0 0 2 3.0
3 0 0 3 4.0
4 0 1 0 5.0
.. .. .. .. ...
19 1 1 3 20.0
20 1 2 0 21.0
21 1 2 1 22.0
22 1 2 2 23.0
23 1 2 3 NaN
[24 rows x 4 columns]
```

### meltlist#

An expression using a list called `a`

in R where you want to melt it
into a data.frame:

```
a <- as.list(c(1:4, NA))
data.frame(melt(a))
```

In Python, this list would be a list of tuples, so
`DataFrame()`

method would convert it to a dataframe as required.

```
In [30]: a = list(enumerate(list(range(1, 5)) + [np.nan]))
In [31]: pd.DataFrame(a)
Out[31]:
0 1
0 0 1.0
1 1 2.0
2 2 3.0
3 3 4.0
4 4 NaN
```

For more details and examples see the Intro to Data Structures documentation.

### meltdf#

An expression using a data.frame called `cheese`

in R where you want to
reshape the data.frame:

```
cheese <- data.frame(
first = c('John', 'Mary'),
last = c('Doe', 'Bo'),
height = c(5.5, 6.0),
weight = c(130, 150)
)
melt(cheese, id=c("first", "last"))
```

In Python, the `melt()`

method is the R equivalent:

```
In [32]: cheese = pd.DataFrame(
....: {
....: "first": ["John", "Mary"],
....: "last": ["Doe", "Bo"],
....: "height": [5.5, 6.0],
....: "weight": [130, 150],
....: }
....: )
....:
In [33]: pd.melt(cheese, id_vars=["first", "last"])
Out[33]:
first last variable value
0 John Doe height 5.5
1 Mary Bo height 6.0
2 John Doe weight 130.0
3 Mary Bo weight 150.0
In [34]: cheese.set_index(["first", "last"]).stack() # alternative way
Out[34]:
first last
John Doe height 5.5
weight 130.0
Mary Bo height 6.0
weight 150.0
dtype: float64
```

For more details and examples see the reshaping documentation.

### cast#

In R `acast`

is an expression using a data.frame called `df`

in R to cast
into a higher dimensional array:

```
df <- data.frame(
x = runif(12, 1, 168),
y = runif(12, 7, 334),
z = runif(12, 1.7, 20.7),
month = rep(c(5,6,7),4),
week = rep(c(1,2), 6)
)
mdf <- melt(df, id=c("month", "week"))
acast(mdf, week ~ month ~ variable, mean)
```

In Python the best way is to make use of `pivot_table()`

:

```
In [35]: df = pd.DataFrame(
....: {
....: "x": np.random.uniform(1.0, 168.0, 12),
....: "y": np.random.uniform(7.0, 334.0, 12),
....: "z": np.random.uniform(1.7, 20.7, 12),
....: "month": [5, 6, 7] * 4,
....: "week": [1, 2] * 6,
....: }
....: )
....:
In [36]: mdf = pd.melt(df, id_vars=["month", "week"])
In [37]: pd.pivot_table(
....: mdf,
....: values="value",
....: index=["variable", "week"],
....: columns=["month"],
....: aggfunc="mean",
....: )
....:
Out[37]:
month 5 6 7
variable week
x 1 93.888747 98.762034 55.219673
2 94.391427 38.112932 83.942781
y 1 94.306912 279.454811 227.840449
2 87.392662 193.028166 173.899260
z 1 11.016009 10.079307 16.170549
2 8.476111 17.638509 19.003494
```

Similarly for `dcast`

which uses a data.frame called `df`

in R to
aggregate information based on `Animal`

and `FeedType`

:

```
df <- data.frame(
Animal = c('Animal1', 'Animal2', 'Animal3', 'Animal2', 'Animal1',
'Animal2', 'Animal3'),
FeedType = c('A', 'B', 'A', 'A', 'B', 'B', 'A'),
Amount = c(10, 7, 4, 2, 5, 6, 2)
)
dcast(df, Animal ~ FeedType, sum, fill=NaN)
# Alternative method using base R
with(df, tapply(Amount, list(Animal, FeedType), sum))
```

Python can approach this in two different ways. Firstly, similar to above
using `pivot_table()`

:

```
In [38]: df = pd.DataFrame(
....: {
....: "Animal": [
....: "Animal1",
....: "Animal2",
....: "Animal3",
....: "Animal2",
....: "Animal1",
....: "Animal2",
....: "Animal3",
....: ],
....: "FeedType": ["A", "B", "A", "A", "B", "B", "A"],
....: "Amount": [10, 7, 4, 2, 5, 6, 2],
....: }
....: )
....:
In [39]: df.pivot_table(values="Amount", index="Animal", columns="FeedType", aggfunc="sum")
Out[39]:
FeedType A B
Animal
Animal1 10.0 5.0
Animal2 2.0 13.0
Animal3 6.0 NaN
```

The second approach is to use the `groupby()`

method:

```
In [40]: df.groupby(["Animal", "FeedType"])["Amount"].sum()
Out[40]:
Animal FeedType
Animal1 A 10
B 5
Animal2 A 2
B 13
Animal3 A 6
Name: Amount, dtype: int64
```

For more details and examples see the reshaping documentation or the groupby documentation.

`factor`

#

pandas has a data type for categorical data.

```
cut(c(1,2,3,4,5,6), 3)
factor(c(1,2,3,2,2,3))
```

In pandas this is accomplished with `pd.cut`

and `astype("category")`

:

```
In [41]: pd.cut(pd.Series([1, 2, 3, 4, 5, 6]), 3)
Out[41]:
0 (0.995, 2.667]
1 (0.995, 2.667]
2 (2.667, 4.333]
3 (2.667, 4.333]
4 (4.333, 6.0]
5 (4.333, 6.0]
dtype: category
Categories (3, interval[float64, right]): [(0.995, 2.667] < (2.667, 4.333] < (4.333, 6.0]]
In [42]: pd.Series([1, 2, 3, 2, 2, 3]).astype("category")
Out[42]:
0 1
1 2
2 3
3 2
4 2
5 3
dtype: category
Categories (3, int64): [1, 2, 3]
```

For more details and examples see categorical introduction and the API documentation. There is also a documentation regarding the differences to R’s factor.

## Source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html

# Comparison with SQL#

Since many potential pandas users have some familiarity with SQL, this page is meant to provide some examples of how various SQL operations would be performed using pandas.

If you’re new to pandas, you might want to first read through 10 Minutes to pandas to familiarize yourself with the library.

As is customary, we import pandas and NumPy as follows:

```
In [1]: import pandas as pd
In [2]: import numpy as np
```

Most of the examples will utilize the `tips`

dataset found within pandas tests. We’ll read
the data into a DataFrame called `tips`

and assume we have a database table of the same name and
structure.

```
In [3]: url = (
...: "https://raw.githubusercontent.com/pandas-dev"
...: "/pandas/main/pandas/tests/io/data/csv/tips.csv"
...: )
...:
In [4]: tips = pd.read_csv(url)
In [5]: tips
Out[5]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 29.03 5.92 Male No Sat Dinner 3
240 27.18 2.00 Female Yes Sat Dinner 2
241 22.67 2.00 Male Yes Sat Dinner 2
242 17.82 1.75 Male No Sat Dinner 2
243 18.78 3.00 Female No Thur Dinner 2
[244 rows x 7 columns]
```

## Copies vs. in place operations#

Most pandas operations return copies of the `Series`

/`DataFrame`

. To make the changes “stick”,
you’ll need to either assign to a new variable:

sorted_df = df.sort_values("col1")

or overwrite the original one:

df = df.sort_values("col1")

Note

You will see an `inplace=True`

or `copy=False`

keyword argument available for
some methods:

```
df.replace(5, inplace=True)
```

There is an active discussion about deprecating and removing `inplace`

and `copy`

for
most methods (e.g. `dropna`

) except for a very small subset of methods
(including `replace`

). Both keywords won’t be
necessary anymore in the context of Copy-on-Write. The proposal can be found
here.

## SELECT#

In SQL, selection is done using a comma-separated list of columns you’d like to select (or a `*`

to select all columns):

```
SELECT total_bill, tip, smoker, time
FROM tips;
```

With pandas, column selection is done by passing a list of column names to your DataFrame:

```
In [6]: tips[["total_bill", "tip", "smoker", "time"]]
Out[6]:
total_bill tip smoker time
0 16.99 1.01 No Dinner
1 10.34 1.66 No Dinner
2 21.01 3.50 No Dinner
3 23.68 3.31 No Dinner
4 24.59 3.61 No Dinner
.. ... ... ... ...
239 29.03 5.92 No Dinner
240 27.18 2.00 Yes Dinner
241 22.67 2.00 Yes Dinner
242 17.82 1.75 No Dinner
243 18.78 3.00 No Dinner
[244 rows x 4 columns]
```

Calling the DataFrame without the list of column names would display all columns (akin to SQL’s
`*`

).

In SQL, you can add a calculated column:

```
SELECT *, tip/total_bill as tip_rate
FROM tips;
```

With pandas, you can use the `DataFrame.assign()`

method of a DataFrame to append a new column:

```
In [7]: tips.assign(tip_rate=tips["tip"] / tips["total_bill"])
Out[7]:
total_bill tip sex smoker day time size tip_rate
0 16.99 1.01 Female No Sun Dinner 2 0.059447
1 10.34 1.66 Male No Sun Dinner 3 0.160542
2 21.01 3.50 Male No Sun Dinner 3 0.166587
3 23.68 3.31 Male No Sun Dinner 2 0.139780
4 24.59 3.61 Female No Sun Dinner 4 0.146808
.. ... ... ... ... ... ... ... ...
239 29.03 5.92 Male No Sat Dinner 3 0.203927
240 27.18 2.00 Female Yes Sat Dinner 2 0.073584
241 22.67 2.00 Male Yes Sat Dinner 2 0.088222
242 17.82 1.75 Male No Sat Dinner 2 0.098204
243 18.78 3.00 Female No Thur Dinner 2 0.159744
[244 rows x 8 columns]
```

## WHERE#

Filtering in SQL is done via a WHERE clause.

```
SELECT *
FROM tips
WHERE time = 'Dinner';
```

DataFrames can be filtered in multiple ways; the most intuitive of which is using boolean indexing.

```
In [8]: tips[tips["total_bill"] > 10]
Out[8]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 29.03 5.92 Male No Sat Dinner 3
240 27.18 2.00 Female Yes Sat Dinner 2
241 22.67 2.00 Male Yes Sat Dinner 2
242 17.82 1.75 Male No Sat Dinner 2
243 18.78 3.00 Female No Thur Dinner 2
[227 rows x 7 columns]
```

The above statement is simply passing a `Series`

of `True`

/`False`

objects to the DataFrame,
returning all rows with `True`

.

```
In [9]: is_dinner = tips["time"] == "Dinner"
In [10]: is_dinner
Out[10]:
0 True
1 True
2 True
3 True
4 True
...
239 True
240 True
241 True
242 True
243 True
Name: time, Length: 244, dtype: bool
In [11]: is_dinner.value_counts()
Out[11]:
time
True 176
False 68
Name: count, dtype: int64
In [12]: tips[is_dinner]
Out[12]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 29.03 5.92 Male No Sat Dinner 3
240 27.18 2.00 Female Yes Sat Dinner 2
241 22.67 2.00 Male Yes Sat Dinner 2
242 17.82 1.75 Male No Sat Dinner 2
243 18.78 3.00 Female No Thur Dinner 2
[176 rows x 7 columns]
```

Just like SQL’s `OR`

and `AND`

, multiple conditions can be passed to a DataFrame using `|`

(`OR`

) and `&`

(`AND`

).

Tips of more than $5 at Dinner meals:

```
SELECT *
FROM tips
WHERE time = 'Dinner' AND tip > 5.00;
```

```
In [13]: tips[(tips["time"] == "Dinner") & (tips["tip"] > 5.00)]
Out[13]:
total_bill tip sex smoker day time size
23 39.42 7.58 Male No Sat Dinner 4
44 30.40 5.60 Male No Sun Dinner 4
47 32.40 6.00 Male No Sun Dinner 4
52 34.81 5.20 Female No Sun Dinner 4
59 48.27 6.73 Male No Sat Dinner 4
116 29.93 5.07 Male No Sun Dinner 4
155 29.85 5.14 Female No Sun Dinner 5
170 50.81 10.00 Male Yes Sat Dinner 3
172 7.25 5.15 Male Yes Sun Dinner 2
181 23.33 5.65 Male Yes Sun Dinner 2
183 23.17 6.50 Male Yes Sun Dinner 4
211 25.89 5.16 Male Yes Sat Dinner 4
212 48.33 9.00 Male No Sat Dinner 4
214 28.17 6.50 Female Yes Sat Dinner 3
239 29.03 5.92 Male No Sat Dinner 3
```

Tips by parties of at least 5 diners OR bill total was more than $45:

```
SELECT *
FROM tips
WHERE size >= 5 OR total_bill > 45;
```

```
In [14]: tips[(tips["size"] >= 5) | (tips["total_bill"] > 45)]
Out[14]:
total_bill tip sex smoker day time size
59 48.27 6.73 Male No Sat Dinner 4
125 29.80 4.20 Female No Thur Lunch 6
141 34.30 6.70 Male No Thur Lunch 6
142 41.19 5.00 Male No Thur Lunch 5
143 27.05 5.00 Female No Thur Lunch 6
155 29.85 5.14 Female No Sun Dinner 5
156 48.17 5.00 Male No Sun Dinner 6
170 50.81 10.00 Male Yes Sat Dinner 3
182 45.35 3.50 Male Yes Sun Dinner 3
185 20.69 5.00 Male No Sun Dinner 5
187 30.46 2.00 Male Yes Sun Dinner 5
212 48.33 9.00 Male No Sat Dinner 4
216 28.15 3.00 Male Yes Sat Dinner 5
```

NULL checking is done using the `notna()`

and `isna()`

methods.

```
In [15]: frame = pd.DataFrame(
....: {"col1": ["A", "B", np.nan, "C", "D"], "col2": ["F", np.nan, "G", "H", "I"]}
....: )
....:
In [16]: frame
Out[16]:
col1 col2
0 A F
1 B NaN
2 NaN G
3 C H
4 D I
```

Assume we have a table of the same structure as our DataFrame above. We can see only the records
where `col2`

IS NULL with the following query:

```
SELECT *
FROM frame
WHERE col2 IS NULL;
```

```
In [17]: frame[frame["col2"].isna()]
Out[17]:
col1 col2
1 B NaN
```

Getting items where `col1`

IS NOT NULL can be done with `notna()`

.

```
SELECT *
FROM frame
WHERE col1 IS NOT NULL;
```

```
In [18]: frame[frame["col1"].notna()]
Out[18]:
col1 col2
0 A F
1 B NaN
3 C H
4 D I
```

## GROUP BY#

In pandas, SQL’s `GROUP BY`

operations are performed using the similarly named
`groupby()`

method. `groupby()`

typically refers to a
process where we’d like to split a dataset into groups, apply some function (typically aggregation)
, and then combine the groups together.

A common SQL operation would be getting the count of records in each group throughout a dataset. For instance, a query getting us the number of tips left by sex:

```
SELECT sex, count(*)
FROM tips
GROUP BY sex;
/*
Female 87
Male 157
*/
```

The pandas equivalent would be:

```
In [19]: tips.groupby("sex").size()
Out[19]:
sex
Female 87
Male 157
dtype: int64
```

Notice that in the pandas code we used `DataFrameGroupBy.size()`

and not
`DataFrameGroupBy.count()`

. This is because
`DataFrameGroupBy.count()`

applies the function to each column, returning
the number of `NOT NULL`

records within each.

```
In [20]: tips.groupby("sex").count()
Out[20]:
total_bill tip smoker day time size
sex
Female 87 87 87 87 87 87
Male 157 157 157 157 157 157
```

Alternatively, we could have applied the `DataFrameGroupBy.count()`

method
to an individual column:

```
In [21]: tips.groupby("sex")["total_bill"].count()
Out[21]:
sex
Female 87
Male 157
Name: total_bill, dtype: int64
```

Multiple functions can also be applied at once. For instance, say we’d like to see how tip amount
differs by day of the week - `DataFrameGroupBy.agg()`

allows you to pass a dictionary
to your grouped DataFrame, indicating which functions to apply to specific columns.

```
SELECT day, AVG(tip), COUNT(*)
FROM tips
GROUP BY day;
/*
Fri 2.734737 19
Sat 2.993103 87
Sun 3.255132 76
Thu 2.771452 62
*/
```

```
In [22]: tips.groupby("day").agg({"tip": "mean", "day": "size"})
Out[22]:
tip day
day
Fri 2.734737 19
Sat 2.993103 87
Sun 3.255132 76
Thur 2.771452 62
```

Grouping by more than one column is done by passing a list of columns to the
`groupby()`

method.

```
SELECT smoker, day, COUNT(*), AVG(tip)
FROM tips
GROUP BY smoker, day;
/*
smoker day
No Fri 4 2.812500
Sat 45 3.102889
Sun 57 3.167895
Thu 45 2.673778
Yes Fri 15 2.714000
Sat 42 2.875476
Sun 19 3.516842
Thu 17 3.030000
*/
```

```
In [23]: tips.groupby(["smoker", "day"]).agg({"tip": ["size", "mean"]})
Out[23]:
tip
size mean
smoker day
No Fri 4 2.812500
Sat 45 3.102889
Sun 57 3.167895
Thur 45 2.673778
Yes Fri 15 2.714000
Sat 42 2.875476
Sun 19 3.516842
Thur 17 3.030000
```

## JOIN#

`JOIN`

s can be performed with `join()`

or `merge()`

. By
default, `join()`

will join the DataFrames on their indices. Each method has
parameters allowing you to specify the type of join to perform (`LEFT`

, `RIGHT`

, `INNER`

,
`FULL`

) or the columns to join on (column names or indices).

Warning

If both key columns contain rows where the key is a null value, those rows will be matched against each other. This is different from usual SQL join behaviour and can lead to unexpected results.

```
In [24]: df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
In [25]: df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})
```

Assume we have two database tables of the same name and structure as our DataFrames.

Now let’s go over the various types of `JOIN`

s.

### INNER JOIN#

```
SELECT *
FROM df1
INNER JOIN df2
ON df1.key = df2.key;
```

```
# merge performs an INNER JOIN by default
In [26]: pd.merge(df1, df2, on="key")
Out[26]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
```

`merge()`

also offers parameters for cases when you’d like to join one DataFrame’s
column with another DataFrame’s index.

```
In [27]: indexed_df2 = df2.set_index("key")
In [28]: pd.merge(df1, indexed_df2, left_on="key", right_index=True)
Out[28]:
key value_x value_y
1 B -0.282863 1.212112
3 D -1.135632 -0.173215
3 D -1.135632 0.119209
```

`merge()`

also supports joining on multiple columns by passing a list of column names.

```
SELECT *
FROM df1_multi
INNER JOIN df2_multi
ON df1_multi.key1 = df2_multi.key1
AND df1_multi.key2 = df2_multi.key2;
```

```
In [29]: df1_multi = pd.DataFrame({
....: "key1": ["A", "B", "C", "D"],
....: "key2": [1, 2, 3, 4],
....: "value": np.random.randn(4)
....: })
....:
In [30]: df2_multi = pd.DataFrame({
....: "key1": ["B", "D", "D", "E"],
....: "key2": [2, 4, 4, 5],
....: "value": np.random.randn(4)
....: })
....:
In [31]: pd.merge(df1_multi, df2_multi, on=["key1", "key2"])
Out[31]:
key1 key2 value_x value_y
0 B 2 -2.104569 0.721555
1 D 4 1.071804 -0.706771
2 D 4 1.071804 -1.039575
```

If the columns have different names between DataFrames, on can be replaced with left_on and right_on.

```
In [32]: df2_multi = pd.DataFrame({
....: "key_1": ["B", "D", "D", "E"],
....: "key_2": [2, 4, 4, 5],
....: "value": np.random.randn(4)
....: })
....:
In [33]: pd.merge(df1_multi, df2_multi, left_on=["key1", "key2"], right_on=["key_1", "key_2"])
Out[33]:
key1 key2 value_x key_1 key_2 value_y
0 B 2 -2.104569 B 2 -0.424972
1 D 4 1.071804 D 4 0.567020
2 D 4 1.071804 D 4 0.276232
```

### LEFT OUTER JOIN#

Show all records from `df1`

.

```
SELECT *
FROM df1
LEFT OUTER JOIN df2
ON df1.key = df2.key;
```

```
In [34]: pd.merge(df1, df2, on="key", how="left")
Out[34]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
```

### RIGHT JOIN#

Show all records from `df2`

.

```
SELECT *
FROM df1
RIGHT OUTER JOIN df2
ON df1.key = df2.key;
```

```
In [35]: pd.merge(df1, df2, on="key", how="right")
Out[35]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
3 E NaN -1.044236
```

### FULL JOIN#

pandas also allows for `FULL JOIN`

s, which display both sides of the dataset, whether or not the
joined columns find a match. As of writing, `FULL JOIN`

s are not supported in all RDBMS (MySQL).

Show all records from both tables.

```
SELECT *
FROM df1
FULL OUTER JOIN df2
ON df1.key = df2.key;
```

```
In [36]: pd.merge(df1, df2, on="key", how="outer")
Out[36]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E NaN -1.044236
```

## UNION#

`UNION ALL`

can be performed using `concat()`

.

```
In [37]: df1 = pd.DataFrame(
....: {"city": ["Chicago", "San Francisco", "New York City"], "rank": range(1, 4)}
....: )
....:
In [38]: df2 = pd.DataFrame(
....: {"city": ["Chicago", "Boston", "Los Angeles"], "rank": [1, 4, 5]}
....: )
....:
```

```
SELECT city, rank
FROM df1
UNION ALL
SELECT city, rank
FROM df2;
/*
city rank
Chicago 1
San Francisco 2
New York City 3
Chicago 1
Boston 4
Los Angeles 5
*/
```

```
In [39]: pd.concat([df1, df2])
Out[39]:
city rank
0 Chicago 1
1 San Francisco 2
2 New York City 3
0 Chicago 1
1 Boston 4
2 Los Angeles 5
```

SQL’s `UNION`

is similar to `UNION ALL`

, however `UNION`

will remove duplicate rows.

```
SELECT city, rank
FROM df1
UNION
SELECT city, rank
FROM df2;
-- notice that there is only one Chicago record this time
/*
city rank
Chicago 1
San Francisco 2
New York City 3
Boston 4
Los Angeles 5
*/
```

In pandas, you can use `concat()`

in conjunction with
`drop_duplicates()`

.

```
In [40]: pd.concat([df1, df2]).drop_duplicates()
Out[40]:
city rank
0 Chicago 1
1 San Francisco 2
2 New York City 3
1 Boston 4
2 Los Angeles 5
```

## LIMIT#

```
SELECT * FROM tips
LIMIT 10;
```

```
In [41]: tips.head(10)
Out[41]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
5 25.29 4.71 Male No Sun Dinner 4
6 8.77 2.00 Male No Sun Dinner 2
7 26.88 3.12 Male No Sun Dinner 4
8 15.04 1.96 Male No Sun Dinner 2
9 14.78 3.23 Male No Sun Dinner 2
```

## pandas equivalents for some SQL analytic and aggregate functions#

### Top n rows with offset#

```
-- MySQL
SELECT * FROM tips
ORDER BY tip DESC
LIMIT 10 OFFSET 5;
```

```
In [42]: tips.nlargest(10 + 5, columns="tip").tail(10)
Out[42]:
total_bill tip sex smoker day time size
183 23.17 6.50 Male Yes Sun Dinner 4
214 28.17 6.50 Female Yes Sat Dinner 3
47 32.40 6.00 Male No Sun Dinner 4
239 29.03 5.92 Male No Sat Dinner 3
88 24.71 5.85 Male No Thur Lunch 2
181 23.33 5.65 Male Yes Sun Dinner 2
44 30.40 5.60 Male No Sun Dinner 4
52 34.81 5.20 Female No Sun Dinner 4
85 34.83 5.17 Female No Thur Lunch 4
211 25.89 5.16 Male Yes Sat Dinner 4
```

### Top n rows per group#

```
-- Oracle's ROW_NUMBER() analytic function
SELECT * FROM (
SELECT
t.*,
ROW_NUMBER() OVER(PARTITION BY day ORDER BY total_bill DESC) AS rn
FROM tips t
)
WHERE rn < 3
ORDER BY day, rn;
```

```
In [43]: (
....: tips.assign(
....: rn=tips.sort_values(["total_bill"], ascending=False)
....: .groupby(["day"])
....: .cumcount()
....: + 1
....: )
....: .query("rn < 3")
....: .sort_values(["day", "rn"])
....: )
....:
Out[43]:
total_bill tip sex smoker day time size rn
95 40.17 4.73 Male Yes Fri Dinner 4 1
90 28.97 3.00 Male Yes Fri Dinner 2 2
170 50.81 10.00 Male Yes Sat Dinner 3 1
212 48.33 9.00 Male No Sat Dinner 4 2
156 48.17 5.00 Male No Sun Dinner 6 1
182 45.35 3.50 Male Yes Sun Dinner 3 2
197 43.11 5.00 Female Yes Thur Lunch 4 1
142 41.19 5.00 Male No Thur Lunch 5 2
```

the same using `rank(method='first')`

function

```
In [44]: (
....: tips.assign(
....: rnk=tips.groupby(["day"])["total_bill"].rank(
....: method="first", ascending=False
....: )
....: )
....: .query("rnk < 3")
....: .sort_values(["day", "rnk"])
....: )
....:
Out[44]:
total_bill tip sex smoker day time size rnk
95 40.17 4.73 Male Yes Fri Dinner 4 1.0
90 28.97 3.00 Male Yes Fri Dinner 2 2.0
170 50.81 10.00 Male Yes Sat Dinner 3 1.0
212 48.33 9.00 Male No Sat Dinner 4 2.0
156 48.17 5.00 Male No Sun Dinner 6 1.0
182 45.35 3.50 Male Yes Sun Dinner 3 2.0
197 43.11 5.00 Female Yes Thur Lunch 4 1.0
142 41.19 5.00 Male No Thur Lunch 5 2.0
```

```
-- Oracle's RANK() analytic function
SELECT * FROM (
SELECT
t.*,
RANK() OVER(PARTITION BY sex ORDER BY tip) AS rnk
FROM tips t
WHERE tip < 2
)
WHERE rnk < 3
ORDER BY sex, rnk;
```

Let’s find tips with (rank < 3) per gender group for (tips < 2).
Notice that when using `rank(method='min')`

function
`rnk_min`

remains the same for the same `tip`

(as Oracle’s `RANK()`

function)

```
In [45]: (
....: tips[tips["tip"] < 2]
....: .assign(rnk_min=tips.groupby(["sex"])["tip"].rank(method="min"))
....: .query("rnk_min < 3")
....: .sort_values(["sex", "rnk_min"])
....: )
....:
Out[45]:
total_bill tip sex smoker day time size rnk_min
67 3.07 1.00 Female Yes Sat Dinner 1 1.0
92 5.75 1.00 Female Yes Fri Dinner 2 1.0
111 7.25 1.00 Female No Sat Dinner 1 1.0
236 12.60 1.00 Male Yes Sat Dinner 2 1.0
237 32.83 1.17 Male Yes Sat Dinner 2 2.0
```

## UPDATE#

```
UPDATE tips
SET tip = tip*2
WHERE tip < 2;
```

```
In [46]: tips.loc[tips["tip"] < 2, "tip"] *= 2
```

## DELETE#

```
DELETE FROM tips
WHERE tip > 9;
```

In pandas we select the rows that should remain instead of deleting the rows that should be removed:

```
In [47]: tips = tips.loc[tips["tip"] <= 9]
```

## Source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html

# Comparison with spreadsheets#

Since many potential pandas users have some familiarity with spreadsheet programs like Excel, this page is meant to provide some examples of how various spreadsheet operations would be performed using pandas. This page will use terminology and link to documentation for Excel, but much will be the same/similar in Google Sheets, LibreOffice Calc, Apple Numbers, and other Excel-compatible spreadsheet software.

If you’re new to pandas, you might want to first read through 10 Minutes to pandas to familiarize yourself with the library.

As is customary, we import pandas and NumPy as follows:

```
In [1]: import pandas as pd
In [2]: import numpy as np
```

## Data structures#

### General terminology translation#

pandas |
Excel |
|---|---|
|
worksheet |
|
column |
|
row headings |
row |
row |
|
empty cell |

`DataFrame`

#

A `DataFrame`

in pandas is analogous to an Excel worksheet. While an Excel workbook can contain
multiple worksheets, pandas `DataFrame`

s exist independently.

`Series`

#

A `Series`

is the data structure that represents one column of a `DataFrame`

. Working with a
`Series`

is analogous to referencing a column of a spreadsheet.

`Index`

#

Every `DataFrame`

and `Series`

has an `Index`

, which are labels on the *rows* of the data. In
pandas, if no index is specified, a `RangeIndex`

is used by default (first row = 0,
second row = 1, and so on), analogous to row headings/numbers in spreadsheets.

In pandas, indexes can be set to one (or multiple) unique values, which is like having a column that
is used as the row identifier in a worksheet. Unlike most spreadsheets, these `Index`

values can
actually be used to reference the rows. (Note that this can be done in Excel with structured
references.)
For example, in spreadsheets, you would reference the first row as `A1:Z1`

, while in pandas you
could use `populations.loc['Chicago']`

.

Index values are also persistent, so if you re-order the rows in a `DataFrame`

, the label for a
particular row don’t change.

See the indexing documentation for much more on how to use an `Index`

effectively.

### Copies vs. in place operations#

Most pandas operations return copies of the `Series`

/`DataFrame`

. To make the changes “stick”,
you’ll need to either assign to a new variable:

sorted_df = df.sort_values("col1")

or overwrite the original one:

df = df.sort_values("col1")

Note

You will see an `inplace=True`

or `copy=False`

keyword argument available for
some methods:

```
df.replace(5, inplace=True)
```

There is an active discussion about deprecating and removing `inplace`

and `copy`

for
most methods (e.g. `dropna`

) except for a very small subset of methods
(including `replace`

). Both keywords won’t be
necessary anymore in the context of Copy-on-Write. The proposal can be found
here.

## Data input / output#

### Constructing a DataFrame from values#

In a spreadsheet, values can be typed directly into cells.

A pandas `DataFrame`

can be constructed in many different ways,
but for a small number of values, it is often convenient to specify it as
a Python dictionary, where the keys are the column names
and the values are the data.

```
In [3]: df = pd.DataFrame({"x": [1, 3, 5], "y": [2, 4, 6]})
In [4]: df
Out[4]:
x y
0 1 2
1 3 4
2 5 6
```

### Reading external data#

Both Excel and pandas can import data from various sources in various formats.

#### CSV#

Let’s load and display the tips
dataset from the pandas tests, which is a CSV file. In Excel, you would download and then
open the CSV.
In pandas, you pass the URL or local path of the CSV file to `read_csv()`

:

```
In [5]: url = (
...: "https://raw.githubusercontent.com/pandas-dev"
...: "/pandas/main/pandas/tests/io/data/csv/tips.csv"
...: )
...:
In [6]: tips = pd.read_csv(url)
In [7]: tips
Out[7]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 29.03 5.92 Male No Sat Dinner 3
240 27.18 2.00 Female Yes Sat Dinner 2
241 22.67 2.00 Male Yes Sat Dinner 2
242 17.82 1.75 Male No Sat Dinner 2
243 18.78 3.00 Female No Thur Dinner 2
[244 rows x 7 columns]
```

Like Excel’s Text Import Wizard,
`read_csv`

can take a number of parameters to specify how the data should be parsed. For
example, if the data was instead tab delimited, and did not have column names, the pandas command
would be:

```
tips = pd.read_csv("tips.csv", sep="\t", header=None)
# alternatively, read_table is an alias to read_csv with tab delimiter
tips = pd.read_table("tips.csv", header=None)
```

#### Excel files#

Excel opens various Excel file formats by double-clicking them, or using the Open menu. In pandas, you use special methods for reading and writing from/to Excel files.

Let’s first create a new Excel file based on the `tips`

dataframe in the above example:

```
tips.to_excel("./tips.xlsx")
```

Should you wish to subsequently access the data in the `tips.xlsx`

file, you can read it into your module using

```
tips_df = pd.read_excel("./tips.xlsx", index_col=0)
```

You have just read in an Excel file using pandas!

### Limiting output#

Spreadsheet programs will only show one screenful of data at a time and then allow you to scroll, so
there isn’t really a need to limit output. In pandas, you’ll need to put a little more thought into
controlling how your `DataFrame`

s are displayed.

By default, pandas will truncate output of large `DataFrame`

s to show the first and last rows.
This can be overridden by changing the pandas options, or using
`DataFrame.head()`

or `DataFrame.tail()`

.

```
In [8]: tips.head(5)
Out[8]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
```

### Exporting data#

By default, desktop spreadsheet software will save to its respective file format (`.xlsx`

, `.ods`

, etc). You can, however, save to other file formats.

pandas can create Excel files, CSV, or a number of other formats.

## Data operations#

### Operations on columns#

In spreadsheets, formulas are often created in individual cells and then dragged into other cells to compute them for other columns. In pandas, you’re able to do operations on whole columns directly.

pandas provides vectorized operations by specifying the individual `Series`

in the
`DataFrame`

. New columns can be assigned in the same way. The `DataFrame.drop()`

method drops
a column from the `DataFrame`

.

```
In [9]: tips["total_bill"] = tips["total_bill"] - 2
In [10]: tips["new_bill"] = tips["total_bill"] / 2
In [11]: tips
Out[11]:
total_bill tip sex smoker day time size new_bill
0 14.99 1.01 Female No Sun Dinner 2 7.495
1 8.34 1.66 Male No Sun Dinner 3 4.170
2 19.01 3.50 Male No Sun Dinner 3 9.505
3 21.68 3.31 Male No Sun Dinner 2 10.840
4 22.59 3.61 Female No Sun Dinner 4 11.295
.. ... ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3 13.515
240 25.18 2.00 Female Yes Sat Dinner 2 12.590
241 20.67 2.00 Male Yes Sat Dinner 2 10.335
242 15.82 1.75 Male No Sat Dinner 2 7.910
243 16.78 3.00 Female No Thur Dinner 2 8.390
[244 rows x 8 columns]
In [12]: tips = tips.drop("new_bill", axis=1)
```

Note that we aren’t having to tell it to do that subtraction cell-by-cell — pandas handles that for us. See how to create new columns derived from existing columns.

### Filtering#

In Excel, filtering is done through a graphical menu.

DataFrames can be filtered in multiple ways; the most intuitive of which is using boolean indexing.

```
In [13]: tips[tips["total_bill"] > 10]
Out[13]:
total_bill tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
5 23.29 4.71 Male No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[204 rows x 7 columns]
```

The above statement is simply passing a `Series`

of `True`

/`False`

objects to the DataFrame,
returning all rows with `True`

.

```
In [14]: is_dinner = tips["time"] == "Dinner"
In [15]: is_dinner
Out[15]:
0 True
1 True
2 True
3 True
4 True
...
239 True
240 True
241 True
242 True
243 True
Name: time, Length: 244, dtype: bool
In [16]: is_dinner.value_counts()
Out[16]:
time
True 176
False 68
Name: count, dtype: int64
In [17]: tips[is_dinner]
Out[17]:
total_bill tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
1 8.34 1.66 Male No Sun Dinner 3
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[176 rows x 7 columns]
```

### If/then logic#

Let’s say we want to make a `bucket`

column with values of `low`

and `high`

, based on whether
the `total_bill`

is less or more than $10.

In spreadsheets, logical comparison can be done with conditional formulas.
We’d use a formula of `=IF(A2 < 10, "low", "high")`

, dragged to all cells in a new `bucket`

column.

The same operation in pandas can be accomplished using
the `where`

method from `numpy`

.

```
In [18]: tips["bucket"] = np.where(tips["total_bill"] < 10, "low", "high")
In [19]: tips
Out[19]:
total_bill tip sex smoker day time size bucket
0 14.99 1.01 Female No Sun Dinner 2 high
1 8.34 1.66 Male No Sun Dinner 3 low
2 19.01 3.50 Male No Sun Dinner 3 high
3 21.68 3.31 Male No Sun Dinner 2 high
4 22.59 3.61 Female No Sun Dinner 4 high
.. ... ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3 high
240 25.18 2.00 Female Yes Sat Dinner 2 high
241 20.67 2.00 Male Yes Sat Dinner 2 high
242 15.82 1.75 Male No Sat Dinner 2 high
243 16.78 3.00 Female No Thur Dinner 2 high
[244 rows x 8 columns]
```

### Date functionality#

*This section will refer to “dates”, but timestamps are handled similarly.*

We can think of date functionality in two parts: parsing, and output. In spreadsheets, date values are generally parsed automatically, though there is a DATEVALUE function if you need it. In pandas, you need to explicitly convert plain text to datetime objects, either while reading from a CSV or once in a DataFrame.

Once parsed, spreadsheets display the dates in a default format, though the format can be changed.
In pandas, you’ll generally want to keep dates as `datetime`

objects while you’re doing
calculations with them. Outputting *parts* of dates (such as the year) is done through date
functions
in spreadsheets, and datetime properties in pandas.

Given `date1`

and `date2`

in columns `A`

and `B`

of a spreadsheet, you might have these
formulas:

column |
formula |
|---|---|
|
|
|
|
|
|
|
|

The equivalent pandas operations are shown below.

```
In [20]: tips["date1"] = pd.Timestamp("2013-01-15")
In [21]: tips["date2"] = pd.Timestamp("2015-02-15")
In [22]: tips["date1_year"] = tips["date1"].dt.year
In [23]: tips["date2_month"] = tips["date2"].dt.month
In [24]: tips["date1_next"] = tips["date1"] + pd.offsets.MonthBegin()
In [25]: tips["months_between"] = tips["date2"].dt.to_period("M") - tips[
....: "date1"
....: ].dt.to_period("M")
....:
In [26]: tips[
....: ["date1", "date2", "date1_year", "date2_month", "date1_next", "months_between"]
....: ]
....:
Out[26]:
date1 date2 date1_year date2_month date1_next months_between
0 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
1 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
2 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
3 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
4 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
.. ... ... ... ... ... ...
239 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
240 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
241 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
242 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
243 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
[244 rows x 6 columns]
```

See Time series / date functionality for more details.

### Selection of columns#

In spreadsheets, you can select columns you want by:

Referencing a range from one worksheet into another

Since spreadsheet columns are typically named in a header row, renaming a column is simply a matter of changing the text in that first cell.

The same operations are expressed in pandas below.

#### Keep certain columns#

```
In [27]: tips[["sex", "total_bill", "tip"]]
Out[27]:
sex total_bill tip
0 Female 14.99 1.01
1 Male 8.34 1.66
2 Male 19.01 3.50
3 Male 21.68 3.31
4 Female 22.59 3.61
.. ... ... ...
239 Male 27.03 5.92
240 Female 25.18 2.00
241 Male 20.67 2.00
242 Male 15.82 1.75
243 Female 16.78 3.00
[244 rows x 3 columns]
```

#### Drop a column#

```
In [28]: tips.drop("sex", axis=1)
Out[28]:
total_bill tip smoker day time size
0 14.99 1.01 No Sun Dinner 2
1 8.34 1.66 No Sun Dinner 3
2 19.01 3.50 No Sun Dinner 3
3 21.68 3.31 No Sun Dinner 2
4 22.59 3.61 No Sun Dinner 4
.. ... ... ... ... ... ...
239 27.03 5.92 No Sat Dinner 3
240 25.18 2.00 Yes Sat Dinner 2
241 20.67 2.00 Yes Sat Dinner 2
242 15.82 1.75 No Sat Dinner 2
243 16.78 3.00 No Thur Dinner 2
[244 rows x 6 columns]
```

#### Rename a column#

```
In [29]: tips.rename(columns={"total_bill": "total_bill_2"})
Out[29]:
total_bill_2 tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
1 8.34 1.66 Male No Sun Dinner 3
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[244 rows x 7 columns]
```

### Sorting by values#

Sorting in spreadsheets is accomplished via the sort dialog.

pandas has a `DataFrame.sort_values()`

method, which takes a list of columns to sort by.

```
In [30]: tips = tips.sort_values(["sex", "total_bill"])
In [31]: tips
Out[31]:
total_bill tip sex smoker day time size
67 1.07 1.00 Female Yes Sat Dinner 1
92 3.75 1.00 Female Yes Fri Dinner 2
111 5.25 1.00 Female No Sat Dinner 1
145 6.35 1.50 Female No Thur Lunch 2
135 6.51 1.25 Female No Thur Lunch 2
.. ... ... ... ... ... ... ...
182 43.35 3.50 Male Yes Sun Dinner 3
156 46.17 5.00 Male No Sun Dinner 6
59 46.27 6.73 Male No Sat Dinner 4
212 46.33 9.00 Male No Sat Dinner 4
170 48.81 10.00 Male Yes Sat Dinner 3
[244 rows x 7 columns]
```

## String processing#

### Finding length of string#

In spreadsheets, the number of characters in text can be found with the LEN function. This can be used with the TRIM function to remove extra whitespace.

```
=LEN(TRIM(A2))
```

You can find the length of a character string with `Series.str.len()`

.
In Python 3, all strings are Unicode strings. `len`

includes trailing blanks.
Use `len`

and `rstrip`

to exclude trailing blanks.

```
In [32]: tips["time"].str.len()
Out[32]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
In [33]: tips["time"].str.rstrip().str.len()
Out[33]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
```

Note this will still include multiple spaces within the string, so isn’t 100% equivalent.

### Finding position of substring#

The FIND
spreadsheet function returns the position of a substring, with the first character being `1`

.

You can find the position of a character in a column of strings with the `Series.str.find()`

method. `find`

searches for the first position of the substring. If the substring is found, the
method returns its position. If not found, it returns `-1`

. Keep in mind that Python indexes are
zero-based.

```
In [34]: tips["sex"].str.find("ale")
Out[34]:
67 3
92 3
111 3
145 3
135 3
..
182 1
156 1
59 1
212 1
170 1
Name: sex, Length: 244, dtype: int64
```

### Extracting substring by position#

Spreadsheets have a MID formula for extracting a substring from a given position. To get the first character:

```
=MID(A2,1,1)
```

With pandas you can use `[]`

notation to extract a substring
from a string by position locations. Keep in mind that Python
indexes are zero-based.

```
In [35]: tips["sex"].str[0:1]
Out[35]:
67 F
92 F
111 F
145 F
135 F
..
182 M
156 M
59 M
212 M
170 M
Name: sex, Length: 244, dtype: str
```

### Extracting nth word#

In Excel, you might use the Text to Columns Wizard for splitting text and retrieving a specific column. (Note it’s possible to do so through a formula as well.)

The simplest way to extract words in pandas is to split the strings by spaces, then reference the word by index. Note there are more powerful approaches should you need them.

```
In [36]: firstlast = pd.DataFrame({"String": ["John Smith", "Jane Cook"]})
In [37]: firstlast["First_Name"] = firstlast["String"].str.split(" ", expand=True)[0]
In [38]: firstlast["Last_Name"] = firstlast["String"].str.rsplit(" ", expand=True)[1]
In [39]: firstlast
Out[39]:
String First_Name Last_Name
0 John Smith John Smith
1 Jane Cook Jane Cook
```

### Changing case#

Spreadsheets provide UPPER, LOWER, and PROPER functions for converting text to upper, lower, and title case, respectively.

The equivalent pandas methods are `Series.str.upper()`

, `Series.str.lower()`

, and
`Series.str.title()`

.

```
In [40]: firstlast = pd.DataFrame({"string": ["John Smith", "Jane Cook"]})
In [41]: firstlast["upper"] = firstlast["string"].str.upper()
In [42]: firstlast["lower"] = firstlast["string"].str.lower()
In [43]: firstlast["title"] = firstlast["string"].str.title()
In [44]: firstlast
Out[44]:
string upper lower title
0 John Smith JOHN SMITH john smith John Smith
1 Jane Cook JANE COOK jane cook Jane Cook
```

## Merging#

The following tables will be used in the merge examples:

```
In [45]: df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
In [46]: df1
Out[46]:
key value
0 A 0.469112
1 B -0.282863
2 C -1.509059
3 D -1.135632
In [47]: df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})
In [48]: df2
Out[48]:
key value
0 B 1.212112
1 D -0.173215
2 D 0.119209
3 E -1.044236
```

In Excel, there are merging of tables can be done through a VLOOKUP.

pandas DataFrames have a `merge()`

method, which provides similar functionality. The
data does not have to be sorted ahead of time, and different join types are accomplished via the
`how`

keyword.

```
In [49]: inner_join = df1.merge(df2, on=["key"], how="inner")
In [50]: inner_join
Out[50]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
In [51]: left_join = df1.merge(df2, on=["key"], how="left")
In [52]: left_join
Out[52]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
In [53]: right_join = df1.merge(df2, on=["key"], how="right")
In [54]: right_join
Out[54]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
3 E NaN -1.044236
In [55]: outer_join = df1.merge(df2, on=["key"], how="outer")
In [56]: outer_join
Out[56]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E NaN -1.044236
```

`merge`

has a number of advantages over `VLOOKUP`

:

The lookup value doesn’t need to be the first column of the lookup table

If multiple rows are matched, there will be one row for each match, instead of just the first

It will include all columns from the lookup table, instead of just a single specified column

It supports more complex join operations

## Other considerations#

### Fill Handle#

Create a series of numbers following a set pattern in a certain set of cells. In a spreadsheet, this would be done by shift+drag after entering the first number or by entering the first two or three values and then dragging.

This can be achieved by creating a series and assigning it to the desired cells.

```
In [57]: df = pd.DataFrame({"AAA": [1] * 8, "BBB": list(range(0, 8))})
In [58]: df
Out[58]:
AAA BBB
0 1 0
1 1 1
2 1 2
3 1 3
4 1 4
5 1 5
6 1 6
7 1 7
In [59]: series = list(range(1, 5))
In [60]: series
Out[60]: [1, 2, 3, 4]
In [61]: df.loc[2:5, "AAA"] = series
In [62]: df
Out[62]:
AAA BBB
0 1 0
1 1 1
2 1 2
3 2 3
4 3 4
5 4 5
6 1 6
7 1 7
```

### Drop Duplicates#

Excel has built-in functionality for removing duplicate values.
This is supported in pandas via `drop_duplicates()`

.

```
In [63]: df = pd.DataFrame(
....: {
....: "class": ["A", "A", "A", "B", "C", "D"],
....: "student_count": [42, 35, 42, 50, 47, 45],
....: "all_pass": ["Yes", "Yes", "Yes", "No", "No", "Yes"],
....: }
....: )
....:
In [64]: df.drop_duplicates()
Out[64]:
class student_count all_pass
0 A 42 Yes
1 A 35 Yes
3 B 50 No
4 C 47 No
5 D 45 Yes
In [65]: df.drop_duplicates(["class", "student_count"])
Out[65]:
class student_count all_pass
0 A 42 Yes
1 A 35 Yes
3 B 50 No
4 C 47 No
5 D 45 Yes
```

### Pivot Tables#

PivotTables
from spreadsheets can be replicated in pandas through Reshaping and pivot tables. Using the `tips`

dataset again,
let’s find the average gratuity by size of the party and sex of the server.

In Excel, we use the following configuration for the PivotTable:

The equivalent in pandas:

```
In [66]: pd.pivot_table(
....: tips, values="tip", index=["size"], columns=["sex"], aggfunc=np.average
....: )
....:
Out[66]:
sex Female Male
size
1 1.276667 1.920000
2 2.528448 2.614184
3 3.250000 3.476667
4 4.021111 4.172143
5 5.140000 3.750000
6 4.600000 5.850000
```

### Adding a row#

Assuming we are using a `RangeIndex`

(numbered `0`

, `1`

, etc.), we can use `concat()`

to add a row to the bottom of a `DataFrame`

.

```
In [67]: df
Out[67]:
class student_count all_pass
0 A 42 Yes
1 A 35 Yes
2 A 42 Yes
3 B 50 No
4 C 47 No
5 D 45 Yes
In [68]: new_row = pd.DataFrame([["E", 51, True]],
....: columns=["class", "student_count", "all_pass"])
....:
In [69]: pd.concat([df, new_row])
Out[69]:
class student_count all_pass
0 A 42 Yes
1 A 35 Yes
2 A 42 Yes
3 B 50 No
4 C 47 No
5 D 45 Yes
0 E 51 True
```

### Find and Replace#

Excel’s Find dialog
takes you to cells that match, one by one. In pandas, this operation is generally done for an
entire column or `DataFrame`

at once through conditional expressions.

```
In [70]: tips
Out[70]:
total_bill tip sex smoker day time size
67 1.07 1.00 Female Yes Sat Dinner 1
92 3.75 1.00 Female Yes Fri Dinner 2
111 5.25 1.00 Female No Sat Dinner 1
145 6.35 1.50 Female No Thur Lunch 2
135 6.51 1.25 Female No Thur Lunch 2
.. ... ... ... ... ... ... ...
182 43.35 3.50 Male Yes Sun Dinner 3
156 46.17 5.00 Male No Sun Dinner 6
59 46.27 6.73 Male No Sat Dinner 4
212 46.33 9.00 Male No Sat Dinner 4
170 48.81 10.00 Male Yes Sat Dinner 3
[244 rows x 7 columns]
In [71]: tips == "Sun"
Out[71]:
total_bill tip sex smoker day time size
67 False False False False False False False
92 False False False False False False False
111 False False False False False False False
145 False False False False False False False
135 False False False False False False False
.. ... ... ... ... ... ... ...
182 False False False False True False False
156 False False False False True False False
59 False False False False False False False
212 False False False False False False False
170 False False False False False False False
[244 rows x 7 columns]
In [72]: tips["day"].str.contains("S")
Out[72]:
67 True
92 False
111 True
145 False
135 False
...
182 True
156 True
59 True
212 True
170 True
Name: day, Length: 244, dtype: bool
```

pandas’ `replace()`

is comparable to Excel’s `Replace All`

.

```
In [73]: tips.replace("Thu", "Thursday")
Out[73]:
total_bill tip sex smoker day time size
67 1.07 1.00 Female Yes Sat Dinner 1
92 3.75 1.00 Female Yes Fri Dinner 2
111 5.25 1.00 Female No Sat Dinner 1
145 6.35 1.50 Female No Thur Lunch 2
135 6.51 1.25 Female No Thur Lunch 2
.. ... ... ... ... ... ... ...
182 43.35 3.50 Male Yes Sun Dinner 3
156 46.17 5.00 Male No Sun Dinner 6
59 46.27 6.73 Male No Sat Dinner 4
212 46.33 9.00 Male No Sat Dinner 4
170 48.81 10.00 Male Yes Sat Dinner 3
[244 rows x 7 columns]
```

## Source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html

# Comparison with SAS#

For potential users coming from SAS this page is meant to demonstrate how different SAS operations would be performed in pandas.

If you’re new to pandas, you might want to first read through 10 Minutes to pandas to familiarize yourself with the library.

As is customary, we import pandas and NumPy as follows:

```
In [1]: import pandas as pd
In [2]: import numpy as np
```

## Data structures#

### General terminology translation#

pandas |
SAS |
|---|---|
|
data set |
column |
variable |
row |
observation |
groupby |
BY-group |
|
|

`DataFrame`

#

A `DataFrame`

in pandas is analogous to a SAS data set - a two-dimensional
data source with labeled columns that can be of different types. As will be
shown in this document, almost any operation that can be applied to a data set
using SAS’s `DATA`

step, can also be accomplished in pandas.

`Series`

#

A `Series`

is the data structure that represents one column of a
`DataFrame`

. SAS doesn’t have a separate data structure for a single column,
but in general, working with a `Series`

is analogous to referencing a column
in the `DATA`

step.

`Index`

#

Every `DataFrame`

and `Series`

has an `Index`

- which are labels on the
*rows* of the data. SAS does not have an exactly analogous concept. A data set’s
rows are essentially unlabeled, other than an implicit integer index that can be
accessed during the `DATA`

step (`_N_`

).

In pandas, if no index is specified, an integer index is also used by default
(first row = 0, second row = 1, and so on). While using a labeled `Index`

or
`MultiIndex`

can enable sophisticated analyses and is ultimately an important
part of pandas to understand, for this comparison we will essentially ignore the
`Index`

and just treat the `DataFrame`

as a collection of columns. Please
see the indexing documentation for much more on how to use an
`Index`

effectively.

### Copies vs. in place operations#

Most pandas operations return copies of the `Series`

/`DataFrame`

. To make the changes “stick”,
you’ll need to either assign to a new variable:

sorted_df = df.sort_values("col1")

or overwrite the original one:

df = df.sort_values("col1")

Note

You will see an `inplace=True`

or `copy=False`

keyword argument available for
some methods:

```
df.replace(5, inplace=True)
```

There is an active discussion about deprecating and removing `inplace`

and `copy`

for
most methods (e.g. `dropna`

) except for a very small subset of methods
(including `replace`

). Both keywords won’t be
necessary anymore in the context of Copy-on-Write. The proposal can be found
here.

## Data input / output#

### Constructing a DataFrame from values#

A SAS data set can be built from specified values by
placing the data after a `datalines`

statement and
specifying the column names.

```
data df;
input x y;
datalines;
1 2
3 4
5 6
;
run;
```

A pandas `DataFrame`

can be constructed in many different ways,
but for a small number of values, it is often convenient to specify it as
a Python dictionary, where the keys are the column names
and the values are the data.

```
In [1]: df = pd.DataFrame({"x": [1, 3, 5], "y": [2, 4, 6]})
In [2]: df
Out[2]:
x y
0 1 2
1 3 4
2 5 6
```

### Reading external data#

Like SAS, pandas provides utilities for reading in data from
many formats. The `tips`

dataset, found within the pandas
tests (csv)
will be used in many of the following examples.

SAS provides `PROC IMPORT`

to read csv data into a data set.

```
proc import datafile='tips.csv' dbms=csv out=tips replace;
getnames=yes;
run;
```

The pandas method is `read_csv()`

, which works similarly.

```
In [3]: url = (
...: "https://raw.githubusercontent.com/pandas-dev/"
...: "pandas/main/pandas/tests/io/data/csv/tips.csv"
...: )
...:
In [4]: tips = pd.read_csv(url)
In [5]: tips
Out[5]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 29.03 5.92 Male No Sat Dinner 3
240 27.18 2.00 Female Yes Sat Dinner 2
241 22.67 2.00 Male Yes Sat Dinner 2
242 17.82 1.75 Male No Sat Dinner 2
243 18.78 3.00 Female No Thur Dinner 2
[244 rows x 7 columns]
```

Like `PROC IMPORT`

, `read_csv`

can take a number of parameters to specify
how the data should be parsed. For example, if the data was instead tab delimited,
and did not have column names, the pandas command would be:

```
tips = pd.read_csv("tips.csv", sep="\t", header=None)
# alternatively, read_table is an alias to read_csv with tab delimiter
tips = pd.read_table("tips.csv", header=None)
```

In addition to text/csv, pandas supports a variety of other data formats
such as Excel, HDF5, and SQL databases. These are all read via a `pd.read_*`

function. See the IO documentation for more details.

### Limiting output#

By default, pandas will truncate output of large `DataFrame`

s to show the first and last rows.
This can be overridden by changing the pandas options, or using
`DataFrame.head()`

or `DataFrame.tail()`

.

```
In [1]: tips.head(5)
Out[1]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
```

The equivalent in SAS would be:

```
proc print data=df(obs=5);
run;
```

### Exporting data#

The inverse of `PROC IMPORT`

in SAS is `PROC EXPORT`

```
proc export data=tips outfile='tips2.csv' dbms=csv;
run;
```

Similarly in pandas, the opposite of `read_csv`

is `to_csv()`

,
and other data formats follow a similar api.

```
tips.to_csv("tips2.csv")
```

## Data operations#

### Operations on columns#

In the `DATA`

step, arbitrary math expressions can
be used on new or existing columns.

```
data tips;
set tips;
total_bill = total_bill - 2;
new_bill = total_bill / 2;
run;
```

pandas provides vectorized operations by specifying the individual `Series`

in the
`DataFrame`

. New columns can be assigned in the same way. The `DataFrame.drop()`

method drops
a column from the `DataFrame`

.

```
In [1]: tips["total_bill"] = tips["total_bill"] - 2
In [2]: tips["new_bill"] = tips["total_bill"] / 2
In [3]: tips
Out[3]:
total_bill tip sex smoker day time size new_bill
0 14.99 1.01 Female No Sun Dinner 2 7.495
1 8.34 1.66 Male No Sun Dinner 3 4.170
2 19.01 3.50 Male No Sun Dinner 3 9.505
3 21.68 3.31 Male No Sun Dinner 2 10.840
4 22.59 3.61 Female No Sun Dinner 4 11.295
.. ... ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3 13.515
240 25.18 2.00 Female Yes Sat Dinner 2 12.590
241 20.67 2.00 Male Yes Sat Dinner 2 10.335
242 15.82 1.75 Male No Sat Dinner 2 7.910
243 16.78 3.00 Female No Thur Dinner 2 8.390
[244 rows x 8 columns]
In [4]: tips = tips.drop("new_bill", axis=1)
```

### Filtering#

Filtering in SAS is done with an `if`

or `where`

statement, on one
or more columns.

```
data tips;
set tips;
if total_bill > 10;
run;
data tips;
set tips;
where total_bill > 10;
/* equivalent in this case - where happens before the
DATA step begins and can also be used in PROC statements */
run;
```

DataFrames can be filtered in multiple ways; the most intuitive of which is using boolean indexing.

```
In [1]: tips[tips["total_bill"] > 10]
Out[1]:
total_bill tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
5 23.29 4.71 Male No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[204 rows x 7 columns]
```

The above statement is simply passing a `Series`

of `True`

/`False`

objects to the DataFrame,
returning all rows with `True`

.

```
In [2]: is_dinner = tips["time"] == "Dinner"
In [3]: is_dinner
Out[3]:
0 True
1 True
2 True
3 True
4 True
...
239 True
240 True
241 True
242 True
243 True
Name: time, Length: 244, dtype: bool
In [4]: is_dinner.value_counts()
Out[4]:
time
True 176
False 68
Name: count, dtype: int64
In [5]: tips[is_dinner]
Out[5]:
total_bill tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
1 8.34 1.66 Male No Sun Dinner 3
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[176 rows x 7 columns]
```

### If/then logic#

In SAS, if/then logic can be used to create new columns.

```
data tips;
set tips;
format bucket $4.;
if total_bill < 10 then bucket = 'low';
else bucket = 'high';
run;
```

The same operation in pandas can be accomplished using
the `where`

method from `numpy`

.

```
In [1]: tips["bucket"] = np.where(tips["total_bill"] < 10, "low", "high")
In [2]: tips
Out[2]:
total_bill tip sex smoker day time size bucket
0 14.99 1.01 Female No Sun Dinner 2 high
1 8.34 1.66 Male No Sun Dinner 3 low
2 19.01 3.50 Male No Sun Dinner 3 high
3 21.68 3.31 Male No Sun Dinner 2 high
4 22.59 3.61 Female No Sun Dinner 4 high
.. ... ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3 high
240 25.18 2.00 Female Yes Sat Dinner 2 high
241 20.67 2.00 Male Yes Sat Dinner 2 high
242 15.82 1.75 Male No Sat Dinner 2 high
243 16.78 3.00 Female No Thur Dinner 2 high
[244 rows x 8 columns]
```

### Date functionality#

SAS provides a variety of functions to do operations on date/datetime columns.

```
data tips;
set tips;
format date1 date2 date1_plusmonth mmddyy10.;
date1 = mdy(1, 15, 2013);
date2 = mdy(2, 15, 2015);
date1_year = year(date1);
date2_month = month(date2);
* shift date to beginning of next interval;
date1_next = intnx('MONTH', date1, 1);
* count intervals between dates;
months_between = intck('MONTH', date1, date2);
run;
```

The equivalent pandas operations are shown below. In addition to these functions pandas supports other Time Series features not available in Base SAS (such as resampling and custom offsets) - see the timeseries documentation for more details.

```
In [1]: tips["date1"] = pd.Timestamp("2013-01-15")
In [2]: tips["date2"] = pd.Timestamp("2015-02-15")
In [3]: tips["date1_year"] = tips["date1"].dt.year
In [4]: tips["date2_month"] = tips["date2"].dt.month
In [5]: tips["date1_next"] = tips["date1"] + pd.offsets.MonthBegin()
In [6]: tips["months_between"] = tips["date2"].dt.to_period("M") - tips[
...: "date1"
...: ].dt.to_period("M")
...:
In [7]: tips[
...: ["date1", "date2", "date1_year", "date2_month", "date1_next", "months_between"]
...: ]
...:
Out[7]:
date1 date2 date1_year date2_month date1_next months_between
0 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
1 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
2 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
3 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
4 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
.. ... ... ... ... ... ...
239 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
240 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
241 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
242 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
243 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
[244 rows x 6 columns]
```

### Selection of columns#

SAS provides keywords in the `DATA`

step to select,
drop, and rename columns.

```
data tips;
set tips;
keep sex total_bill tip;
run;
data tips;
set tips;
drop sex;
run;
data tips;
set tips;
rename total_bill=total_bill_2;
run;
```

The same operations are expressed in pandas below.

#### Keep certain columns#

```
In [1]: tips[["sex", "total_bill", "tip"]]
Out[1]:
sex total_bill tip
0 Female 14.99 1.01
1 Male 8.34 1.66
2 Male 19.01 3.50
3 Male 21.68 3.31
4 Female 22.59 3.61
.. ... ... ...
239 Male 27.03 5.92
240 Female 25.18 2.00
241 Male 20.67 2.00
242 Male 15.82 1.75
243 Female 16.78 3.00
[244 rows x 3 columns]
```

#### Drop a column#

```
In [2]: tips.drop("sex", axis=1)
Out[2]:
total_bill tip smoker day time size
0 14.99 1.01 No Sun Dinner 2
1 8.34 1.66 No Sun Dinner 3
2 19.01 3.50 No Sun Dinner 3
3 21.68 3.31 No Sun Dinner 2
4 22.59 3.61 No Sun Dinner 4
.. ... ... ... ... ... ...
239 27.03 5.92 No Sat Dinner 3
240 25.18 2.00 Yes Sat Dinner 2
241 20.67 2.00 Yes Sat Dinner 2
242 15.82 1.75 No Sat Dinner 2
243 16.78 3.00 No Thur Dinner 2
[244 rows x 6 columns]
```

#### Rename a column#

```
In [3]: tips.rename(columns={"total_bill": "total_bill_2"})
Out[3]:
total_bill_2 tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
1 8.34 1.66 Male No Sun Dinner 3
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[244 rows x 7 columns]
```

### Sorting by values#

Sorting in SAS is accomplished via `PROC SORT`

```
proc sort data=tips;
by sex total_bill;
run;
```

pandas has a `DataFrame.sort_values()`

method, which takes a list of columns to sort by.

```
In [1]: tips = tips.sort_values(["sex", "total_bill"])
In [2]: tips
Out[2]:
total_bill tip sex smoker day time size
67 1.07 1.00 Female Yes Sat Dinner 1
92 3.75 1.00 Female Yes Fri Dinner 2
111 5.25 1.00 Female No Sat Dinner 1
145 6.35 1.50 Female No Thur Lunch 2
135 6.51 1.25 Female No Thur Lunch 2
.. ... ... ... ... ... ... ...
182 43.35 3.50 Male Yes Sun Dinner 3
156 46.17 5.00 Male No Sun Dinner 6
59 46.27 6.73 Male No Sat Dinner 4
212 46.33 9.00 Male No Sat Dinner 4
170 48.81 10.00 Male Yes Sat Dinner 3
[244 rows x 7 columns]
```

## String processing#

### Finding length of string#

SAS determines the length of a character string with the
LENGTHN
and LENGTHC
functions. `LENGTHN`

excludes trailing blanks and `LENGTHC`

includes trailing blanks.

```
data _null_;
set tips;
put(LENGTHN(time));
put(LENGTHC(time));
run;
```

You can find the length of a character string with `Series.str.len()`

.
In Python 3, all strings are Unicode strings. `len`

includes trailing blanks.
Use `len`

and `rstrip`

to exclude trailing blanks.

```
In [1]: tips["time"].str.len()
Out[1]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
In [2]: tips["time"].str.rstrip().str.len()
Out[2]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
```

### Finding position of substring#

SAS determines the position of a character in a string with the
FINDW function.
`FINDW`

takes the string defined by the first argument and searches for the first position of the substring
you supply as the second argument.

```
data _null_;
set tips;
put(FINDW(sex,'ale'));
run;
```

You can find the position of a character in a column of strings with the `Series.str.find()`

method. `find`

searches for the first position of the substring. If the substring is found, the
method returns its position. If not found, it returns `-1`

. Keep in mind that Python indexes are
zero-based.

```
In [1]: tips["sex"].str.find("ale")
Out[1]:
67 3
92 3
111 3
145 3
135 3
..
182 1
156 1
59 1
212 1
170 1
Name: sex, Length: 244, dtype: int64
```

### Extracting substring by position#

SAS extracts a substring from a string based on its position with the SUBSTR function.

```
data _null_;
set tips;
put(substr(sex,1,1));
run;
```

With pandas you can use `[]`

notation to extract a substring
from a string by position locations. Keep in mind that Python
indexes are zero-based.

```
In [1]: tips["sex"].str[0:1]
Out[1]:
67 F
92 F
111 F
145 F
135 F
..
182 M
156 M
59 M
212 M
170 M
Name: sex, Length: 244, dtype: str
```

### Extracting nth word#

The SAS SCAN function returns the nth word from a string. The first argument is the string you want to parse and the second argument specifies which word you want to extract.

```
data firstlast;
input String $60.;
First_Name = scan(string, 1);
Last_Name = scan(string, -1);
datalines2;
John Smith;
Jane Cook;
;;;
run;
```

The simplest way to extract words in pandas is to split the strings by spaces, then reference the word by index. Note there are more powerful approaches should you need them.

```
In [1]: firstlast = pd.DataFrame({"String": ["John Smith", "Jane Cook"]})
In [2]: firstlast["First_Name"] = firstlast["String"].str.split(" ", expand=True)[0]
In [3]: firstlast["Last_Name"] = firstlast["String"].str.rsplit(" ", expand=True)[1]
In [4]: firstlast
Out[4]:
String First_Name Last_Name
0 John Smith John Smith
1 Jane Cook Jane Cook
```

### Changing case#

The SAS UPCASE LOWCASE and PROPCASE functions change the case of the argument.

```
data firstlast;
input String $60.;
string_up = UPCASE(string);
string_low = LOWCASE(string);
string_prop = PROPCASE(string);
datalines2;
John Smith;
Jane Cook;
;;;
run;
```

The equivalent pandas methods are `Series.str.upper()`

, `Series.str.lower()`

, and
`Series.str.title()`

.

```
In [1]: firstlast = pd.DataFrame({"string": ["John Smith", "Jane Cook"]})
In [2]: firstlast["upper"] = firstlast["string"].str.upper()
In [3]: firstlast["lower"] = firstlast["string"].str.lower()
In [4]: firstlast["title"] = firstlast["string"].str.title()
In [5]: firstlast
Out[5]:
string upper lower title
0 John Smith JOHN SMITH john smith John Smith
1 Jane Cook JANE COOK jane cook Jane Cook
```

## Merging#

The following tables will be used in the merge examples:

```
In [1]: df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
In [2]: df1
Out[2]:
key value
0 A 0.469112
1 B -0.282863
2 C -1.509059
3 D -1.135632
In [3]: df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})
In [4]: df2
Out[4]:
key value
0 B 1.212112
1 D -0.173215
2 D 0.119209
3 E -1.044236
```

In SAS, data must be explicitly sorted before merging. Different
types of joins are accomplished using the `in=`

dummy
variables to track whether a match was found in one or both
input frames.

```
proc sort data=df1;
by key;
run;
proc sort data=df2;
by key;
run;
data left_join inner_join right_join outer_join;
merge df1(in=a) df2(in=b);
if a and b then output inner_join;
if a then output left_join;
if b then output right_join;
if a or b then output outer_join;
run;
```

pandas DataFrames have a `merge()`

method, which provides similar functionality. The
data does not have to be sorted ahead of time, and different join types are accomplished via the
`how`

keyword.

```
In [1]: inner_join = df1.merge(df2, on=["key"], how="inner")
In [2]: inner_join
Out[2]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
In [3]: left_join = df1.merge(df2, on=["key"], how="left")
In [4]: left_join
Out[4]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
In [5]: right_join = df1.merge(df2, on=["key"], how="right")
In [6]: right_join
Out[6]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
3 E NaN -1.044236
In [7]: outer_join = df1.merge(df2, on=["key"], how="outer")
In [8]: outer_join
Out[8]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E NaN -1.044236
```

## Missing data#

Both pandas and SAS have a representation for missing data.

pandas represents missing data with the special float value `NaN`

(not a number). Many of the
semantics are the same; for example missing data propagates through numeric operations, and is
ignored by default for aggregations.

```
In [1]: outer_join
Out[1]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E NaN -1.044236
In [2]: outer_join["value_x"] + outer_join["value_y"]
Out[2]:
0 NaN
1 0.929249
2 NaN
3 -1.308847
4 -1.016424
5 NaN
dtype: float64
In [3]: outer_join["value_x"].sum()
Out[3]: np.float64(-3.5940742896293765)
```

One difference is that missing data cannot be compared to its sentinel value. For example, in SAS you could do this to filter missing values.

```
data outer_join_nulls;
set outer_join;
if value_x = .;
run;
data outer_join_no_nulls;
set outer_join;
if value_x ^= .;
run;
```

In pandas, `Series.isna()`

and `Series.notna()`

can be used to filter the rows.

```
In [1]: outer_join[outer_join["value_x"].isna()]
Out[1]:
key value_x value_y
5 E NaN -1.044236
In [2]: outer_join[outer_join["value_x"].notna()]
Out[2]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
```

pandas provides a variety of methods to work with missing data. Here are some examples:

### Drop rows with missing values#

```
In [3]: outer_join.dropna()
Out[3]:
key value_x value_y
1 B -0.282863 1.212112
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
```

### Forward fill from previous rows#

```
In [4]: outer_join.ffill()
Out[4]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 1.212112
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E -1.135632 -1.044236
```

### Replace missing values with a specified value#

Using the mean:

```
In [5]: outer_join["value_x"].fillna(outer_join["value_x"].mean())
Out[5]:
0 0.469112
1 -0.282863
2 -1.509059
3 -1.135632
4 -1.135632
5 -0.718815
Name: value_x, dtype: float64
```

## GroupBy#

### Aggregation#

SAS’s `PROC SUMMARY`

can be used to group by one or
more key variables and compute aggregations on
numeric columns.

```
proc summary data=tips nway;
class sex smoker;
var total_bill tip;
output out=tips_summed sum=;
run;
```

pandas provides a flexible `groupby`

mechanism that allows similar aggregations. See the
groupby documentation for more details and examples.

```
In [1]: tips_summed = tips.groupby(["sex", "smoker"])[["total_bill", "tip"]].sum()
In [2]: tips_summed
Out[2]:
total_bill tip
sex smoker
Female No 869.68 149.77
Yes 527.27 96.74
Male No 1725.75 302.00
Yes 1217.07 183.07
```

### Transformation#

In SAS, if the group aggregations need to be used with the original frame, it must be merged back together. For example, to subtract the mean for each observation by smoker group.

```
proc summary data=tips missing nway;
class smoker;
var total_bill;
output out=smoker_means mean(total_bill)=group_bill;
run;
proc sort data=tips;
by smoker;
run;
data tips;
merge tips(in=a) smoker_means(in=b);
by smoker;
adj_total_bill = total_bill - group_bill;
if a and b;
run;
```

pandas provides a Transformation mechanism that allows these type of operations to be succinctly expressed in one operation.

```
In [1]: gb = tips.groupby("smoker")["total_bill"]
In [2]: tips["adj_total_bill"] = tips["total_bill"] - gb.transform("mean")
In [3]: tips
Out[3]:
total_bill tip sex smoker day time size adj_total_bill
67 1.07 1.00 Female Yes Sat Dinner 1 -17.686344
92 3.75 1.00 Female Yes Fri Dinner 2 -15.006344
111 5.25 1.00 Female No Sat Dinner 1 -11.938278
145 6.35 1.50 Female No Thur Lunch 2 -10.838278
135 6.51 1.25 Female No Thur Lunch 2 -10.678278
.. ... ... ... ... ... ... ... ...
182 43.35 3.50 Male Yes Sun Dinner 3 24.593656
156 46.17 5.00 Male No Sun Dinner 6 28.981722
59 46.27 6.73 Male No Sat Dinner 4 29.081722
212 46.33 9.00 Male No Sat Dinner 4 29.141722
170 48.81 10.00 Male Yes Sat Dinner 3 30.053656
[244 rows x 8 columns]
```

### By group processing#

In addition to aggregation, pandas `groupby`

can be used to
replicate most other by group processing from SAS. For example,
this `DATA`

step reads the data by sex/smoker group and filters to
the first entry for each.

```
proc sort data=tips;
by sex smoker;
run;
data tips_first;
set tips;
by sex smoker;
if FIRST.sex or FIRST.smoker then output;
run;
```

In pandas this would be written as:

```
In [4]: tips.groupby(["sex", "smoker"]).first()
Out[4]:
total_bill tip day time size adj_total_bill
sex smoker
Female No 5.25 1.00 Sat Dinner 1 -11.938278
Yes 1.07 1.00 Sat Dinner 1 -17.686344
Male No 5.51 2.00 Thur Lunch 2 -11.678278
Yes 5.25 5.15 Sun Dinner 2 -13.506344
```

## Other considerations#

### Disk vs memory#

pandas operates exclusively in memory, where a SAS data set exists on disk. This means that the size of data able to be loaded in pandas is limited by your machine’s memory, but also that the operations on that data may be faster.

If out of core processing is needed, one possibility is the
dask.dataframe
library (currently in development) which
provides a subset of pandas functionality for an on-disk `DataFrame`

### Data interop#

pandas provides a `read_sas()`

method that can read SAS data saved in
the XPORT or SAS7BDAT binary format.

```
libname xportout xport 'transport-file.xpt';
data xportout.tips;
set tips(rename=(total_bill=tbill));
* xport variable names limited to 6 characters;
run;
```

```
df = pd.read_sas("transport-file.xpt")
df = pd.read_sas("binary-file.sas7bdat")
```

You can also specify the file format directly. By default, pandas will try to infer the file format based on its extension.

```
df = pd.read_sas("transport-file.xpt", format="xport")
df = pd.read_sas("binary-file.sas7bdat", format="sas7bdat")
```

XPORT is a relatively limited format and the parsing of it is not as optimized as some of the other pandas readers. An alternative way to interop data between SAS and pandas is to serialize to csv.

```
# version 0.17, 10M rows
In [8]: %time df = pd.read_sas('big.xpt')
Wall time: 14.6 s
In [9]: %time df = pd.read_csv('big.csv')
Wall time: 4.86 s
```

## Source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_stata.html

# Comparison with Stata#

For potential users coming from Stata this page is meant to demonstrate how different Stata operations would be performed in pandas.

As is customary, we import pandas and NumPy as follows:

```
In [1]: import pandas as pd
In [2]: import numpy as np
```

## Data structures#

### General terminology translation#

pandas |
Stata |
|---|---|
|
data set |
column |
variable |
row |
observation |
groupby |
bysort |
|
|

`DataFrame`

#

A `DataFrame`

in pandas is analogous to a Stata data set – a two-dimensional
data source with labeled columns that can be of different types. As will be
shown in this document, almost any operation that can be applied to a data set
in Stata can also be accomplished in pandas.

`Series`

#

A `Series`

is the data structure that represents one column of a
`DataFrame`

. Stata doesn’t have a separate data structure for a single column,
but in general, working with a `Series`

is analogous to referencing a column
of a data set in Stata.

`Index`

#

Every `DataFrame`

and `Series`

has an `Index`

– labels on the
*rows* of the data. Stata does not have an exactly analogous concept. In Stata, a data set’s
rows are essentially unlabeled, other than an implicit integer index that can be
accessed with `_n`

.

In pandas, if no index is specified, an integer index is also used by default
(first row = 0, second row = 1, and so on). While using a labeled `Index`

or
`MultiIndex`

can enable sophisticated analyses and is ultimately an important
part of pandas to understand, for this comparison we will essentially ignore the
`Index`

and just treat the `DataFrame`

as a collection of columns. Please
see the indexing documentation for much more on how to use an
`Index`

effectively.

### Copies vs. in place operations#

`Series`

/`DataFrame`

. To make the changes “stick”,
you’ll need to either assign to a new variable:

sorted_df = df.sort_values("col1")

or overwrite the original one:

df = df.sort_values("col1")

Note

You will see an `inplace=True`

or `copy=False`

keyword argument available for
some methods:

```
df.replace(5, inplace=True)
```

`inplace`

and `copy`

for
most methods (e.g. `dropna`

) except for a very small subset of methods
(including `replace`

). Both keywords won’t be
necessary anymore in the context of Copy-on-Write. The proposal can be found
here.

## Data input / output#

### Constructing a DataFrame from values#

A Stata data set can be built from specified values by
placing the data after an `input`

statement and
specifying the column names.

```
input x y
1 2
3 4
5 6
end
```

A pandas `DataFrame`

can be constructed in many different ways,
but for a small number of values, it is often convenient to specify it as
a Python dictionary, where the keys are the column names
and the values are the data.

```
In [3]: df = pd.DataFrame({"x": [1, 3, 5], "y": [2, 4, 6]})
In [4]: df
Out[4]:
x y
0 1 2
1 3 4
2 5 6
```

### Reading external data#

Like Stata, pandas provides utilities for reading in data from
many formats. The `tips`

data set, found within the pandas
tests (csv)
will be used in many of the following examples.

Stata provides `import delimited`

to read csv data into a data set in memory.
If the `tips.csv`

file is in the current working directory, we can import it as follows.

```
import delimited tips.csv
```

The pandas method is `read_csv()`

, which works similarly. Additionally, it will automatically download
the data set if presented with a url.

```
In [5]: url = (
...: "https://raw.githubusercontent.com/pandas-dev"
...: "/pandas/main/pandas/tests/io/data/csv/tips.csv"
...: )
...:
In [6]: tips = pd.read_csv(url)
In [7]: tips
Out[7]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 29.03 5.92 Male No Sat Dinner 3
240 27.18 2.00 Female Yes Sat Dinner 2
241 22.67 2.00 Male Yes Sat Dinner 2
242 17.82 1.75 Male No Sat Dinner 2
243 18.78 3.00 Female No Thur Dinner 2
[244 rows x 7 columns]
```

Like `import delimited`

, `read_csv()`

can take a number of parameters to specify
how the data should be parsed. For example, if the data were instead tab delimited,
did not have column names, and existed in the current working directory,
the pandas command would be:

```
tips = pd.read_csv("tips.csv", sep="\t", header=None)
# alternatively, read_table is an alias to read_csv with tab delimiter
tips = pd.read_table("tips.csv", header=None)
```

pandas can also read Stata data sets in `.dta`

format with the `read_stata()`

function.

```
df = pd.read_stata("data.dta")
```

In addition to text/csv and Stata files, pandas supports a variety of other data formats
such as Excel, SAS, HDF5, Parquet, and SQL databases. These are all read via a `pd.read_*`

function. See the IO documentation for more details.

### Limiting output#

By default, pandas will truncate output of large `DataFrame`

s to show the first and last rows.
This can be overridden by changing the pandas options, or using
`DataFrame.head()`

or `DataFrame.tail()`

.

```
In [8]: tips.head(5)
Out[8]:
total_bill tip sex smoker day time size
0 16.99 1.01 Female No Sun Dinner 2
1 10.34 1.66 Male No Sun Dinner 3
2 21.01 3.50 Male No Sun Dinner 3
3 23.68 3.31 Male No Sun Dinner 2
4 24.59 3.61 Female No Sun Dinner 4
```

The equivalent in Stata would be:

```
list in 1/5
```

### Exporting data#

The inverse of `import delimited`

in Stata is `export delimited`

```
export delimited tips2.csv
```

Similarly in pandas, the opposite of `read_csv`

is `DataFrame.to_csv()`

.

```
tips.to_csv("tips2.csv")
```

pandas can also export to Stata file format with the `DataFrame.to_stata()`

method.

```
tips.to_stata("tips2.dta")
```

## Data operations#

### Operations on columns#

In Stata, arbitrary math expressions can be used with the `generate`

and
`replace`

commands on new or existing columns. The `drop`

command drops
the column from the data set.

```
replace total_bill = total_bill - 2
generate new_bill = total_bill / 2
drop new_bill
```

pandas provides vectorized operations by specifying the individual `Series`

in the
`DataFrame`

. New columns can be assigned in the same way. The `DataFrame.drop()`

method drops
a column from the `DataFrame`

.

```
In [9]: tips["total_bill"] = tips["total_bill"] - 2
In [10]: tips["new_bill"] = tips["total_bill"] / 2
In [11]: tips
Out[11]:
total_bill tip sex smoker day time size new_bill
0 14.99 1.01 Female No Sun Dinner 2 7.495
1 8.34 1.66 Male No Sun Dinner 3 4.170
2 19.01 3.50 Male No Sun Dinner 3 9.505
3 21.68 3.31 Male No Sun Dinner 2 10.840
4 22.59 3.61 Female No Sun Dinner 4 11.295
.. ... ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3 13.515
240 25.18 2.00 Female Yes Sat Dinner 2 12.590
241 20.67 2.00 Male Yes Sat Dinner 2 10.335
242 15.82 1.75 Male No Sat Dinner 2 7.910
243 16.78 3.00 Female No Thur Dinner 2 8.390
[244 rows x 8 columns]
In [12]: tips = tips.drop("new_bill", axis=1)
```

### Filtering#

Filtering in Stata is done with an `if`

clause on one or more columns.

```
list if total_bill > 10
```

DataFrames can be filtered in multiple ways; the most intuitive of which is using boolean indexing.

```
In [13]: tips[tips["total_bill"] > 10]
Out[13]:
total_bill tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
5 23.29 4.71 Male No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[204 rows x 7 columns]
```

`Series`

of `True`

/`False`

objects to the DataFrame,
returning all rows with `True`

.

```
In [14]: is_dinner = tips["time"] == "Dinner"
In [15]: is_dinner
Out[15]:
0 True
1 True
2 True
3 True
4 True
...
239 True
240 True
241 True
242 True
243 True
Name: time, Length: 244, dtype: bool
In [16]: is_dinner.value_counts()
Out[16]:
time
True 176
False 68
Name: count, dtype: int64
In [17]: tips[is_dinner]
Out[17]:
total_bill tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
1 8.34 1.66 Male No Sun Dinner 3
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[176 rows x 7 columns]
```

### If/then logic#

In Stata, an `if`

clause can also be used to create new columns.

```
generate bucket = "low" if total_bill < 10
replace bucket = "high" if total_bill >= 10
```

The same operation in pandas can be accomplished using
the `where`

method from `numpy`

.

```
In [18]: tips["bucket"] = np.where(tips["total_bill"] < 10, "low", "high")
In [19]: tips
Out[19]:
total_bill tip sex smoker day time size bucket
0 14.99 1.01 Female No Sun Dinner 2 high
1 8.34 1.66 Male No Sun Dinner 3 low
2 19.01 3.50 Male No Sun Dinner 3 high
3 21.68 3.31 Male No Sun Dinner 2 high
4 22.59 3.61 Female No Sun Dinner 4 high
.. ... ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3 high
240 25.18 2.00 Female Yes Sat Dinner 2 high
241 20.67 2.00 Male Yes Sat Dinner 2 high
242 15.82 1.75 Male No Sat Dinner 2 high
243 16.78 3.00 Female No Thur Dinner 2 high
[244 rows x 8 columns]
```

### Date functionality#

Stata provides a variety of functions to do operations on date/datetime columns.

```
generate date1 = mdy(1, 15, 2013)
generate date2 = date("Feb152015", "MDY")
generate date1_year = year(date1)
generate date2_month = month(date2)
* shift date to beginning of next month
generate date1_next = mdy(month(date1) + 1, 1, year(date1)) if month(date1) != 12
replace date1_next = mdy(1, 1, year(date1) + 1) if month(date1) == 12
generate months_between = mofd(date2) - mofd(date1)
list date1 date2 date1_year date2_month date1_next months_between
```

The equivalent pandas operations are shown below. In addition to these functions, pandas supports other Time Series features not available in Stata (such as time zone handling and custom offsets) – see the timeseries documentation for more details.

```
In [20]: tips["date1"] = pd.Timestamp("2013-01-15")
In [21]: tips["date2"] = pd.Timestamp("2015-02-15")
In [22]: tips["date1_year"] = tips["date1"].dt.year
In [23]: tips["date2_month"] = tips["date2"].dt.month
In [24]: tips["date1_next"] = tips["date1"] + pd.offsets.MonthBegin()
In [25]: tips["months_between"] = tips["date2"].dt.to_period("M") - tips[
....: "date1"
....: ].dt.to_period("M")
....:
In [26]: tips[
....: ["date1", "date2", "date1_year", "date2_month", "date1_next", "months_between"]
....: ]
....:
Out[26]:
date1 date2 date1_year date2_month date1_next months_between
0 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
1 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
2 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
3 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
4 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
.. ... ... ... ... ... ...
239 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
240 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
241 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
242 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
243 2013-01-15 2015-02-15 2013 2 2013-02-01 <25 * MonthEnds>
[244 rows x 6 columns]
```

### Selection of columns#

Stata provides keywords to select, drop, and rename columns.

```
keep sex total_bill tip
drop sex
rename total_bill total_bill_2
```

The same operations are expressed in pandas below.

#### Keep certain columns#

```
In [27]: tips[["sex", "total_bill", "tip"]]
Out[27]:
sex total_bill tip
0 Female 14.99 1.01
1 Male 8.34 1.66
2 Male 19.01 3.50
3 Male 21.68 3.31
4 Female 22.59 3.61
.. ... ... ...
239 Male 27.03 5.92
240 Female 25.18 2.00
241 Male 20.67 2.00
242 Male 15.82 1.75
243 Female 16.78 3.00
[244 rows x 3 columns]
```

#### Drop a column#

```
In [28]: tips.drop("sex", axis=1)
Out[28]:
total_bill tip smoker day time size
0 14.99 1.01 No Sun Dinner 2
1 8.34 1.66 No Sun Dinner 3
2 19.01 3.50 No Sun Dinner 3
3 21.68 3.31 No Sun Dinner 2
4 22.59 3.61 No Sun Dinner 4
.. ... ... ... ... ... ...
239 27.03 5.92 No Sat Dinner 3
240 25.18 2.00 Yes Sat Dinner 2
241 20.67 2.00 Yes Sat Dinner 2
242 15.82 1.75 No Sat Dinner 2
243 16.78 3.00 No Thur Dinner 2
[244 rows x 6 columns]
```

#### Rename a column#

```
In [29]: tips.rename(columns={"total_bill": "total_bill_2"})
Out[29]:
total_bill_2 tip sex smoker day time size
0 14.99 1.01 Female No Sun Dinner 2
1 8.34 1.66 Male No Sun Dinner 3
2 19.01 3.50 Male No Sun Dinner 3
3 21.68 3.31 Male No Sun Dinner 2
4 22.59 3.61 Female No Sun Dinner 4
.. ... ... ... ... ... ... ...
239 27.03 5.92 Male No Sat Dinner 3
240 25.18 2.00 Female Yes Sat Dinner 2
241 20.67 2.00 Male Yes Sat Dinner 2
242 15.82 1.75 Male No Sat Dinner 2
243 16.78 3.00 Female No Thur Dinner 2
[244 rows x 7 columns]
```

### Sorting by values#

Sorting in Stata is accomplished via `sort`

```
sort sex total_bill
```

pandas has a `DataFrame.sort_values()`

method, which takes a list of columns to sort by.

```
In [30]: tips = tips.sort_values(["sex", "total_bill"])
In [31]: tips
Out[31]:
total_bill tip sex smoker day time size
67 1.07 1.00 Female Yes Sat Dinner 1
92 3.75 1.00 Female Yes Fri Dinner 2
111 5.25 1.00 Female No Sat Dinner 1
145 6.35 1.50 Female No Thur Lunch 2
135 6.51 1.25 Female No Thur Lunch 2
.. ... ... ... ... ... ... ...
182 43.35 3.50 Male Yes Sun Dinner 3
156 46.17 5.00 Male No Sun Dinner 6
59 46.27 6.73 Male No Sat Dinner 4
212 46.33 9.00 Male No Sat Dinner 4
170 48.81 10.00 Male Yes Sat Dinner 3
[244 rows x 7 columns]
```

## String processing#

### Finding length of string#

Stata determines the length of a character string with the `strlen()`

and
`ustrlen()`

functions for ASCII and Unicode strings, respectively.

```
generate strlen_time = strlen(time)
generate ustrlen_time = ustrlen(time)
```

You can find the length of a character string with `Series.str.len()`

.
In Python 3, all strings are Unicode strings. `len`

includes trailing blanks.
Use `len`

and `rstrip`

to exclude trailing blanks.

```
In [32]: tips["time"].str.len()
Out[32]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
In [33]: tips["time"].str.rstrip().str.len()
Out[33]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
```

### Finding position of substring#

Stata determines the position of a character in a string with the `strpos()`

function.
This takes the string defined by the first argument and searches for the
first position of the substring you supply as the second argument.

```
generate str_position = strpos(sex, "ale")
```

You can find the position of a character in a column of strings with the `Series.str.find()`

method. `find`

searches for the first position of the substring. If the substring is found, the
method returns its position. If not found, it returns `-1`

. Keep in mind that Python indexes are
zero-based.

```
In [34]: tips["sex"].str.find("ale")
Out[34]:
67 3
92 3
111 3
145 3
135 3
..
182 1
156 1
59 1
212 1
170 1
Name: sex, Length: 244, dtype: int64
```

### Extracting substring by position#

Stata extracts a substring from a string based on its position with the `substr()`

function.

```
generate short_sex = substr(sex, 1, 1)
```

With pandas you can use `[]`

notation to extract a substring
from a string by position locations. Keep in mind that Python
indexes are zero-based.

```
In [35]: tips["sex"].str[0:1]
Out[35]:
67 F
92 F
111 F
145 F
135 F
..
182 M
156 M
59 M
212 M
170 M
Name: sex, Length: 244, dtype: str
```

### Extracting nth word#

The Stata `word()`

function returns the nth word from a string.
The first argument is the string you want to parse and the
second argument specifies which word you want to extract.

```
clear
input str20 string
"John Smith"
"Jane Cook"
end
generate first_name = word(name, 1)
generate last_name = word(name, -1)
```

The simplest way to extract words in pandas is to split the strings by spaces, then reference the word by index. Note there are more powerful approaches should you need them.

```
In [36]: firstlast = pd.DataFrame({"String": ["John Smith", "Jane Cook"]})
In [37]: firstlast["First_Name"] = firstlast["String"].str.split(" ", expand=True)[0]
In [38]: firstlast["Last_Name"] = firstlast["String"].str.rsplit(" ", expand=True)[1]
In [39]: firstlast
Out[39]:
String First_Name Last_Name
0 John Smith John Smith
1 Jane Cook Jane Cook
```

### Changing case#

The Stata `strupper()`

, `strlower()`

, `strproper()`

,
`ustrupper()`

, `ustrlower()`

, and `ustrtitle()`

functions
change the case of ASCII and Unicode strings, respectively.

```
clear
input str20 string
"John Smith"
"Jane Cook"
end
generate upper = strupper(string)
generate lower = strlower(string)
generate title = strproper(string)
list
```

The equivalent pandas methods are `Series.str.upper()`

, `Series.str.lower()`

, and
`Series.str.title()`

.

```
In [40]: firstlast = pd.DataFrame({"string": ["John Smith", "Jane Cook"]})
In [41]: firstlast["upper"] = firstlast["string"].str.upper()
In [42]: firstlast["lower"] = firstlast["string"].str.lower()
In [43]: firstlast["title"] = firstlast["string"].str.title()
In [44]: firstlast
Out[44]:
string upper lower title
0 John Smith JOHN SMITH john smith John Smith
1 Jane Cook JANE COOK jane cook Jane Cook
```

## Merging#

The following tables will be used in the merge examples:

```
In [45]: df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
In [46]: df1
Out[46]:
key value
0 A 0.469112
1 B -0.282863
2 C -1.509059
3 D -1.135632
In [47]: df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})
In [48]: df2
Out[48]:
key value
0 B 1.212112
1 D -0.173215
2 D 0.119209
3 E -1.044236
```

In Stata, to perform a merge, one data set must be in memory
and the other must be referenced as a file name on disk. In
contrast, Python must have both `DataFrames`

already in memory.

By default, Stata performs an outer join, where all observations
from both data sets are left in memory after the merge. One can
keep only observations from the initial data set, the merged data set,
or the intersection of the two by using the values created in the
`_merge`

variable.

```
* First create df2 and save to disk
clear
input str1 key
B
D
D
E
end
generate value = rnormal()
save df2.dta
* Now create df1 in memory
clear
input str1 key
A
B
C
D
end
generate value = rnormal()
preserve
* Left join
merge 1:n key using df2.dta
keep if _merge == 1
* Right join
restore, preserve
merge 1:n key using df2.dta
keep if _merge == 2
* Inner join
restore, preserve
merge 1:n key using df2.dta
keep if _merge == 3
* Outer join
restore
merge 1:n key using df2.dta
```

pandas DataFrames have a `merge()`

method, which provides similar functionality. The
data does not have to be sorted ahead of time, and different join types are accomplished via the
`how`

keyword.

```
In [49]: inner_join = df1.merge(df2, on=["key"], how="inner")
In [50]: inner_join
Out[50]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
In [51]: left_join = df1.merge(df2, on=["key"], how="left")
In [52]: left_join
Out[52]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
In [53]: right_join = df1.merge(df2, on=["key"], how="right")
In [54]: right_join
Out[54]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
3 E NaN -1.044236
In [55]: outer_join = df1.merge(df2, on=["key"], how="outer")
In [56]: outer_join
Out[56]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E NaN -1.044236
```

## Missing data#

Both pandas and Stata have a representation for missing data.

pandas represents missing data with the special float value `NaN`

(not a number). Many of the
semantics are the same; for example missing data propagates through numeric operations, and is
ignored by default for aggregations.

```
In [57]: outer_join
Out[57]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E NaN -1.044236
In [58]: outer_join["value_x"] + outer_join["value_y"]
Out[58]:
0 NaN
1 0.929249
2 NaN
3 -1.308847
4 -1.016424
5 NaN
dtype: float64
In [59]: outer_join["value_x"].sum()
Out[59]: np.float64(-3.5940742896293765)
```

One difference is that missing data cannot be compared to its sentinel value. For example, in Stata you could do this to filter missing values.

```
* Keep missing values
list if value_x == .
* Keep non-missing values
list if value_x != .
```

In pandas, `Series.isna()`

and `Series.notna()`

can be used to filter the rows.

```
In [60]: outer_join[outer_join["value_x"].isna()]
Out[60]:
key value_x value_y
5 E NaN -1.044236
In [61]: outer_join[outer_join["value_x"].notna()]
Out[61]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
```

pandas provides a variety of methods to work with missing data. Here are some examples:

### Drop rows with missing values#

```
In [62]: outer_join.dropna()
Out[62]:
key value_x value_y
1 B -0.282863 1.212112
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
```

### Forward fill from previous rows#

```
In [63]: outer_join.ffill()
Out[63]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 1.212112
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E -1.135632 -1.044236
```

### Replace missing values with a specified value#

Using the mean:

```
In [64]: outer_join["value_x"].fillna(outer_join["value_x"].mean())
Out[64]:
0 0.469112
1 -0.282863
2 -1.509059
3 -1.135632
4 -1.135632
5 -0.718815
Name: value_x, dtype: float64
```

## GroupBy#

### Aggregation#

Stata’s `collapse`

can be used to group by one or
more key variables and compute aggregations on
numeric columns.

```
collapse (sum) total_bill tip, by(sex smoker)
```

pandas provides a flexible `groupby`

mechanism that allows similar aggregations. See the
groupby documentation for more details and examples.

```
In [65]: tips_summed = tips.groupby(["sex", "smoker"])[["total_bill", "tip"]].sum()
In [66]: tips_summed
Out[66]:
total_bill tip
sex smoker
Female No 869.68 149.77
Yes 527.27 96.74
Male No 1725.75 302.00
Yes 1217.07 183.07
```

### Transformation#

In Stata, if the group aggregations need to be used with the
original data set, one would usually use `bysort`

with `egen()`

.
For example, to subtract the mean for each observation by smoker group.

```
bysort sex smoker: egen group_bill = mean(total_bill)
generate adj_total_bill = total_bill - group_bill
```

pandas provides a Transformation mechanism that allows these type of operations to be succinctly expressed in one operation.

```
In [67]: gb = tips.groupby("smoker")["total_bill"]
In [68]: tips["adj_total_bill"] = tips["total_bill"] - gb.transform("mean")
In [69]: tips
Out[69]:
total_bill tip sex smoker day time size adj_total_bill
67 1.07 1.00 Female Yes Sat Dinner 1 -17.686344
92 3.75 1.00 Female Yes Fri Dinner 2 -15.006344
111 5.25 1.00 Female No Sat Dinner 1 -11.938278
145 6.35 1.50 Female No Thur Lunch 2 -10.838278
135 6.51 1.25 Female No Thur Lunch 2 -10.678278
.. ... ... ... ... ... ... ... ...
182 43.35 3.50 Male Yes Sun Dinner 3 24.593656
156 46.17 5.00 Male No Sun Dinner 6 28.981722
59 46.27 6.73 Male No Sat Dinner 4 29.081722
212 46.33 9.00 Male No Sat Dinner 4 29.141722
170 48.81 10.00 Male Yes Sat Dinner 3 30.053656
[244 rows x 8 columns]
```

### By group processing#

In addition to aggregation, pandas `groupby`

can be used to
replicate most other `bysort`

processing from Stata. For example,
the following example lists the first observation in the current
sort order by sex/smoker group.

```
bysort sex smoker: list if _n == 1
```

In pandas this would be written as:

```
In [70]: tips.groupby(["sex", "smoker"]).first()
Out[70]:
total_bill tip day time size adj_total_bill
sex smoker
Female No 5.25 1.00 Sat Dinner 1 -11.938278
Yes 1.07 1.00 Sat Dinner 1 -17.686344
Male No 5.51 2.00 Thur Lunch 2 -11.678278
Yes 5.25 5.15 Sun Dinner 2 -13.506344
```

## Other considerations#

### Disk vs memory#

pandas and Stata both operate exclusively in memory. This means that the size of
data able to be loaded in pandas is limited by your machine’s memory.
If out of core processing is needed, one possibility is the
dask.dataframe
library, which provides a subset of pandas functionality for an
on-disk `DataFrame`

.

## Source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html

# Comparison with SPSS#

For potential users coming from SPSS, this page is meant to demonstrate how various SPSS operations would be performed using pandas.

As is customary, we import pandas and NumPy as follows:

```
In [1]: import pandas as pd
In [2]: import numpy as np
```

## Data structures#

### General terminology translation#

pandas |
SPSS |
|---|---|
data file |
|
column |
variable |
row |
case |
groupby |
split file |
|
system-missing |

`DataFrame`

#

A `DataFrame`

in pandas is analogous to an SPSS data file - a two-dimensional
data source with labeled columns that can be of different types. As will be shown in this
document, almost any operation that can be performed in SPSS can also be accomplished in pandas.

`Series`

#

A `Series`

is the data structure that represents one column of a `DataFrame`

. SPSS doesn’t have a
separate data structure for a single variable, but in general, working with a `Series`

is analogous
to working with a variable in SPSS.

`Index`

#

Every `DataFrame`

and `Series`

has an `Index`

– labels on the *rows* of the data. SPSS does not
have an exact analogue, as cases are simply numbered sequentially from 1. In pandas, if no index is
specified, a `RangeIndex`

is used by default (first row = 0, second row = 1, and so on).

While using a labeled `Index`

or `MultiIndex`

can enable sophisticated analyses and is ultimately an
important part of pandas to understand, for this comparison we will essentially ignore the `Index`

and
just treat the `DataFrame`

as a collection of columns. Please see the indexing documentation
for much more on how to use an `Index`

effectively.

## Copies vs. in place operations#

`Series`

/`DataFrame`

. To make the changes “stick”,
you’ll need to either assign to a new variable:

sorted_df = df.sort_values("col1")

or overwrite the original one:

df = df.sort_values("col1")

Note

You will see an `inplace=True`

or `copy=False`

keyword argument available for
some methods:

```
df.replace(5, inplace=True)
```

`inplace`

and `copy`

for
most methods (e.g. `dropna`

) except for a very small subset of methods
(including `replace`

). Both keywords won’t be
necessary anymore in the context of Copy-on-Write. The proposal can be found
here.

## Data input / output#

### Reading external data#

Like SPSS, pandas provides utilities for reading in data from many formats. The `tips`

dataset, found within
the pandas tests (csv)
will be used in many of the following examples.

In SPSS, you would use File > Open > Data to import a CSV file:

```
FILE > OPEN > DATA
/TYPE=CSV
/FILE='tips.csv'
/DELIMITERS=","
/FIRSTCASE=2
/VARIABLES=col1 col2 col3.
```

The pandas equivalent would use `read_csv()`

:

```
url = (
"https://raw.githubusercontent.com/pandas-dev"
"/pandas/main/pandas/tests/io/data/csv/tips.csv"
)
tips = pd.read_csv(url)
tips
```

Like SPSS’s data import wizard, `read_csv`

can take a number of parameters to specify how the data should be parsed.
For example, if the data was instead tab delimited, and did not have column names, the pandas command would be:

```
tips = pd.read_csv("tips.csv", sep="\t", header=None)
# alternatively, read_table is an alias to read_csv with tab delimiter
tips = pd.read_table("tips.csv", header=None)
```

## Data operations#

### Filtering#

In SPSS, filtering is done through Data > Select Cases:

```
SELECT IF (total_bill > 10).
EXECUTE.
```

In pandas, boolean indexing can be used:

```
tips[tips["total_bill"] > 10]
```

### Sorting#

In SPSS, sorting is done through Data > Sort Cases:

```
SORT CASES BY sex total_bill.
EXECUTE.
```

In pandas, this would be written as:

```
tips.sort_values(["sex", "total_bill"])
```

## String processing#

### Finding length of string#

In SPSS:

```
COMPUTE length = LENGTH(time).
EXECUTE.
```

`Series.str.len()`

.
In Python 3, all strings are Unicode strings. `len`

includes trailing blanks.
Use `len`

and `rstrip`

to exclude trailing blanks.

```
In [3]: tips["time"].str.len()
Out[3]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
In [4]: tips["time"].str.rstrip().str.len()
Out[4]:
67 6
92 6
111 6
145 5
135 5
..
182 6
156 6
59 6
212 6
170 6
Name: time, Length: 244, dtype: int64
```

### Changing case#

In SPSS:

```
COMPUTE upper = UPCASE(time).
COMPUTE lower = LOWER(time).
EXECUTE.
```

The equivalent pandas methods are `Series.str.upper()`

, `Series.str.lower()`

, and
`Series.str.title()`

.

```
In [5]: firstlast = pd.DataFrame({"string": ["John Smith", "Jane Cook"]})
In [6]: firstlast["upper"] = firstlast["string"].str.upper()
In [7]: firstlast["lower"] = firstlast["string"].str.lower()
In [8]: firstlast["title"] = firstlast["string"].str.title()
In [9]: firstlast
Out[9]:
string upper lower title
0 John Smith JOHN SMITH john smith John Smith
1 Jane Cook JANE COOK jane cook Jane Cook
```

## Merging#

In SPSS, merging data files is done through Data > Merge Files.

The following tables will be used in the merge examples:

```
In [10]: df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
In [11]: df1
Out[11]:
key value
0 A 0.469112
1 B -0.282863
2 C -1.509059
3 D -1.135632
In [12]: df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})
In [13]: df2
Out[13]:
key value
0 B 1.212112
1 D -0.173215
2 D 0.119209
3 E -1.044236
```

`merge()`

method, which provides similar functionality. The
data does not have to be sorted ahead of time, and different join types are accomplished via the
`how`

keyword.

```
In [14]: inner_join = df1.merge(df2, on=["key"], how="inner")
In [15]: inner_join
Out[15]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
In [16]: left_join = df1.merge(df2, on=["key"], how="left")
In [17]: left_join
Out[17]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
In [18]: right_join = df1.merge(df2, on=["key"], how="right")
In [19]: right_join
Out[19]:
key value_x value_y
0 B -0.282863 1.212112
1 D -1.135632 -0.173215
2 D -1.135632 0.119209
3 E NaN -1.044236
In [20]: outer_join = df1.merge(df2, on=["key"], how="outer")
In [21]: outer_join
Out[21]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E NaN -1.044236
```

## GroupBy operations#

### Split-file processing#

In SPSS, split-file analysis is done through Data > Split File:

```
SORT CASES BY sex.
SPLIT FILE BY sex.
DESCRIPTIVES VARIABLES=total_bill tip
/STATISTICS=MEAN STDDEV MIN MAX.
```

The pandas equivalent would be:

```
tips.groupby("sex")[["total_bill", "tip"]].agg(["mean", "std", "min", "max"])
```

## Missing data#

SPSS uses the period (`.`

) for numeric missing values and blank spaces for string missing values.
pandas uses `NaN`

(Not a Number) for numeric missing values and `None`

or `NaN`

for string
missing values.

In pandas, `Series.isna()`

and `Series.notna()`

can be used to filter the rows.

```
In [22]: outer_join[outer_join["value_x"].isna()]
Out[22]:
key value_x value_y
5 E NaN -1.044236
In [23]: outer_join[outer_join["value_x"].notna()]
Out[23]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 NaN
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
```

pandas provides a variety of methods to work with missing data. Here are some examples:

### Drop rows with missing values#

```
In [24]: outer_join.dropna()
Out[24]:
key value_x value_y
1 B -0.282863 1.212112
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
```

### Forward fill from previous rows#

```
In [25]: outer_join.ffill()
Out[25]:
key value_x value_y
0 A 0.469112 NaN
1 B -0.282863 1.212112
2 C -1.509059 1.212112
3 D -1.135632 -0.173215
4 D -1.135632 0.119209
5 E -1.135632 -1.044236
```

### Replace missing values with a specified value#

Using the mean:

```
In [26]: outer_join["value_x"].fillna(outer_join["value_x"].mean())
Out[26]:
0 0.469112
1 -0.282863
2 -1.509059
3 -1.135632
4 -1.135632
5 -0.718815
Name: value_x, dtype: float64
```

## Other considerations#

## Output management#

While pandas does not have a direct equivalent to SPSS’s Output Management System (OMS), you can capture and export results in various ways:

```
# Save summary statistics to CSV
tips.groupby('sex')[['total_bill', 'tip']].mean().to_csv('summary.csv')
# Save multiple results to Excel sheets
with pd.ExcelWriter('results.xlsx') as writer:
tips.describe().to_excel(writer, sheet_name='Descriptives')
tips.groupby('sex').mean().to_excel(writer, sheet_name='Means by Gender')
```

## Source: https://pandas.pydata.org/docs/getting_started/overview.html

# Package overview#

pandas is a Python package that provides fast,
flexible, and expressive data structures designed to make working with
“relational” or “labeled” data both easy and intuitive. It aims to be the
fundamental high-level building block for Python’s practical, **real-world** data
analysis. Additionally, it seeks to become **the
most powerful and flexible open source data analysis/manipulation tool
available in any language**. It is already well on its way toward this goal.

pandas is well suited for many different kinds of data:

Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet

Ordered and unordered (not necessarily fixed-frequency) time series data.

Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels

Any other form of observational / statistical data sets. The data need not be labeled at all to be placed into a pandas data structure

The two primary data structures of pandas, `Series`

(1-dimensional)
and `DataFrame`

(2-dimensional), handle the vast majority of typical use
cases in finance, statistics, social science, and many areas of
engineering. For R users, `DataFrame`

provides everything that R’s
`data.frame`

provides and much more. pandas is built on top of NumPy and is intended to integrate well within a scientific
computing environment with many other 3rd party libraries.

Here are just a few of the things that pandas does well:

Easy handling of

missing data(represented as NaN) in floating point as well as non-floating point dataSize mutability: columns can be

inserted and deletedfrom DataFrame and higher dimensional objectsAutomatic and explicit

data alignment: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let`Series`

,`DataFrame`

, etc. automatically align the data for you in computationsPowerful, flexible

group byfunctionality to perform split-apply-combine operations on data sets, for both aggregating and transforming dataMake it

easy to convertragged, differently-indexed data in other Python and NumPy data structures into DataFrame objectsIntelligent label-based

slicing,fancy indexing, andsubsettingof large data setsIntuitive

mergingandjoiningdata setsFlexible

reshapingand pivoting of data sets

Hierarchicallabeling of axes (possible to have multiple labels per tick)Robust IO tools for loading data from

flat files(CSV and delimited), Excel files, databases, and saving / loading data from the ultrafastHDF5 format

Time series-specific functionality: date range generation and frequency conversion, moving window statistics, date shifting, and lagging.

Many of these principles are here to address the shortcomings frequently experienced using other languages / scientific research environments. For data scientists, working with data is typically divided into multiple stages: munging and cleaning data, analyzing / modeling it, then organizing the results of the analysis into a form suitable for plotting or tabular display. pandas is the ideal tool for all of these tasks.

Some other notes

pandas is

fast. Many of the low-level algorithmic bits have been extensively tweaked in Cython code. However, as with anything else generalization usually sacrifices performance. So if you focus on one feature for your application you may be able to create a faster specialized tool.pandas is a dependency of statsmodels, making it an important part of the statistical computing ecosystem in Python.

pandas has been used extensively in production in financial applications.

## Data structures#

Dimensions |
Name |
Description |
|---|---|---|
1 |
Series |
1D labeled homogeneously-typed array |
2 |
DataFrame |
General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column |

### Why more than one data structure?#

The best way to think about the pandas data structures is as flexible containers for lower dimensional data. For example, DataFrame is a container for Series, and Series is a container for scalars. We would like to be able to insert and remove objects from these containers in a dictionary-like fashion.

Also, we would like sensible default behaviors for the common API functions which take into account the typical orientation of time series and cross-sectional data sets. When using the N-dimensional array (ndarrays) to store 2- and 3-dimensional data, a burden is placed on the user to consider the orientation of the data set when writing functions; axes are considered more or less equivalent (except when C- or Fortran-contiguousness matters for performance). In pandas, the axes are intended to lend more semantic meaning to the data; i.e., for a particular data set, there is likely to be a “right” way to orient the data. The goal, then, is to reduce the amount of mental effort required to code up data transformations in downstream functions.

For example, with tabular data (DataFrame) it is more semantically helpful to
think of the **index** (the rows) and the **columns** rather than axis 0 and
axis 1. Iterating through the columns of the DataFrame thus results in more
readable code:

```
for col in df.columns:
series = df[col]
# do something with series
```

## Mutability and copying of data#

All pandas data structures are value-mutable (the values they contain can be
altered) but not always size-mutable. The length of a Series cannot be
changed, but, for example, columns can be inserted into a DataFrame. However,
the vast majority of methods produce new objects and leave the input data
untouched. In general we like to **favor immutability** where sensible.

## Getting support#

The first stop for pandas issues and ideas is the GitHub Issue Tracker. If you have a general question, pandas community experts can answer through Stack Overflow.

## Community#

pandas is actively supported today by a community of like-minded individuals around the world who contribute their valuable time and energy to help make open source pandas possible. Thanks to all of our contributors.

If you’re interested in contributing, please visit the contributing guide.

## Project governance#

The governance process that pandas project has used informally since its inception in 2008 is formalized in Project Governance documents. The documents clarify how decisions are made and how the various elements of our community interact, including the relationship between open source collaborative development and work that may be funded by for-profit or non-profit entities.

Wes McKinney is the Benevolent Dictator for Life (BDFL).

## Development team#

The list of the Core Team members and more detailed information can be found on the pandas website.

## Institutional partners#

The information about current institutional partners can be found on pandas website page.

## License#

```
BSD 3-Clause License
Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
All rights reserved.
Copyright (c) 2011-2026, Open source contributors.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## Source: https://pandas.pydata.org/docs/getting_started/tutorials.html

# Community tutorials#

This is a guide to many pandas tutorials by the community, geared mainly for new users.

## pandas cookbook by Julia Evans#

The goal of this 2015 cookbook (by Julia Evans) is to give you some concrete examples for getting started with pandas. These are examples with real-world data, and all the bugs and weirdness that entails. For the table of contents, see the pandas-cookbook GitHub repository.

## pandas workshop by Stefanie Molin#

An introductory workshop by Stefanie Molin designed to quickly get you up to speed with pandas using real-world datasets. It covers getting started with pandas, data wrangling, and data visualization (with some exposure to matplotlib and seaborn). The pandas-workshop GitHub repository features detailed environment setup instructions (including a Binder environment), slides and notebooks for following along, and exercises to practice the concepts. There is also a lab with new exercises on a dataset not covered in the workshop for additional practice.

## Learn pandas by Hernan Rojas#

A set of lesson for new pandas users: https://bitbucket.org/hrojas/learn-pandas

## Practical data analysis with Python#

This guide is an introduction to the data analysis process using the Python data ecosystem and an interesting open dataset. There are four sections covering selected topics as munging data, aggregating data, visualizing data and time series.

## Exercises for new users#

Practice your skills with real data sets and exercises. For more resources, please visit the main repository.

## Modern pandas#

Tutorial series written in 2016 by Tom Augspurger. The source may be found in the GitHub repository TomAugspurger/effective-pandas.

## Excel charts with pandas, vincent and xlsxwriter#

## Joyful pandas#

A tutorial written in Chinese by Yuanhao Geng. It covers the basic operations for NumPy and pandas, 4 main data manipulation methods (including indexing, groupby, reshaping and concatenation) and 4 main data types (including missing data, string data, categorical data and time series data). At the end of each chapter, corresponding exercises are posted. All the datasets and related materials can be found in the GitHub repository datawhalechina/joyful-pandas.

## Video tutorials#

Pandas From The Ground Up (2015) (2:24) GitHub repo

Introduction Into Pandas (2016) (1:28) GitHub repo

Pandas: .head() to .tail() (2016) (1:26) GitHub repo

Data analysis in Python with pandas (2016-2018) GitHub repo and Jupyter Notebook

Best practices with pandas (2018) GitHub repo and Jupyter Notebook
