## Source: https://docs.astropy.org/en/stable/install.html

# Installation#

## Overview#

The first step to installing `astropy`

is to ensure that you have a Python
environment which is **isolated** from your system Python installation. This is
important because `astropy`

has many dependencies, and you do not want to accidentally
break your system by installing incompatible versions of these dependencies.

For this installation guide we use the conda
package manager provided by miniforge.
This is a popular choice and works well, especially for newcomers. It is easy to install
and use on all platforms and it makes it easy to install the latest Python version. If
you already have a `miniforge`

-based Python environment then you can skip to
Install astropy.

Another option for more experienced users is a virtual environment manager such as the Python standard library venv module. There are numerous resources available to help you set up a virtual environment in this manner if you choose this option.

Note

We **do not recommend** using `astropy`

with an existing miniconda or Anaconda Python distribution. The `astropy`

package provided
by Anaconda Inc. in the `defaults`

channel can be outdated and these distributions
can require a license for use at a large organisation. Instead, use `miniforge`

as
described below.

Once you have a Python environment set up, you will install `astropy`

using pip or
conda. Here we document using pip because it is easier to install the optional
dependencies, but feel free to use conda if you prefer.

## Install `miniforge`

#

You will install Python by first installing miniforge. This provides the conda package manager with the default remote package repository set to the community-led conda-forge channel.

In a new terminal (miniforge Prompt on Windows) run `conda list`

to test that the
install has worked.

## Create Python Environment#

To create a new Python environment for `astropy`

and other packages, start by
launching a terminal (under a UNIX-like system) or the miniforge Prompt (under Windows).
Now we will create and activate a new virtual environment to install `astropy`

into:

```
$ conda create --channel conda-forge --name astropy python
$ conda activate astropy
```

In this case the environment we have created is named `astropy`

but you can use any
name you like.

In the future when you make a new terminal, you will need to run ```
conda activate
astropy
```

to activate this environment.

## Install `astropy`

#

You can install `astropy`

and the rest of your dependencies using either pip or
conda. Both methods are fully supported and will work well.

Warning

Once you have created your base Python environment with conda, you should try to stick with one method for installing new packages in your environment. In particular, conda is not aware of packages installed with pip and may overwrite them.

### Using pip#

To install `astropy`

and your choice of dependencies, run
one of the following commands:

```
```

In most cases, this will install a pre-compiled version of `astropy`

(called a
*wheel*). However, if you are installing astropy on an uncommon platform, astropy will be
installed from a source file. In this unusual case you will need a C compiler to be
installed (see Build from source below) for the installation to succeed.

Warning

Do **not** install `astropy`

or other packages using `sudo`

or any
elevated privilege.

### Using conda#

To install `astropy`

and the minimal set of required dependencies, run:

```
```

Install the recommended dependencies with:

```
```

Install the optional dependencies with:

```
beautifulsoup4 html5lib bleach pandas sortedcontainers pytz jplephem mpmath \
asdf-astropy bottleneck fsspec s3fs certifi
```

### Testing#

You can test that your newly installed version of `astropy`

is working via the
documentation on how to test your installed version of astropy.

## Requirements#

`astropy`

has the following strict requirements:

Python 3.11 or later

NumPy >=1.24 or later

PyERFA >=2.0.1.1 or later

PyYAML >=6.0.0 or later

packaging >=22.0.0 or later

`astropy`

also depends on a number of other packages for optional features.
The following are particularly recommended:

SciPy >=1.9.2 or later: To power a variety of features in several modules.

Matplotlib >=3.9.1 or later: To provide plotting functionality that

`astropy.visualization`

enhances.

The further dependencies provide more specific features:

BeautifulSoup: To read

`Table`

objects from HTML files.html5lib: To read

`Table`

objects from HTML files using the pandas reader.bleach: Used to sanitize text when disabling HTML escaping in the

`Table`

HTML writer.ipydatagrid: Used in

`astropy.table.Table.show_in_notebook()`

to display the Astropy table in Jupyter notebook for`backend="ipydatagrid"`

.xmllint: To validate VOTABLE XML files. This is a command line tool installed outside of Python.

pandas: To convert

`Table`

objects from/to pandas DataFrame objects.sortedcontainers for faster

`SCEngine`

indexing engine with`Table`

, although this may still be slower in some cases than the default indexing engine.pytz: To specify and convert between timezones.

jplephem: To retrieve JPL ephemeris of Solar System objects.

setuptools: Used for discovery of entry points which are used to insert fitters into

`astropy.modeling.fitting`

.mpmath: Used for the ‘kraft-burrows-nousek’ interval in

`poisson_conf_interval`

