#!/usr/bin/python3.5
# find . -name pom.xml -exec sed -i 's/5.0.15-SNAPSHOT/5.0.11-SNAPSHOT/g' {} \;

from sys import argv
from pathlib import Path


def inplace_change(filename, old_string, new_string):
    with open(str(filename), 'r') as file:
        content = file.read()

    with open(str(filename), 'w') as outfile:
        content = content.replace(old_string, new_string)
        outfile.write(content)


def change_version(path, old_string, new_string):
    path = Path(path)
    for file in path.glob("**/pom.xml"):
        inplace_change(file, old_string, new_string)

def help():
    print("""Usage:
    change_version_pom.py PATH OLD_VERSION NEW_VERSION
    PATH - root path of project
    OLD_VERSION - current version
    NEW_VERSION - new version""")


if len(argv) < 4:
    help()
    exit()

path = argv[1]
old_string = argv[2]
new_string = argv[3]

change_version(path, old_string, new_string)
