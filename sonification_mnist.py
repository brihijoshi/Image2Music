import numpy as np
import random

#chromatic = [C, C#, D, D#, E, F, F#, G, G#, A, A#, B]
#C = chromatic[0]
#D = chromatic[2]
#E = chromatic[4]
#F = chromatic[5]
#G = chromatic[7]
#A = chromatic[9]
#B = chromatic[11]

###############################################################

# 1. Play the flattened out image -> raster scan through every individual pixel and play value

imgs = np.loadtxt(open(r"C:/Users/Aditya Adhikary/Desktop/DA/DA Proj/Project/testData.csv", "rb"), delimiter=",")

print(imgs.shape)

flattened = imgs.flatten().tolist()

print(len(flattened))

print(flattened[:100])

Scale.default.set("major", tuning=Tuning.just)
    
p1 >> pluck(flattened,dur=0.2, slide=1, slidedelay=0.5)

p2 >> play("0x0-")

print(SynthDefs)

#####################################################

# 2. Binarize the image based on a threshold, then pick major chords randomly for every 1, diminished or minor for every 0

from sklearn import preprocessing
#Binarized image

imgs = np.loadtxt(open(r"C:/Users/Aditya Adhikary/Desktop/DA/DA Proj/Project/testData.csv", "rb"), delimiter=",")

binarizer = preprocessing.Binarizer().fit(imgs)

binary = binarizer.transform(imgs)

print(binary)

flattened_binary = binary.flatten().tolist()

print(flattened_binary[:200])

dim = [0, 1, 3, 4, 6, 7, 9, 10]
dim_chords = list(zip(dim,dim[1:],dim[2:]))

print(dim_chords)

maj = [0, 2, 4, 5, 7, 9, 11]
maj_chords = list(zip(maj,maj[1:],maj[2:]))

print(maj_chords)
    
#print(Scale.minor)

minor = [0, 2, 3, 5, 7, 8, 10]
min_chords = list(zip(minor,minor[1:],minor[2:]))

print(min_chords)

chord_sequence = []
for ele in flattened_binary:
    if ele == 0.0:
        r = random.choice([0,1])
        if r == 0:
            chord_sequence.append(random.choice(min_chords))
        else:
            chord_sequence.append(random.choice(dim_chords))
    else:
        chord_sequence.append(random.choice(maj_chords))
  
print(chord_sequence[:100])

p0 >> viola(chord_sequence,dur=2)
p4 >> play("x-o[---]xxo{-=o*}", dur=1)

p1 >> pluck(maj_chords)

p2 >> pluck(min_chords)

p3 >> pluck(dim_chords)

print(SynthDefs)

################################################################################

# 3. play every column of the images as a single chord

imgs = np.loadtxt(open(r"C:/Users/Aditya Adhikary/Desktop/DA/DA Proj/Project/testData.csv", "rb"), delimiter=",")

p1 >> pluck([(0,0,3.0,2,4,4,10,101.3)])

p2 >> pluck([101.1])

chord_seq = []
for col in imgs.T:
    #print(col)
    #col = filter(lambda a: a != 0, col)
    chord_seq.append(tuple(col))

print(chord_seq[:10])

p5 >> glass(chord_seq,dur = 1)

p6 >> soprano(chord_seq,dur = 1)

print(SynthDefs)

####################################################################################

# 4. Assign various sounds from a set of predefined sounds to the pixel values while scanning

import string

letters = list(string.ascii_letters)
print(letters)

beats = ['o','x', '-','=','*']
stringbeat = ''
for i in beats:
    stringbeat+=i

#p7 >> play(beats)

#p1 >> pluck(fmod = 2)

#p1 >> pluck(fmod=linvar([-10,10],8), dur=1/4, sus=1)

print(Samples)

others = {'!': 'Yeah!',
'#': 'Crash',
'$': 'Beatbox',
'%': 'Noise bursts',
'&': 'Chime',
'*': 'Clap',
'+': 'Clicks',
'-': 'Hi hat closed',
'/': 'Reverse sounds',
'1': 'Vocals (One)',
'2': 'Vocals (Two)',
'3': 'Vocals (Three)',
'4': 'Vocals (Four)',
':': 'Hi-hats',
'=': 'Hi hat open',
'@': 'Gameboy noise',
#'|': 'Hangdrum',
'~': 'Ride cymbal',
'\\': 'Lazer',
'^': 'Donk'}

other_sounds = list(others.keys())
#print(other_sounds)
all_sounds = letters + other_sounds
print(all_sounds)

print(len(all_sounds))

imgs = np.loadtxt(open(r"C:/Users/Aditya Adhikary/Desktop/DA/DA Proj/Project/testData.csv", "rb"), delimiter=",")

print(imgs.shape)

flattened = imgs.flatten().tolist()

print(len(flattened))

#p1 >> play('!bt{yu}')

sound_sequence = ''
for ele in flattened:
    if ele == 0.0:
        #sound_sequence+=random.choice(all_sounds)
        sound_sequence+=' '
    else:
        sound_sequence+=all_sounds[int(ele)%len(all_sounds)]
        
print(sound_sequence[:100])

p1 >> play(sound_sequence[:500],dur = 0.25,pan = [-1, 0, 1])

#####################################################################################

# 5. experimental: average out the first and last columns, second and second-last columns, and so on. Pointers moving from both sides of the images

imgs = np.loadtxt(open(r"C:/Users/Aditya Adhikary/Desktop/DA/DA Proj/Project/testData.csv", "rb"), delimiter=",")

print(imgs.shape)

new_imgs = []

for i in range(len(imgs.T)):
    col1 = imgs.T[i]
    col2 = imgs.T[len(imgs.T)-i-1]
    col = (col1+col2)/2
    new_imgs.append(col.tolist())

print(new_imgs[:2])
    
new_imgs = new_imgs[:int(len(new_imgs)/2)]

flattened = [item for sublist in new_imgs for item in sublist]

print(len(flattened))

p5 >> pluck(flattened,dur = 1)

#########################################################################################

# 6. experimental: Take the derivatives in x and y direction

imgs = np.loadtxt(open(r"C:/Users/Aditya Adhikary/Desktop/DA/DA Proj/Project/testData.csv", "rb"), delimiter=",")

print(imgs.shape)

diffx = np.diff(imgs, axis=0)
diffy = np.diff(imgs, axis=1)

diffx = np.absolute(diffx)
diffy = np.absolute(diffy)

flatx = diffx.flatten().tolist()
flaty = diffy.flatten().tolist()

p1 >> glass(flatx,dur=1, slide=1, slidedelay=0.5,fmod=linvar([-10,10],8), sus=1,vib=4, vibdepth=0.1)

p2 >> soft(flaty,dur=1, slide=1, slidedelay=0.5,fmod=linvar([-10,10],8), sus=1,vib=4, vibdepth=0.1)

print(SynthDefs)

#p1 >> pluck([Scale.minorPentatonic],pan = [-1, 0, 1])

#p2 >> pluck(fmod=linvar([-10,10],8), dur=1/4, sus=1,vib=4, vibdepth=0.1)
