
# Swiatelka
* swiatelka - change lights in UMCS windows.

# Synopsis
* `swiatelka [-h] [-f FILENAME | -c COLOR | -b] [-p]`

# Prerequisites
* Python 3.6 or higher
* requirements from [requirements.txt](requirements.txt)
* `venv` (optional)

# Installation
* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`

# Usage
* `./swiatelka.py -[the option]`
* `python3 swiatelka.py -[the option]`

# Description
> Change lights in UMCS windows.

| Options   |           |
|-----------|-----------|
| `-h`, `--help` | Show help message and exit |
| `-f [FILENAME]`, `--filename [FILENAME]` | Bitmap file to display (*you can use your own .bmp files or pre-existing templates from the "Grafiki" folder*) |
| `-c [COLOR]`, `--color [COLOR]` | Display solid color on the windows (*observe the values corresponding to the color option*)|
| `-b`, `--blackout` | Turns off all the lights on the windows - changes color to black|
| `-p [PATTERN]`, `--preview [PATTERN]` | Preview pattern on terminal instead of displaying on the windows|
| `-pa`, `--preview-all` | Preview all patterns on terminal from folder "Grafiki"|
***
> #### Pre-existing templates from the "Grafiki" folder :
* [`MFII.bmp`](Grafiki/MFII.bmp) - the inscription "I ❤️ MFII"
* [`Polska.bmp`](Grafiki/Polska.bmp) - the flag of Poland
* [`Ukraina.bmp`](Grafiki/Ukraina.bmp) - the flag of Ukraine
* [`UMCS.bmp`](Grafiki/UMCS.bmp) - the inscription "I ❤️ UMCS"
* [`MFII_wide.bmp`](Grafiki/MFII_wide.bmp) - the inscription "MFII"
***
> #### Values corresponding to the color option :
* black
* white
* light_gray
* gray
* dark_gray
* red
* pink
* purple
* light_blue
* blue
* yellow_green
* green
* yellow
* orange
* brown
* pale_pink
***
###### *Made by SKNI*
