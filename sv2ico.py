#!/usr/bin/env python

#
# svg2ico.py
# Create Win ico files easily.
#
# Copyright (C) 2008 M. Aru <ginopc(a)tiscali.it>
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
__version__ = "0.1"

import os
import sys
import subprocess

# check comandline parameters
#
# 
# Syntax: svg2ico.py filename [-w WIDTH] [-h HEIGHT]
if len(sys.argv)!=2:
	sys.exit("Usage\tInput PNG file\n")

oFileName=sys.argv[1]
fileList=[]

class Svg2Ico:
	"""A simple class"""
	width=16
	heigth=16
	fileName='icon.ico'
	
	def _init(self, width, height):
	   self.width=width
	   self.heigth=height
	   
	def saveToFilename(fileName):
	   self.fileName=fileName
		return 'hello world'
		
if __name__ == '__main__':   #pragma: no cover
    e = svg2ico()
    e.affect()