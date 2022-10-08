from os import getcwd, remove, rename
from requests import get
from zipfile import ZipFile

CWD = getcwd()
INSTALL = f"{CWD}/install/"
REPO = f"{CWD}/repo/"


def extract(file):
    with ZipFile(f"{INSTALL}/{file}.zip", "r") as zip:
        dir = zip.namelist()[0]
        zip.extractall(f"{INSTALL}")
        rename(f"{INSTALL}/{dir}", f"{INSTALL}/{file}")


def install(targ):
    try:
        with open(f"{REPO}/{targ}", "r") as pkg:
            pkg_data = pkg.readlines()

        pkg_type = pkg_data[0]
        pkg_link = pkg_data[1]
        written_depends = pkg_data[2:]

        if written_depends != []:
            for depend in written_depends:
                open(f"{INSTALL}/{depend}.zip", "wb").write(get(depend).content)
                extract(depend)
                remove(f"{INSTALL}/{depend}.zip")

        open(f"{INSTALL}/{targ}.zip", "wb").write(get(pkg_link).content)
        extract(targ)
        remove(f"{INSTALL}/{targ}.zip")

    except FileNotFoundError:
        print("ERR! Package doesn't exist.")


def uninstall(targ):
    print(targ)
