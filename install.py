#!/usr/bin/env python
import shutil
import os

def get_chmod():
    os.system("chmod a+x /usr/local/bin/mfetch")

def move_to_bin():
    shutil.copyfile("mfetch.py", "/usr/local/bin/mfetch")

def main():
    move_to_bin()
    get_chmod()

if __name__ == "__main__":
    main()

