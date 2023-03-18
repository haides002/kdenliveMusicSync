# kdenliveMusicSync
A lil python script, that creates json for your kdenlive projec, in order to get markers on every single beat of a so.

## Usage
You edit the Variables at the top of the file in order to make it match your song. Then you paste the output of the script into your Kdenlive project. Id suggest you **make a backup** before you tamper with the project file. I would recommend only using this if you know at least a bit about json.

## Example
``` python
FPS = 60
MARKERTYPE = 0
BPM = 150
OFFSET = 0
SONGLENGTH = 16654
```
these variables gave me the markers I needed and i put them in the <property ```name="kdenlive:markers">[]``` list in the audiotrack.
And I created this [ULTRAKILL](devilmayquake.com) clip compilation.
<iframe width="560" height="315" src="https://www.youtube.com/embed/c3mXKyQGOtU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
