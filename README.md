# kdenliveMusicSync
A lil python script, that creates xml for your kdenlive project, in order to get markers on every single beat of a piece of music.

## Usage
You edit the Variables at the top of the file in order to make it match your song. Then you paste the output of the script into your Kdenlive project. Id suggest you **make a backup** before you tamper with the project file. I would recommend only using this if you know at least a bit about xml.

## Example
``` python
FPS = 60
MARKERTYPE = 0
BPM = 150
OFFSET = 0
SONGLENGTH = 16654
```
these variables gave me the markers I needed and i put them in the `<property name="kdenlive:markers">[]` list in the audiotrack.
And I created [this](https://youtu.be/c3mXKyQGOtU) [ULTRAKILL](http://devilmayquake.com/) clip compilation.