.asdf-astropy >=0.3 or later: Enables the serialization of various Astropy classes into a portable, hierarchical, human-readable representation.

bottleneck: Improves the performance of sigma-clipping and other functionality that may require computing statistics on arrays with NaN values.

certifi: Useful when downloading files from HTTPS or FTP+TLS sites in case Python is not able to locate up-to-date root CA certificates on your system; this package is usually already included in many Python installations (e.g., as a dependency of the

`requests`

package).pyarrow >=14.0.2 or later: To read/write

`Table`

objects from/to Parquet files.fsspec >=2023.4.0 or later: Enables access to subsets of remote FITS files without having to download the entire file.

s3fs >=2023.4.0 or later: Enables access to files hosted in AWS S3 cloud storage.

However, note that these packages require installation only if those particular
features are needed. `astropy`

will import even if these dependencies are not
installed.

The following packages can optionally be used when testing:

pytest-xdist: Used for distributed testing.

pytest-mpl: Used for testing with Matplotlib figures.

objgraph: Used only in tests to test for reference leaks.

IPython >=8.0.0 or later: Used for testing the notebook interface of

`Table`

.coverage: Used for code coverage measurements.

skyfield: Used for testing Solar System coordinates.

sgp4: Used for testing satellite positions.

tox: Used to automate testing and documentation builds.

## Build from Source#

See the latest documentation on how to build astropy from source.

### Test Source Code Build#

See the latest documentation on how to run the tests in a source checkout of astropy.

## Install Pre-built Development Version#

Most nights a development snapshot of `astropy`

will be compiled.
This is useful if you want to test against a development version of astropy but
do not want to have to build it yourselves. You can see the
available astropy dev snapshots page
to find out what is currently being offered.

Installing these “nightlies” of `astropy`

can be achieved by using `pip`

:

```
```

The extra index URL tells `pip`

to check the `pip`

index on
pypi.anaconda.org, where the nightlies are stored, and the `--pre`

command
tells `pip`

to install pre-release versions (in this case `.dev`

releases).

You can test this installation by running the tests as described in the section Running tests on an installed astropy.

## Source: https://docs.astropy.org/en/latest/install.html

# Installation#

## Overview#

The first step to installing `astropy`

is to ensure that you have a Python
environment which is **isolated** from your system Python installation. This is
important because `astropy`

has many dependencies, and you do not want to accidentally
break your system by installing incompatible versions of these dependencies.

For this installation guide we use the conda
package manager provided by miniforge.
This is a popular choice and works well, especially for newcomers. It is easy to install
and use on all platforms and it makes it easy to install the latest Python version. If
you already have a `miniforge`

-based Python environment then you can skip to
Install astropy.

Another option for more experienced users is a virtual environment manager such as the Python standard library venv module. There are numerous resources available to help you set up a virtual environment in this manner if you choose this option.

Note

We **do not recommend** using `astropy`

with an existing miniconda or Anaconda Python distribution. The `astropy`

package provided
by Anaconda Inc. in the `defaults`

channel can be outdated and these distributions
can require a license for use at a large organisation. Instead, use `miniforge`

as
described below.

Once you have a Python environment set up, you will install `astropy`

using pip or
conda. Here we document using pip because it is easier to install the optional
dependencies, but feel free to use conda if you prefer.

## Install `miniforge`

#

You will install Python by first installing miniforge. This provides the conda package manager with the default remote package repository set to the community-led conda-forge channel.

In a new terminal (miniforge Prompt on Windows) run `conda list`

to test that the
install has worked.

## Create Python Environment#

To create a new Python environment for `astropy`

and other packages, start by
launching a terminal (under a UNIX-like system) or the miniforge Prompt (under Windows).
Now we will create and activate a new virtual environment to install `astropy`

into:

```
$ conda create --channel conda-forge --name astropy python
$ conda activate astropy
```

In this case the environment we have created is named `astropy`

but you can use any
name you like.

In the future when you make a new terminal, you will need to run ```
conda activate
astropy
```

to activate this environment.

## Install `astropy`

#

You can install `astropy`

and the rest of your dependencies using either pip or
conda. Both methods are fully supported and will work well.

Warning

Once you have created your base Python environment with conda, you should try to stick with one method for installing new packages in your environment. In particular, conda is not aware of packages installed with pip and may overwrite them.

### Using pip#

To install `astropy`

and your choice of dependencies, run
one of the following commands:

```
```

In most cases, this will install a pre-compiled version of `astropy`

(called a
*wheel*). However, if you are installing astropy on an uncommon platform, astropy will be
installed from a source file. In this unusual case you will need a C compiler to be
installed (see Build from source below) for the installation to succeed.

