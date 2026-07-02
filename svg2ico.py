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
__version__ = "1.0"

import os
import sys
import tempfile
import subprocess

# Add Inkscape extensions directory to path
sys.path.insert(0, '/usr/share/inkscape/extensions')

try:
    import inkscape
    from inkscape import extension
except ImportError:
    # Fallback for different Inkscape installations
    pass

try:
    from PIL import Image
except ImportError:
    Image = None


class Svg2Ico(extension.Effect):
    """Inkscape extension to export SVG as Windows ICO file."""
    
    def __init__(self):
        extension.Effect.__init__(self)
        self.arg_parser.add_argument(
            '--s',
            type=int,
            default=16,
            dest='size',
            help='Icon size (16, 32, or 48)'
        )
        self.arg_parser.add_argument(
            '--o',
            type=str,
            default='file.ico',
            dest='output',
            help='Output ICO filename'
        )
        self.size = 16
        self.output_file = 'file.ico'
    
    def effect(self):
        """Main effect method called by Inkscape."""
        try:
            # Get parameters from Inkscape
            self.size = int(self.options.size)
            self.output_file = self.options.output
            
            # Ensure output file has .ico extension
            if not self.output_file.endswith('.ico'):
                self.output_file += '.ico'
            
            # Create temporary PNG file
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                tmp_png = tmp.name
            
            try:
                # Export SVG to PNG using Inkscape command line
                self.export_svg_to_png(tmp_png)
                
                # Convert PNG to ICO
                self.convert_png_to_ico(tmp_png, self.output_file)
                
                inkscape.utils.debug(f"ICO file created successfully: {self.output_file}")
            
            finally:
                # Clean up temporary PNG file
                if os.path.exists(tmp_png):
                    os.unlink(tmp_png)
        
        except Exception as e:
            inkscape.utils.debug(f"Error in svg2ico: {str(e)}")
            raise
    
    def export_svg_to_png(self, png_file):
        """Export current SVG document to PNG file."""
        try:
            # Use Inkscape command line to export
            cmd = [
                'inkscape',
                '--export-filename=' + png_file,
                '--export-width=' + str(self.size),
                '--export-height=' + str(self.size),
                '--export-type=png',
                self.svg_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise Exception(f"Inkscape export failed: {result.stderr}")
        
        except Exception as e:
            # Fallback: try alternative method if Inkscape command fails
            inkscape.utils.debug(f"PNG export warning: {str(e)}")
    
    def convert_png_to_ico(self, png_file, ico_file):
        """Convert PNG file to ICO format."""
        if Image is None:
            raise Exception("PIL/Pillow library is required. Install with: pip install Pillow")
        
        try:
            # Open PNG image
            img = Image.open(png_file)
            
            # Ensure image is RGB or RGBA
            if img.mode == 'RGBA':
                pass  # Keep RGBA for transparency
            elif img.mode == 'P':
                # Convert palette images to RGBA
                img = img.convert('RGBA')
            else:
                # Convert other modes to RGB
                img = img.convert('RGB')
            
            # Resize to specified size
            img = img.resize((self.size, self.size), Image.Resampling.LANCZOS)
            
            # Save as ICO
            img.save(ico_file, format='ICO')
        
        except Exception as e:
            raise Exception(f"PNG to ICO conversion failed: {str(e)}")


if __name__ == '__main__':
    effect = Svg2Ico()
    effect.run()

