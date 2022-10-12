from os import getcwd, remove, rename, system
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
        remove(f"{INSTALL}/{file}.zip")

def compile(maindir, depends):
    return


def interpret(maindir, depends):
    return


def install(targ):
    try:
        with open(f"{REPO}/{targ}", "r") as pkg:
            pkg_data = pkg.readlines()

        pkg_type = pkg_data[0].split()[0]
        pkg_where = pkg_data[1]        
        pkg_link = pkg_data[2]
        
        depends = pkg_data[3:]
        links = []

        if depends != []:
            for depend in depends:
                link = depend.split()[1]
                open(f"{INSTALL}/{link}.zip", "wb").write(get(link).content)
                extract(link)
                links.append(link)

        open(f"{INSTALL}/{targ}.zip", "wb").write(get(pkg_link).content)
        extract(targ)

        if pkg_type == "C":
            compile(f"{INSTALL}/{targ}", depends)

        if pkg_type == "I":
            interpret(f"{INSTALL}/{targ}", depends)

    except FileNotFoundError:
        print("ERR! Package doesn't exist.")


def uninstall(targ):
    print(targ)
