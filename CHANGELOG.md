# Fountainhead Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).
Restart Sublime Text and re-open Fountain files for the updates to be properly applied.


## [1.0.0] - 2015-02-17
Happy to announce that version 1.0.0 has finally arrived for Fountainhead. This version is about creating a great writing and editing environment. Future versions will deal with previewing and converting screenplays.

### Added
- Ability to capitalize entire lines of text using ⌘K,K / ⌃K,K. See below for full documentation. Great when editing!
- Manual Capitalization section in the help documentation.
- Reference and link to the Input font for coding, by Font Bureau. Read more about it here: http://input.fontbureau.com
- Dialogue and Lyric syntax scopes. Lyrics are character dialogue that begin with ~.
- Ability to change between single or double line spacing after Dialogue, using the dialogue_double_line_space setting.
- README.md FAQ entry on beginning characters that end in a period (e.g., JR.) with an "@".

### Changed
- Scene and Character lists retain their capitalization as entered, which means they will most likely be in all uppercase letters (except @ characters). Great when editing!
- Improved support for default Sublime Text Color Schemes. Dialogue and Lyrics default to foreground (Action) colors, and Characters default to string scopes.
- All version updates combined into a single change log (CHANGELOG.md).
- All color schemes to use the new Dialog, Lyrics, and Character scopes.

### Fixed
- Removed Default.sublime-keymap, which was causing conflicts with the Default (OSX).sublime-keymap file, and is redundant with the Linux and Windows keymap files.
- Scene and Character pop-up menus are updated properly when new scenes/characters are entered (Sublime Text 3 feature).
- Pressing Enter/Return at the end of a parenthetical will no longer make the line uppercase.
- Dialogue that is not a complete sentence will no longer be automatically capitalized when Enter/Return is pressed.

### Notes

#### Manual Capitalization

For those times that manual capitalization is needed (e.g., edits), the following commands are provided:

Key Combination     | Performs the Following Action
--------------------|-------------------------------
⌘K,⌘L / ⌃K,⌃L (1) | Convert highlighted text to lowercase
⌘K,⌘U / ⌃K,⌃U (1) | Convert highlighted text to uppercase
⌘K,K / ⌃K,K (2)    | Capitalize the entire line

(1) The comma is used to separate the sequence of key presses (X,Y is equal to "Press X, and then press Y").

(2) All commands use lowercase letters (e.g., K is equal to pressing k), unless preceded by ⇧/Shift.

The above commands can also be selected through the use of menus:

[[Tools > Fountainhead > Convert to Lowercase]]
[[Tools > Fountainhead > Convert to Uppercase]]
[[Tools > Fountainhead > Capitalize Current Line]]
or
[[Tools > Command Palette]] (⇧⌘P / ⇧⌃P) and entering "Fountainhead: Convert to Lowercase"
[[Tools > Command Palette]] (⇧⌘P / ⇧⌃P) and entering "Fountainhead: Convert to Uppercase"
[[Tools > Command Palette]] (⇧⌘P / ⇧⌃P) and entering "Fountainhead: Capitalize Current Line"


## [0.7.0] - 2015-01-28

### Added
- OpenDyslexic monospaced font to settings. Read more about this font, which helps dyslexic individuals, at http://opendyslexic.org
- Instructions on how to install fonts added to the README and help files.

### Notes

#### Installing Fonts

##### Mac

1. Double-click the font file (usually ending in .otf or .ttf)
2. The Font Book app will open and display the font
3. Click Install Font on the bottom of the preview window

##### Windows

Taken from http://windows.microsoft.com/en-us/windows-vista/install-or-uninstall-fonts

1. Open Fonts by clicking the Start button, clicking Control Panel, clicking Appearance and Personalization, and then clicking Fonts.
2. Click File, and then click Install New Font.
    - If you don't see the File menu, press ALT.
3. In the Add Fonts dialog box, under Drives, click the drive where the font that you want to install is located.
4. Under Folders, double-click the folder containing the fonts that you want to add.
5. Under List of fonts, click the font that you want to add, and then click Install.

##### Linux (Ubuntu)

1. Double-click the font file (usually ending in .otf or .ttf)
2. Font Viewer will launch and display the font
3. Click Install Font in the lower right-hand corner of the preview window


## [0.6.1] - 2015-01-23

### Fixed
- Add missing ő and ű (Thanks to fricy for finding the issue).
- Cleaned up Fountainhead.tmLanguage scene_headings scope to remove redundant capital letters (since the ?i regex makes it case insensitive).


## [0.6.0] - 2015-01-22

### Added
- Support for accented characters.


## [0.5.1] - 2014-12-19

### Fixed
- Action text with parentheses no longer auto-capitalizes.


## [0.5.0] - 2014-12-18

### Added
- Anatomatic's Night Owl color scheme.


## [0.4.2] - 2014-12-16

### Fixed
- Action and Dialogue spacing issues and they no longer auto-capitalize.


## [0.4.1] - 2014-12-16

### Fixed
- Character auto-capitalization.


## [0.4.0] - 2014-12-16

### Added
- Help documentation now located in Tools > Fountainhead > Help

### Changed
- README.md to include the new documentation.
- By default, no Fountainhead color schemes are selected in settings, allowing the user to select Sublime Text's general color schemes. Fountain-only color schemes can be selected in Fountainhead's user settings.

### Fixed
- Cleaned up fountain syntax support and added the ability to use \* to produce a * in your script.


## [0.3.5] - 2014-12-02

### Fixed
- Fountain syntax found using comparison to path name for ST2 support.


## [0.3.4] - 2014-12-01

### Changed
- File settings are retrieved using view.settings().get() as opposed to sublime.load_settings().get().


## [0.3.3] - 2014-11-30

### Changed
- Character and Scene completion files created in User/Fountainhead/.
- User/Fountainhead/ is created if it doesn't currently exist.


## [0.3.2] - 2014-11-30

### Fixed
- SublimeHelper in sublime_helper/__init__.py is now imported properly.


## [0.3.1] - 2014-11-30

### Changed
- Move SublimeHelper into sublime_helper/__init__.py.


## [0.3.0] - 2014-11-30

### Added
- Sublime Text 2 support.


## [0.2.0] - 2014-11-29

### Added
- Support for Character and Scene Lists in Windows and Linux.


## [0.1.0] - 2014-11-21

Initial release.