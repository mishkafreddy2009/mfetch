import shutil
import os

def get_chmod():
    os.system("chmod a+x mf.py")

def move_to_bin():
    shutil.copyfile("mf.py", "/usr/local/bin/mf")

def main():
    get_chmod()
    move_to_bin()

if __name__ == "__main__":
    main()

