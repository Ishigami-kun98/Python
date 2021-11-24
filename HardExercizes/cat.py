import sys
import os, sys
from stat import *
def chmod(fn, mode):
    os.chmod(fn, int(mode, base=8))
def cat(fn):
    print(open(fn).read()[:-1])

if __name__ == "__main__":
    chmod(sys.argv[2], sys.argv[1])
    #cat(sys.argv[1])