import cv2
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image")
args = vars(ap.parse_args())

# reading the image
img = cv2.imread((args["image"]))
#convert to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#invert the gray image
inv_img = 255 - gray_img

#Apply gaussian blur
blur_img = cv2.GaussianBlur(inv_img, (21, 21), 0)

#blend using color dodge
sk_img = cv2.divide(gray_img, 255-blur_img, scale=256.0)

#create windows to display images
cv2.imshow('Thy Sketch', sk_img)

k = cv2.waitKey(0)
# Close window and save image
if k == 27:
    cv2.imwrite('sketch.png', sk_img)
    #close all the opened windows
    cv2.destroyAllWindows()