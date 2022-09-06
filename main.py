#!/usr/bin/env python

from argparse import ArgumentParser
from rice import install, uninstall, CWD, INSTALLED, REPO
from os import path, mkdir

if not path.exists(INSTALLED):
    print("NOTIF! CREATING INSTALLED DIRECTORY...")
    mkdir(INSTALLED)

if not path.exists(REPO):
    print("NOTIF! CREATING REPO DIRECTORY...")
    mkdir(REPO)


parser = ArgumentParser(description="A little package manager.")
parser.add_argument(
    "--install", "--i", default=False, dest="i_target", help="Install a package."
)
parser.add_argument(
    "--uninstall", "--u", default=False, dest="u_target", help="Uninstall a package"
)

args = parser.parse_args()

if args.i_target:
    install(args.i_target)

if args.u_target:
    uninstall(args.u_target)
