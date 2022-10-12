# The Rice Package Manager
### Creating this is redundant.

## How to Use
To install a pkg:
    ./rice.py -i [package]

How to remove a pkg [removes pkg and orphans]:
    ./rice.py -u [package]

...And that's *all* you can do!

## How to Add A Package
The package file format is organized as followed:
* (C/I) COMPILE OR INTERPRET TARG FILE (LIKE A MAKE FILE)
* LINK
* (C/I) | DEPEND NAMES | DEPENDENCY LINKS

NOTE: Currently, it only supports ".zip" files as of now (12/10/22). 