import cv2
import sys

# Get the image path from the command line
imagePath = sys.argv[1]

# Create a cv2 image object using the given path
image = cv2.imread(imagePath)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
img_invert=cv2.bitwise_not(gray)

# Apply a Gaussian blur to reduce noise
gblur_img=cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)

# Dodge the image to remove all dark areas that aren't heavily tinted, 
# leaving only dark areas that are strongly tinted
dodged_img=cv2.divide(gray,255-gblur_img,scale=256)

# Burn the image to darken the areas of the painting that are strongly darkened even more,
# returning the final image
final_image=255-cv2.divide(255-dodged_img, 255-gblur_img, scale=256)

# Save the image
cv2.imwrite('daniel_forward_sketch.jpg', final_image)