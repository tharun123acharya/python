import os
import sys
import pathlib
import zipfile
dirname=input("enter directory name to backup:")
if not os.path.isdir(dirname):
    print("directory,dirname,doesn't exists")
    sys.exit(0)
    curdir=pathlib.path(dirname)
    with zipfile.zipfile("myzip.zip",mode="w") as archive:
        for file in curdir.rglob("*"):
            print(file.path)
    archive.write(file.path)
    if os.path.isfile("myzip.zip"):
        print ("archive myzip.zip created successfully")
    else:
        print("error in creating zip archive")
