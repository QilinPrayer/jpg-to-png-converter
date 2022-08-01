"""
Simple JPG to PNG converter made for
Complete Python Developer in 2022: Zero to Mastery class.
Takes two system arguments:
/target_dir - folder with jpg files to be converted
/receiving_dir - folder to send new png files
"""

import sys
from pathlib import Path
from PIL import Image

# grab first and second argument
first = sys.argv[1]
second = sys.argv[2]

# check if \new\ (folder) exists, if not create
receiving_dir = Path(f".{second}")
if not receiving_dir.exists():
    receiving_dir.mkdir()

# loop through Pokedex
target_dir = Path(f".{first}")
target_iter = [jpg for jpg in target_dir.iterdir(
) if jpg in list(target_dir.glob('**/*.jpg'))]
# convert images to png
for jpg in target_iter:
    outfile = f'.{second}/{Path(jpg).stem}.png'
    with Image.open(jpg) as img:
        img.save(outfile)
# save to the new folder
