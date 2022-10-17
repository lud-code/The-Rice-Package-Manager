# The Rice Package Manager

Creating this is redundant.

## How to Use

To install a pkg:
    ./rice.py -i [package]

How to remove a pkg [removes pkg and orphans]:
    ./rice.py -u [package]

...And that's *all* you can do!

## How to Add A Package

The package file format is organized as followed:
> RUN CMD
> LINK
> COMPILE CMD
DEPENDENCIES:
> NAME | RUN CMD | LINK | COMPILE CMD

NOTE: Currently, it only supports ".zip" files as of now (12/10/22).
