## Source: https://geopandas.org/en/stable/about.html

# About GeoPandas#

GeoPandas is an open source project to add support for geographic data to pandas objects. It
currently implements `GeoSeries`

and `GeoDataFrame`

types which are subclasses of
`pandas.Series`

and `pandas.DataFrame`

respectively. GeoPandas objects can act on
`shapely`

geometry objects and perform geometric operations.

GeoPandas is a community-led project written, used and supported by a wide range of people from all around of world of a large variety of backgrounds. Want to get involved in the community? See our community guidelines.

GeoPandas will always be 100% open source software, free for all to use and released under the liberal terms of the BSD-3-Clause license.

GeoPandas is a fiscally sponsored project of NumFOCUS, a nonprofit dedicated to supporting the open-source scientific computing community. If you like GeoPandas and want to support our mission, please consider making a donation to support our efforts.

NumFOCUS is a 501(c)(3) non-profit charity in the United States; as such, donations to NumFOCUS are tax-deductible as allowed by law. As with any donation, you should consult with your personal tax adviser or the IRS about your particular tax situation.

## Project history#

Kelsey Jordahl founded GeoPandas project in 2013 during the Scipy Conference and released a version 0.1.0 in July 2014. In 2016, Joris Van den Bossche took the lead and became the maintainer of the project. Since the beginning, GeoPandas is a BSD-licensed open-source project supported by a community of contributors from around the world and is now maintained by a team of core developers.

In 2020 GeoPandas became NumFOCUS Affiliated Project and received two Small Development Grants to support its development. In 2023, GeoPandas became NumFOCUS Sponsored Project.

## Timeline#

**2013**: Beginning of the development**2014**: GeoPandas 0.1.0 released**2020**: GeoPandas became NumFOCUS Affiliated Project**2023**: GeoPandas became NumFOCUS Sponsored Project

## Source: https://geopandas.org/en/stable/about/team.html

# Team#

## Core developers#

Joris Van den Bossche -

**lead maintainer**| @jorisvandenbosscheMartin Fleischmann | @martinfleis

James McBride | @jdmcbr

Brendan Ward | @brendan-ward

Levi Wolf | @ljwolf

Matt Richards | @m-richards

## Founder#

Kelsey Jordahl | @kjordahl

## Alumni developers#

Jacob Wasserman | @jwass

## Source: https://geopandas.org/en/stable/about/roadmap.html

# Roadmap#

The current roadmap reflects longer-term vision covering enhancements that should happen in upcoming releases.

## S2 geometry engine#

The geometry engine used in GeoPandas is `shapely`

, which serves as a Python API for
`GEOS`

. It means that all geometry operations in GeoPandas are planar, using (possibly)
projected coordinate reference systems. Some applications focusing on the global context
may find planar operations limiting as they come with troubles around anti-meridian and
poles. One solution is an implementation of a spherical geometry engine, namely `S2`

,
that should eliminate these limitations and offer an alternative to `GEOS`

.

The GeoPandas community is currently working together with the R-spatial community that
has already exposed `S2`

in an R counterpart of GeoPandas `sf`

on Python bindings for
`S2`

, that should be used as a secondary geometry engine in GeoPandas.

## Prepared geometries#

GeoPandas is using spatial indexing for the operations that may benefit from it. Further
performance gains can be achieved using prepared geometries. Preparation creates a
spatial index of individual line segments of geometries, greatly enhancing the speed of
spatial predicates like `intersects`

or `contains`

. Given that the preparation has
become less computationally expensive in `shapely`

2.0, GeoPandas should expose the
preparation to the user but, more importantly, use smart automatic geometry preparation
under the hood.

## Static plotting improvements#

GeoPandas currently covers a broad range of geospatial tasks, from data exploration to
advanced analysis. However, one moment may tempt the user to use different software -
plotting. GeoPandas can create static maps based on `matplotlib`

, but they are a bit
basic at the moment. It isn’t straightforward to generate a complex map in a
production-quality which can go straight to an academic journal or an infographic. We
want to change this and remove barriers which we currently have and make it simple to
create beautiful maps.

## Source: https://geopandas.org/en/stable/about/citing.html

# Citing#

When citing GeoPandas, you can use Zenodo DOI for each release.
Below is the example of resulting BiBTeX record for GeoPandas 0.8.1 and a reference using APA 6th ed.

*Kelsey Jordahl, Joris Van den Bossche, Martin Fleischmann, Jacob Wasserman, James McBride, Jeffrey Gerard, … François Leblanc. (2020, July 15). geopandas/geopandas: v0.8.1 (Version v0.8.1). Zenodo. http://doi.org/10.5281/zenodo.3946761*

```
@software{kelsey_jordahl_2020_3946761,
author = {Kelsey Jordahl and
Joris Van den Bossche and
Martin Fleischmann and
Jacob Wasserman and
James McBride and
Jeffrey Gerard and
Jeff Tratner and
Matthew Perry and
Adrian Garcia Badaracco and
Carson Farmer and
Geir Arne Hjelle and
Alan D. Snow and
Micah Cochran and
Sean Gillies and
Lucas Culbertson and
Matt Bartos and
Nick Eubank and
maxalbert and
Aleksey Bilogur and
Sergio Rey and
Christopher Ren and
Dani Arribas-Bel and
Leah Wasser and
Levi John Wolf and
Martin Journois and
Joshua Wilson and
Adam Greenhall and
Chris Holdgraf and
Filipe and
Fran\c{c}ois Leblanc},
title = {geopandas/geopandas: v0.8.1},
month = jul,
year = 2020,
publisher = {Zenodo},
version = {v0.8.1},
doi = {10.5281/zenodo.3946761},
url = {https://doi.org/10.5281/zenodo.3946761}
}
```

## Source: https://geopandas.org/en/stable/about/logo.html

# GeoPandas logo#

GeoPandas project uses a logo derived from `pandas`

logo, enclosing it in a globe illustrating the geographic nature of our data.

## Versions#

We have four versions of our logo:

### Primary logo#

The primary logo should be used in a majority of cases. Inverted logo or icon should be used only when necessary.

### Inverted colors#

If you want to place the GeoPandas logo on a dark background, use the inverted version.

### Icon#

Although it is possible to use icon independently, we would prefer using the complete variant above.

### Inverted icon#

## Download#

You can download all version in SVG and PNG from GitHub repository.

## Colors#

Pink and yellow accent colors are shared with `pandas`

.

### Green#

**HEX:** #139C5A

**RGB:** (19, 156, 90)

### Yellow#

**HEX:** #FFCA00

**RGB:** (255, 202, 0)

### Pink#

**HEX:** #E70488

**RGB:** (231, 4, 136)
