import cv2
import numpy as np
import  pprint


img = cv2.imread('CNN_DATA/X0.png',0)

ret, img =  cv2.threshold(img,127,255,cv2.THRESH_BINARY)

arr = np.array(img).clip(max=1).astype('int8')

for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
                if(arr[i][j] == 0):
                        arr[i][j] = 1
                else:
                        arr[i][j] = -1

pprint.pprint(ret, width=120)
pprint.pprint(arr,  indent=80)

X = [[1, -1, -1],
        [-1, 1, -1],
        [-1, -1, 1]]
