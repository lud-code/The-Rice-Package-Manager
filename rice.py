#!/usr/bin/env python

from argparse import ArgumentParser
from cmds import install, uninstall, CWD, INSTALLED, REPO
from os import path, mkdir

parser = ArgumentParser(description="A little package manager.")
parser.add_argument(
    "-i", default=False, dest="i_target", help="Install a package."
)
parser.add_argument(
    "-u", default=False, dest="u_target", help="Uninstall a package"
)
args = parser.parse_args()


def main():
    if not path.exists(INSTALLED):
        print("NOTIF! CREATING INSTALLED DIRECTORY...")
        mkdir(INSTALLED)

    if not path.exists(REPO):
        print("NOTIF! CREATING REPO DIRECTORY...")
        mkdir(REPO)

    if args.i_target:
        install(args.i_target)

    if args.u_target:
        uninstall(args.u_target)


if __name__ == "__main__":
    main()