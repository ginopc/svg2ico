# svg2ico

Inkscape extension for exporting SVG artwork as a Windows `.ico` file.

Original extension by [Maurizio Aru](https://github.com/ginopc). This fork updates the extension for modern Inkscape and modern Windows icon expectations while preserving the original project and license credit.

Current fork version: `1.0.0`

## What's Improved

- Works with current Inkscape `File > Save As` output extension flow
- Exports a multi-size `.ico` by default
- Embeds these icon sizes in one file:
  `16`, `24`, `32`, `48`, `64`, `128`, `256`
- Removes the old extra options prompt during export

## Installation

Copy these files into your Inkscape user extensions folder:

- `svg2ico.inx`
- `svg2ico.py`

On Windows this is usually:

`%AppData%\inkscape\extensions`

Then restart Inkscape.

## Usage

In Inkscape:

1. Open your SVG.
2. Choose `File > Save As...`
3. Select `Win Icon File (*.ico)`.
4. Save the file.

The exported `.ico` contains multiple embedded sizes so Windows can choose the most appropriate one automatically.

## Notes

- This extension targets Windows `.ico` output.
- The largest embedded icon size is `256x256`, which is the practical top-end for Windows ICO content.

## Attribution

- Original author: [Maurizio Aru](https://github.com/ginopc)
- Modernization and compatibility updates: this fork

See [CHANGELOG.md](./CHANGELOG.md) for a summary of fork changes.
