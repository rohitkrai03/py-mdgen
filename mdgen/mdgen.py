

import sys
import utils

import os

# get the source directory
source = os.path.normpath(sys.argv[1])
# get the target directory
target = os.path.normpath(sys.argv[2])

utils.convert_md_directory(source, target)

print("HTML files for your markdown has been generated in {}".format(target))

