## Source: https://pydicom.github.io/pydicom/stable/tutorials/installation.html

# How to install pydicom¶

Note

We recommend installing into a virtual environment, which is an isolated Python environment that allows you to install packages without admin privileges.

## Install the official release¶

*pydicom*, being a Python library, requires Python. If you’re not sure whether or not your version of
Python is supported, check this table.

### Install using pip¶

*pydicom* is available on PyPI, the
official third-party Python software repository. The simplest way to install
from PyPI is using pip with the command:

```
```

You may need to use this instead, depending on your operating system:

```
```

You can also perform an offline installation by
downloading and installing
one of the release `*.whl`

files. For example, with the v2.0 release:

```
```

### Install using conda¶

*pydicom* is also available for conda at
conda-forge:

```
```

### Additional type hints¶

The default *pydicom* type hinting doesn’t cover standard element keywords accessed
through `Dataset`

:

```
# foo.py
from pydicom import Dataset
ds = Dataset()
ds.PatientName = 1234
```

```
$ mypy foo.py
Success: no issues found in 1 source file
```

To add extra type hints for these attributes you can install the types-pydicom package:

```
```

```
$ mypy foo.py
foo.py:5: error: Incompatible types in assignment (expression has type "int", variable has type "str | PersonName | None") [assignment]
Found 1 error in 1 file (checked 1 source file)
```

### Downloading example/test DICOM files¶

To keep the package size small, a number of the larger DICOM files are not
distributed with *pydicom* and are instead kept in the
pydicom-data repository. To get the complete set of
testing and example files you can either install the *pydicom-data* repository:

```
```

Or download the missing files to the local cache (after installing *pydicom*):

```
python -c "import pydicom; pydicom.data.fetch_data_files()"
```

## Install the optional libraries¶

If you’re going to be manipulating pixel data then NumPy is required.

Using pip:

```
```

Through conda:

```
```

To decode JPEG compressed pixel data one or more additional libraries will
need to be installed. See this page for a list of
which library is needed to handle a given JPEG format, as specified by
the dataset’s (0002,0010) *Transfer Syntax UID* value.

### Installing Pillow¶

Pillow is a popular Python imaging library that can handle the decompression of some JPEG and JPEG 2000 images.

Using pip; you may need to make sure that the libjpeg (for JPEG) and openjpeg (for JPEG 2000) libraries are installed beforehand:

```
```

Through conda:

```
```

### Installing pyjpegls¶

pyjpegls is a Python interface to the CharLS C++ library and can decompress JPEG-LS images. It is a fork of CharPyLS created to provide compatibility with the latest Python versions.

Using pip:

```
```

Through conda:

```
```

### Installing GDCM¶

GDCM is a C++ library for working with DICOM datasets that can decompress JPEG, JPEG-LS and JPEG 2000 images.

The wheels on PyPI are built by the python-gdcm project for current versions of Python on Windows, MacOS and Linux, and can be installed using pip:

```
```

The wheels available through conda-forge tend to be older versions and not as well supported. They’re available on conda using:

```
```

### Installing pylibjpeg¶

pylibjpeg is a Python framework for decompressing JPEG, JPEG-LS, JPEG 2000 images and compressing or decompressing RLE images provided a suitable plugin is installed.

Using pip:

```
```

## Install the development version¶

To install a snapshot of the latest code (the `main`

branch) from
GitHub:

```
```

The `main`

branch is under active development and while it is usually
stable, it may have undocumented changes or bugs.

If you want to keep up-to-date with the latest code, make sure you have
Git installed and then clone the `main`

branch (this will create a `pydicom`

directory in your current directory):

```
git clone --depth=1 https://github.com/pydicom/pydicom.git
```

Then install using pip in editable (`-e`

) mode:

```
```

When you want to update your copy of the source code, run `git pull`

from
within the `pydicom`

directory and Git will download and apply any changes.

# **Add this**
NewDefinedUID = UID('1.2.3.4.500')
"""1.2.3.4.500"""
```

The line `"""1.2.3.4.500"""`

is the docstring for our new UID. In order for
it to be included in the API reference documentation we’ll also need to update
uid.rst:

```
JPEG2000MultiComponentLossless
JPEG2000MultiComponent
RLELossless
NewDefinedUID
```

When making changes, and especially when adding new features, it’s important
that they’re documented. It’s very difficult for users to find and
understand how to use code that hasn’t been documented, or whose documentation
contains errors. For more information on how to properly document *pydicom*
see writing documentation.

Now we run the tests again so we can see whether or not the code we added is working:

```
$ pytest test_uid.py
```

Everything should pass. If it doesn’t, make sure you’ve correctly added the
new UID. Once you’re happy that the tests in `test_uid.py`

are working you
should make sure the entire test suite passes:

```
$ pytest
```

## Preview your changes¶

It’s a good idea to go through all the changes you’ve made by first staging and then displaying the difference between the current copy and the initial version we first checked out with:

```
$ git add --all
$ git diff --cached
```

You can scroll through the output using the up and down keys and quit with
**q**. Lines with a **-** in front will be removed and lines with a **+**
added. If everything looks good then it’s time to commit the changes.

## Commit your changes and make a pull request¶

To commit the changes:

```
$ git commit
```

This will open a text editor so you can add the commit message. Alternatively, if you only want a short commit message you can do:

```
$ git commit -m "Add NewDefinedUID"
```

Which will commit with the message *“Add NewDefinedUID”*. After committing the
patch, send it to your fork:

```
$ git push origin new-uid
```

You can create a pull request by visiting the pydicom GitHub page where you should see your branch under *“Your recently push
branches”*. Click *“Compare & pull request”* and fill out the title (with a
`[WIP]`

prefix, i.e. `[WIP] Add NewDefinedUID to uid.py`

) and follow the
instructions in the main entry window.

To submit the pull request (PR) for real - **please don’t do this for
this example!** - then on the next page you would click *“Create pull
request”*.
Creating the PR would automatically start our checks; that the tests pass and
the test coverage is good, that the documentation builds OK, etc.

If all the checks passed and you were happy with your changes, you’d change
the PR title prefix to `[MRG]`

. This would indicate that you considered the
PR ready to be reviewed and merged into the main branch. You could also ask
for a review or help at any point after creating the PR.

## What happens next?¶

One or more reviewers would look at your pull request and may make suggestions,
ask for clarification or request changes. Once the reviewers were happy,
the pull request would be approved and your changes merged into the
`main`

branch where they would become part of *pydicom*.

However, because this is just an example, all we’re going to do is clean up the
changes we’ve made. First we switch back to the `main`

branch:

```
$ git checkout main
```

We delete the local copy of the branch we created:

```
$ git branch -d new-uid
```

And lastly we delete the remote copy on GitHub. Go to
`https://github.com/YourUsername/pydicom/branches`

, find the `new-uid`

branch and click the corresponding red bin icon. All done!
