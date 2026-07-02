#!/bin/bash

#
# svg2ico Inkscape Extension Installer
# Automatic installation script for Linux and macOS
#

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Detect OS
OS_TYPE=$(uname -s)

echo -e "${YELLOW}svg2ico Inkscape Extension Installer${NC}"
echo "======================================"
echo ""

# Determine Inkscape extensions directory
if [ "$OS_TYPE" = "Darwin" ]; then
    # macOS
    INKSCAPE_EXT_DIR="$HOME/Library/Application Support/Inkscape/extensions"
elif [ "$OS_TYPE" = "Linux" ]; then
    # Linux
    INKSCAPE_EXT_DIR="$HOME/.config/inkscape/extensions"
else
    echo -e "${RED}Error: Unsupported operating system ($OS_TYPE)${NC}"
    echo "Please install manually. See README.md for instructions."
    exit 1
fi

echo "Detected OS: $OS_TYPE"
echo "Inkscape extensions directory: $INKSCAPE_EXT_DIR"
echo ""

# Check if extensions directory exists
if [ ! -d "$INKSCAPE_EXT_DIR" ]; then
    echo -e "${YELLOW}Creating Inkscape extensions directory...${NC}"
    mkdir -p "$INKSCAPE_EXT_DIR"
    if [ $? -ne 0 ]; then
        echo -e "${RED}Error: Could not create extensions directory${NC}"
        exit 1
    fi
fi

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Copy extension files
echo "Installing svg2ico extension files..."

if [ ! -f "$SCRIPT_DIR/svg2ico.py" ]; then
    echo -e "${RED}Error: svg2ico.py not found in $SCRIPT_DIR${NC}"
    exit 1
fi

if [ ! -f "$SCRIPT_DIR/svg2ico.inx" ]; then
    echo -e "${RED}Error: svg2ico.inx not found in $SCRIPT_DIR${NC}"
    exit 1
fi

# Copy files
cp "$SCRIPT_DIR/svg2ico.py" "$INKSCAPE_EXT_DIR/svg2ico.py"
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Could not copy svg2ico.py${NC}"
    exit 1
fi

cp "$SCRIPT_DIR/svg2ico.inx" "$INKSCAPE_EXT_DIR/svg2ico.inx"
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Could not copy svg2ico.inx${NC}"
    exit 1
fi

# Make Python script executable
chmod +x "$INKSCAPE_EXT_DIR/svg2ico.py"
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Could not set execute permissions on svg2ico.py${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Extension files installed successfully${NC}"
echo ""

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}⚠ Warning: Python 3 is not installed or not in PATH${NC}"
    echo "  The extension requires Python 3.6 or later"
    echo "  Please install Python 3 before using the extension"
    echo ""
fi

# Check for Pillow
echo "Checking for required Python dependencies..."
python3 -c "from PIL import Image" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠ Warning: Pillow (PIL) is not installed${NC}"
    echo "  Installing Pillow is required for the extension to work"
    echo ""
    echo "  Install it using:"
    if [ "$OS_TYPE" = "Darwin" ]; then
        echo "    pip3 install Pillow"
    else
        echo "    Ubuntu/Debian: sudo apt-get install python3-pil"
        echo "    Fedora/RHEL:   sudo dnf install python3-pillow"
        echo "    Or:            pip3 install Pillow"
    fi
    echo ""
else
    echo -e "${GREEN}✓ Pillow is installed${NC}"
fi

echo ""
echo -e "${GREEN}Installation complete!${NC}"
echo "Please restart Inkscape for the extension to appear in the menu."
echo ""
echo "To use svg2ico:"
echo "  1. Open or create an SVG file in Inkscape"
echo "  2. Go to Extensions > Export > SVG to ICO"
echo "  3. Select the desired size and output filename"
echo "  4. Click Apply"
