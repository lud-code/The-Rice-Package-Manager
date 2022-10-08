from os import getcwd

CWD = getcwd()
INSTALLED = f"{CWD}/installed/"
REPO = f"{CWD}/repo/"


def install(targ):
    try:
        with open(f"{REPO}/{targ}") as pkg:
            pkg_data = pkg.readlines()

        pkg_type = pkg_data[0]
        pkg_link = pkg_data[1]
        pkg_dependency = pkg_data[2:]

    except FileNotFoundError:
        print("ERR! Package doesn't exist.")


def uninstall(targ):
    print(targ)
