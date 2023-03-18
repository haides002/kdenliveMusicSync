# variables you should assing your self
FPS = 60 # the fps of your project
MARKERTYPE = 0 # customize the type of marker

BPM = 150 # pretty self explanetory
OFFSET = 0 # how many frames until the song starts
SONGLENGTH = 16654 # length of the song in frames 


# variables that are dynamic (do not change them)
beatDuration = 60 / BPM
barDuration = beatDuration * 4
framesBetweenBars = FPS*barDuration

def calculatePos(bar):
	return (bar * framesBetweenBars) + OFFSET

def printMarkerCode(bar):
	print('    {')
	print('        "comment": "' + str(bar) + ' - 1",')
	print('        "pos": ' + str(calculatePos(bar)) + ',')
	print('        "type": ' + str(MARKERTYPE))
	print('    },')

i = 0
while (calculatePos(i) < SONGLENGTH):
	printMarkerCode(i)
	i = i + 1