Warning

Do **not** install `astropy`

or other packages using `sudo`

or any
elevated privilege.

### Using conda#

To install `astropy`

and the minimal set of required dependencies, run:

```
```

Install the recommended dependencies with:

```
```

Install the optional dependencies with:

```
beautifulsoup4 html5lib bleach pandas sortedcontainers pytz jplephem mpmath \
asdf-astropy bottleneck fsspec s3fs certifi
```

### Testing#

You can test that your newly installed version of `astropy`

is working via the
documentation on how to test your installed version of astropy.

## Requirements#

`astropy`

has the following strict requirements:

Python 3.11 or later

NumPy >=2.0 or later

PyERFA >=2.0.1.3 or later

PyYAML >=6.0.0 or later

packaging >=25.0 or later

`astropy`

also depends on a number of other packages for optional features.
The following are particularly recommended:

SciPy >=1.13 or later: To power a variety of features in several modules.

Matplotlib >=3.9.1 or later: To provide plotting functionality that

`astropy.visualization`

enhances.

The further dependencies provide more specific features:

BeautifulSoup: To read

`Table`

objects from HTML files.html5lib: To read

`Table`

objects from HTML files using the pandas reader.bleach: Used to sanitize text when disabling HTML escaping in the

`Table`

HTML writer.ipydatagrid: Used in

`astropy.table.Table.show_in_notebook()`

to display the Astropy table in Jupyter notebook for`backend="ipydatagrid"`

.xmllint: To validate VOTABLE XML files. This is a command line tool installed outside of Python.

pandas: To convert

`Table`

objects from/to pandas DataFrame objects.sortedcontainers for faster

`SCEngine`

indexing engine with`Table`

, although this may still be slower in some cases than the default indexing engine.pytz: To specify and convert between timezones.

jplephem: To retrieve JPL ephemeris of Solar System objects.

setuptools: Used for discovery of entry points which are used to insert fitters into

`astropy.modeling.fitting`

.mpmath: Used for the ‘kraft-burrows-nousek’ interval in

`poisson_conf_interval`

.asdf-astropy >=0.7.0 or later: Enables the serialization of various Astropy classes into a portable, hierarchical, human-readable representation.

bottleneck: Improves the performance of sigma-clipping and other functionality that may require computing statistics on arrays with NaN values.

certifi: Useful when downloading files from HTTPS or FTP+TLS sites in case Python is not able to locate up-to-date root CA certificates on your system; this package is usually already included in many Python installations (e.g., as a dependency of the

`requests`

package).pyarrow >=16.0 or later: To read/write

`Table`

objects from/to Parquet files.fsspec >=2023.4.0 or later: Enables access to subsets of remote FITS files without having to download the entire file.

s3fs >=2023.4.0 or later: Enables access to files hosted in AWS S3 cloud storage.

However, note that these packages require installation only if those particular
features are needed. `astropy`

will import even if these dependencies are not
installed.

The following packages can optionally be used when testing:

pytest-xdist: Used for distributed testing.

pytest-mpl: Used for testing with Matplotlib figures.

objgraph: Used only in tests to test for reference leaks.

IPython >=8.0.0 or later: Used for testing the notebook interface of

`Table`

.coverage: Used for code coverage measurements.

skyfield: Used for testing Solar System coordinates.

sgp4: Used for testing satellite positions.

tox: Used to automate testing and documentation builds.

## Build from Source#

If you want to build the code from source, follow the instructions for Creating a development environment. Note that instead of cloning from your fork, you can choose to clone from the main repository:

```
git clone https://github.com/astropy/astropy.git
cd astropy
```

Building the documentation is typically not necessary unless you are developing code or documentation or do not have internet access, because the stable, latest, and archived versions of Astropy’s documentation are available at docs.astropy.org . The process is described in Building the Documentation from Source.

### Test Source Code Build#

The easiest way to run the tests in a source checkout of `astropy`

is to use tox:

```
tox -e test-alldeps
```

There are also alternative methods of Running Tests if you would like more control over the testing process.

## Install Pre-built Development Version#

Most nights a development snapshot of `astropy`

will be compiled.
This is useful if you want to test against a development version of astropy but
do not want to have to build it yourselves. You can see the
available astropy dev snapshots page
to find out what is currently being offered.

Installing these “nightlies” of `astropy`

can be achieved by using `pip`

:

```
```

The extra index URL tells `pip`

to check the `pip`

index on
pypi.anaconda.org, where the nightlies are stored, and the `--pre`

command
tells `pip`

to install pre-release versions (in this case `.dev`

releases).

You can test this installation by running the tests as described in the section Running tests on an installed astropy.
