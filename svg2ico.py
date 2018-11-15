#!/usr/bin/env python

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
__version__ = "0.2"

import os
import sys
import subprocess
import argparse

#
# Sgv2Ico Main Class
#
class Svg2Ico:
	
	width = 16
	heigth = 16
	ifName = 'in.png'
	ofName = 'out.ico'
	
	def __init__(self, size, iName):
		self.width = size
		self.heigth = size
		self.ifName = iName
	   
	def createPPM(pnfFileName, isAlphaChannel):
		return 0
		
	def resizeImage(self, iFile, oFile, width):
	   return 0
	   
	def convertToIco(self, iFile):
		return 0
	   
	def saveToFilename(self, fName):
		self.ofName = fName
		print("[DEBUG] Width: %d, Heigth: %d" % (self.width, self.heigth))
		print("[DEBUG] iFile: %s, oFile: %s" % (self.ifName, self.ofName))
		from PIL import Image
		img = Image.open(self.ifName)
		img.save(fName)

#
# Check command line parameters
# 
def parseOptions():
	parser = argparse.ArgumentParser(description='Convert svg to ico')
	parser.add_argument('--s', type=int, default=16, help='Icon Size')
	parser.add_argument('--o', default="file.ico", help='Output FileName')
	parser.add_argument('iFile', default="file.png", help='Input FileName')
	args = parser.parse_args()
	return args

		
if __name__ == '__main__':   #pragma: no cover
	args = parseOptions()
	e = Svg2Ico(args.s, args.iFile)
	e.saveToFilename(args.o)

