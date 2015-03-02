

import sys
import utils

import os

# get the source directory
source = sys.argv[1]
# get the target directory
target = sys.argv[2]

utils.convert_md_directory(source, target)



