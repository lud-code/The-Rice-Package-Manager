#!/usr/bin/env python

from argparse import ArgumentParser
from pacman import install, uninstall

parser = ArgumentParser(description="A little package manager.")
parser.add_argument("--install", "--i", default=False, dest="i_target", help="Install a package.")
parser.add_argument("--uninstall", "--u", default=False, dest="u_target", help="Uninstall a package")

args = parser.parse_args()

if args.i_target:
    install(args.i_target)

if args.u_target:
    uninstall(args.u_target)
