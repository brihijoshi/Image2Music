import numpy as np
from skimage import color
from skimage import io



img = io.imread('images/sunrise.JPG')
img_hsv = color.rgb2hsv(img)

print(img_hsv.shape)

brightness = []
for i in range(len(img_hsv)):
    for j in range(len(img_hsv[0])):
        brightness.append(img_hsv[i,j][2])
        
threshold = 0.5

#major = [Scale.major,Scale.chinese,Scale.mixolydian,Scale.lydian,Scale.halfWhole]
#minor = [Scale.romanianMinor,Scale.diminished, Scale.halfDim, Scale.zhi, Scale.locrian]

major = [Scale.major, Scale.chinese]
minor = [Scale.diminished, P[0,0.5,2,3,4,4.5,6]]

play_arr = None

if brightness[0] > threshold:
    play_arr = major[np.random.randint(0,len(major))] 
else:
    play_arr = minor[np.random.randint(0,len(minor))]
    
for i in range(1,100):
    if brightness[i] > threshold:        
        play_arr.concat(major[np.random.randint(0,len(major))])
    else:
        play_arr.concat(minor[np.random.randint(0,len(minor))])

print(brightness[:100])

print(play_arr.concat(major[np.random.randint(0,len(major))]))


p1 >> piano(P[0, 0.5, 2, 3, 4, 4.5, 6, 0, 4, 6, 7, 11], dur=1)

print(Scale.names())
