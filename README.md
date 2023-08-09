# Swiatelka
* swiatelka - change lights in UMCS windows.

# Prerequisites
* Python 3.6 or higher
* requirements from [requirements.txt](requirements.txt)
* `venv` (optional)

# Installation
* user in group `dialout`
* `python3 -m venv venv` (optional)
* `source venv/bin/activate` (optional)
* `pip install -r requirements.txt`

# Usage
* `./swiatelka.py [-h] [-f FILENAME | -c COLOR | -b] [-p]`
* `python3 swiatelka.py [-h] [-f FILENAME | -c COLOR | -b] [-p]`

# Description
> Change lights in UMCS windows.

| Options   |           |
|-----------|-----------|
| `-h`, `--help` | Show help message and exit |
| `-f [FILENAME]`, `--filename [FILENAME]` | Bitmap file to display (*you can use your own `5x28px` .bmp files or pre-existing templates from the "Grafiki" folder*) |
| `-c [COLOR]`, `--color [COLOR]` | Display solid color on the windows (*observe the values corresponding to the color option*)|
| `-b`, `--blackout` | Turns off all the lights on the windows - changes color to black|
| `-p [PATTERN]`, `--preview [PATTERN]` | Preview pattern on terminal instead of displaying on the windows|
| `-pa`, `--preview-all` | Preview all patterns on terminal from folder "Grafiki"|
***
> #### Pre-existing templates from the "Grafiki" folder :
* [MFII.bmp](Grafiki/MFII.bmp) - the inscription "I ❤️ MFII" ![MFII](https://git.skni.umcs.pl/skni/swiatelka/-/raw/master/Grafiki/MFII.bmp)
* [Polska.bmp](Grafiki/Polska.bmp) - the flag of Poland ![Polska](https://git.skni.umcs.pl/skni/swiatelka/-/raw/master/Grafiki/Polska.bmp)
* [Ukraina.bmp](Grafiki/Ukraina.bmp) - the flag of Ukraine ![Ukraina](https://git.skni.umcs.pl/skni/swiatelka/-/raw/master/Grafiki/Ukraina.bmp)
* [UMCS.bmp](Grafiki/UMCS.bmp) - the inscription "I ❤️ UMCS" ![UMCS](https://git.skni.umcs.pl/skni/swiatelka/-/raw/master/Grafiki/UMCS.bmp)
* [MFII_wide.bmp](Grafiki/MFII_wide.bmp) - the inscription "MFII" ![MFII_wide](https://git.skni.umcs.pl/skni/swiatelka/-/raw/master/Grafiki/MFII_wide.bmp)
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

## D-Bus daemon configuration:
put the pl.umcs.skni.LedManager.conf file in
/etc/dbus-1/system.d

## Mirrors:
* <https://git.skni.umcs.pl/skni/swiatelka> — main development repozitory
* <https://github.com/skni-umcs/swiatelka> — Mirror
***
###### *Made by SKNI*

