# svg2ico

Inkscape extension to save image to WinIco file.

## Project Description

**svg2ico** is an extension for [Inkscape](https://inkscape.org/) that allows you to convert and export SVG vector drawings to Windows icon files in `.ico` format. The extension supports various standard sizes (16x16, 32x32, 48x48 pixels) and makes it easy to generate professional icons directly within Inkscape without needing additional software.

### Features
- Direct conversion from SVG to ICO
- Support for multiple icon sizes
- Integrated interface in Inkscape
- Compatible with Inkscape 0.92 and later

## Installation

### Automatic Installation (Recommended)

#### Linux / macOS
1. Download the repository or extract the archive
2. Open a terminal in the folder containing the files
3. Run the installation script:
   ```bash
   bash install.sh
   ```
4. Follow the on-screen instructions
5. Restart Inkscape

#### Windows
1. Download the repository or extract the archive
2. Double-click `install.bat`
3. If prompted, click "Run anyway" in the security message
4. Follow the on-screen instructions
5. Restart Inkscape

---

### Manual Installation

#### Linux
1. Locate the Inkscape extensions folder:
   ```bash
   ~/.config/inkscape/extensions/
   ```
2. Copy the files `svg2ico.py` and `svg2ico.inx` to the extensions folder
3. Make the `svg2ico.py` file executable:
   ```bash
   chmod +x ~/.config/inkscape/extensions/svg2ico.py
   ```
4. Restart Inkscape

#### macOS
1. Locate the Inkscape extensions folder:
   ```bash
   ~/Library/Application\ Support/Inkscape/extensions/
   ```
2. Copy the files `svg2ico.py` and `svg2ico.inx` to the extensions folder
3. Make the `svg2ico.py` file executable:
   ```bash
   chmod +x ~/Library/Application\ Support/Inkscape/extensions/svg2ico.py
   ```
4. Restart Inkscape

#### Windows
1. Locate the Inkscape extensions folder (usually):
   ```
   C:\Program Files\Inkscape\share\extensions\
   ```
2. Copy the files `svg2ico.py` and `svg2ico.inx` to the extensions folder
3. Restart Inkscape

## Usage

1. Open or create an SVG drawing in Inkscape
2. Select the object you want to convert to an icon
3. Go to the **Extensions > Export** menu and select **SVG to ICO**
4. Choose the desired size (16x16, 32x32 or 48x48)
5. Specify the output filename
6. Click **Apply**

### Installation Troubleshooting

#### "Extension does not appear in Inkscape menu"
- Verify that the files `svg2ico.py` and `svg2ico.inx` are in the correct folder
- Make sure `svg2ico.py` is executable (Linux/macOS): `chmod +x svg2ico.py`
- Completely restart Inkscape
- Check Inkscape logs: Help > System Console

#### "Error: Pillow not found"
Install the Pillow library:
- **Ubuntu/Debian**: `sudo apt-get install python3-pil`
- **Fedora/RHEL**: `sudo dnf install python3-pillow`
- **macOS**: `pip3 install Pillow`
- **Windows**: `pip install Pillow`

#### "Error: Python 3 not found"
Install Python 3:
- **Ubuntu/Debian**: `sudo apt-get install python3`
- **Fedora/RHEL**: `sudo dnf install python3`
- **macOS**: `brew install python3`
- **Windows**: Download from https://www.python.org/downloads/

## Technical Information

### Plugin Architecture

svg2ico is a native Inkscape extension that extends the `extension.Effect` class of the Inkscape framework. The extension integrates a visual panel within the Inkscape editor to allow users to configure export parameters.

### Conversion Flow

1. **Parameter Loading**: The user selects the icon size (16x16, 32x32 or 48x48) and specifies the output filename through the graphical interface
2. **SVG to PNG Export**: The SVG document open in Inkscape is exported to a temporary PNG file using Inkscape's rendering engine via command line
3. **Resizing**: The PNG image is resized to the requested size using the **LANCZOS** algorithm to maintain quality
4. **ICO Conversion**: The PNG image is converted to Windows ICO format using the PIL/Pillow library
5. **Cleanup**: The temporary PNG file is automatically deleted

### Plugin Configuration

The plugin is configured through the `svg2ico.inx` file which defines:

- **ID**: `org.inkscape.output.svg2ico` - Unique plugin identifier
- **Parameters**:
  - `--s`: Icon size (16, 32 or 48 pixels)
  - `--o`: Output filename (must end with `.ico`)
- **Export Type**: Output in ICO format (Windows Icon File)
- **Interpreter**: Python 3

### Dependencies

#### Required
- **Inkscape 1.0+**: Rendering engine and extension framework
- **Python 3.6+**: Python interpreter to run the script
- **Pillow/PIL**: Python library for image manipulation

#### Optional
- **ImageMagick** (convert): Alternative for image conversion (fallback)

### Dependency Installation

#### Ubuntu/Debian
```bash
sudo apt-get install python3-pil
```

#### Fedora/RHEL
```bash
sudo dnf install python3-pillow
```

#### macOS
```bash
pip3 install Pillow
```

#### Windows
```bash
pip install Pillow
```

### Supported Formats

**Input**: SVG (Scalable Vector Graphics)
**Output**: ICO (Windows Icon File)

**Supported color modes**:
- RGB (Red, Green, Blue)
- RGBA (RGB + Transparency)
- Palette (automatically converted to RGBA)
- Grayscale

### Current Limitations

- Supported sizes are limited to 16x16, 32x32 and 48x48 pixels
- Conversion occurs via rasterization (vector → raster)
- Requires Inkscape to be properly installed on the system

## Work in Progress

### Known Issues
- [ ] **Inkscape 1.0+ Compatibility**: Update support for Inkscape 1.0+ APIs and later versions
- [ ] **Alpha Channel**: Improve transparency handling (alpha channel) in converted PNG images
- [ ] **Additional Sizes**: Add support for other standard icon sizes (256x256, 512x512)
- [ ] **Batch Conversion**: Implement simultaneous conversion of multiple icons
- [ ] **Preview**: Add an icon preview before export

## About

* Author: [Maurizio Aru](https://github.com/ginopc)
* License: GNU General Public License v2.0
