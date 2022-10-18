from os import getcwd, remove, rmdir, rename, system, path
from shutil import rmtree
from requests import get
from zipfile import ZipFile

CWD = getcwd()
INSTALL = f"{CWD}/install/"
REPO = f"{CWD}/repo/"


def extract(file, link):
    if path.exists(f"{INSTALL}/{file}"):
        print("NOTIF! Package already exists.")
        reinst = input("ASK! Reinstall? [y/N]")

        if reinst == "y" or reinst == "Y":
            rmtree(f"{INSTALL}/{file}")

        else:
            exit()

    open(file, "wb").write(get(link).content)

    with ZipFile(f"{INSTALL}/{file}.zip", "r") as zip:
        dir = zip.namelist()[0]
        zip.extractall(f"{INSTALL}")
        rename(f"{INSTALL}/{dir}", f"{INSTALL}/{file}")
        remove(f"{INSTALL}/{file}.zip")


def fix(cmd, name, run):
    if cmd != "NA":
        system(f"cd {INSTALL}/{name} & {cmd}")

    open(f"/usr/bin/{name}", "w").write(f"#!/usr/bin/env bash\n{run}")
    system(f"sudo chmod +x /usr/bin/{name}")


def install(targ):
    try:
        lines = open(f"{REPO}/{targ}", "r").readlines()

        pkg_run = lines[0].replace("DIR", f"{INSTALL}{targ}")
        pkg_link = lines[1]
        pkg_ccmd = lines[2]
        depends = lines[3:]

        if depends != []:
            for dep in depends:
                dep_name = dep.split("|")[0]
                dep_run = dep.split("|")[1].replace("DIR", f"{INSTALL}{dep_name}")
                dep_link = dep.split("|")[2]
                dep_ccmd = dep.split("|")[3]

                extract(f"{INSTALL}/{dep_name}.zip", dep_link)
                fix(dep_ccmd, dep_name, dep_run)

        extract(f"{INSTALL}/{targ}.zip", pkg_link)
        fix(pkg_ccmd, targ, pkg_run)

    except FileNotFoundError:
        print("ERR! Package doesn't exist.")


def uninstall(targ):
    if not path.exists(f"{INSTALL}/{targ}"):
        print("ERR! Package doesn't exists.")
        return

    rmtree(f"{INSTALL}/{targ}")
    remove(f"/usr/bin/{targ}")
