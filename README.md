# Description
This program helps D&D 5e players to create and level up their characters.  It is designed to keep track of everything that would affect roll modifiers, hit points, armor class, spell save DCs, etc., and to calculate those values.  It tracks race, classes (allowing multiclassing), background, feats, proficiencies, class archetypes, fighting styles, and armor.  When the program is done running it outputs a text file containing information that can be copied to a character sheet, and that same text file can be read back in to the program later in order to add a level to the character.  Although the program is command-line, it is designed to be used by non-programmers, i.e. if you type something that is not a valid response, it will show you the possible choices and then ask again.  Capitalization is ignored, and user input can be abbreviated as long as the program can distinguish among the possible choices, e.g. you can type "str" instead of "Strength".

# Requirements
[Python 3](https://www.python.org), including modules "random", "os", and "platform", which are part of the standard installation.

On Android, this program will run with [QPython3](https://play.google.com/store/apps/details?id=com.hipipal.qpy3).

# Running the program
On Windows (and probably other operating systems), after you have installed Python 3 and downloaded `ddcharsheet.py`, you can simply double-click on ddcharsheet.py to launch the program.  By default, files will be output to the same folder where the program is.

On Android, after installing QPython3, save `ddcharsheet.py` to `/storage/emulated/0/com.hipipal/qpyplus/scripts3/`.  Open the QPython3 app, tap "Programs", "ddcharsheet.py", then "Run".  By default, files will be output to your device's Documents folder.