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

#
# Sgv2Ico Main Class
#
class Svg2Ico:
	
	sizes = []
	
	def __init__(self, sizes):
		self.sizes = sizes
	   
	def convert_stream(self, input_stream, output_stream):
		from PIL import Image
		import io

		try:
			import cairosvg
		except ImportError:
			sys.stderr.write(f"Error: The 'cairosvg' Python Module could not be found.\nThe running Python Interpreter is: {sys.executable}")
			sys.exit(1)


		# Read the SVG data from stdin
		svg_data = input_stream.read()
		
		# Convert SVG to PNG
		png_data = io.BytesIO(cairosvg.svg2png(bytestring=svg_data, output_width=1024, output_height=1024))

		input_svg = Image.open(png_data)

		input_svg.save(output_stream, 'ico', sizes=self.sizes)


#
# Check command line parameters
# 
def parse_options():
	parser = argparse.ArgumentParser(description='Convert SVG to ICO')
	parser.add_argument('filename', nargs='?', default=None, help='Input SVG filename (optional)')
	parser.add_argument('--s', type=lambda s: [(int(item),int(item)) for item in s.split(',')], default="16,32,64,128,256,512", help='Icon Sizes')
	args = parser.parse_args()
	return args

		
if __name__ == '__main__':   #pragma: no cover
	args = parse_options()
	e = Svg2Ico(args.s)
	e.convert_stream(sys.stdin.buffer, sys.stdout.buffer)

