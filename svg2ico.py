#!/usr/bin/env python3

#
# svg2ico.py
# Create Win ico files easily.
#
# Copyright (C) 2008 Maurizio Aru <ginopc(a)tiscali.it>
# 
# Based on icon_generator code extesion by David R. Damerell (david@nixbioinf.org)
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
__version__ = "0.3"

import os
import sys
import subprocess
import argparse
import inkex
import io
from PIL import Image
from PIL import ImageOps

class IcoOutput(inkex.RasterOutputExtension):
	def add_arguments(self, pars):
		pars.add_argument("--sizes", type=str, default="16,32,64")

	def save(self, stream):
		# Get the specified sizes as a comma-separated string and convert to a list of integers
		sizes_str = self.options.sizes
		sizes = [int(size.strip()) for size in sizes_str.split(',')]

		# Initialize a list to store the resized PNG images
		png_images = []

		# Open a file for writing
		with open("/Users/watkinsp/source/repos/svg2ico/introspection_output.txt", "w") as output_file:
			# Redirect the output to the file using the file parameter
			print(dir(self.img), file=output_file)

		# Render the SVG for each size and resize the images
		for size in sizes:
			image = io.BytesIO()
			self.img.convert("RGBA").save(
				image,
				format="png"
			)

			# Append the resized image to the list
			png_images.append(image)

		# Determine the number of images based on the sizes
		num_images = len(sizes)

		# Create an ICO file with all the images
		with io.BytesIO() as ico_file:
			ico_file.write(b'\x00\x00\x01\x00')  # ICO header (ICO file type)
			ico_file.write(int.to_bytes(num_images, 2, 'little'))  # Number of images

			# Image directory entries for each size
			offset = 6 + (16 * num_images)  # Offset to the image data
			for i, size in enumerate(sizes):
				png_data_size = png_images[i].getbuffer().nbytes
				ico_file.write(bytes([size]))  # Width
				ico_file.write(bytes([size]))  # Height
				ico_file.write(bytes([0]))  # Color count (0 = no palette)
				ico_file.write(bytes([0]))  # Reserved (0)
				ico_file.write(int.to_bytes(1, 2, 'little'))  # Color planes (1)
				ico_file.write(int.to_bytes(32, 2, 'little'))  # Bits per pixel (32-bit RGBA)
				ico_file.write(int.to_bytes(png_data_size, 4, 'little'))  # Image size
				ico_file.write(int.to_bytes(offset, 4, 'little'))  # Offset to image data
				offset += png_data_size

			# Image data for each size
			for image in png_images:
				ico_file.write(image.getvalue())

			# Save the ICO data to the standard output (STDOUT)
			stream.write(ico_file.getvalue())

if __name__ == "__main__":
	IcoOutput().run()

