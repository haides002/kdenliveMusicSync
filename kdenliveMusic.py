# variables you should assing your self
BPM = 150
FPS = 60
OFFSET = 48
MARKERTYPE = 0
SONGLENGTH = 16654

# variables that are dynamic (do not change them)
beatDuration = 60 / BPM
barDuration = beatDuration * 4
framesBetweenBars = 96
frame = 0
i = 0

def calculatePos(bar):
	return (bar * framesBetweenBars) + OFFSET

def printMarkerCode(bar):
	print('    {')
	print('        "comment": "' + str(bar) + ' - 3",')
	print('        "pos": ' + str(calculatePos(bar)) + ',')
	print('        "type": ' + str(MARKERTYPE))
	print('    },')

while (calculatePos(i) < SONGLENGTH):
	printMarkerCode(i)
	i = i + 1