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
__version__ = "1.0.0"

import os
import struct

import inkex
from inkex.command import take_snapshot
from PIL import Image


class Svg2Ico(inkex.OutputExtension):
    icon_sizes = (16, 24, 32, 48, 64, 128, 256)

    def save(self, stream):
        entries = []
        try:
            for size in self.icon_sizes:
                entries.append(self.render_icon_image(size))
            self.write_ico(entries, stream)
        finally:
            for _, png_name in entries:
                if os.path.exists(png_name):
                    os.unlink(png_name)

    def render_icon_image(self, size):
        png_name = take_snapshot(
            self.document,
            self.tempdir,
            name="svg2ico-{0}".format(size),
            ext="png",
            export_width=size,
            export_height=size,
        )

        with Image.open(png_name) as img:
            icon = img.convert("RGBA")
            if icon.size != (size, size):
                icon = icon.resize((size, size), Image.Resampling.LANCZOS)
            return self.ico_image_data(icon), png_name

    @staticmethod
    def ico_image_data(img):
        width, height = img.size
        xor_rows = []
        and_rows = []
        rgba = img.load()
        mask_stride = ((width + 31) // 32) * 4

        for y in range(height - 1, -1, -1):
            xor_row = bytearray()
            mask_row = bytearray(mask_stride)

            for x in range(width):
                r, g, b, a = rgba[x, y]
                xor_row.extend((b, g, r, a))
                if a == 0:
                    mask_row[x // 8] |= 0x80 >> (x % 8)

            xor_rows.append(bytes(xor_row))
            and_rows.append(bytes(mask_row))

        xor_bitmap = b"".join(xor_rows)
        and_bitmap = b"".join(and_rows)
        return struct.pack(
            "<IIIHHIIIIII",
            40,
            width,
            height * 2,
            1,
            32,
            0,
            len(xor_bitmap) + len(and_bitmap),
            0,
            0,
            0,
            0,
        ) + xor_bitmap + and_bitmap

    @staticmethod
    def write_ico(entries, stream):
        header = struct.pack("<HHH", 0, 1, len(entries))
        stream.write(header)

        directory_size = 6 + (16 * len(entries))
        offset = directory_size

        for image_data, _ in entries:
            dib_header = image_data[:40]
            width = struct.unpack("<I", dib_header[4:8])[0]
            height = struct.unpack("<I", dib_header[8:12])[0] // 2
            icon_width = 0 if width == 256 else width
            icon_height = 0 if height == 256 else height
            entry = struct.pack(
                "<BBBBHHII",
                icon_width,
                icon_height,
                0,
                0,
                1,
                32,
                len(image_data),
                offset,
            )
            stream.write(entry)
            offset += len(image_data)

        for image_data, _ in entries:
            stream.write(image_data)


if __name__ == "__main__":
    Svg2Ico().run()
