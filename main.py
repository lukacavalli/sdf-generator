import cv2
img = cv2.imread('square.png', 1)
img = cv2.resize(img, (300, 300))
ret, imgBW = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
coords = set()

def drawABorder(imgBW, width, height, leftToRight: bool):
    black = False
    for i in range(width):
        for j in range(height):
            if leftToRight:
                x = i
                y = j
            else:
                x = j
                y = i
            (b, g, r) = imgBW[x, y]
            if (b == 0 and g == 0 and r == 0 and not black):
                coords.add(str(x) + ',' + str(y))
                imgBW[x, y] = (0,0,255)
                black = True
            elif (b == 255 and g == 255 and r == 255 and black):
                coords.add(str(x) + ',' + str(y))
                imgBW[x, y] = (0,0,255)
                black = False
            

drawABorder(imgBW, 300, 300, False)
drawABorder(imgBW, 300, 300, True)
print(coords)
print(len(coords))
cv2.imshow('image', imgBW)
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)