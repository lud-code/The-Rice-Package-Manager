#!/usr/bin/python

from pycurl import Curl
from certifi import where
from io import BytesIO
from sys import argv
from os import cwd
from json import load

NAME = "Rice"
VERSION = "0.0.1"

# CMDS: help, add, rem, purge, up, list, find
HELP = "help"
ADD = "add"
REM = "rem"
PURGE = "purge"
UP = "up"
LIST = "LIST"
FIND = "FIND"
CWD = get_cwd()
HELP_SCREEN = f"""{NAME} v{VERSION}
Commands:
    {HELP}      -- print help screen
    {ADD}  [PKG]-- add a package
    {REM}  [PKG]-- remove a package
    {PURGE}     -- remove all orphaned packages
    {UP}   [PKG]-- update all or a selected package
    *NOTE* If no package is entered, all packages
    will be upgraded. To update ports, type in
    'new_ports' as the package.
    {LIST}      -- list all installed packages
    {LIST} [PKG]-- find a package in your ports
"""

buffer = BytesIO()
curl = Curl()


def add_pkg(pkg_name):
    try:
        port = open(f"{CWD}/{pkg_name}.json", "r")

    except FileNotFoundError:
        print("ERROR! Port does not exist!")
        
        return

    port_data = load(port)

    

def rem_pkg(pkg_name):
    return

def purge_pkg():
    return

def up_pkg(pkg_name):
    return

def list_pkg():
    return

def find_pkg(pkg_name):
    return

def main():
    cmd = argv[1:]
    head = cmd[0]
    body = cmd[1:]

    if head == HELP:
        print(HELP_SCREEN)

    if head == ADD:
        add_pkg(body)

    if head == REM:
        rem_pkg(body)

    if head == PURGE:
        purge_pkg()

    if head == UP:
        up_pkg(body)

    if head == LIST:
        list_pkg()

    if head == FIND:
        find_pkg(body)


if __name__ == "__main__":
    main()
