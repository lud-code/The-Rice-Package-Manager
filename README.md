# The Rice Package Manager
### The creation of this was redundant.

## How to Use
To install a pkg:
    ./rice.py -i [package]

How to remove a pkg [removes pkg and orphans]:
    ./rice.py -u [package]

...And that's *all* you can do!

## How to Add A Package
The package file format is organized as followed:
* COMPILE OR INTERPRET?
* LINK, e.x., https://github.com/ex/project/archive/refs/head/main.zip
* DEPENDECY LINKS [put all of them]