#!/usr/bin/env python3

#
# svg2ico.py
# Create Win ico files easily.
#
# Copyright (C) 2023 Peter Watkins <watkipet@gmail.com>
#    Based on svg2ico
#    Copyright (C) 2008 Maurizio Aru <ginopc(a)tiscali.it>
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
__version__ = "1.0.0"

import inkex
import io

class IcoOutput(inkex.RasterOutputExtension):
	def add_arguments(self, pars):
		pars.add_argument("--tab")
		pars.add_argument("--size16", type=lambda s: s.lower()=="true", default=True)
		pars.add_argument("--size24", type=lambda s: s.lower()=="true", default=True)
		pars.add_argument("--size32", type=lambda s: s.lower()=="true", default=True)
		pars.add_argument("--size48", type=lambda s: s.lower()=="true", default=True)
		pars.add_argument("--size64", type=lambda s: s.lower()=="true", default=True)
		pars.add_argument("--size128", type=lambda s: s.lower()=="true", default=True)
		pars.add_argument("--size256", type=lambda s: s.lower()=="true", default=True)
		pars.add_argument("--format", type=str, default="png")

	def save(self, stream):
		sizes = []
		if self.options.size16: sizes.append((16,16))
		if self.options.size24: sizes.append((24,24))
		if self.options.size32: sizes.append((32,32))
		if self.options.size48: sizes.append((48,48))
		if self.options.size64: sizes.append((64,64))
		if self.options.size128: sizes.append((128,128))
		if self.options.size256: sizes.append((256,256))

		# Convert to ICO format using Pillow
		ico_image_data = io.BytesIO()
		self.img.convert("RGBA").save(
			ico_image_data,
			format="ico",
			sizes=sizes,
			bitmap_format=self.options.format.lower()
		)

		# Save the ICO data to the standard output (STDOUT)
		stream.write(ico_image_data.getvalue())

if __name__ == "__main__":
	IcoOutput().run()

