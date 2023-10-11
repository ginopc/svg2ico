# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.0.0] - 2023-10-11
### Changed
- Migrated to Python 3. This extension is now compatible with Inkscape 1.0 or later (but not prior versions).
- Instead of picking a single image size for the ICO, you can now embed multiple images via the `Sizes` page in the Export Settings Dialog.
- Now uses Inkscape's [inkex library](https://inkscape.gitlab.io/extensions/documentation/index.html).

### Added
- Added the option to embed either PNG (default) or BMP images into the ICO file via the `Format` page in the Export Settings Dialog.


## [0.2] - 2018-11-15
- Initial version by [Maurizio Aru](https://github.com/ginopc)