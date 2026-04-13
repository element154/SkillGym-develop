## Source: https://docs.astropy.org/en/stable/visualization/index.html

# Data Visualization (`astropy.visualization`

)#

## Introduction#

`astropy.visualization`

provides functionality that can be helpful when
visualizing data. This includes a framework for plotting Astronomical images
with coordinates with Matplotlib (previously the standalone **wcsaxes**
package), functionality related to image normalization (including both scaling
and stretching), smart histogram plotting, RGB color image creation from
separate images, and custom plotting styles for Matplotlib.

## Using `astropy.visualization`

#

## Scripts#

This module includes a command-line script, `fits2bitmap`

to convert FITS
images to bitmaps, including scaling and stretching of the image. To find out
more about the available options and how to use it, type:

```
$ fits2bitmap --help
```
